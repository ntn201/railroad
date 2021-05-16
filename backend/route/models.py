from django.db import models
from station.models import Station


class Route(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    route_name = models.CharField(max_length=60, default='')
    arrive_order = models.IntegerField()

    def __str__(self):
        return f"Train: {self.train_id} - Station: {self.station}"

    


