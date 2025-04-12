from django.contrib import admin
from django.template import Context, Template
from django.utils.html import format_html

from ..models.email import Email


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    """Admin view for Email model."""

    readonly_fields = ["preview_email", "id"]
    list_display = ["name", "subject"]
    ordering = ["name"]

    def attachment_link(self, obj):
        if obj.attachment:
            return format_html(
                '<a href="{}" target="_blank">📎 {}</a>',
                obj.attachment.url,
                obj.attachment.name,
            )
        return "—"

    attachment_link.short_description = "Attachment"

    def preview_email(self, obj):
        """
        Preview the email body.
        :param obj: Email object.
        :return: HTML preview of the email body.
        """
        try:

            html = Template(obj.body).render(Context({}))
            return format_html(
                """
                <div style="border:1px solid #ccc; padding:1rem;">
                    <strong>Subject:</strong> {}</p>
                    <hr>
                    <div>{}</div>
                </div>
                """,
                obj.subject,
                html,
            )
        except Exception as e:
            return f"Error rendering template: {e}"

    preview_email.short_description = "Preview"
