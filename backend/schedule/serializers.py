from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ['route_name', 'arrive_order', 'arrive_time']