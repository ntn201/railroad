from rest_framework import serializers
from .models import Train


class TrainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Train
        fields = ['id', 'train_name', 'route_id', 'departing_time', 'number_of_seats']
