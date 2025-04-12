import uuid

from django.db import models
from rest_framework import serializers


class TimeSlot(models.Model):
    """TimeSlot object representing a time range for a session."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30, null=True, blank=True)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    is_session = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        String representation of the TimeSlot object.
        :return: String representation of the TimeSlot object.
        """
        title = ""

        if self.title:
            title += self.title + " | "
        title += (
            self.start_time.strftime("%H:%M") + " - " + self.end_time.strftime("%H:%M")
        )

        return title


class TimeSlotBasicSerializer(serializers.ModelSerializer):
    """Serializer for TimeSlot object."""

    class Meta:
        """
        Meta class for TimeSlotBasicSerializer.
        """

        model = TimeSlot
        fields = ["id", "title", "start_time", "end_time"]
