from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=60)
    station_id = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.station_id}. {self.name}"
    
    class Meta:
        ordering = ['station_id']
