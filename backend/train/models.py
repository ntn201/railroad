import django.contrib.postgres.fields
from django.contrib.postgres.fields import ArrayField
from django.db import models
from ..station.models import Station
from ..utils import get_passing_station

class Train(models.Model):
    name = models.CharField(max_length=120)
    number_of_seats = models.IntegerField()
    starting_station = models.OneToOneField(Station)
    final_station = models.OneToOneField(Station)
    passing_stations = ArrayField(models.OneToOneField(Station))

    def __str__ (self):
        return self.name

    def __init__(self, number_of_seats, starting, final):
        self.name = starting.name + " - " + final.name
        self.number_of_seats = number_of_seats
        self.starting_station = starting
        self.final_station = final
        self.passing_stations = get_passing_station(starting, final)

