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
from seat.serializers import SeatSerializer
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

        train = Train.objects.get(train_name=body['train_name']).id
        sta = Station.objects.get(station_name=body['starting_station'])
        des = Station.objects.get(station_name=body['destination'])
        price = abs(des.station_distance - sta.station_distance)
        if body["ticket_type"] == "Return-trip":
            price = price * 2
        seats = body['seat_number']

        for s in seats:
            if s > 56:
                return Response(f"We don't have that seat number please choose another")

            seat = Seat.objects.filter(train_id=train).get(seat_number=s)
            if seat.is_taken:
                return Response(f"Seat number {s} is already taken.")
            Seat.takeSeat(train, train, s)
            ticket_data = {
                'customer_name': body['customer_name'],
                'customer_phone': body['customer_phone'],
                'customer_email': body['customer_email'],
                'ticket_type': body['ticket_type'],
                'train_id': train,
                'starting_station': sta.id,
                'destination': des.id,
                'seat_number': seat.id
            }
            srlr = TicketSerializer(data=ticket_data)
            if srlr.is_valid():
                srlr.save()
            
        return Response(srlr.data, status=status.HTTP_201_CREATED)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)


