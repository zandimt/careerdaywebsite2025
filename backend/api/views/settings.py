from django.http import HttpRequest, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from ..utility.get_settings import get_settings


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_all_settings(request: "HttpRequest") -> Response | JsonResponse:
    """
    Retrieve the settings for the application.
    :param request:
    :return:
    """
    return JsonResponse(get_settings())
