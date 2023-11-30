import pytest
from django.contrib.gis.geos import Point
from django.urls import reverse
from rest_framework.test import APIClient

from trucks.models import FoodTruck

pytestmark = pytest.mark.django_db


def test_list_food_trucks():
    FoodTruck.objects.create(
        name="Foo",
        facility_type="",
        location=Point(-25.878206329839472, -48.57465225438457),
        address="Sample Address 1313",
    )
    client = APIClient()
    url = reverse("foodtruck-list")
    response = client.get(url)
    assert response.status_code == 200
    res_body = response.json()
    assert res_body["count"] == 1


def test_distance_filter_return_one_truck():
    client = APIClient()
    FoodTruck.objects.create(
        name="Near truck",
        facility_type="",
        location=Point(-25.878206329839472, -48.57465225438457),
        address="Sample Address 1313",
    )

    FoodTruck.objects.create(
        name="Near truck",
        facility_type="",
        location=Point(-25.921820180091757, -48.57806681469511),
        address="Sample Address 1313",
    )
    url = (
        reverse("foodtruck-list")
        + "?latitude=-25.877401101053024&longitude=-48.57331839565998&distance=1000"
    )
    response = client.get(url)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["count"] == 1
    truck_response_body = response_body["results"][0]
    assert truck_response_body["name"] == "Near truck"


def test_distance_filter_return_zero_truck():
    client = APIClient()
    FoodTruck.objects.create(
        name="Foo",
        facility_type="",
        location=Point(-25.922804237456827, -48.57871906045171),
        address="Sample Address 1313",
    )
    url = (
        reverse("foodtruck-list")
        + "?latitude=-25.882287942439486&longitude=-48.57244672867446&distance=500"
    )
    response = client.get(url)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["count"] == 0
