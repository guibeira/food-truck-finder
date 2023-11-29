from rest_framework import viewsets
from .models import FoodTruck
from .serializers import FoodTruckSerializer


class FoodTruckListView(viewsets.ModelViewSet):
    queryset = FoodTruck.objects.all().order_by("name")
    serializer_class = FoodTruckSerializer
