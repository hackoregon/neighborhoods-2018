from rest_framework_gis.serializers import GeoFeatureModelSerializer

from . import models

class CrimeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Crime
        geo_field = 'geom'
        exclude = ('lat', 'lon',)

class AffordableHousingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.AffordableHousing
        geo_field = "geom"
        exclude = ('lat', 'long',)

class CampSweepsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.CampSweeps
        geo_field = "geom"
        exclude = ('lat', 'long',)

class BusStopsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.BusStops
        geo_field = "geom"
        fields = "__all__"

class DemolitionsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Demolitions
        geo_field = "geom"
        fields = "__all__"

class HousingAreasSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.HousingAreas
        geo_field = "geom"
        fields = "__all__"

class NeighborhoodsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Neighborhoods
        geo_field = "geom"
        fields = "__all__"

class ParksTrailsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.ParksTrails
        geo_field = "geom"
        fields = "__all__"

class SchoolDistrictsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.SchoolDistricts
        geo_field = "geom"
        fields = "__all__"

class TransitCentersSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.TransitCenters
        geo_field = "geom"
        fields = "__all__"

class VoterPrecinctsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.VoterPrecincts
        geo_field = "geom"
        fields = "__all__"

class ZipCodesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.ZipCodes
        geo_field = "geom"
        fields = "__all__"

class ZoningSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Zoning
        geo_field = "geom"
        fields = "__all__"
