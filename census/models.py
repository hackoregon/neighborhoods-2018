from django.contrib.gis.db import models


class Census1990(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    trbg = models.CharField(max_length=7, blank=True, null=True)
    fips = models.CharField(max_length=12, blank=True, null=True)
    bg = models.CharField(max_length=1, blank=True, null=True)
    ct90 = models.FloatField(blank=True, null=True)
    pop90 = models.FloatField(blank=True, null=True)
    hh90 = models.FloatField(blank=True, null=True)
    du90 = models.IntegerField(blank=True, null=True)
    sf90 = models.FloatField(blank=True, null=True)
    mf90 = models.FloatField(blank=True, null=True)
    vac90 = models.IntegerField(blank=True, null=True)
    hhsize90 = models.FloatField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'census_1990'


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


class EvictionsBlockgroups(models.Model):
   geoid = models.DecimalField(db_column="GEOID", max_digits=65535, decimal_places=65535)
   year = models.DecimalField(max_digits=65535, decimal_places=65535)
   name = models.CharField(max_length=10)
   parent_location = models.CharField(max_length=25)
   population = models.DecimalField(max_digits=65535, decimal_places=65535)
   poverty_rate = models.DecimalField(max_digits=65535, decimal_places=65535)
   pctrenter_occupied = models.DecimalField(
       max_digits=65535, decimal_places=65535)
   median_gross_rent = models.DecimalField(db_column="Median_gross_rent", max_digits=65535, decimal_places=65535, blank=True, null=True)
   median_household_income = models.DecimalField(
       max_digits=65535, decimal_places=65535, blank=True, null=True)
   median_property_value = models.DecimalField(
       max_digits=65535, decimal_places=65535, blank=True, null=True)
   rent_burden = models.DecimalField(
       max_digits=65535, decimal_places=65535, blank=True, null=True)
   pct_white = models.DecimalField(max_digits=65535, decimal_places=65535)
   pct_af_am = models.DecimalField(max_digits=65535, decimal_places=65535)
   pct_hispanic = models.DecimalField(max_digits=65535, decimal_places=65535)
   pct_am_ind = models.DecimalField(max_digits=65535, decimal_places=65535)
   pct_asian = models.DecimalField(max_digits=65535, decimal_places=65535)
   pct_nh_pi = models.DecimalField(max_digits=65535, decimal_places=65535)
   pct_multiple = models.DecimalField(max_digits=65535, decimal_places=65535)
   pct_other = models.DecimalField(max_digits=65535, decimal_places=65535)
   renter_occupied_households = models.DecimalField(
       max_digits=65535, decimal_places=65535)
   eviction_filings = models.DecimalField(
       max_digits=65535, decimal_places=65535, blank=True, null=True)
   evictions = models.DecimalField(
       max_digits=65535, decimal_places=65535, blank=True, null=True)
   eviction_rate = models.DecimalField(
       max_digits=65535, decimal_places=65535, blank=True, null=True)
   eviction_filing_rate = models.DecimalField(
       max_digits=65535, decimal_places=65535, blank=True, null=True)
   imputed = models.BooleanField()
   subbed = models.BooleanField()

   class Meta:
       managed = False
       db_table = "evictions_blockgroups"


class ImsNbrhdDemographics(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    total_population_2000 = models.FloatField(blank=True, null=True)
    total_population_2010 = models.FloatField(blank=True, null=True)
    pc_change_in_total_pop = models.FloatField(blank=True, null=True)
    number_households_2000 = models.FloatField(blank=True, null=True)
    number_households_2010 = models.FloatField(blank=True, null=True)
    pc_change_in_number_of_households = models.FloatField(
        blank=True, null=True)
    pop_density_2000 = models.FloatField(blank=True, null=True)
    pop_density_2010 = models.FloatField(blank=True, null=True)
    pc_household_with_children_under_18_2000 = models.FloatField(
        blank=True, null=True)
    pc_household_with_children_under_18_2010 = models.FloatField(
        blank=True, null=True)
    pc_household_with_individuals_65_ovr_2000 = models.FloatField(
        blank=True, null=True)
    pc_household_with_individuals_65_ovr_2010 = models.FloatField(
        blank=True, null=True)
    pc_non_white_2000 = models.FloatField(blank=True, null=True)
    pc_non_white_2010 = models.FloatField(blank=True, null=True)
    change_in_pc_avg_household_size = models.FloatField(blank=True, null=True)
    avg_household_size_2000 = models.FloatField(blank=True, null=True)
    avg_household_size_2010 = models.FloatField(blank=True, null=True)
    pc_owner_occupied_housing_units_2000 = models.FloatField(
        blank=True, null=True)
    pc_owner_occupied_housing_units_2010 = models.FloatField(
        blank=True, null=True)
    pc_householders_living_alone_2000 = models.FloatField(
        blank=True, null=True)
    pc_householders_living_alone_2010 = models.FloatField(
        blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ims_nbrhd_demographics'
