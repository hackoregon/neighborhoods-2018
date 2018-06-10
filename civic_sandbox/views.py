
from rest_framework.decorators import api_view
from .models import BikeParking, BikeLane, TaxLotBlockGroup, Park, ParksTrail, MultiuseTrail, CommunityGarden, BikeGreenway, RailStop, Demolition, CampSweep, CampReport
from .serializers import BikeParkingSerializer, BikeLaneSerializer, TaxLotBlockGroupSerializer, ParkSerializer, ParksTrailSerializer, MultiuseTrailSerializer, CommunityGardenSerializer, BikeGreenwaySerializer, RailStopSerializer, DemolitionSerializer, CampSweepSerializer, CampReportSerializer
from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from .helpers import sandbox_view_factory
from .meta import bike_parking_meta, bike_lanes_meta, taxlot_block_groups_meta, parks_meta, parks_trails_meta, multiuse_trails_meta, community_gardens_meta, bike_greenways_meta, rail_stops_meta, demolitions_meta, camp_sweeps_meta, camp_reports_meta



bikeparking = sandbox_view_factory(
  model_class=BikeParking,
  serializer_class=BikeParkingSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom',
  attributes =bike_parking_meta['attributes'],
  dates=bike_parking_meta['dates'],
  )

bikelanes = sandbox_view_factory(
  model_class=BikeLane,
  serializer_class=BikeLaneSerializer,
  multi_geom_class=MultiLineString,
  geom_field='geom',
  attributes =bike_lanes_meta['attributes'],
  dates=bike_lanes_meta['dates'], 
  )

taxlotblockgroups = sandbox_view_factory(
  model_class=TaxLotBlockGroup,
  serializer_class=TaxLotBlockGroupSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =taxlot_block_groups_meta['attributes'],
  dates=taxlot_block_groups_meta['dates'], 
  )

parks = sandbox_view_factory(
  model_class=Park,
  serializer_class=ParkSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =parks_meta['attributes'],
  dates=parks_meta['dates'], 
  )

parkstrails = sandbox_view_factory(
  model_class=ParksTrail,
  serializer_class=ParksTrailSerializer,
  multi_geom_class=MultiLineString,
  geom_field='geom',
  attributes =parks_trails_meta['attributes'],
  dates=parks_trails_meta['dates'], 
  )

multiusetrails = sandbox_view_factory(
  model_class=MultiuseTrail,
  serializer_class=MultiuseTrailSerializer,
  multi_geom_class=MultiLineString,
  geom_field='geom',
  attributes =multiuse_trails_meta['attributes'],
  dates=multiuse_trails_meta['dates'], 
  )

communitygardens = sandbox_view_factory(
  model_class=CommunityGarden,
  serializer_class=CommunityGardenSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =community_gardens_meta['attributes'],
  dates=community_gardens_meta['dates'], 
  )

bikegreenways = sandbox_view_factory(
  model_class=BikeGreenway,
  serializer_class=BikeGreenwaySerializer,
  multi_geom_class=MultiLineString,
  geom_field='geom',
  attributes =bike_greenways_meta['attributes'],
  dates=bike_greenways_meta['dates'], 
  )

railstops = sandbox_view_factory(
  model_class=RailStop,
  serializer_class=RailStopSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom',
  attributes =rail_stops_meta['attributes'],
  dates=rail_stops_meta['dates'], 
  )

demolitions = sandbox_view_factory(
  model_class=Demolition,
  serializer_class=DemolitionSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom',
  attributes =demolitions_meta['attributes'],
  dates=demolitions_meta['dates'], 
  )

campsweeps = sandbox_view_factory(
  model_class=CampSweep,
  serializer_class=CampSweepSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom',
  attributes =camp_sweeps_meta['attributes'],
  dates=camp_sweeps_meta['dates'], 
  )

campreports = sandbox_view_factory(
  model_class=CampReport,
  serializer_class=CampReportSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom',
  attributes =camp_reports_meta['attributes'],
  dates=camp_reports_meta['dates'], 
  )