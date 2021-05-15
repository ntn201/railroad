import django.contrib.postgres.fields
from django.contrib.postgres.fields import ArrayField
from django.db import models
from station.models import Station
from utils import get_passing_station

class Train(models.Model):
    name = models.CharField(max_length=120)
    number_of_seats = models.IntegerField()
    starting_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='+')
    final_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='+')
    passing_stations = ArrayField(models.CharField(max_length=60))

    def __str__ (self):
        return self.name

