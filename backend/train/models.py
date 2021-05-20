from django.db import models
from route.models import Route
from station.models import Station


class Train(models.Model):
    id = models.AutoField(primary_key=True)
    train_name = models.CharField(max_length=120, unique=True)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    departing_time = models.DateTimeField()
    number_of_seats = models.IntegerField(default=56)

    def __str__(self):
        return self.train_name
