from django.http import HttpRequest, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from ..models.session import Session
from ..serializers.session_serializer import SessionSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_sessions(request: "HttpRequest") -> JsonResponse:
    """
    Retrieve a list of all sessions.

    Args:
        request: The HTTP request object.

    Returns:
        Response: A JSON response containing the list of sessions.
    """
    sessions = Session.objects.all().order_by("time_slot__start_time")
    serializer = SessionSerializer(sessions, many=True)

    return JsonResponse({"sessions": serializer.data})
