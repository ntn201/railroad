from django.db import models
from station.models import Station


class Route(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='+')
    train_id = models.CharField(max_length=10)
    arrive_time = models.TimeField()
    arrive_order = models.IntegerField()

    def __str__(self):
        return f"Train: {self.train_id} - Station: {self.station}"

    @classmethod
    def create(cls, station, train_id, arrive_time, arrive_order):
        route = cls(station=station, train_id=train_id, arrive_time=arrive_time, arrive_order=arrive_order)
        return route


