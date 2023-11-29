from rest_framework import viewsets
from .models import FoodTruck
from .serializers import FoodTruckSerializer
from .filters import FoodTruckDistanceFilter


class FoodTruckListView(viewsets.ModelViewSet):
    queryset = FoodTruck.objects.all().order_by("name")
    serializer_class = FoodTruckSerializer
    filterset_class = FoodTruckDistanceFilter
