from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['id', 'customer_name', 'customer_id', 'customer_phone', 'departing_station', 'destination',
                  'train_id', 'ticket_type', 'seat_number', 'price', 'bought_at']
