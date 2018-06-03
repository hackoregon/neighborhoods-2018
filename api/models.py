
from django.contrib.gis.db import models


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
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    geom = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'housing_areas'


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




class TransitCenters(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    geom = models.MultiPointField()

    class Meta:
        managed = False
        db_table = 'transit_centers'


class VoterPrecincts(models.Model):
    county = models.CharField(max_length=50)
    precinct = models.FloatField(primary_key=True)
    area = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'voter_precincts'


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
