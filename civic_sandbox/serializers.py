from rest_framework_gis.serializers import GeoFeatureModelSerializer

from rest_framework.serializers import ModelSerializer

from .models import BikeParking, BikeLane, TaxLotBlockGroup, Park, ParksTrail, MultiuseTrail, CommunityGarden, BikeGreenway, RailStop, Demolition, CampSweep, CampReport

class BikeParkingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BikeParking
        fields = '__all__'
        geo_field = 'geom'

class BikeLaneSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BikeLane
        fields = '__all__'
        geo_field = 'geom'
    
class TaxLotBlockGroupSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TaxLotBlockGroup
        geo_field = 'geom'
        fields = '__all__'

class ParkSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Park
        geo_field = 'geom'
        fields = '__all__'

class ParksTrailSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ParksTrail
        geo_field = 'geom'
        fields = '__all__'

class MultiuseTrailSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MultiuseTrail
        geo_field = 'geom'
        fields = '__all__'

class CommunityGardenSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CommunityGarden
        geo_field = 'geom'
        fields = '__all__'

class BikeGreenwaySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BikeGreenway
        geo_field = 'geom'
        fields = '__all__'

class RailStopSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RailStop
        geo_field = 'geom'
        fields = '__all__'
    
class DemolitionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Demolition
        geo_field = 'geom'
        fields = '__all__'

    
class CampSweepSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CampSweep
        geo_field = 'geom'
        fields = '__all__'

class CampReportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CampReport
        geo_field = 'geom'
        fields = '__all__'