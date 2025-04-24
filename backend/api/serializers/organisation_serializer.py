from rest_framework import serializers

from ..models.organisation import Organisation
from ..models.session import SessionBasicSerializer


class OrganisationSerializer(serializers.ModelSerializer):
    """
    Serializer for Organisation object.
    """

    session = SessionBasicSerializer(many=True, read_only=True)

    class Meta:
        """
        Meta class for OrganisationPresentationSerializer.
        """

        model = Organisation
        fields = [
            "id",
            "name",
            "tagline",
            "description",
            "website",
            "partner_type",
            "logo",
            "session",
        ]
