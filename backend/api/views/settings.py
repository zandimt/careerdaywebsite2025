from django.http import JsonResponse, HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..utility.get_settings import get_settings


@api_view(['GET'])
def get_all_settings(request: 'HttpRequest') -> Response | JsonResponse:
    """
    Retrieve the settings for the application.
    :param request:
    :return:
    """
    return JsonResponse(get_settings())