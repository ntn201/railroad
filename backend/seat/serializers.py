from rest_framework import serializers
from .models import Seat


class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = ['id', 'train_id', 'seat_number', 'is_taken']