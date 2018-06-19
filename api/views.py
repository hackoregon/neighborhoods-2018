from django.shortcuts import render
from django.db import connection
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, exceptions

from . import models, serializers, utils, filters
from .pagination import LargeResultSetPagination

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
    queryset = models.CampSweeps.objects.only('reportdate', 'id', 'geom', 'location').all()
    serializer_class = serializers.CampSweepsSerializer
    pagination_class = LargeResultSetPagination

class CampReportList(ListAPIView):
    queryset = models.CampReports.objects.all()
    serializer_class = serializers.CampReportsSerializer

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

class NeighborhoodVoterRegistrationByAgeGroupList(ListAPIView):
    queryset = models.NeighborhoodVoterRegistrationByAgeGroup.objects.all()
    serializer_class = serializers.NeighborhoodVoterRegistrationByAgeGroupSerializer
    pagination_class = LargeResultSetPagination
    filter_fields = ('year', 'neighborhood')

class NeighborhoodVoterRegistrationByAgeGroupGeomList(ListAPIView):
    queryset = models.NeighborhoodVoterRegistrationByAgeGroupGeom.objects.all()
    serializer_class = serializers.NeighborhoodVoterRegistrationByAgeGroupGeomSerializer
    pagination_class = LargeResultSetPagination
    filter_fields = ('year', 'neighborhood')

class ODEFRLunchList(ListAPIView):
    queryset = models.ODEFRLunch.objects.all()
    serializer_class = serializers.ODEFRLunchSerializer

class ODEEnrollmentList(ListAPIView):
    queryset = models.ODEEnrollment.objects.all()
    serializer_class = serializers.ODEEnrollmentSerializer

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

class SchoolClassSizeList(ListAPIView):
    queryset = models.SchoolDemographics.objects.filter(
        teacher_experience__isnull=False,
        class_size__isnull=False
    ).only(
        'name', 'year', 'teacher_experience', 'class_size', 'type'
    ).all()
    serializer_class = serializers.SchoolClassSizeSerializer
    filter_fields = ('year',)
    filter_backends = (filters.SchoolClassSizeFilter,)

class SchoolDemographicsList(ListAPIView):
    queryset = models.SchoolDemographics.objects.all()
    serializer_class = serializers.SchoolDemographicsSerializer
    filter_fields = ('year', 'type', 'name')
    filter_backends = (filters.SchoolDemographicsFilter,)

class SchoolDemographicsTotalsList(ListAPIView):
    queryset = models.SchoolDemographicsTotals.objects.all()
    serializer_class = serializers.SchoolDemographicsTotalsSerializer

class SchoolDemographicsCountList(ListAPIView):
    queryset = models.SchoolDemographicsCount.objects.all()
    serializer_class = serializers.SchoolDemographicsCountSerializer
    filter_fields = ('year', 'name', 'type')

class SchoolDemographicsReducedLunchesList(ListAPIView):
    queryset = models.SchoolDemographicsReducedLunches.objects.all()
    serializer_class = serializers.SchoolDemographicsReducedLunchesSerializer
    filter_fields = ('year', 'name', 'type')
    filter_backends = (filters.SchoolDemographicsFilter,)

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

class VoterMovementAngleByAgeList(ListAPIView):
    queryset = models.VoterMovementAngleByAge.objects.all()
    serializer_class = serializers.VoterMovementAngleByAgeSerializer

class VoterMovementAverageByAgeList(ListAPIView):
    queryset = models.VoterMovementAverageByAge.objects.all()
    serializer_class = serializers.VoterMovementAverageByAgeSerializer

class VoterMovementCountByAgeList(ListAPIView):
    queryset = models.VoterMovementCountByAge.objects.all()
    serializer_class = serializers.VoterMovementCountByAgeSerializer

class VoterPrecinctsList(ListAPIView):
    queryset = models.VoterPrecincts.objects.all()
    serializer_class = serializers.VoterPrecinctsSerializer

class VoterRegistrationByAgeList(ListAPIView):
    queryset = models.VoterRegistrationByAge.objects.all()
    serializer_class = serializers.VoterRegistrationByAgeSerializer

class ZipCodesList(ListAPIView):
    # another slow class
    queryset = models.ZipCodes.objects.all()
    serializer_class = serializers.ZipCodesSerializer

class ZoningList(ListAPIView):
    #empty
    queryset = models.Zoning.objects.all()
    serializer_class = serializers.ZoningSerializer

@api_view(http_method_names=['GET'])
def camp_sweeps_by_time(request):
    """
    Number of camp sweeps by time.  Optional query parameters are:
    Query params: timeframe
    options: 'month', 'week'
    default: 'week'
    """
    timeframe = request.query_params.get('timeframe', 'week').lower()

    if timeframe not in ('week', 'month'):
        msg = 'Invalid query parameter "%s": must be either "week", or "month"' % timeframe
        return Response({'error': msg}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    raw_sql_query = """SELECT count(*),
        date_trunc(%s, reportdate) as report_time
        FROM camp_sweeps
        GROUP BY report_time
        ORDER BY report_time ASC;"""

    with connection.cursor() as cursor:
        cursor.execute(raw_sql_query, [timeframe])
        result = utils.dictfetchall(cursor)

    return Response(data=result)

@api_view(http_method_names=['GET'])
def camp_sweeps_by_neighborhood(request):
    """
    Total number of camp sweeps broken down by neighborhood.
    """
    raw_sql_query = """
    SELECT count(camp_sweeps.id) AS sweep_count, rlis_neighborhoods.name
    FROM camp_sweeps
	INNER JOIN rlis_neighborhoods ON st_intersects(camp_sweeps.geom, rlis_neighborhoods.geom)
	GROUP BY rlis_neighborhoods.name, rlis_neighborhoods.geom
	HAVING count(camp_sweeps) > 3
    ORDER BY 1 DESC;
    """
    with connection.cursor() as cursor:
        cursor.execute(raw_sql_query, )
        result = utils.dictfetchall(cursor)
    return Response(data=result)

@api_view(http_method_names=['GET'])
def school_names(request):
    """
    Simple list of unique school names from our School Demographics model.
    """
    names = models.SchoolDemographics.objects.order_by('name').distinct('name').values_list('name', flat=True)
    return Response(data=names)

@api_view(http_method_names=['GET'])
def neighborhood_names(request):
    """
    List available Neighborhood names for filtering `api/neighborhood_ages`
    """
    names = models.NeighborhoodVoterRegistrationByAgeGroup.objects.order_by(
        'neighborhood'
    ).distinct('neighborhood').values_list('neighborhood', flat=True)
    return Response(data=names)