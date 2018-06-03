from rest_framework_gis.serializers import GeoFeatureModelSerializer

from rest_framework.serializers import ModelSerializer

from . import models

class Census1990Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Census1990
        geo_field = "geom"
        fields = "__all__"

class Census2000Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Census2000
        geo_field = "geom"
        fields = "__all__"


class Census2010Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Census2010
        geo_field = "geom"
        fields = "__all__"

class ImsNbrhdDemograpicsSerializer(ModelSerializer):
    class Meta:
        model = models.ImsNbrhdDemographics
        fields = "__all__"

class EvictionsBlockgroupsSerializer(ModelSerializer):
    class Meta:
        model = models.EvictionsBlockgroups
        fields = "__all__"

class Census2010Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Census2010
        geo_field = "geom"
        fields = "__all__"
