import django.contrib.postgres.fields
from django.contrib.postgres.fields import ArrayField
from django.db import models

class RailRoute(models.Model):
    name  = models.CharField(max_length=10)
    route = ArrayField(models.CharField(max_length=60))
    time  = ArrayField(models.DateTimeField())

    def __str__(self):
        return self.name