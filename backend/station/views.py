from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Station
from .serializers import StationSerializer


class StationList(APIView):
    def get(self, request, format=None):
        station = Station.objects.all()
        srlr = StationSerializer(station, many=True)
        return Response(srlr.data)
    
    def post(self, request, format=None):
        srlr = StationSerializer(data=request.data)
        if srlr.is_valid():
            srlr.save()
            return Response(srlr.data, status=status.HTTP_201_CREATED)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)


class StationDetail(APIView):
    def get_object(self, pk):
        try:
            return Station.objects.get(pk=pk)
        except Station.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        station = self.get_object(pk)
        srlr = StationSerializer(station)
        return Response(srlr.data)
    
    def put(self, request, pk, format=None):
        station = self.get_object(pk)
        srlr = StationSerializer(station, data=request.data)
        if srlr.is_valid():
            srlr.save()
            return Response(srlr.data)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format):
        station = self.get_object(pk)
        station.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)