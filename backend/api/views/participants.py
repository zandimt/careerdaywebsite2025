from datetime import datetime

from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from uuid import UUID
from ..models import Participant, Session
from ..models.session import SessionRegistration
from ..serializers.participant_serializer import ParticipantSerializer
from ..utility.session_manager import (is_attending_session,
                                       is_session_registrations_open,
                                       is_timeslot_used)
from ..utility.validate_object import validate_object

# TODO: Authentication?

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def get_all_participants(request: "HttpRequest") -> Response | JsonResponse:
    """
    Retrieve a list of all participants or create a new participant.
    :param request: The HTTP request object.
    :return: A JSON response containing the participant data or a 404 Not Found response.
    """
    match request.method:
        case "GET":
            membership_id = request.GET.get("membership_id")

            if membership_id:
                participant = Participant.objects.filter(membership_id=membership_id)

                if participant.exists():
                    serializer = ParticipantSerializer(participant.first())
                    return JsonResponse(serializer.data)
                return Response(status=status.HTTP_404_NOT_FOUND)

            participants = Participant.objects.all()
            serializer = ParticipantSerializer(participants, many=True)
            return JsonResponse(serializer.data, safe=False)
        case "POST":
            serializer = ParticipantSerializer(data=request.POST)
            user = request.user
            # TODO: Debug this
            existing = Participant.objects.filter(membership_id=user.membership_id)

            participant_data = {
                "first_name": user.first_name,
                "preposition_name": user.preposition_name,
                "last_name": user.last_name,
                "email_address": user.email_address,
                "phone_number": user.phone_number,
                "url": user.url,
                "study_phase": user.study_phase,
                "study": user.study,
                "study_year": user.study_year,
                "membership_id": user.membership_id,
            }

            serializer = ParticipantSerializer(data=participant_data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_participant(
    request: "HttpRequest", participant_id: UUID
) -> Response | JsonResponse:
    participant = validate_object(Participant, participant_id)

    match request.method:
        case "GET":
            serializer = ParticipantSerializer(participant)
            return JsonResponse(serializer.data)
        case "PUT":
            serializer = ParticipantSerializer(participant, data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        case "DELETE":
            participant.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_participant_all_sessions(
    request: "HttpRequest", participant_id: UUID
) -> Response | JsonResponse:
    participant = validate_object(Participant, participant_id)

    match request.method:
        case "GET":
            sessions = list(
                Session.objects.filter(
                    Q(sessionregistration__participant_id=participant_id)
                    | Q(is_registrable=True)
                ).values("id", flat=True)
            )

            return JsonResponse({"sessions": sessions})
        case "POST":
            session_id = request.POST.get("session_id")

            if session_id is None:
                return Response(
                    {"Session ID is not provided."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            session = validate_object(Session, session_id)

            if not session.is_registrable:
                return Response(
                    {
                        "Session is not registrable; all participants are enrolled by default."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if not is_session_registrations_open():
                return Response(
                    {"Session registrations are not open."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if is_attending_session(participant, session):
                return Response(
                    {"Participant is already registered for this session."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if is_timeslot_used(session, participant):
                return Response(
                    {
                        "Participant is already registered for a session in the same timeslot."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if session.participants > session.max_attendance:
                return Response(
                    {"Session is full."}, status=status.HTTP_400_BAD_REQUEST
                )

            SessionRegistration.objects.create(
                participant_id=participant_id, session=session_id
            )
            session.save()

            return Response(
                {"Participant registered for session successfully."},
                status=status.HTTP_201_CREATED,
            )

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE"])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_participant_session(
    request: "HttpRequest", participant_id: UUID, session_id: UUID
) -> Response | JsonResponse:
    participant = validate_object(Participant, participant_id)
    session = validate_object(Session, session_id)

    if is_attending_session(participant, session):
        session_registration = SessionRegistration.objects.get(
            participant_id=participant_id, session_id=session_id
        )
    else:
        return Response(
            {"Participant is not registered for the session."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    match request.method:
        case "GET":
            return Response(
                {"Participant is registered for the session."},
                status=status.HTTP_200_OK,
            )
        case "DELETE":
            session_registration.delete()
            return Response(
                {"Participant unregistered from the session."},
                status=status.HTTP_200_OK,
            )

    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
@permission_classes([IsAuthenticated, IsAdminUser])
def check_in_participant(
        request: "HttpRequest", participant_id: UUID
) -> Response | JsonResponse:
    participant = validate_object(Participant, participant_id)
    participant.checked_in_at = datetime.now()
    participant.save()
    serializer = ParticipantSerializer(participant)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)



@api_view(["POST"])
@permission_classes([IsAuthenticated, IsAdminUser])
def check_out_participant(
    request: "HttpRequest", participant_id: UUID
) -> Response | JsonResponse:
    participant = validate_object(Participant, participant_id)

    participant.checked_in_at = None
    participant.save()
    serializer = ParticipantSerializer(participant)

    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
