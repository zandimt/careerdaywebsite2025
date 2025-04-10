from rest_framework import serializers
from ..models.participant import Participant


class ParticipantSerializer(serializers.ModelSerializer):
    """Serializer for Participant object."""
    registered_at = serializers.DateTimeField(read_only=True)
    checked_in_at = serializers.DateTimeField(read_only=True)

    class Meta:
        """
        Meta class for ParticipantSerializer.
        """
        model = Participant
        fields = ['id', 'first_name', 'preposition_name', 'last_name', 'email_address', 'phone_number', 'study_phase',
                  'study', 'study_year', 'dietary_requirements', 'membership_id', 'registered_at',
                  'checked_in_at']
