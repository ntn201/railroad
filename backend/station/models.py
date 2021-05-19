from django.db import models


class Station(models.Model):
    id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=60, default="forgeten station")
    station_distance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.station_distance}. {self.station_name}"
    
    class Meta:
        ordering = ['id']
