from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import os

class SurveyProgress(models.Model):
    # Status Choices
    COMPLETED = 'Completed'
    DOCUMENTS_AWAITED = 'Documents Awaited'
    IN_PROGRESS = 'In progress'
    PERMISSION_AWAITED = 'Permission Awaited'
    PERMISSION_GRANTED = 'Permission granted'
    NA = 'N/A'

    STATUS_CHOICES = [
        (COMPLETED, 'Completed'),
        (DOCUMENTS_AWAITED, 'Documents Awaited'),
        (IN_PROGRESS, 'In progress'),
        (PERMISSION_AWAITED, 'Permission Awaited'),
        (PERMISSION_GRANTED, 'Permission granted'),
        (NA, 'N/A'),
    ]

    # Building Type Choices
    RESIDENTIAL = 'Residential'
    OFFICE = 'Office'
    HOTEL = 'Hotel'
    HEALTH = 'Health'
    MALL = 'Mall'
    EDUCATIONAL = 'Educational'
    OTHER = 'Other Buildings'

    BUILDING_TYPE_CHOICES = [
        (RESIDENTIAL, 'Residential'),
        (OFFICE, 'Office'),
        (HOTEL, 'Hotel'),
        (HEALTH, 'Health'),
        (MALL, 'Mall'),
        (EDUCATIONAL, 'Educational'),
        (OTHER, 'Other Buildings'),
    ]

    # City Choices
    KARACHI = 'Karachi'
    HYDERABAD = 'Hyderabad'
    NAWABSHAH = 'Nawabshah'
    LARKANA = 'Larkana'
    SUKKUR = 'Sukkur'

    CITY_CHOICES = [
        (KARACHI, 'Karachi'),
        (HYDERABAD, 'Hyderabad'),
        (NAWABSHAH, 'Nawabshah'),
        (LARKANA, 'Larkana'),
        (SUKKUR, 'Sukkur'),
    ]

    # Dynamic upload path function
    def upload_to_city_folder(instance, filename):
        city_folder = instance.select_city.replace(" ", "_")
        return os.path.join('Uploaded_Images', city_folder, filename)

    # Model Fields
    id = models.BigAutoField(primary_key=True)
    select_city = models.CharField(max_length=100, choices=CITY_CHOICES)
    Building_Code = models.BigIntegerField()
    name = models.CharField(max_length=254, null=True, blank=True)
    building_type = models.CharField(max_length=254, choices=BUILDING_TYPE_CHOICES, null=True, blank=True)
    building = models.CharField(max_length=254, null=True, blank=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    mobile_no = models.CharField(max_length=50, blank=True, null=True)
    built_up_area = models.FloatField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    google_pin = models.URLField(max_length=500, blank=True, null=True)
    architect_developer = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    picture = models.ImageField(upload_to=upload_to_city_folder, blank=True, null=True)  # Dynamic path
    survey_date = models.DateField(blank=True, null=True)
    survey_lead = models.CharField(max_length=255, null=True)
    comments = models.TextField(blank=True, null=True)
    geom = models.PointField(srid=4326, null=True, blank=True)

    # Save method to create geometry
    def save(self, *args, **kwargs):
        if self.latitude is not None and self.longitude is not None:
            self.geom = Point(self.latitude, self.longitude)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.building_type} - {self.select_city}"
