from django.db import models
from station.models import Station
from seat.models import Seat
from train.models import Train
from datetime import datetime
try:
    from django.utils import timezone
except ImportError:
    from datetime import datetime as timezone


# Create your models here.
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=60, default='Type your name in')
    customer_id = models.CharField(max_length=10, default='0000000000')
    customer_phone = models.CharField(default='Customer phone number', max_length=200)
    departing_id = models.ForeignKey(Station, on_delete=models.CASCADE, related_name= "Departure", default= True)
    destination_id = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="destination", default= True)
    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)

    TICKET_TYPE = (
        ('One-way', 'One-way'),
        ('Return-trip', 'Return-trip'),
    )
    ticket_type = models.CharField('ticket type', choices=TICKET_TYPE, max_length=255, blank=True, null=True)
    seat_number = models.ForeignKey(Seat, on_delete=models.CASCADE)

    price = models.FloatField('Price (in thousands dong)', default=0.0)

    bought_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.train_id} - {self.seat_number}"



