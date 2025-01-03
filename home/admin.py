from django.contrib import admin
from .models import SurveyProgress, BuildingSurvey

# Register SurveyProgress with the correct admin class
@admin.register(SurveyProgress)
class SurveyProgressAdmin(admin.ModelAdmin):
    list_display = (
        'name',              # Exists in SurveyProgress
        'building_type',     # Exists in SurveyProgress
        'select_city',       # Exists in SurveyProgress
        'status',            # Exists in SurveyProgress
        'survey_date'        # Exists in SurveyProgress
    )
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

# Register BuildingSurvey with the correct admin class
@admin.register(BuildingSurvey)
class BuildingSurveyAdmin(admin.ModelAdmin):
    list_display = (
        'building_name', 
        'building_type', 
        'surveyor_name', 
        'date', 
        'total_residents',
        'total_plot_area',
        'renewable_energy_installed',
    )
    list_filter = ('building_type', 'renewable_energy_installed', 'year_of_construction')
    search_fields = ('building_name', 'surveyor_name', 'address', 'city_zone')
    ordering = ('date', 'building_name')

    fieldsets = (
        ('Building Location', {
            'fields': ('longitude', 'latitude')
        }),

        ('Survey Details', {
            'fields': ('code_for_building', 'date', 'weather', 'time')
        }),
        ('Surveyor & Respondent', {
            'fields': ('surveyor_name', 'surveyor_contact_no', 'respondent_name', 'respondent_contact_no')
        }),
        ('Building Type', {
            'fields': ('building_type',)
        }),
        ('Building Details', {
            'fields': (
                'building_name', 'address', 'manager_name', 'manager_contact_no', 
                'city_zone', 'total_residents', 'total_plot_area', 'total_built_area', 
                'floors_ground', 'floors_basement', 'year_of_construction', 
                'total_rooms_units', 'architect'
            )
        }),
        ('Rooms & Facilities', {
            'fields': (
                'standard_rooms', 'executive_rooms', 'deluxe_rooms', 'meeting_rooms',
                'offices', 'shops', 'restaurants', 'parking_floors', 'parking_spaces'
            )
        }),
        ('Specifications', {
            'fields': (
                'working_hours', 'building_dimensions', 'transformer_capacity',
                'single_access_point', 'multiple_access_points'
            )
        }),
        ('Heights', {
            'fields': ('ground_floor_height', 'first_floor_height', 'basement_height', 'total_height')
        }),
        ('Energy', {
            'fields': ('electricity_consumption', 'renewable_energy_installed', 'renewable_energy_type')
        }),
    )
