from django.db import models
from train.models import Train


# Create your models here.
class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return f"Train {self.train_id} - Seat {self.seat_number}"

    def createSeat(self, train_id):
        for i in range(1, 57):
            seat = Seat(train_id=train_id, seat_number=i)
            seat.save()

    def takeSeat(self, train_id, seat):
        seat = Seat.objects.filter(train_id=train_id).get(seat_number=seat)
        seat.is_taken = True
        seat.save()