
from rest_framework.decorators import api_view
from .models import BikeParking, BikeLane, TaxLotBlockGroup, Park
from .serializers import BikeParkingSerializer, BikeLaneSerializer, TaxLotBlockGroupSerializer, ParksSerializer
from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from .helpers import sandbox_view_factory
from .meta import bikeparking_meta, bikelanes_meta, taxlot_block_groups_meta, parks_meta



bikeparking = sandbox_view_factory(
  model_class=BikeParking,
  serializer_class=BikeParkingSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom',
  attributes =bikeparking_meta['attributes'],
  dates=bikeparking_meta['dates'],
  )

bikelanes = sandbox_view_factory(
  model_class=BikeLane,
  serializer_class=BikeLaneSerializer,
  multi_geom_class=MultiLineString,
  geom_field='geom',
  attributes =bikelanes_meta['attributes'],
  dates=bikelanes_meta['dates'], 
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
  serializer_class=ParksSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =parks_meta['attributes'],
  dates=parks_meta['dates'], 
  )
