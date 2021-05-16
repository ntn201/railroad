from django.db import models
from train.models import Train


# Create your models here.
class Seat(models.Model):
    train_name = models.ForeignKey(Train, on_delete=models.CASCADE)
    car_number = models.IntegerField()
    seat_number = models.IntegerField()

    def __str__(self):
        return f"Train {self.train_name} - Car {self.car_number} - Seat {self.seat_number}"