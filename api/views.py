from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import models, serializers

class CrimesList(ListAPIView):
    queryset = models.Crime.objects.all()
    serializer_class = serializers.CrimeSerializer

class AffordableHousingList(ListAPIView):
    queryset = models.AffordableHousing.objects.all()
    serializer_class = serializers.AffordableHousingSerializer

class CampSweepsList(ListAPIView):
    queryset = models.CampSweeps.objects.all()
    serializer_class = serializers.CampSweepsSerializer

class BusStopsList(ListAPIView):
    queryset = models.BusStops.objects.all()
    serializer_class = serializers.BusStopsSerializer

class DemolitionsList(ListAPIView):
    queryset = models.Demolitions.objects.all()
    serializer_class = serializers.DemolitionsSerializer

class HousingAreasList(ListAPIView):
    queryset = models.HousingAreas.objects.all()
    serializer_class = serializers.HousingAreasSerializer

class ParksTrailsList(ListAPIView):
    queryset = models.ParksTrails.objects.all()
    serializer_class = serializers.ParksTrailsSerializer

class SchoolDistrictsList(ListAPIView):
    queryset = models.SchoolDistricts.objects.all()
    serializer_class = serializers.SchoolDistrictsSerializer

class TransitCentersList(ListAPIView):
    queryset = models.TransitCenters.objects.all()
    serializer_class = serializers.TransitCentersSerializer

class VoterPrecinctsList(ListAPIView):
    queryset = models.VoterPrecincts.objects.all()
    serializer_class = serializers.VoterPrecinctsSerializer

class ZipCodesList(ListAPIView):
    queryset = models.ZipCodes.objects.all()
    serializer_class = serializers.ZipCodesSerializer

class ZoningList(ListAPIView):
    queryset = models.Zoning.objects.all()
    serializer_class = serializers.ZoningSerializer