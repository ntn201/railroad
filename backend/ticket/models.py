from django.db import models
from station.models import Station
from seat.models import Seat
from train.models import Train
try:
    from django.utils import timezone
except ImportError:
    from datetime import datetime as timezone


# Create your models here.
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=60,
                                     default='Type your name in')

    customer_phone = models.CharField(default='Customer phone number', max_length=200)
    customer_email = models.CharField(default='Customer email', max_length=200,null=True)

    departing_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name= "Departure", default= True)
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="destination", default= True)
    train_name = models.ForeignKey(Train, on_delete=models.CASCADE)

    TICKET_TYPE = (
        ('One-way', 'One-way'),
        ('Round-trip', 'Round-trip'),
    )

    ticket_type = models.CharField('ticket type',
                                   choices=TICKET_TYPE,
                                   max_length=255,
                                   blank=True,
                                   null=True)
    seat_number = models.ForeignKey(Seat, on_delete=models.CASCADE)

    price = models.IntegerField('Price (in thousands dong)', default=0)

    bought_in = models.DateTimeField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)