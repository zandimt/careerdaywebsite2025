from rest_framework import serializers

from ..models.organisation import OrganisationBasicSerializer
from ..models.session import Session
from ..models.timeslot import TimeSlotBasicSerializer


class SessionSerializer(serializers.ModelSerializer):
    """
    Serializer for Session object.
    """

    organisation = OrganisationBasicSerializer(read_only=True)

    class Meta:
        model = Session
        fields = [
            "id",
            "title",
            "organisation",
            "description",
            "time_slot",
            "location",
            "max_attendance",
            "is_registrable",
        ]
