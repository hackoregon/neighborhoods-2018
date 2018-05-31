from rest_framework_gis.serializers import GeoFeatureModelSerializer

from . import models

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
