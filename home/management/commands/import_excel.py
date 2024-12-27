from django.core.management.base import BaseCommand
import pandas as pd
from home.models import Karachi_Buildings
from django.contrib.gis.geos import Point


class Command(BaseCommand):
    help = 'Import Karachi buildings data from Excel file'

    def handle(self, *args, **kwargs):
        file_path = '/home/usman/Music/Survey application/IFC _karachi.xlsx'
        df = pd.read_excel(file_path)

        # Clean data: handle longitude with commas and parse dates
        df['Longitude'] = pd.to_numeric(df['Longitude'].astype(str).str.replace(',', ''), errors='coerce')
        df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')

        for _, row in df.iterrows():
            try:
                # Handle composite uniqueness check (Name + Building Type + Address)
                Karachi_Buildings.objects.update_or_create(
                    name=row['Name'],
                    building_type=row['Building Type'],
                    address=row['Address'],
                    defaults={
                        'sr_no': row['Sr.no.'],
                        'building': row['Building'],
                        'longitude': row['Longitude'],
                        'latitude': row['Latitude'],
                        'mobile_no': row['Mobile No.'],
                        'built_up_area': row['Built-up Area(SqFt)'],
                        'google_pin': row['Google Pin'],
                        'architect_developer': row['Architect/Developer'],
                        'contact': row['Contact'],
                        'status': row['Status'],
                        # Fix for date parsing with dayfirst=True
                        'survey_date': pd.to_datetime(row['Survey Date'], errors='coerce', dayfirst=True),
                        # Apply .replace() only if it's a string
                        'survey_lead': row['Survey Lead'].replace('\n', ' ') if isinstance(row['Survey Lead'], str) else row['Survey Lead'],
                        'comments': row['Comments'],
                        # Create Point only if coordinates are valid
                        'geom': Point(row['Longitude'], row['Latitude']) if pd.notnull(row['Longitude']) and pd.notnull(row['Latitude']) else None,
                    }
                )
                self.stdout.write(self.style.SUCCESS(f"Imported: {row['Name']} - {row['Building Type']}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error importing {row['Name']}: {e}"))
