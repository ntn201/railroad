from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Ticket
from .serializers import TicketSerializer
from train.models import Train
from station.models import Station
from seat.models import Seat
import json

# Create your views here.
class TicketList(APIView):
    def get(self, request, format=None):
        ticket = Ticket.objects.all()
        srlr = TicketSerializer(ticket, many=True)
        return Response(srlr.data)

    def post(self, request, format=None):
        srlr = TicketSerializer(data=request.data)
        if srlr.is_valid():
            srlr.save()
            return Response(srlr.data, status=status.HTTP_201_CREATED)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetail(APIView):
    def get_object(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ticket = self.get_object(pk=pk)
        srlr = TicketSerializer(ticket)
        return Response(srlr.data)

    def put(self, request, pk, format=None):
        ticket = self.get_object(pk=pk)
        srlr = TicketSerializer(ticket, data=request.data)
        if srlr.is_valid():
            srlr.save()
            return Response(srlr.data)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ticket = self.get_object(pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketCreator(APIView):
    def post(self, request, format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        train = Train.objects.get(train_name=body['train_name'])
        sta = Station.objects.get(station_name=body['starting_station'])
        des = Station.objects.get(station_name=body['destination'])
        seats = body['seat_number']

        for s in seats:
            seat = Seat.objects.filter(train_name=body['train_name']).get(seat_number=s)
            ticket_data = {
                'customer_name': body['customer_name'],
                'customer_phone': body['customer_phone'],
                'customer_email': body['customer_email'],
                'ticket_type': body['ticket_type'],
                'train_name': train.id,
                'starting_station': sta.id,
                'destination': des.id,
                'seat_number': seat.id,
                'price': 10,
            }

            srlr = TicketSerializer(data=ticket_data)
            if srlr.is_valid():
                srlr.save()
                return Response(srlr.data, status=status.HTTP_201_CREATED)
            return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)


