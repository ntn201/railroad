from django.db import models
from ..train import Train

class Station(models.Model):
    name = models.CharField(max_length=60)
    available_train = models.ManyToManyField(Train)
