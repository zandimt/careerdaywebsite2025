from django.contrib import admin

from ..models.timeslot import TimeSlot


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    # TODO: Figure out why it's not in 24 hours
    """Admin view for TimeSlot model."""
    readonly_fields = ["id", "created_at", "updated_at"]
    list_display = ["title", "start_time", "end_time", "is_session"]
    list_filter = ["is_session"]
    ordering = ["start_time"]
