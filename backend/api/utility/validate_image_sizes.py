from django.core.exceptions import ValidationError
from django.db.models.fields.files import ImageFieldFile


def validate_min_size_logo(image: ImageFieldFile) -> bool:
    if image.width < 200 or image.height < 200:
        raise ValidationError(f"Logo size should be at least 200 x 200 pixels.")
    return True
