from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Karachi_Buildings(models.Model):
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

    id = models.BigAutoField(primary_key=True)  # Auto-incremented primary key
    sr_no = models.BigIntegerField()
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
    picture = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    survey_date = models.DateField(blank=True, null=True)
    survey_lead = models.CharField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    geom = models.PointField(srid=4326, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Ensure coordinates are valid before saving geometry
        if self.latitude is not None and self.longitude is not None:
            self.geom = Point(self.latitude, self.longitude)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.building_type}"
