from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand

import csv
from trucks.models import FoodTruck


class Command(BaseCommand):
    help = "Import food trucks from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to import")

    def handle(self, *args, **options):
        file_path = options["csv_file"]
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                FoodTruck.objects.create(
                    name=row["Applicant"].strip(),
                    facility_type=row["FacilityType"].strip(),
                    location=Point(float(row["Longitude"]), float(row["Latitude"])),
                    address=row["Address"],
                )
        self.stdout.write(self.style.SUCCESS("Successfully imported food trucks"))
