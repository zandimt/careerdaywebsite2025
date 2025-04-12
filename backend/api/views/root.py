from django.http import HttpRequest, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(["GET"])
@permission_classes([AllowAny])
def get_api_root(request: "HttpRequest") -> JsonResponse:
    """
    Returns the API root URLs for the application.
    :param request: The HTTP request object.
    :return: A JSON response containing the full URLs for the API endpoints.
    """
    endpoints = {
        "svcover": "svcover",
        "participants": "participants",
        "organisations": "organisations",
        "timeslots": "timeslots",
        "sessions": "sessions",
        "settings": "settings",
    }
    full_urls = {
        key: request.build_absolute_uri(path) for key, path in endpoints.items()
    }
    return JsonResponse(full_urls)
