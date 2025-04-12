from typing import Any

from rest_framework.exceptions import NotFound


def validate_object(target: Any, object_id: Any) -> Any:
    try:
        return target.objects.get(pk=object_id)
    except target.DoesNotExist:
        raise NotFound(f"{target} ({object_id} does not exist.")
