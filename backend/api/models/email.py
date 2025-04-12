from django.db import models
import uuid


class Email(models.Model):
    """Email object representing an email template."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    body = models.TextField(help_text="Supports HTML.")
    file = models.FileField(upload_to='emails/', null=True, blank=True)

    def __str__(self):
        """
        String representation of the Email object.
        :return: String representation of the Email object.
        """
        return self.name
