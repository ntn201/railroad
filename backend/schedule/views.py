from django.shortcuts import render
from .models import Schedule
from .serializers import ScheduleSerializer
from station.models import Station
from station.serializers import StationSerializer
from route.models import Route
from route.serializers import RouteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class ScheduleList(APIView):
    def get(self, request, format=None):
        schedule = Schedule.objects.all()
        srlr = ScheduleSerializer(schedule, many=True)
        return Response(srlr.data)

    def post(self, request, format=None):
        srlr = ScheduleSerializer(data=request.data)
        if srlr.is_valid():
            srlr.save()
            return Response(srlr.data, status=status.HTTP_201_CREATED)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleDetail(APIView):
    def get_object(self, pk):
        try:
            return Schedule.objects.get(pk=pk)
        except Schedule.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        schedule = self.get_object(pk=pk)
        srlr = ScheduleSerializer(schedule)
        return Response(srlr.data)
    
    def put(self, request, pk, format=None):
        schedule = self.get_object(pk=pk)
        srlr = ScheduleSerializer(schedule, data=request.data)
        if srlr.is_valid():
            srlr.save()
            return Response(srlr.data)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        schedule = self.get_object(pk)
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddSchedule(APIView):
    def get(self, format=None):
        s = Station.objects.get(id=5)
        srlr = StationSerializer(s)
        return Response(srlr.data)

    def post(self, format=None):
        route = Route.objects.get(route_name="Ha Noi - Lao Cai")
        stations = 5
        