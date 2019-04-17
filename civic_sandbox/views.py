
from rest_framework.decorators import api_view
from .models import BikeParking, BikeLane, Park, ParksTrail, MultiuseTrail, CommunityGarden, BikeGreenway, RailStop, Demolition, CampSweep, CampReport, RetailGrocer, Tree, BusStop, IMSNeighborhood, BlockGroup, NeighborhoodVoterRegistrationByAgeGroup, ReportsByMonth, BikeCount, BikeDailyEstimate

from .serializers import BikeParkingSerializer, BikeLaneSerializer, ParkSerializer, ParksTrailSerializer, MultiuseTrailSerializer, CommunityGardenSerializer, BikeGreenwaySerializer, RailStopSerializer, DemolitionSerializer, CampSweepSerializer, CampReportSerializer, RetailGrocerSerializer, TreeSerializer, BusStopSerializer, Under18Serializer, Over65Serializer, PopulationSerializer, IncomeSerializer, OwnerOccupiedSerializer, LivingAloneSerializer,GrossRentSerializer, EvictionsSerializer, RenterOccupiedSerializer, RentBurdenSerializer, PctRenterOccupiedSerializer, Voters18to25Serializer, Voters26to32Serializer, Voters33to39Serializer, Voters40to49Serializer, Voters50plusSerializer, ReportsByMonthSerializer, BikeDailyEstimateSerializer, BikeCountSerializer, EvictionRateSerializer, PovertyRateSerializer

from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from .helpers import sandbox_view_factory 

from .meta import bike_parking_meta, bike_lanes_meta,parks_meta, parks_trails_meta, multiuse_trails_meta, community_gardens_meta, bike_greenways_meta, rail_stops_meta, demolitions_meta, camp_sweeps_meta, camp_reports_meta, retail_grocers_meta, trees_meta, bus_stops_meta, under18_meta, over65_meta, population_meta, owner_occupied_meta, living_alone_meta,  bg_income_meta, bg_evictions_meta, bg_gross_rent_meta, bg_pctrenter_occupied_meta, bg_rent_burden_meta, bg_renter_occupied_meta, voters18to25_meta, voters26to32_meta, voters33to39_meta, voters40to49_meta, voters50plus_meta, reports_month_meta, bike_counts_meta, bike_daily_meta, bg_eviction_rate_meta, bg_poverty_rate_meta




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

retailgrocers = sandbox_view_factory(
  model_class=RetailGrocer,
  serializer_class=RetailGrocerSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom',
  attributes =retail_grocers_meta['attributes'],
  dates=retail_grocers_meta['dates'], 
  )


trees = sandbox_view_factory(
  model_class=Tree,
  serializer_class=TreeSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom',
  attributes =trees_meta['attributes'],
  dates=trees_meta['dates'], 
  )

busstops = sandbox_view_factory(
  model_class=BusStop,
  serializer_class=BusStopSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom',
  attributes =bus_stops_meta['attributes'],
  dates=bus_stops_meta['dates'], 
  )

under18 = sandbox_view_factory(
  model_class=IMSNeighborhood,
  serializer_class=Under18Serializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =under18_meta['attributes'],
  dates=under18_meta['dates'], 
  )

over65 = sandbox_view_factory(
  model_class=IMSNeighborhood,
  serializer_class=Over65Serializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =over65_meta['attributes'],
  dates=over65_meta['dates'], 
  )

population = sandbox_view_factory(
  model_class=IMSNeighborhood,
  serializer_class=PopulationSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =population_meta['attributes'],
  dates=population_meta['dates'], 
  )


owneroccupied = sandbox_view_factory(
  model_class=IMSNeighborhood,
  serializer_class=OwnerOccupiedSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =population_meta['attributes'],
  dates=population_meta['dates'], 
  )

livingalone = sandbox_view_factory(
  model_class=IMSNeighborhood,
  serializer_class=LivingAloneSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =living_alone_meta['attributes'],
  dates=living_alone_meta['dates'], 
  )

