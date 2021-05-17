from rest_framework import serializers
from .models import Seat

class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = ['train_name', 'car_number', 'seat_number']