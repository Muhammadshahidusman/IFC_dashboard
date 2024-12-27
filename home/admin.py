from django.contrib import admin
from .models import Karachi_Buildings

@admin.register(Karachi_Buildings)
class KarachiBuildingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'sr_no', 'name', 'building_type', 'status', 'latitude', 'longitude')
    list_filter = ('building_type', 'status')
    search_fields = ('name', 'address', 'building_type', 'architect_developer', 'sr_no')
    ordering = ('id',)
    readonly_fields = ('geom',)  # Prevent accidental changes to geom field
    
    # Enable inline editing for the following fields
    list_editable = ('status', 'latitude', 'longitude')
    
    list_per_page = 50  # Show more entries per page
    save_on_top = True  # Add save button at the top for bulk edits
    
    # fieldsets = (
    #     ('General Information', {
    #         'fields': ('sr_no', 'name', 'building_type', 'building', 'architect_developer', 'status')
    #     }),
    #     ('Location', {
    #         'fields': ('latitude', 'longitude', 'geom')
    #     }),
    #     ('Contact Details', {
    #         'fields': ('mobile_no', 'contact', 'address', 'google_pin')
    #     }),
    #     ('Additional Details', {
    #         'fields': ('survey_date', 'survey_lead', 'comments', 'picture')
    #     }),
    # )
    
    # Prevent empty fields that can hide the save button
    def save_model(self, request, obj, form, change):
        if not obj.name:
            obj.name = "Unnamed Building"
        if not obj.status:
            obj.status = "N/A"
        super().save_model(request, obj, form, change)
    
    def get_readonly_fields(self, request, obj=None):
        # Allow geom to be editable for superusers only
        if request.user.is_superuser:
            return ()
        return self.readonly_fields
