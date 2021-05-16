from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Station
from .serializers import StationSerializer


@csrf_exempt
def station_list(request):
    if request.method == 'GET':
        stations = Station.objects.all()
        srlr = StationSerializer(stations, many=True)
        return JsonResponse(srlr.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        srlr = StationSerializer(data=data)
        if srlr.is_valid():
            srlr.save()
            return JsonResponse(srlr.data, status=201)
        return JsonResponse(srlr.errors, status=400)
        