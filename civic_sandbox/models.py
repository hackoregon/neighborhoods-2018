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

