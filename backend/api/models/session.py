from django.db import models
from rest_framework import serializers

from .timeslot import TimeSlot
from .participant import Participant
from .organisation import Organisation
import uuid


class Session(models.Model):
    """Session object representing a session with a speaker and time slot."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=60, null=False)
    organisation = models.ForeignKey(Organisation, null=False, blank=True, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    time_slot = models.ForeignKey(TimeSlot, null=False, blank=True, on_delete=models.PROTECT)
    location = models.TextField(max_length=20, blank=False)
    max_attendance = models.IntegerField(default=40, null=False)
    is_registrable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """String representation of the Session object."""
        return self.title

    @property
    def participants(self):
        """
        Property to get the number of participants in the session.
        :return: Number of participants in the session.
        """
        return self.session_set.aggregate(count=models.Count('id'))


class SessionRegistration(models.Model):
    """SessionRegistration object representing a registration for a session."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participant = models.ForeignKey(Participant, default=None, on_delete=models.CASCADE,
                                    related_name='session_participants')
    session = models.ForeignKey(Session, default=None, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        String representation of the SessionRegistration object.
        :return:
        """
        return self.participant.name() + ' | ' + self.session.title


class SessionBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'title', 'description', 'location', 'max_attendance', 'is_registrable']

