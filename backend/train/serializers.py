from rest_framework import serializers
from .models import Train


class TrainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Train
        fields = ['train_name', 'route_name', 'departing_time', 'number_of_cars', 'number_of_seats']
