# Generated by Django 5.1.4 on 2024-12-26 12:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Karachi_Buildings',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sr_no', models.BigIntegerField()),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('building_type', models.CharField(blank=True, choices=[('Residential', 'Residential'), ('Office', 'Office'), ('Hotel', 'Hotel'), ('Health', 'Health'), ('Mall', 'Mall'), ('Educational', 'Educational'), ('Other Buildings', 'Other Buildings')], max_length=254, null=True)),
                ('building', models.CharField(blank=True, max_length=254, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=50, null=True)),
                ('built_up_area', models.FloatField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('google_pin', models.URLField(blank=True, max_length=500, null=True)),
                ('architect_developer', models.CharField(blank=True, max_length=255, null=True)),
                ('contact', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Documents Awaited', 'Documents Awaited'), ('In progress', 'In progress'), ('Permission Awaited', 'Permission Awaited'), ('Permission granted', 'Permission granted'), ('N/A', 'N/A')], max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='uploads/images/')),
                ('survey_date', models.DateField(blank=True, null=True)),
                ('survey_lead', models.CharField(max_length=255)),
                ('comments', models.TextField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
        ),
    ]