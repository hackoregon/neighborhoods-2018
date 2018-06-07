
from django.contrib.gis.db import models


class ActiveMultiuseTrail(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    tranplanid = models.CharField(max_length=20, blank=True, null=True)
    segmentnam = models.CharField(max_length=35, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    facility = models.CharField(max_length=3, blank=True, null=True)
    yearbuilt = models.IntegerField(blank=True, null=True)
    yearretire = models.IntegerField(blank=True, null=True)
    lengthmile = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_le_1 = models.FloatField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_multiuse_trail'


class AffordableHousing(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    total_unit = models.IntegerField()
    affordable = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=25)
    concat = models.CharField(max_length=100)
    county = models.CharField(max_length=50)
    alcohol_an = models.CharField(max_length=50)
    developmen = models.IntegerField()
    elderly = models.IntegerField()
    ex_release = models.IntegerField()
    family = models.IntegerField()
    agricultur = models.IntegerField()
    homeless = models.IntegerField()
    physical_d = models.IntegerField()
    veterans = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()
    geom = models.MultiPointField()

    class Meta:
        managed = False
        db_table = 'affordable_housing'


class BikeCountLocations(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    sector = models.CharField(max_length=5, blank=True, null=True)
    counttype = models.CharField(max_length=10, blank=True, null=True)
    counttime = models.CharField(max_length=10, blank=True, null=True)
    year_loc_a = models.CharField(max_length=5, blank=True, null=True)
    priority = models.CharField(max_length=15, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bike_count_locations'


class BikeCounts(models.Model):
   id = models.IntegerField(primary_key=True)
   # Field name made lowercase.
   sector = models.CharField(db_column="Sector", max_length=15)
   # Field name made lowercase.
   location = models.CharField(db_column="Location", max_length=50)
   count_time = models.CharField(max_length=5)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2017 = models.IntegerField(db_column="2017", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2016 = models.IntegerField(db_column="2016", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2015 = models.IntegerField(db_column="2015", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2014 = models.IntegerField(db_column="2014", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2013 = models.IntegerField(db_column="2013", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2012 = models.IntegerField(db_column="2012", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2011 = models.IntegerField(db_column="2011", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2010 = models.IntegerField(db_column="2010", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2009 = models.IntegerField(db_column="2009", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2008 = models.IntegerField(db_column="2008", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2007 = models.IntegerField(db_column="2007", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2006 = models.IntegerField(db_column="2006", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2005 = models.IntegerField(db_column="2005", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2004 = models.IntegerField(db_column="2004", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2003 = models.IntegerField(db_column="2003", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2002 = models.IntegerField(db_column="2002", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2001 = models.IntegerField(db_column="2001", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2000 = models.IntegerField(db_column="2000", blank=True, null=True)
   prior_to_2000 = models.IntegerField(blank=True, null=True)

   class Meta:
       managed = False
       db_table = "bike_counts"


class BikeDailyEstimates(models.Model):
   # Field name made lowercase.
   sector = models.CharField(db_column="Sector", max_length=15)
   id = models.IntegerField(primary_key=True)
   # Field name made lowercase.
   location = models.CharField(db_column="Location", max_length=50)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2016 = models.IntegerField(db_column="2016", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2015 = models.IntegerField(db_column="2015", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2014 = models.IntegerField(db_column="2014", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2013 = models.IntegerField(db_column="2013", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2012 = models.IntegerField(db_column="2012", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2011 = models.IntegerField(db_column="2011", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2010 = models.IntegerField(db_column="2010", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2009 = models.IntegerField(db_column="2009", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2008 = models.IntegerField(db_column="2008", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2007 = models.IntegerField(db_column="2007", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2006 = models.IntegerField(db_column="2006", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2005 = models.IntegerField(db_column="2005", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2004 = models.IntegerField(db_column="2004", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2003 = models.IntegerField(db_column="2003", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2002 = models.IntegerField(db_column="2002", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2001 = models.IntegerField(db_column="2001", blank=True, null=True)
   # Field renamed because it wasn’t a valid Python identifier.
   number_2000 = models.IntegerField(db_column="2000", blank=True, null=True)
   prior_to_2000 = models.IntegerField(blank=True, null=True)

   class Meta:
       managed = False
       db_table = "bike_daily_estimates"


class BikeGreenways(models.Model):
    objectid = models.IntegerField(primary_key=True)
    tranplanid = models.CharField(max_length=50)
    segmentnam = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    facility = models.CharField(max_length=50)
    yearbuilt = models.IntegerField()
    yearretire = models.IntegerField()
    lengthmile = models.FloatField()
    shape_leng = models.FloatField()
    shape_le_1 = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'bike_greenways'


class BikeLanes(models.Model):
    objectid = models.IntegerField(primary_key=True)
    tranplanid = models.CharField(max_length=50)
    segmentnam = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    facility = models.CharField(max_length=50)
    yearbuilt = models.IntegerField()
    yearretire = models.IntegerField()
    lengthmile = models.FloatField()
    shape_leng = models.FloatField()
    shape_le_1 = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'bike_lanes'


class BikeParking(models.Model):
    objectid = models.IntegerField(primary_key=True)
    assetid = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    maintresp = models.CharField(max_length=50)
    locationid = models.CharField(max_length=50)
    imagepath = models.CharField(max_length=50)
    bikeparktype = models.IntegerField()
    numspaces = models.IntegerField()
    numunits = models.IntegerField()
    bplevel = models.CharField(max_length=50)
    bpstyle = models.CharField(max_length=50)
    finish = models.CharField(max_length=50)
    mounting = models.CharField(max_length=50)
    covered = models.CharField(max_length=50)
    bpfund = models.CharField(max_length=50)
    rotation = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'bike_parking'


class BusStops(models.Model):
    """
    Rename Fields
    """
    keyitem = models.CharField(primary_key=True, max_length=50)
    rte = models.CharField(max_length=50)
    dir = models.FloatField()
    loc_id = models.FloatField()
    location = models.CharField(max_length=50)
    jurisdic = models.CharField(max_length=50)
    zip = models.FloatField()
    route = models.CharField(max_length=50)
    rte_desc = models.CharField(max_length=50)
    dir_desc = models.CharField(max_length=50)
    stop_seq = models.IntegerField()
    type = models.CharField(max_length=50)
    frequent = models.CharField(max_length=50)
    geom = models.MultiPointField()

    class Meta:
        managed = False
        db_table = 'bus_stops'


class CampSweeps(models.Model):
    id = models.IntegerField(primary_key=True)
    reportdate = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    maintenanceproject = models.CharField(max_length=50)
    greenspace = models.CharField(max_length=50)
    excessiveheatcold = models.CharField(max_length=50)
    estimatedgeocode = models.CharField(max_length=50)
    polygonaspoint = models.CharField(max_length=50)
    lat = models.FloatField()
    long = models.FloatField()
    notes = models.CharField(max_length=200)
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'camp_sweeps'


class CommunityGardens(models.Model):
    objectid = models.IntegerField()
    propertyid = models.IntegerField()
    sitename = models.CharField(max_length=50)
    area = models.FloatField()
    acres = models.FloatField()
    status = models.CharField(max_length=50)
    r_value = models.IntegerField()
    plotsperga = models.IntegerField()
    waitlist = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'community_gardens'


class Crime(models.Model):
    # TODO: convert to using case_number as the PK?
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=200)
    case_number = models.CharField(max_length=50)
    crime_against = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)
    number_of_records = models.IntegerField()
    occur_date = models.DateTimeField()
    offense_category = models.CharField(max_length=50)
    offense_count = models.IntegerField()
    offense_type = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    report_date = models.DateTimeField()
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'crime'


class Demolitions(models.Model):
    objectid = models.IntegerField(primary_key=True)
    folderkey = models.IntegerField()
    propertyke = models.IntegerField()
    stateidkey = models.CharField(max_length=50)
    applicatio = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    sequence = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    house = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    propstreet = models.CharField(max_length=50)
    streettype = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    permit = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    work_descr = models.CharField(max_length=50)
    issued = models.DateTimeField(blank=True, null=True)
    finaled = models.DateTimeField(blank=True, null=True)
    lastaction = models.DateTimeField(blank=True, null=True)
    foldertype = models.CharField(max_length=50)
    folderacti = models.DateTimeField()
    folderuser = models.CharField(max_length=50)
    intakecomp = models.DateTimeField()
    gis_proces = models.CharField(max_length=50)
    gis_proc_1 = models.DateTimeField()
    gis_locati = models.CharField(max_length=50)
    propkey = models.CharField(max_length=50)
    trim_url = models.CharField(max_length=50)
    neighborho = models.CharField(max_length=100)
    neighbor_1 = models.CharField(max_length=100)
    business_a = models.CharField(max_length=150)
    portland_m = models.CharField(max_length=100)
    publish_st = models.CharField(max_length=50)
    occupancyg = models.CharField(max_length=50)
    constructi = models.CharField(max_length=50)
    submittedv = models.CharField(max_length=50)
    finalvalua = models.CharField(max_length=50)
    numnewunit = models.CharField(max_length=50)
    totalsqft = models.CharField(max_length=50)
    numbstorie = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    geom = models.MultiPointField()
    description = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'demolitions'


class HousingAreas(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'housing_areas'


class MetroLimit(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    area = models.FloatField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metro_limit'


class NeighborhoodAges(models.Model):
    age = models.SmallIntegerField()
    neighborhood = models.CharField(max_length=50)
    year_2006 = models.FloatField(db_column="2006")
    year_2007 = models.FloatField(db_column="2007")
    year_2008 = models.FloatField(db_column="2008")
    year_2009 = models.FloatField(db_column="2009")
    year_2010 = models.FloatField(db_column="2010")
    year_2011 = models.FloatField(db_column="2011")
    year_2012 = models.FloatField(db_column="2012")
    year_2013 = models.FloatField(db_column="2013")
    year_2014 = models.FloatField(db_column="2014")
    year_2015 = models.FloatField(db_column="2015")
    year_2016 = models.FloatField(db_column="2016")

    class Meta:
        managed = False
        db_table = 'neighborhood_ages_over_time'

class ParkRideLots(models.Model):
    station = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    spaces = models.FloatField()
    status = models.CharField(max_length=50)
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'park_ride_lots'


class Parks(models.Model):
    objectid = models.IntegerField()
    propertyid = models.IntegerField()
    name = models.CharField(max_length=50)
    acres = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'parks'


class ParksTrails(models.Model):
    id = models.IntegerField(primary_key=True)
    objectid = models.IntegerField()
    propertyid = models.CharField(max_length=50)
    local_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)
    surface = models.CharField(max_length=50)
    width_ft = models.IntegerField()
    source = models.CharField(max_length=50)
    regional_t = models.CharField(max_length=50)
    columbia_s = models.CharField(max_length=50)
    forty_mile = models.CharField(max_length=50)
    i_205 = models.CharField(max_length=50)
    marine_dri = models.CharField(max_length=50)
    marquam = models.CharField(max_length=50)
    springwate = models.CharField(max_length=50)
    willamette = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    red_electr = models.CharField(max_length=50)
    hillsdale_field = models.CharField(max_length=50)
    fanno_cree = models.CharField(max_length=75)
    miles = models.FloatField()
    shape_leng = models.FloatField()
    fire_acces = models.CharField(max_length=50)
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'parks_trails'

class PercentSharedHousing(models.Model):
    id = models.IntegerField(primary_key=True)
    dates = models.DateField(blank=True, null=True)
    four_or_more = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'percent_shared_housing'


class RailStops(models.Model):
    station = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    line = models.CharField(max_length=50)
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'rail_stops'


class RetailLocations(models.Model):
    company_na = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    full_addre = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    metro_area = models.CharField(max_length=50)
    neighborho = models.CharField(max_length=50)
    primary_si = models.IntegerField()
    primary_1 = models.CharField(max_length=50)
    primary_2 = models.IntegerField()
    sic_code_1 = models.IntegerField()
    sic_code_2 = models.CharField(max_length=50)
    primary_na = models.IntegerField()
    primary_3 = models.CharField(max_length=50)
    lat = models.FloatField()
    long = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'retail_locations'


# class RlisNeighborhoods(models.Model):
#     ogc_fid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=-1, blank=True, null=True)
#     sum_area = models.FloatField(blank=True, null=True)
#     sum_sqmile = models.FloatField(blank=True, null=True)
#     geom = models.GeometryField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'rlis_neighborhoods'


# class RlisTaxlot2017(models.Model):
#     x = models.FloatField(db_column='X', blank=True, null=True)
#     y = models.FloatField(db_column='Y', blank=True, null=True)
#     area = models.FloatField(db_column='AREA', blank=True, null=True)
#     tlid = models.TextField(db_column='TLID', blank=True, null=True)
#     rno = models.TextField(db_column='RNO', blank=True, null=True)
#     owneraddr = models.TextField(db_column='OWNERADDR', blank=True, null=True)
#     ownercity = models.TextField(db_column='OWNERCITY', blank=True, null=True)
#     ownerstate = models.TextField(
#         db_column='OWNERSTATE', blank=True, null=True)
#     ownerzip = models.TextField(db_column='OWNERZIP', blank=True, null=True)
#     sitestrno = models.BigIntegerField(
#         db_column='SITESTRNO', blank=True, null=True)
#     siteaddr = models.TextField(db_column='SITEADDR', blank=True, null=True)
#     sitecity = models.TextField(db_column='SITECITY', blank=True, null=True)
#     sitezip = models.TextField(db_column='SITEZIP', blank=True, null=True)
#     landval = models.BigIntegerField(
#         db_column='LANDVAL', blank=True, null=True)
#     bldgval = models.BigIntegerField(
#         db_column='BLDGVAL', blank=True, null=True)
#     totalval = models.BigIntegerField(
#         db_column='TOTALVAL', blank=True, null=True)
#     bldgsqft = models.FloatField(db_column='BLDGSQFT', blank=True, null=True)
#     a_t_acres = models.FloatField(db_column='A_T_ACRES', blank=True, null=True)
#     yearbuilt = models.BigIntegerField(
#         db_column='YEARBUILT', blank=True, null=True)
#     prop_code = models.FloatField(db_column='PROP_CODE', blank=True, null=True)
#     landuse = models.TextField(db_column='LANDUSE', blank=True, null=True)
#     taxcode = models.FloatField(db_column='TAXCODE', blank=True, null=True)
#     saledate = models.FloatField(db_column='SALEDATE', blank=True, null=True)
#     saleprice = models.BigIntegerField(
#         db_column='SALEPRICE', blank=True, null=True)
#     county = models.TextField(db_column='COUNTY', blank=True, null=True)
#     juris_city = models.TextField(
#         db_column='JURIS_CITY', blank=True, null=True)
#     gis_acres = models.FloatField(db_column='GIS_ACRES', blank=True, null=True)
#     stateclass = models.TextField(
#         db_column='STATECLASS', blank=True, null=True)
#     ortaxlot = models.TextField(db_column='ORTAXLOT', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'rlis_taxlot_2017'


# class RlisTaxlotPts2015(models.Model):
#     x = models.CharField(db_column='X', max_length=-1, blank=True, null=True)
#     y = models.CharField(db_column='Y', max_length=-1, blank=True, null=True)
#     area = models.CharField(
#         db_column='AREA', max_length=-1, blank=True, null=True)
#     tlid = models.CharField(
#         db_column='TLID', max_length=-1, blank=True, null=True)
#     rno = models.CharField(
#         db_column='RNO', max_length=-1, blank=True, null=True)
#     owneraddr = models.CharField(
#         db_column='OWNERADDR', max_length=-1, blank=True, null=True)
#     ownercity = models.CharField(
#         db_column='OWNERCITY', max_length=-1, blank=True, null=True)
#     ownerstate = models.CharField(
#         db_column='OWNERSTATE', max_length=-1, blank=True, null=True)
#     ownerzip = models.CharField(
#         db_column='OWNERZIP', max_length=-1, blank=True, null=True)
#     sitestrno = models.CharField(
#         db_column='SITESTRNO', max_length=-1, blank=True, null=True)
#     siteaddr = models.CharField(
#         db_column='SITEADDR', max_length=-1, blank=True, null=True)
#     sitecity = models.CharField(
#         db_column='SITECITY', max_length=-1, blank=True, null=True)
#     sitezip = models.CharField(
#         db_column='SITEZIP', max_length=-1, blank=True, null=True)
#     landval = models.CharField(
#         db_column='LANDVAL', max_length=-1, blank=True, null=True)
#     bldgval = models.CharField(
#         db_column='BLDGVAL', max_length=-1, blank=True, null=True)
#     totalval = models.CharField(
#         db_column='TOTALVAL', max_length=-1, blank=True, null=True)
#     bldgsqft = models.CharField(
#         db_column='BLDGSQFT', max_length=-1, blank=True, null=True)
#     a_t_acres = models.CharField(
#         db_column='A_T_ACRES', max_length=-1, blank=True, null=True)
#     yearbuilt = models.CharField(
#         db_column='YEARBUILT', max_length=-1, blank=True, null=True)
#     prop_code = models.CharField(
#         db_column='PROP_CODE', max_length=-1, blank=True, null=True)
#     landuse = models.CharField(
#         db_column='LANDUSE', max_length=-1, blank=True, null=True)
#     taxcode = models.CharField(
#         db_column='TAXCODE', max_length=-1, blank=True, null=True)
#     saledate = models.CharField(
#         db_column='SALEDATE', max_length=-1, blank=True, null=True)
#     saleprice = models.CharField(
#         db_column='SALEPRICE', max_length=-1, blank=True, null=True)
#     county = models.CharField(
#         db_column='COUNTY', max_length=-1, blank=True, null=True)
#     x_coord = models.CharField(
#         db_column='X_COORD', max_length=-1, blank=True, null=True)
#     y_coord = models.CharField(
#         db_column='Y_COORD', max_length=-1, blank=True, null=True)
#     juris_city = models.CharField(
#         db_column='JURIS_CITY', max_length=-1, blank=True, null=True)
#     gis_acres = models.CharField(
#         db_column='GIS_ACRES', max_length=-1, blank=True, null=True)
#     stateclass = models.CharField(
#         db_column='STATECLASS', max_length=-1, blank=True, null=True)
#     ortaxlot = models.CharField(
#         db_column='ORTAXLOT', max_length=-1, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'rlis_taxlot_pts_2015'


class SchoolDistricts(models.Model):
    distno = models.CharField(primary_key=True, max_length=50)
    distname = models.CharField(max_length=50)
    distinstid = models.IntegerField()
    ncesdistid = models.IntegerField()
    area = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'school_districts'


class Scope(models.Model):
    area = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'scope'


class TransitCenters(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    geom = models.GeometryField()
    in_scope = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'transit_centers'


class Trees(models.Model):
    objectid = models.IntegerField()
    date_inventoried = models.DateTimeField(blank=True, null=True)
    species = models.CharField(max_length=50, blank=True, null=True)
    dbh = models.FloatField(blank=True, null=True)
    condition = models.CharField(max_length=50, blank=True, null=True)
    site_type = models.CharField(max_length=50, blank=True, null=True)
    site_width = models.FloatField(blank=True, null=True)
    wires = models.CharField(max_length=50, blank=True, null=True)
    site_development = models.CharField(max_length=50, blank=True, null=True)
    site_size = models.CharField(max_length=50, blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.CharField(max_length=50, blank=True, null=True)
    collected_by = models.CharField(max_length=50, blank=True, null=True)
    planted_by = models.CharField(max_length=50, blank=True, null=True)
    plant_date = models.DateTimeField(blank=True, null=True)
    scientific = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    genus = models.CharField(max_length=50, blank=True, null=True)
    common = models.CharField(max_length=50, blank=True, null=True)
    functionaltype = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    edible = models.CharField(max_length=50, blank=True, null=True)
    species_description = models.CharField(
        max_length=50, blank=True, null=True)
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'trees'


class VoterMovementAngleByAge(models.Model):
    current_age = models.SmallIntegerField()
    consec_dist = models.FloatField()
    radians = models.FloatField
    age_group = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'age_move_distance_angle'


class VoterPrecincts(models.Model):
    county = models.CharField(max_length=50)
    precinct = models.FloatField(primary_key=True)
    area = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'voter_precincts'


class VoterRegistrationByAge(models.Model):
    age = models.SmallIntegerField()
    year_2006 = models.FloatField(db_column="2006")
    year_2007 = models.FloatField(db_column="2007")
    year_2008 = models.FloatField(db_column="2008")
    year_2009 = models.FloatField(db_column="2009")
    year_2010 = models.FloatField(db_column="2010")
    year_2011 = models.FloatField(db_column="2011")
    year_2012 = models.FloatField(db_column="2012")
    year_2013 = models.FloatField(db_column="2013")
    year_2014 = models.FloatField(db_column="2014")
    year_2015 = models.FloatField(db_column="2015")
    year_2016 = models.FloatField(db_column="2016")

    class Meta:
        managed = False
        db_table = 'age_group_registration_percent'


class ZipCodes(models.Model):
    objectid = models.IntegerField(primary_key=True)
    zipcode = models.IntegerField()
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    shape_length = models.FloatField()
    shape_area = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'zip_codes'


class Zoning(models.Model):
    id = models.IntegerField(primary_key=True)
    city_no = models.IntegerField()
    zone = models.CharField(max_length=50)
    zone_class = models.CharField(max_length=50)
    zonegen_cl = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.FloatField()
    sqmiles = models.FloatField()
    geom = models.PolygonField()

    class Meta:
        managed = False
        db_table = 'zoning'
