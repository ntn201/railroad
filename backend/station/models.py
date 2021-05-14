from django.db import models
from ..train import Train

class Station(models.Model):
    name = models.CharField(max_length=60)
    available_train = models.ManyToManyField(Train)
    
    def __init__(self, name):
        self.name = name
       
    def __str__(self):
        return self.name
