from django.contrib.gis.db import models

class BikeParking(models.Model):
    objectid = models.IntegerField(primary_key=True)
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'bike_parking'

class BikeLane(models.Model):
    objectid = models.IntegerField(primary_key=True)
    geom = models.LineStringField()

    class Meta:
        managed = False
        db_table = 'bike_lanes'

class TaxLotBlockGroup(models.Model):
    fips = models.CharField(max_length=50, primary_key=True)
    year = models.CharField(max_length=4)
    prop_value = models.CharField(max_length=50)
    geom = models.PolygonField()

    class Meta:
        managed = False
        db_table = 'taxlot_mview'

class Park(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    acres = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'parks'

class ParksTrail(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'parks_trails'


class MultiuseTrail(models.Model):
    ogc_fid = models.IntegerField(primary_key=True)
    geom = models.LineStringField()

    class Meta:
        managed = False
        db_table = 'active_multiuse_trail'

class CommunityGarden(models.Model):
    id = models.IntegerField(primary_key=True)
    sitename = models.CharField(max_length=50)
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'community_gardens'

class BikeGreenway(models.Model):
    objectid = models.IntegerField(primary_key=True)
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'bike_greenways'

class RailStop(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'rail_stops'

class Demolition(models.Model):
    objectid = models.IntegerField(primary_key=True)
    year = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'demolitions'

class CampSweep(models.Model):
    id = models.IntegerField(primary_key=True)
    reportdate = models.DateField()
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'camp_sweeps'


class CampReport(models.Model):
    id = models.IntegerField(db_column='ItemID', primary_key=True)
    date = models.DateTimeField()
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'campsite_reports'