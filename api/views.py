from django.shortcuts import render
from django.db import connection
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, exceptions

from . import models, serializers, utils

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

class Census2000List(ListAPIView):
    queryset = models.Census2000.objects.all()
    serializer_class = serializers.Census2000Serializer

class Census2010List(ListAPIView):
    queryset = models.Census2010.objects.all()
    serializer_class = serializers.Census2010Serializer

class DemolitionsList(ListAPIView):
    queryset = models.Demolitions.objects.all()
    serializer_class = serializers.DemolitionsSerializer

class HousingAreasList(ListAPIView):
    queryset = models.HousingAreas.objects.all()
    serializer_class = serializers.HousingAreasSerializer

class NeighborhoodsList(ListAPIView):
    queryset = models.Neighborhoods.objects.all()
    serializer_class = serializers.NeighborhoodsSerializer

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
    # another slow class
    queryset = models.ZipCodes.objects.all()
    serializer_class = serializers.ZipCodesSerializer

class ZoningList(ListAPIView):
    #empty
    queryset = models.Zoning.objects.all()
    serializer_class = serializers.ZoningSerializer

class BlockgroupsElList(ListAPIView):
    # no longer existsCommonMiddleware
    queryset = models.BlockgroupsEl.objects.all()
    serializer_class = serializers.BlockgroupsElSerializer


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
	HAVING count(camp_sweeps) > 3;
    """
    with connection.cursor() as cursor:
        cursor.execute(raw_sql_query, )
        result = utils.dictfetchall(cursor)
    return Response(data=result)
