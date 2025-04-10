from django.db import models
import uuid


class Participant(models.Model):
    """Participant object representing a participant in the event."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=35, null=False)
    preposition_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=35, null=False)
    email_address = models.EmailField(null=False)
    phone_number = models.CharField(max_length=15, null=False)
    study_phase = models.CharField(max_length=25, null=False)
    study = models.CharField(max_length=25, null=False)
    study_year = models.CharField(max_length=25, null=False)
    dietary_requirements = models.CharField(max_length=25, null=True, blank=True)
    membership_id = models.IntegerField(null=False, unique=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    checked_in_at = models.DateTimeField(null=True, blank=True)

    def name(self):
        """
        Get the full name of the participant.
        :return: Full name of the participant.
        """
        if self.preposition_name:
            return f"{self.first_name} {self.preposition_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """
        String representation of the Participant object.
        :return: String representation of the Participant object.
        """
        return self.name()

    class Meta:
        """
        Meta class for Participant.
        """
        ordering = ['-registered_at']

    # TODO: Implement email_participant method (either here or elsewhere)
    def email_participant(self):
        ...