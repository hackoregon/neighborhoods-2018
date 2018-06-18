from rest_framework_gis.serializers import GeoFeatureModelSerializer

from rest_framework.serializers import ModelSerializer

from . import models

class ActiveMultiUseTrailSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.ActiveMultiuseTrail
        geo_field = "geom"
        fields = "__all__"

class AffordableHousingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.AffordableHousing
        geo_field = "geom"
        exclude = ('lat', 'long',)

class BikeCountLocationsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.BikeCountLocations
        geo_field = "geom"
        fields = "__all__"

class BikeCountsSerializer(ModelSerializer):
    class Meta:
        model = models.BikeCounts
        fields = "__all__"

class BikeDailyEstimatesSerializer(ModelSerializer):
    class Meta:
        model = models.BikeDailyEstimates
        fields = "__all__"

class BikeGreenwaysSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.BikeGreenways
        geo_field = "geom"
        fields = "__all__"

class BikeLanesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.BikeLanes
        geo_field = "geom"
        fields = "__all__"

class BikeParkingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.BikeParking
        geo_field = "geom"
        fields = "__all__"

class BusStopsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.BusStops
        geo_field = "geom"
        fields = "__all__"

class CampSweepsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.CampSweeps
        geo_field = "geom"
        fields = ('id', 'geom', 'reportdate', 'location')


class CampReportsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.CampReports
        geo_field = "geom"
        fields = "__all__"

class CommunityGardensSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.CommunityGardens
        geo_field = "geom"
        fields = "__all__"

class CrimeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Crime
        geo_field = 'geom'
        exclude = ('lat', 'lon',)

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


class HousingAreasSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.HousingAreas
        geo_field = "geom"
        fields = "__all__"

class MetroLimitSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.MetroLimit
        geo_field = "geom"
        fields = "__all__"

class NeighborhoodVoterRegistrationByAgeGroupSerializer(ModelSerializer):
    class Meta:
        model = models.NeighborhoodVoterRegistrationByAgeGroup
        fields = "__all__"

class NeighborhoodVoterRegistrationByAgeGroupGeomSerializer(ModelSerializer):
    class Meta:
        model = models.NeighborhoodVoterRegistrationByAgeGroupGeom
        fields = "__all__"

class ODEEnrollmentSerializer(ModelSerializer):
    class Meta:
        model = models.ODEEnrollment
        fields = "__all__"

class ODEFRLunchSerializer(ModelSerializer):
    class Meta:
        model = models.ODEFRLunch
        fields = "__all__"

class ParkRideLotsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.ParkRideLots
        geo_field = "geom"
        fields = "__all__"

class ParksSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Parks
        geo_field = "geom"
        fields = "__all__"


class ParksTrailsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.ParksTrails
        geo_field = "geom"
        fields = "__all__"

class PercentSharedHousingSerializer(ModelSerializer):
    class Meta:
        model = models.PercentSharedHousing
        fields = "__all__"

class RailStopsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.RailStops
        geo_field = "geom"
        fields = "__all__"

class RetailLocationsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.RetailLocations
        geo_field = "geom"
        fields = "__all__"

class SchoolClassSizeSerializer(ModelSerializer):
    class Meta:
        model = models.SchoolDemographics
        fields = ('name', 'year', 'teacher_experience', 'class_size', 'type')

class SchoolDemographicsSerializer(ModelSerializer):
    class Meta:
        model = models.SchoolDemographics
        fields = "__all__"

class SchoolDemographicsTotalsSerializer(ModelSerializer):
    class Meta:
        model = models.SchoolDemographicsTotals
        fields = "__all__"

class SchoolDistrictsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.SchoolDistricts
        geo_field = "geom"
        fields = "__all__"

class ScopeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Scope
        geo_field = "geom"
        fields = "__all__"

class TeacherExperienceSerializer(ModelSerializer):
    class Meta:
        model = models.TeacherExperience
        fields = "__all__"

class TeacherExperienceSubtotalsSerializer(ModelSerializer):
    class Meta:
        model = models.TeacherExperienceSubtotals
        fields = "__all__"

class TransitCentersSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.TransitCenters
        geo_field = "geom"
        fields = "__all__"

class TreesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.Trees
        geo_field = "geom"
        fields = "__all__"

class VoterMovementAngleByAgeSerializer(ModelSerializer):
    class Meta:
        model = models.VoterMovementAngleByAge
        # exclude = ('id',)
        fields = "__all__"

class VoterMovementAverageByAgeSerializer(ModelSerializer):
    class Meta:
        model = models.VoterMovementAverageByAge
        exclude = ('id',)

class VoterMovementCountByAgeSerializer(ModelSerializer):
    class Meta:
        model = models.VoterMovementCountByAge
        exclude = ('id',)

class VoterPrecinctsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = models.VoterPrecincts
        geo_field = "geom"
        fields = "__all__"

class VoterRegistrationByAgeSerializer(ModelSerializer):
    class Meta:
        model = models.VoterRegistrationByAge
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
