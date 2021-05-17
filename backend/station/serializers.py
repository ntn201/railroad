from rest_framework import serializers
from .models import Station


class StationSerializer(serializers.ModelSerializer):
    """name = serializers.CharField(required=True, max_length=60)

    def create(self, validated_data):
        return Station.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance"""
    
    class Meta:
        model = Station
        fields = ['name']