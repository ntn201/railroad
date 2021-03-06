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
from schedule.models import Schedule
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

        
        price = abs(Schedule.objects.filter(route_id=Train.objects.get(id = body['train_id']).route_id).get(station_id=body['destination_id']).travel_time - Schedule.objects.filter(route_id=Train.objects.get(id = body['train_id']).route_id).get(station_id=body['departing_id']).travel_time)
        if body["ticket_type"] == "Return-trip":
            price = price * 2
        seats = body['seat_number']

        for s in seats:
            if s > 56:
                return Response(f"We don't have that seat number please choose another")

            seat = Seat.objects.filter(train_id=body['train_id']).get(seat_number=s)
            if seat.is_taken:
                return Response(f"Seat number {s} is already taken.")
            Seat.takeSeat(body['train_id'], body['train_id'], s)
            ticket_data = {
                'customer_name': body['customer_name'],
                'customer_id': body['customer_id'],
                'customer_phone': body['customer_phone'],
                'ticket_type': body['ticket_type'],
                'train_id': body['train_id'],
                'departing_id': body['departing_id'],
                'destination_id': body['destination_id'],
                'seat_number': seat.id,
                'price': price
            }
            srlr = TicketSerializer(data=ticket_data)
            if srlr.is_valid():
                srlr.save()
            
        return Response(srlr.data, status=status.HTTP_201_CREATED)


