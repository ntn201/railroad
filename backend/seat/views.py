from django.shortcuts import render
from .models import Seat
from .serializers import SeatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from train.models import Train

class SeatList(APIView):
    def get(self, request, format=None):
        seat = Seat.objects.all()
        srlr = SeatSerializer(seat, many=True)
        return Response(srlr.data)

    def post(self, request, format=None):
        srlr = SeatSerializer(data=request.data)
        if srlr.is_valid():
            srlr.save()
            return Response(srlr.data, status=status.HTTP_201_CREATED)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)

class SeatDetail(APIView):
    def get_object(self, pk):
        try:
            return Seat.objects.get(pk=pk)
        except Seat.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        seat = self.get_object(pk=pk)
        srlr = SeatSerializer(seat)
        return Response(srlr.data)
    
    def put(self, request, pk, format=None):
        seat = self.get_object(pk=pk)
        srlr = SeatSerializer(seat, data=request.data)
        if srlr.is_valid():
            srlr.save()
            return Response(srlr.data)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        seat = self.get_object(pk)
        seat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



