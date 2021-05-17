from django.shortcuts import render
from .models import Train
from .serializers import TrainSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class TrainList(APIView):
    def get(self, request, format=None):
        train = Train.objects.all()
        srlr = TrainSerializer(train, many=True)
        return Response(srlr.data)

    def post(self, request, format=None):
        srlr = TrainSerializer(data=request.data)
        if srlr.is_valid():
            srlr.save()
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

