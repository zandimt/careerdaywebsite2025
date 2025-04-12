import json

import requests
from django.conf import settings
from django.http import HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET", "OPTIONS"])
@permission_classes([AllowAny])
def get_cover_session(request: "HttpRequest") -> JsonResponse | Response:
    """
    Handles the retrieval of session member information from the COVER API.

    This function checks for the presence of a 'cover_session_id' cookie in the request.
    If the cookie is found, it sends a GET request to the COVER API to fetch session member details.
    If the cookie is not found, it returns a 404 Not Found response.

    Args:
        request (HttpRequest): The HTTP request object containing cookies.

    Returns:
        JsonResponse: A JSON response with the session member details if the cookie is present.
        Response: A 404 Not Found response if the cookie is missing.
    """
    if "cover_session_id" in request.COOKIES:
        cover_session_id: str = request.COOKIES["cover_session_id"]
        url: str = (
            settings.COVER_API_URL
            + "?method=session_get_member&session_id="
            + cover_session_id
        )
        response: "requests.Response" = requests.request(method="get", url=url)
        return JsonResponse({"cover_session_id": cover_session_id})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
