from django.contrib.gis.db import models


class Census2000(models.Model):
    id = models.IntegerField(primary_key=True)
    trbg = models.CharField(max_length=50)
    fips = models.CharField(max_length=50)
    bg = models.CharField(max_length=50)
    ct00 = models.FloatField()
    dist = models.IntegerField()
    pop00 = models.IntegerField()
    hh00 = models.IntegerField()
    du00 = models.IntegerField()
    sf00 = models.IntegerField()
    mf00 = models.IntegerField()
    vac00 = models.IntegerField()
    hhsize00 = models.FloatField()
    pop01 = models.IntegerField()
    hh01 = models.IntegerField()
    du01 = models.IntegerField()
    pop02 = models.IntegerField()
    hh02 = models.IntegerField()
    du02 = models.IntegerField()
    pop03 = models.IntegerField()
    hh03 = models.IntegerField()
    du03 = models.IntegerField()
    pop04 = models.IntegerField()
    hh04 = models.IntegerField()
    du04 = models.IntegerField()
    pop05 = models.IntegerField()
    hh05 = models.IntegerField()
    du05 = models.IntegerField()
    pop06 = models.IntegerField()
    hh06 = models.IntegerField()
    du06 = models.IntegerField()
    pop08 = models.IntegerField()
    hh08 = models.IntegerField()
    du08 = models.IntegerField()
    geom = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'census_2000'

class Census2010(models.Model):
    id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    tract = models.CharField(max_length=50)
    tract_no = models.FloatField()
    bg = models.CharField(max_length=50)
    trbg = models.CharField(max_length=50)
    fips = models.CharField(max_length=50)
    pop10 = models.IntegerField()
    du10 = models.IntegerField()
    vac10 = models.IntegerField()
    white = models.IntegerField()
    black = models.IntegerField()
    aian = models.IntegerField()
    asian = models.IntegerField()
    nhpi = models.IntegerField()
    other_race = models.IntegerField()
    pop_2_race = models.IntegerField()
    hispanic = models.IntegerField()
    geom = models.PolygonField()

    class Meta:
        managed = False
        db_table = 'census_2010'
