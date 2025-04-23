from django.http import HttpRequest, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from ..models.timeslot import TimeSlot
from ..serializers.timeslot_serializer import TimeSlotSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_timeslots(request: "HttpRequest") -> JsonResponse:
    """
    Retrieve a list of all timeslots.

    Args:
        request: The HTTP request object.

    Returns:
        Response: A JSON response containing the list of timeslots.
    """
    timeslots = TimeSlot.objects.all().order_by("start_time")
    serializer = TimeSlotSerializer(timeslots, many=True)
    return JsonResponse({"timeslots": serializer.data})
