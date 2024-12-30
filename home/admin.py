from django.contrib import admin
from .models import SurveyProgress

@admin.register(SurveyProgress)
class SurveyProgressAdmin(admin.ModelAdmin):
    list_display = ('name', 'building_type', 'select_city', 'status', 'survey_date')
    list_filter = ('select_city', 'status', 'building_type')
    search_fields = ('name', 'architect_developer', 'address', 'Building_Code')
    ordering = ('survey_date',)
    fieldsets = (
        ('Building Information', {
            'fields': ('select_city','name', 'Building_Code', 'building_type', 'building', 'built_up_area', 'address')
        }),
        ('Contact Details', {
            'fields': ('architect_developer', 'contact', 'mobile_no', 'google_pin')
        }),
        ('Survey Details', {
            'fields': ('status', 'survey_lead', 'survey_date', 'comments')
        }),
        ('Location and Images', {
            'fields': ('longitude', 'latitude', 'geom', 'picture')
        }),
    )
