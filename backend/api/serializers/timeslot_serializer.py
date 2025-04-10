from rest_framework import serializers
from ..models.timeslot import TimeSlot
from .session_serializer import SessionSerializer


class TimeSlotSerializer(serializers.ModelSerializer):
    """Serializer for TimeSlot object."""
    session_set = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = TimeSlot
        fields = ['id', 'title', 'is_session', 'start_time', 'end_time', 'location', 'session_set']