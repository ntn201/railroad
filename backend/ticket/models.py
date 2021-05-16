from django.db import models
<<<<<<< HEAD
=======
from train.models import Train
from station.models import Station
from seats.models import Seats
>>>>>>> 3bcbefce09f29119fab4620d41ec81a49879c8cc
try:
    from django.utils import timezone
except ImportError:
    from datetime import datetime as timezone


# Create your models here.
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=60,
                                     default='Type your name in')

    phone = models.CharField(default='Customer phone number', max_length=200)
    email = models.CharField(default='Customer email', max_length=200,null=True)

    starting_station = models.CharField(default='Where from?', max_length=255)
    destination = models.CharField(default='Where to?', max_length= 255)

    TICKET_TYPE = (
        ('One-way', 'One-way'),
        ('Round-trip', 'Round-trip'),
    )

    ticket_type = models.CharField('ticket type',
                                   choices=TICKET_TYPE,
                                   max_length=255,
                                   blank=True,
                                   null=True)
    number_of_seats = models.IntegerField(default=0)
    # seat =
    price = models.IntegerField('Price (in thousands dong)', default=0)

    TICKET_STATUS_CHOICES = (
        ('TAKEN', 'TAKEN'),
        ('PAID', 'PAID'),
    )
    status = models.CharField('Status',
                              choices=TICKET_STATUS_CHOICES,
                              max_length=255,
                              blank=True,
                              null=True)

    bought_in = models.DateTimeField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    note = models.CharField(default='Note', max_length=255)

    def __str__(self):
        return str(self.id)

    