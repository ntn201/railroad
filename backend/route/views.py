from django.shortcuts import render
from .models import Route
from .serializers import RouteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class RouteList(APIView):
    def get(self, request, format=None):
        route = Route.objects.all()
        srlr = RouteSerializer(route, many=True)
        return Response(srlr.data)

    def post(self, request, format=None):
        srlr = RouteSerializer(data=request.data)
        if srlr.is_valid():
            srlr.save()
            return Response(srlr.data, status=status.HTTP_201_CREATED)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)

class RouteDetail(APIView):
    def get_object(self, pk):
        try:
            return Route.objects.get(pk=pk)
        except Route.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        route = self.get_object(pk=pk)
        srlr = RouteSerializer(route)
        return Response(srlr.data)
    
    def put(self, request, pk, format=None):
        route = self.get_object(pk=pk)
        srlr = RouteSerializer(route, data=request.data)
        if srlr.is_valid():
            srlr.save()
            return Response(srlr.data)
        return Response(srlr.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        route = self.get_object(pk)
        route.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

