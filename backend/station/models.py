from django.db import models


class Station(models.Model):
    id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=60, default="forgeten station")

    def __str__(self):
        return f"{self.station_name} Station"
    
    class Meta:
        ordering = ['id']
