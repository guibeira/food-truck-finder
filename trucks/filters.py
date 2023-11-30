from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django_filters import rest_framework as filters

from .models import FoodTruck


class FoodTruckDistanceFilter(filters.FilterSet):
    distance = filters.NumberFilter(method="filter_distance")
    latitude = filters.NumberFilter(method="filter_distance")
    longitude = filters.NumberFilter(method="filter_distance")

    class Meta:
        model = FoodTruck
        fields = ["distance", "latitude", "longitude"]

    def filter_distance(self, queryset, name, value):
        if name == "distance" and "latitude" in self.data and "longitude" in self.data:
            latitude = self.data["latitude"]
            longitude = self.data["longitude"]
            user_location = Point(float(latitude),float(longitude), srid=4326)
            return (
                queryset.annotate(distance=Distance("location", user_location))
                .filter(location__distance_lte=(user_location, value))
                .order_by("distance")
            )
        return queryset
