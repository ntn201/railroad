from django.shortcuts import render
from .models import Route
from station.models import Station

# Create your views here.
def find_route(starting, destination):
    sta = Station.objects.get(name=starting)
    des = Station.objects.get(name=destination)

    sta_routes = Route.objects.filter(station=sta)
    des_routes = Route.objects.filter(station=des)

    for des_route in des_routes.all():
        for sta_route in sta_routes.all():
            if des_route.train_id == sta_route.train_id and des_route.arrive_order > sta_route.arrive_order:
                return des_route.train_id
        


