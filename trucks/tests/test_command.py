import pytest
from django.core.management import call_command
from django.contrib.gis.geos import Point
import unittest.mock as mock
from trucks.models import FoodTruck

pytestmark = pytest.mark.django_db


def test_import_food_trucks_command():
    csv_content = """Applicant,FacilityType,Latitude,Longitude,Address
                     Test Truck,Truck,37.7749,-122.4194,123 Test St
                     Another Truck,Truck,37.7750,-122.4185,456 Another St"""

    with mock.patch("builtins.open", mock.mock_open(read_data=csv_content)):
        call_command("import_foodtrucks", "mocked_file.csv")

        assert FoodTruck.objects.count() == 2

        truck1 = FoodTruck.objects.get(name="Test Truck")
        assert truck1.facility_type == "Truck"
        assert truck1.location.equals(Point(-122.4194, 37.7749))
        assert truck1.address == "123 Test St"

        truck2 = FoodTruck.objects.get(name="Another Truck")
        assert truck2.facility_type == "Truck"
        assert truck2.location.equals(Point(-122.4185, 37.7750))
        assert truck2.address == "456 Another St"
