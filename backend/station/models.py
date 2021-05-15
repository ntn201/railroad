from django.db import models

#
class Station(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, station):
        stn = cls(name=station)
        return stn
    
    