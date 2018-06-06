from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import models, serializers

class ActiveMultiuseTrailList(ListAPIView):
    queryset = models.ActiveMultiuseTrail.objects.all()
    serializer_class = serializers.ActiveMultiUseTrailSerializer

class AffordableHousingList(ListAPIView):
    queryset = models.AffordableHousing.objects.all()
    serializer_class = serializers.AffordableHousingSerializer

class BikeCountLocationsList(ListAPIView):
    queryset = models.BikeCountLocations.objects.all()
    serializer_class = serializers.BikeCountLocationsSerializer

class BikeCountsList(ListAPIView):
    queryset = models.BikeCounts.objects.all()
    serializer_class = serializers.BikeCountsSerializer

class BikeDailyEstimatesList(ListAPIView):
    queryset = models.BikeDailyEstimates.objects.all()
    serializer_class = serializers.BikeDailyEstimatesSerializer

class BikeGreenwaysList(ListAPIView):
    queryset = models.BikeGreenways.objects.all()
    serializer_class = serializers.BikeGreenwaysSerializer

class BikeLanesList(ListAPIView):
    queryset = models.BikeLanes.objects.all()
    serializer_class = serializers.BikeLanesSerializer

class BikeParkingList(ListAPIView):
    queryset = models.BikeParking.objects.all()
    serializer_class = serializers.BikeParkingSerializer

class BusStopsList(ListAPIView):
    queryset = models.BusStops.objects.all()
    serializer_class = serializers.BusStopsSerializer

class CampSweepsList(ListAPIView):
    queryset = models.CampSweeps.objects.all()
    serializer_class = serializers.CampSweepsSerializer

class CommunityGardensList(ListAPIView):
    queryset = models.CommunityGardens.objects.all()
    serializer_class = serializers.CommunityGardensSerializer

class CrimesList(ListAPIView):
    queryset = models.Crime.objects.all()
    serializer_class = serializers.CrimeSerializer

class DemolitionsList(ListAPIView):
    queryset = models.Demolitions.objects.all()
    serializer_class = serializers.DemolitionsSerializer

class HousingAreasList(ListAPIView):
    queryset = models.HousingAreas.objects.all()
    serializer_class = serializers.HousingAreasSerializer

class MetroLimitList(ListAPIView):
    queryset = models.MetroLimit.objects.all()
    serializer_class = serializers.MetroLimitSerializer

class ParkRideLotsList(ListAPIView):
    queryset = models.ParkRideLots.objects.all()
    serializer_class = serializers.ParkRideLotsSerializer

class ParksList(ListAPIView):
    queryset = models.Parks.objects.all()
    serializer_class = serializers.ParksSerializer

class ParksTrailsList(ListAPIView):
    queryset = models.ParksTrails.objects.all()
    serializer_class = serializers.ParksTrailsSerializer

class PercentSharedHousingList(ListAPIView):
    queryset = models.PercentSharedHousing.objects.all()
    serializer_class = serializers.PercentSharedHousingSerializer

class RailStopsList(ListAPIView):
    queryset = models.RailStops.objects.all()
    serializer_class = serializers.RailStopsSerializer

class RetailLocationsList(ListAPIView):
    queryset = models.RetailLocations.objects.all()
    serializer_class = serializers.RetailLocationsSerializer

# class RlisNeighborhoodsList(ListAPIView):
#     queryset = models.RlisNeighborhoods.objects.all()
#     serializer_class = serializers.RlisNeighborhoodsSerializer

# class RlisTaxlot2017List(ListAPIView):
#     queryset = models.RlisTaxlot2017.objects.all()
#     serializer_class = serializers.RlisTaxlot2017Serializer

# class RlisTaxlotPts2015List(ListAPIView):
#     queryset = models.RlisTaxlotPts2015.objects.all()
#     serializer_class = serializers.RlisTaxlotPts2015Serializer

class SchoolDistrictsList(ListAPIView):
    queryset = models.SchoolDistricts.objects.all()
    serializer_class = serializers.SchoolDistrictsSerializer

class ScopeList(ListAPIView):
    queryset = models.Scope.objects.all()
    serializer_class = serializers.ScopeSerializer

class TeacherExperienceList(ListAPIView):
    queryset = models.TeacherExperience.objects.all()
    serializer_class = serializers.TeacherExperienceSerializer

class TeacherExperienceSubtotalsList(ListAPIView):
    queryset = models.TeacherExperienceSubtotals.objects.all()
    serializer_class = serializers.TeacherExperienceSubtotalsSerializer

class TransitCentersList(ListAPIView):
    queryset = models.TransitCenters.objects.all()
    serializer_class = serializers.TransitCentersSerializer

class TreesList(ListAPIView):
    queryset = models.Trees.objects.all()
    serializer_class = serializers.TreesSerializer

class VoterPrecinctsList(ListAPIView):
    queryset = models.VoterPrecincts.objects.all()
    serializer_class = serializers.VoterPrecinctsSerializer

class ZipCodesList(ListAPIView):
    queryset = models.ZipCodes.objects.all()
    serializer_class = serializers.ZipCodesSerializer

class ZoningList(ListAPIView):
    queryset = models.Zoning.objects.all()
    serializer_class = serializers.ZoningSerializer
