from django.db import models
from train.models import Train
try:
    from django.utils import timezone
except ImportError:
    from datetime import datetime as timezone


# Create your models here.
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    print("Customer information")
    customer_name = models.CharField(max_length=60,
                                     default='Type your name in')

    phone = models.CharField(default='Customer phone number', max_length=200)
    email = models.CharField(default='Customer email', max_length=200,null=True)

    # seat =
    price = models.IntegerField(default=0)

    STATUS_CHOICES = (
        ('TAKEN', 'TAKEN'),
        ('PAID', 'PAID'),
    )
    status = models.CharField('Status',
                              choices=STATUS_CHOICES,
                              max_length=255,
                              blank=True,
                              null=True)

    bought_in = models.DateTimeField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    note = models.CharField(default='Note', max_length=255)

    def __str__(self):
        return str(self.id)