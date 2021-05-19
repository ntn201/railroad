from django.db import models


class Station(models.Model):
    id = models.AutoField(primary_key=True)
    station_id = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.station_id}. {self.name}"
    
    class Meta:
        ordering = ['id']
