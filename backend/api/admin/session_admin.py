from django.contrib import admin

from ..models.session import Session, SessionRegistration


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    """Admin view for Session model."""

    readonly_fields = ["id", "created_at", "updated_at"]
    list_display = ["title", "description", "time_slot", "organisation"]
    list_filter = ["time_slot", "organisation"]
    ordering = ["time_slot"]


@admin.register(SessionRegistration)
class SessionRegistrationAdmin(admin.ModelAdmin):
    """Admin view for SessionRegistration model."""

    readonly_fields = ["id", "registered_at"]
    list_display = ["participant", "session", "registered_at"]
    list_filter = ["session"]
    ordering = ["-registered_at"]
