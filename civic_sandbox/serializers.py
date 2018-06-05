from rest_framework_gis.serializers import GeoFeatureModelSerializer

from rest_framework.serializers import ModelSerializer

from .models import BikeParking, BikeLane, TaxLotBlockGroup

class BikeParkingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BikeParking
        fields = "__all__"
        geo_field = 'geom'

class BikeLaneSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BikeLane
        fields = "__all__"
        geo_field = 'geom'
    
class TaxLotBlockGroupSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TaxLotBlockGroup
        geo_field = "geom"
        fields = "__all__"