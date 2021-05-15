from django.db import models
from station.models import Station
from utils import get_passing_station
from route.models import Route


class Train(models.Model):
    name = models.CharField(max_length=120)
    number_of_seats = models.IntegerField()
    starting_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='+')
    final_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='+')

    def __str__ (self):
        return self.name

