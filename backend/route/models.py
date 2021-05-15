from django.db import models
from station.models import Station

class Route(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='+')
    train_id = models.CharField(max_length=10)
    arrive_time = models.TimeField()
    arrive_order = models.IntegerField()
