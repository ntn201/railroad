from django.db import models
from route.models import Route
from station.models import Station
try:
    from django.utils import timezone
except ImportError:
    from datetime import datetime as timezone


# Create your models here.
class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    route_name = models.ForeignKey(Route, on_delete=models.CASCADE)
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE, default="forgoten station")
    arrive_order = models.IntegerField(default=1)
    travel_time = models.IntegerField(default=0)

    def __str__(self):
        return str(self.route_name)