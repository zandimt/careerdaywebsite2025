import base64
import csv
import mimetypes
import io
import os

from django.conf import settings
from django.contrib import admin
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import Context, Template
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from PyPDF2 import PdfReader, PdfWriter

from ..forms import EmailForm
from ..models.participant import Participant
from ..utility.generate_qr_code import generate_qr_code


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    """Admin view for Participant model."""
    readonly_fields = ['id', 'registered_at', 'updated_at']
    list_display = ['name', 'email_address', 'phone_number', 'url', 'checked_in_at', 'registered_at']
    actions = ['email_content', 'export_as_badges', 'export_as_csv']
    ordering = ['-registered_at']

    @admin.action(description="Email content to selected participants")
    def email_content(self, request, queryset):
        """
        Email content to selected participants.
        :param request: HTTP request object.
        :param queryset: Queryset of selected participants.
        """
        if 'apply' in request.POST:
            form = EmailForm(request.POST)
            if form.is_valid():
                template = form.cleaned_data['template']
                for participant in queryset:
                    context = Context({
                        'name': participant.name,
                        'email_address': participant.email_address,
                        })
                    include_qr = form.cleaned_data['include_qr']
                    html = Template(template.body).render(context)
                    msg = EmailMessage(
                        subject=template.subject,
                        body=html,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        to=[participant.email_address],
                    )
                    msg.content_subtype = 'html'

                    if template.file:
                        file_content = template.file.read()
                        file_name = template.file.name.split('/')[-1]
                        mime_type, _ = mimetypes.guess_type(template.file.name)
                        msg.attach(file_name, file_content, mime_type)


                    if include_qr:
                        qr = generate_qr_code(participant.id)
                        filename = f'{participant.name.replace(' ', '')}_{participant.id}.png'
                        msg.attach(filename, qr.read(), 'image/png')

                    msg.send()
                self.message_user(request, f'Sent {template.name} to {queryset.count()} participants.')
                return redirect(request.get_full_path())
        else:
            form = EmailForm()

            qr_previews = []
            for participant in queryset:
                qr_img = generate_qr_code(participant.id)
                base64_data = base64.b64encode(qr_img.read()).decode('utf-8')
                qr_previews.append({
                    'participant': participant,
                    'qr_base64': base64_data,
                })

            return render(request, 'admin/email_action.html', {
                'form': form,
                'participants': queryset,
                'qr_previews': qr_previews,
                'action_checkbox_name': ACTION_CHECKBOX_NAME,
            })


    @admin.action(description="Export selected participants as badges")
    def export_as_badges(self, request, queryset) -> HttpResponse:
        """
        Export selected participants as badges.
        :param request: HTTP request object.
        :param queryset: Queryset of selected participants.
        """
        width = 1110.24  # in points
        height = 755.91
        size = 80
        background_path = os.path.join(settings.BASE_DIR, 'api', 'templates', 'card.pdf')
        font_path = os.path.join(settings.BASE_DIR, 'static', 'fonts', 'FiraSans-Bold.ttf')
        pdfmetrics.registerFont(TTFont("FiraSans", font_path))
        output_pdf = PdfWriter()


        for participant in queryset:
            if participant.url:
                qr = generate_qr_code(participant.url)
            elif participant.membership_id:
                qr = generate_qr_code(f'https://svcover.nl/profile/{participant.membership_id}')
            else:
                qr = generate_qr_code('https://svcover.nl')
            qr_img = ImageReader(qr)

            overlay_io = io.BytesIO()
            c = canvas.Canvas(overlay_io, pagesize=(width, height))

            c.drawImage(qr_img, x=40, y=40, width=164, height=164)
            c.setFont("FiraSans", size)
            text = participant.name
            text_width = c.stringWidth(text, "FiraSans", size)
            c.drawString(x=(width - text_width) / 2, y=height/2 - 40, text=text)

            c.showPage()
            c.save()
            overlay_io.seek(0)

            background_pdf = PdfReader(background_path)
            overlay_pdf = PdfReader(overlay_io)

            background_page = background_pdf.pages[0]
            overlay_page = overlay_pdf.pages[0]
            background_page.merge_page(overlay_page)

            output_pdf.add_page(background_page)

        output_stream = io.BytesIO()
        output_pdf.write(output_stream)
        output_stream.seek(0)

        response = HttpResponse(output_stream, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="badges.pdf"'

        self.message_user(request, "Exported participant badges!")
        return response


    @admin.action(description="Export selected participants as CSV")
    def export_as_csv(self, request, queryset):
        """
        Export selected participants as CSV.
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="participants.csv"'

        fieldnames = [
            'id', 'name', 'email_address', 'phone_number', 'url',
        ]

        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()

        for participant in queryset:
            writer.writerow({
                'id': participant.id,
                'name': participant.name,
                'email_address': participant.email_address,
                'phone_number': participant.phone_number,
                'url': participant.url,
            })

        return response