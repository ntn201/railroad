from django.db import models
from route.models import Route
from station.models import Station


class Train(models.Model):
    train_name = models.CharField(max_length=120)
    route_name = models.ForeignKey(Route, on_delete=models.CASCADE)
    departing_time = models.DateTimeField()
    number_of_cars = models.IntegerField()
    number_of_seats = models.IntegerField()

    def __str__ (self):
        return self.train_name
