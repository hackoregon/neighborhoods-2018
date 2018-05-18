from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import models, serializers

class CrimesList(ListAPIView):
    queryset = models.Crime.objects.all()
    serializer_class = serializers.CrimeSerializer

class AffordableHousingList(ListAPIView):
    queryset = models.AffordableHousing.objects.all()
    serializer_class = serializers.AffordableHousingSerializer

class CampCleanupsList(ListAPIView):
    queryset = models.CampCleanups.objects.all()
    serializer_class = serializers.CampCleanupsSerializer

class DatCrimeNeighList(ListAPIView):
    queryset = models.DatCrimeNeigh.objects.all()
    serializer_class = serializers.DatCrimeNeighSerializer