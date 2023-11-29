from rest_framework import serializers
from .models import FoodTruck


class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = ("id", "name", "facility_type", "location", "address")
