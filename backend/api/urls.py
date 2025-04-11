"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import root, svcover, organisations, participants, timeslots, sessions, settings


urlpatterns = [
    # Default
    path('', root.get_api_root),
    # Cover
    path('svcover/', svcover.get_cover_session),
    # Participants
    path('participants/', participants.get_all_participants),
    path('participants/<uuid:participant_id>/', participants.get_participant),
    path('participants/<uuid:participant_id>/check_in/', participants.check_in_participant),
    path('participants/<uuid:participant_id>/check_out/', participants.check_out_participant),
    path('participants/<uuid:participant_id>/sessions/', participants.get_participant_all_sessions),
    path('participants/<uuid:participant_id>/sessions/<uuid:session_id>/', participants.get_participant_session),
    # Organisations
    path('organisations/', organisations.get_all_organisations),
    path('organisations/<uuid:organisation_id>/', organisations.get_organisation),
    # Timeslots
    path('timeslots/', timeslots.get_all_timeslots),
    # Sessions
    path('sessions/', sessions.get_all_sessions),
    # Settings
    path('settings', settings.get_all_settings),
]
