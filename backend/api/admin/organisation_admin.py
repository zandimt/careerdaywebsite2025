from django.contrib import admin
from ..models.organisation import Organisation

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    """Admin view for Organisation model."""
    readonly_fields = ['id', 'created_at', 'updated_at']
    list_display = ['name', 'website', 'partner_type']
    list_filter = ['partner_type']
    ordering = ['name']