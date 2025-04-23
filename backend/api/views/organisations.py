from django.http import HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..models.organisation import Organisation, OrganisationBasicSerializer
from ..serializers.organisation_serializer import OrganisationSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_organisations(request: "HttpRequest") -> JsonResponse:
    """
    Retrieve a list of all organisations.

    Args:
        request: The HTTP request object.

    Returns:
        Response: A JSON response containing the list of organisations.
    """
    organisations = Organisation.objects.all()
    serializer = OrganisationBasicSerializer(organisations, many=True)
    return JsonResponse({"organisations": serializer.data})


@api_view(["GET"])
@permission_classes([AllowAny])
def get_organisation(
    request: "HttpRequest", organisation_id: int
) -> Response | JsonResponse:
    """
    Retrieve a specific organisation by its ID.

    Args:
        request: The HTTP request object.
        organisation_id: The ID of the organisation to retrieve.

    Returns:
        Response: A JSON response containing the organisation details.
    """
    try:
        organisation = Organisation.objects.get(id=organisation_id)
        serializer = OrganisationSerializer(organisation)
        return JsonResponse({"organisation": serializer.data})
    except Organisation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
