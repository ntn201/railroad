from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ['id', 'route_id', 'station_id', 'arrive_order', 'arrive_time']