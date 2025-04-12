from datetime import datetime

from constance import config

from ..models import Participant
from ..models.session import Session, SessionRegistration


def is_attending_session(participant: Participant, session: Session) -> bool:
    """
    Check if a participant is attending a session.
    :param participant: The participant object.
    :param session: The session object.
    :return: True if the participant is attending the session, False otherwise.
    """
    return SessionRegistration.objects.filter(
        participant_id=participant.id, session_id=session.id
    ).exists()


def is_session_registrations_open() -> bool:
    """
    Check if session registrations are open.
    :return: True if session registrations are open, False otherwise.
    """
    now = datetime.now()
    start_time = config.SESSIONS_OPEN.replace(tzinfo=None)
    end_time = config.SESSIONS_CLOSED.replace(tzinfo=None)

    return True if start_time <= now <= end_time else False


def is_timeslot_used(session: Session, participant: Participant) -> bool:
    """
    Check if a participant has already registered for a session in the same timeslot.
    :param session: The session object.
    :param participant: The participant object.
    :return: True if the participant has already registered for a session in the same timeslot, False otherwise.
    """
    participant_sessions = SessionRegistration.objects.filter(
        participant_id=participant.id
    )

    for registered in participant_sessions:
        compared_session = Session.objects.get(pk=registered.id)

        if compared_session.time_slot == session.time_slot:
            return True

    return False
