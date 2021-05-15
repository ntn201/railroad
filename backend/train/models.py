from django.contrib.postgres.fields import ArrayField
from django.db import models
from route.models import Route
from station.models import Station

class Train(models.Model):
    name = models.CharField(max_length=120)
    number_of_seats = ArrayField(ArrayField(models.IntegerField(null=True, blank=True), size=56, default=list), default=list)
    starting_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='+')
    final_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='+')

    def __str__ (self):
        return self.name