income = sandbox_view_factory(
  model_class=BlockGroup,
  serializer_class=IncomeSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =bg_income_meta['attributes'],
  dates=bg_income_meta['dates'], 
  )

evictions = sandbox_view_factory(
  model_class=BlockGroup,
  serializer_class=EvictionsSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =bg_evictions_meta['attributes'],
  dates= bg_evictions_meta['dates'], 
  )


grossrent = sandbox_view_factory(
  model_class=BlockGroup,
  serializer_class=GrossRentSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =bg_gross_rent_meta['attributes'],
  dates= bg_gross_rent_meta['dates'], 
  )

pctrenteroccupied = sandbox_view_factory(
  model_class=BlockGroup,
  serializer_class=PctRenterOccupiedSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =bg_pctrenter_occupied_meta['attributes'],
  dates= bg_pctrenter_occupied_meta['dates'], 
  )

rentburden = sandbox_view_factory(
  model_class=BlockGroup,
  serializer_class=RentBurdenSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =bg_rent_burden_meta['attributes'],
  dates= bg_rent_burden_meta['dates'], 
  )

renteroccupied = sandbox_view_factory(
  model_class=BlockGroup,
  serializer_class=RenterOccupiedSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =bg_renter_occupied_meta['attributes'],
  dates= bg_renter_occupied_meta['dates'], 
  )

evictionrate = sandbox_view_factory(
  model_class=BlockGroup,
  serializer_class=EvictionRateSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =bg_eviction_rate_meta['attributes'],
  dates= bg_eviction_rate_meta['dates'], 
  )

povertyrate = sandbox_view_factory(
  model_class=BlockGroup,
  serializer_class=PovertyRateSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =bg_poverty_rate_meta['attributes'],
  dates= bg_poverty_rate_meta['dates'], 
  )


voters18to25 = sandbox_view_factory(
  model_class=NeighborhoodVoterRegistrationByAgeGroup,
  serializer_class=Voters18to25Serializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =voters18to25_meta['attributes'],
  dates= voters18to25_meta['dates'], 
  )

voters26to32 = sandbox_view_factory(
  model_class=NeighborhoodVoterRegistrationByAgeGroup,
  serializer_class=Voters26to32Serializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =voters26to32_meta['attributes'],
  dates= voters26to32_meta['dates'], 
  )

voters33to39 = sandbox_view_factory(
  model_class=NeighborhoodVoterRegistrationByAgeGroup,
  serializer_class=Voters33to39Serializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =voters33to39_meta['attributes'],
  dates= voters33to39_meta['dates'], 
  )

voters40to49 = sandbox_view_factory(
  model_class=NeighborhoodVoterRegistrationByAgeGroup,
  serializer_class=Voters40to49Serializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =voters40to49_meta['attributes'],
  dates= voters40to49_meta['dates'], 
  )

voters50plus = sandbox_view_factory(
  model_class=NeighborhoodVoterRegistrationByAgeGroup,
  serializer_class=Voters50plusSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =voters50plus_meta['attributes'],
  dates= voters50plus_meta['dates'], 
  )

reportsbymonth = sandbox_view_factory(
  model_class=ReportsByMonth,
  serializer_class=ReportsByMonthSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='geom',
  attributes =reports_month_meta['attributes'],
  dates= reports_month_meta['dates'], 
  )

bikecounts = sandbox_view_factory(
  model_class=BikeCount,
  serializer_class=BikeCountSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom',
  attributes =bike_counts_meta['attributes'],
  dates= bike_counts_meta['dates'], 
  )


bikeestimates = sandbox_view_factory(
  model_class=BikeDailyEstimate,
  serializer_class=BikeDailyEstimateSerializer,
  multi_geom_class=MultiPoint,
  geom_field='geom',
  attributes =bike_daily_meta['attributes'],
  dates= bike_daily_meta['dates'], 
  )