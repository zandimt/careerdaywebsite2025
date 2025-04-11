from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models.participant import Participant
from .models.organisation import Organisation
from .models.session import Session, SessionRegistration
from .models.timeslot import TimeSlot

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    """Admin view for Participant model."""
    readonly_fields = ['id', 'registered_at', 'updated_at']
    list_display = ['name', 'email_address', 'phone_number', 'url', 'checked_in_at', 'registered_at']
    actions = ['email_qr_code', 'email_schedule', 'export_as_csv']
    ordering = ['-registered_at']

    # TODO: Implement Admin Actions
    @admin.action(description="Email QR Code to selected participants.")
    def email_qr_code(self, request, queryset) -> None:
        """
        Email QR Code to selected participants.
        :param request: HTTP request object.
        :param queryset: Queryset of selected participants.
        """
        self.message_user(request, "Not implemented yet!")

    @admin.action(description="Email schedule to selected participants.")
    def email_schedule(self, request, queryset) -> None:
        """
        Email schedule to selected participants.
        :param request: HTTP request object.
        :param queryset: Queryset of selected participants.
        """
        self.message_user(request, "Not implemented yet!")

    @admin.action(description="Export selected participants as CSV.")
    def export_as_csv(self, request, queryset) -> None:
        """
        Export selected participants as CSV.
        :param request: HTTP request object.
        :param queryset: Queryset of selected participants.
        """
        self.message_user(request, "Not implemented yet!")

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    """Admin view for Organisation model."""
    readonly_fields = ['id', 'created_at', 'updated_at']
    list_display = ['name', 'website', 'partner_type']
    list_filter = ['partner_type']
    ordering = ['name']

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    # TODO: Figure out why it's not in 24 hours
    """Admin view for TimeSlot model."""
    readonly_fields = ['id', 'created_at', 'updated_at']
    list_display = ['title', 'start_time', 'end_time', 'is_session']
    list_filter = ['is_session']
    ordering = ['start_time']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    """Admin view for Session model."""
    readonly_fields = ['id', 'created_at', 'updated_at']
    list_display = ['title', 'description', 'time_slot', 'organisation']
    list_filter = ['time_slot', 'organisation']
    ordering = ['time_slot']

@admin.register(SessionRegistration)
class SessionRegistrationAdmin(admin.ModelAdmin):
    """Admin view for SessionRegistration model."""
    readonly_fields = ['id', 'registered_at']
    list_display = ['participant', 'session', 'registered_at']
    list_filter = ['session']
    ordering = ['-registered_at']

