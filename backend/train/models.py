import django.contrib.postgres.fields
from django.contrib.postgres.fields import ArrayField
from django.db import models
from utils import get_passing_station


class Train(models.Model):
    name = models.CharField(max_length=120)
    number_of_seats = models.IntegerField()
    starting_station = models.CharField(max_length=60)
    final_station = models.CharField(max_length=60)
    passing_stations = ArrayField(models.CharField(max_length=60))

    def __str__ (self):
        return self.name

