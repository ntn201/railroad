from django.db import models
from train.models import Train


# Create your models here.
class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    train_name = models.ForeignKey(Train, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return f"Train {self.train_name} - Seat {self.seat_number}"

    def createSeat(self, train_name):
        for i in range(1, 57):
            seat = Seat(train_name=train_name, seat_number=i)
            seat.save()