from django.contrib.gis.db import models


class FoodTruck(models.Model):
    name = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
