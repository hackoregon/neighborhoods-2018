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

class CampCleanupsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.CampCleanups
        geo_field = "geom"
        exclude = ('lat', 'long',)

class DatCrimeNeighSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.DatCrimeNeigh
        geo_field = "geom"
        exclude = ('lat', 'long',)
