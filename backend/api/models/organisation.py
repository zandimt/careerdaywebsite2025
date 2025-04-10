from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError
import uuid
from rest_framework import serializers

PARTNER_TYPES = [
    ('PRESENTER', 'Presenter'),
    ('INFORMATION_MARKET', 'Information Market'),
    ('DIGITAL', 'Digital Partner'),
]


def validate_minimum_size(image: ImageFieldFile) -> bool:
    """
    Validate the minimum size of the logo image.
    :param image: The image file to validate.
    :return: True if the image is smaller than the minimum size, False otherwise.
    """
    is_too_small = False
    if image.width < 200 or image.height < 200:
        is_too_small = True
    if is_too_small:
        raise ValidationError(f'Logo size should be at least 200 x 200 pixels.')
    return is_too_small


class Organisation(models.Model):
    """Organisation object representing an organisation."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25, null=False)
    tagline = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    website = models.URLField(max_length=200, null=False)
    partner_type = MultiSelectField(choices=PARTNER_TYPES, null=True, blank=True)
    # TODO: Validate minimum sizes for images
    logo = models.ImageField(null=False, blank=False,
                             validators=[validate_minimum_size, FileExtensionValidator(['png', 'jpg', 'jpeg', 'svg'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class for Organisation."""
        verbose_name_plural = 'Organisations'

    @property
    def speaker(self) -> bool:
        """
        Property to get the speaker associated with the organisation.
        :return: Speaker object or None if not found.
        """
        return self.session_set.count() > 0

    def __str__(self) -> str:
        """
        String representation of the Organisation object.
        :return: String representation of the Organisation object.
        """
        return self.name


class OrganisationBasicSerializer(serializers.ModelSerializer):
    """Serializer for Organisation object."""
    class Meta:
        """
        Meta class for OrganisationSerializer.
        """
        model = Organisation
        fields = ['id', 'name', 'tagline', 'description', 'website', 'partner_type', 'logo']