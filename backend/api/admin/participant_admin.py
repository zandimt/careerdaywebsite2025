import base64
import mimetypes

from django.conf import settings
from django.contrib import admin
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template import Context, Template

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

    # TODO: Implement Admin Actions
    @admin.action(description="Email content to selected participants.")
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
                    context = Context(
                        {'name': participant.name,
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
                        filename = f'{participant.name().replace(' ', '')}_{participant.id}.png'
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

    @admin.action(description="Export selected participants as badges.")
    def export_as_badges(self, request, queryset) -> None:
        """
        Export selected participants as badges.
        :param request: HTTP request object.
        :param queryset: Queryset of selected participants.
        """
        self.message_user(request, "Not implemented yet!")

    @admin.action(description="Export selected participants as CSV.")
    def export_as_csv(self, request, queryset) -> None:
        """
        Export selected participants as CSV.
        :param request: HTTP request object.
        :param queryset: Queryset of selected participants.
        """
        self.message_user(request, "Not implemented yet!")