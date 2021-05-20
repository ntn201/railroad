from django.shortcuts import render
from .models import Train
from .serializers import TrainSerializer
from seat.models import Seat
from route.models import Route
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import json

class TrainList(APIView):
    def get(self, request, format=None):
        train = Train.objects.all()
        srlr = TrainSerializer(train, many=True)
        return Response(srlr.data)

    def post(self, request, format=None):
        request.route_name = Route.objects.get(route_name=request.route_name)
        srlr = TrainSerializer(data=request.data)
        if srlr.is_valid():
            srlr.save()
            Seat(train_name=srlr, seat_number=1).save()
            return Response(srlr.data, status=status.HTTP_201_CREATED)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainDetail(APIView):
    def get_object(self, pk):
        try:
            return Train.objects.get(pk=pk)
        except Train.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        train = self.get_object(pk=pk)
        srlr = TrainSerializer(train)
        return Response(srlr.data)
    
    def put(self, request, pk, format=None):
        train = self.get_object(pk=pk)
        srlr = TrainSerializer(train, data=request.data)
        if srlr.is_valid():
            srlr.save()
            return Response(srlr.data)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        train = self.get_object(pk)
        train.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TrainCreator(APIView):    
    def post(self, request, format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        train_data = {
            'train_name' : body['train_name'],
            'route_id' : body["route_id"],
            'departing_time': body['departing_time'],
            'number_of_seats': body['number_of_seats']
        }

        srlr = TrainSerializer(data=train_data)
        if srlr.is_valid():
            srlr.save()
            train = Train.objects.get(train_name=body['train_name'])
            Seat.createSeat(train, train)
            return Response(srlr.data , status=status.HTTP_201_CREATED)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)
        

        
