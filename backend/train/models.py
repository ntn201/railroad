import django.contrib.postgres.fields
from django.contrib.postgres.fields import ArrayField
from django.db import models
from ..utils import get_passing_station

class Train(models.Model):
    name = models.CharField(max_length=120)
    number_of_seats = models.IntegerField()
    starting_station = models.CharField(max_length=60)
    final_station = models.CharField(max_length=60)
    passing_stations = ArrayField(models.CharField(max_length=60))

    def __str__ (self):
        return self.name

    def __init__(self, number_of_seats, starting, final):
        self.name = starting.name + " - " + final.name
        self.number_of_seats = number_of_seats
        self.starting_station = starting
        self.final_station = final
        self.passing_stations = get_passing_station(starting, final)

