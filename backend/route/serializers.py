from rest_framework import serializers
from .models import Route

class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ['station', 'route_name', 'arrive_order']