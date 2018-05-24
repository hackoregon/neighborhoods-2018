
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


class BlockgroupsEl(models.Model):
    id = models.IntegerField(primary_key=True)
    geoid = models.CharField(max_length=50)
    west = models.FloatField()
    south = models.FloatField()
    east = models.FloatField()
    north = models.FloatField()
    n = models.CharField(max_length=50)
    pl = models.CharField(max_length=50)
    p_00 = models.FloatField()
    pr_00 = models.FloatField()
    pro_00 = models.FloatField()
    mgr_00 = models.FloatField()
    mhi_00 = models.FloatField()
    mpv_00 = models.FloatField()
    rb_00 = models.FloatField()
    pw_00 = models.FloatField()
    paa_00 = models.FloatField()
    ph_00 = models.FloatField()
    pai_00 = models.FloatField()
    pa_00 = models.FloatField()
    pnp_00 = models.FloatField()
    pm_00 = models.FloatField()
    po_00 = models.FloatField()
    roh_00 = models.FloatField()
    ef_00 = models.FloatField()
    e_00 = models.FloatField()
    er_00 = models.FloatField()
    efr_00 = models.FloatField()
    imputed_00 = models.FloatField()
    subbed_00 = models.FloatField()
    p_01 = models.FloatField()
    pr_01 = models.FloatField()
    pro_01 = models.FloatField()
    mgr_01 = models.FloatField()
    mhi_01 = models.FloatField()
    mpv_01 = models.FloatField()
    rb_01 = models.FloatField()
    pw_01 = models.FloatField()
    paa_01 = models.FloatField()
    ph_01 = models.FloatField()
    pai_01 = models.FloatField()
    pa_01 = models.FloatField()
    pnp_01 = models.FloatField()
    pm_01 = models.FloatField()
    po_01 = models.FloatField()
    roh_01 = models.FloatField()
    ef_01 = models.FloatField()
    e_01 = models.FloatField()
    er_01 = models.FloatField()
    efr_01 = models.FloatField()
    imputed_01 = models.FloatField()
    subbed_01 = models.FloatField()
    p_02 = models.FloatField()
    pr_02 = models.FloatField()
    pro_02 = models.FloatField()
    mgr_02 = models.FloatField()
    mhi_02 = models.FloatField()
    mpv_02 = models.FloatField()
    rb_02 = models.FloatField()
    pw_02 = models.FloatField()
    paa_02 = models.FloatField()
    ph_02 = models.FloatField()
    pai_02 = models.FloatField()
    pa_02 = models.FloatField()
    pnp_02 = models.FloatField()
    pm_02 = models.FloatField()
    po_02 = models.FloatField()
    roh_02 = models.FloatField()
    ef_02 = models.FloatField()
    e_02 = models.FloatField()
    er_02 = models.FloatField()
    efr_02 = models.FloatField()
    imputed_02 = models.FloatField()
    subbed_02 = models.FloatField()
    p_03 = models.FloatField()
    pr_03 = models.FloatField()
    pro_03 = models.FloatField()
    mgr_03 = models.FloatField()
    mhi_03 = models.FloatField()
    mpv_03 = models.FloatField()
    rb_03 = models.FloatField()
    pw_03 = models.FloatField()
    paa_03 = models.FloatField()
    ph_03 = models.FloatField()
    pai_03 = models.FloatField()
    pa_03 = models.FloatField()
    pnp_03 = models.FloatField()
    pm_03 = models.FloatField()
    po_03 = models.FloatField()
    roh_03 = models.FloatField()
    ef_03 = models.FloatField()
    e_03 = models.FloatField()
    er_03 = models.FloatField()
    efr_03 = models.FloatField()
    imputed_03 = models.FloatField()
    subbed_03 = models.FloatField()
    p_04 = models.FloatField()
    pr_04 = models.FloatField()
    pro_04 = models.FloatField()
    mgr_04 = models.FloatField()
    mhi_04 = models.FloatField()
    mpv_04 = models.FloatField()
    rb_04 = models.FloatField()
    pw_04 = models.FloatField()
    paa_04 = models.FloatField()
    ph_04 = models.FloatField()
    pai_04 = models.FloatField()
    pa_04 = models.FloatField()
    pnp_04 = models.FloatField()
    pm_04 = models.FloatField()
    po_04 = models.FloatField()
    roh_04 = models.FloatField()
    ef_04 = models.FloatField()
    e_04 = models.FloatField()
    er_04 = models.FloatField()
    efr_04 = models.FloatField()
    imputed_04 = models.FloatField()
    subbed_04 = models.FloatField()
    p_05 = models.FloatField()
    pr_05 = models.FloatField()
    pro_05 = models.FloatField()
    mgr_05 = models.FloatField()
    mhi_05 = models.FloatField()
    mpv_05 = models.FloatField()
    rb_05 = models.FloatField()
    pw_05 = models.FloatField()
    paa_05 = models.FloatField()
    ph_05 = models.FloatField()
    pai_05 = models.FloatField()
    pa_05 = models.FloatField()
    pnp_05 = models.FloatField()
    pm_05 = models.FloatField()
    po_05 = models.FloatField()
    roh_05 = models.FloatField()
    ef_05 = models.FloatField()
    e_05 = models.FloatField()
    er_05 = models.FloatField()
    efr_05 = models.FloatField()
    imputed_05 = models.FloatField()
    subbed_05 = models.FloatField()
    p_06 = models.FloatField()
    pr_06 = models.FloatField()
    pro_06 = models.FloatField()
    mgr_06 = models.FloatField()
    mhi_06 = models.FloatField()
    mpv_06 = models.FloatField()
    rb_06 = models.FloatField()
    pw_06 = models.FloatField()
    paa_06 = models.FloatField()
    ph_06 = models.FloatField()
    pai_06 = models.FloatField()
    pa_06 = models.FloatField()
    pnp_06 = models.FloatField()
    pm_06 = models.FloatField()
    po_06 = models.FloatField()
    roh_06 = models.FloatField()
    ef_06 = models.FloatField()
    e_06 = models.FloatField()
    er_06 = models.FloatField()
    efr_06 = models.FloatField()
    imputed_06 = models.FloatField()
    subbed_06 = models.FloatField()
    p_07 = models.FloatField()
    pr_07 = models.FloatField()
    pro_07 = models.FloatField()
    mgr_07 = models.FloatField()
    mhi_07 = models.FloatField()
    mpv_07 = models.FloatField()
    rb_07 = models.FloatField()
    pw_07 = models.FloatField()
    paa_07 = models.FloatField()
    ph_07 = models.FloatField()
    pai_07 = models.FloatField()
    pa_07 = models.FloatField()
    pnp_07 = models.FloatField()
    pm_07 = models.FloatField()
    po_07 = models.FloatField()
    roh_07 = models.FloatField()
    ef_07 = models.FloatField()
    e_07 = models.FloatField()
    er_07 = models.FloatField()
    efr_07 = models.FloatField()
    imputed_07 = models.FloatField()
    subbed_07 = models.FloatField()
    p_08 = models.FloatField()
    pr_08 = models.FloatField()
    pro_08 = models.FloatField()
    mgr_08 = models.FloatField()
    mhi_08 = models.FloatField()
    mpv_08 = models.FloatField()
    rb_08 = models.FloatField()
    pw_08 = models.FloatField()
    paa_08 = models.FloatField()
    ph_08 = models.FloatField()
    pai_08 = models.FloatField()
    pa_08 = models.FloatField()
    pnp_08 = models.FloatField()
    pm_08 = models.FloatField()
    po_08 = models.FloatField()
    roh_08 = models.FloatField()
    ef_08 = models.FloatField()
    e_08 = models.FloatField()
    er_08 = models.FloatField()
    efr_08 = models.FloatField()
    imputed_08 = models.FloatField()
    subbed_08 = models.FloatField()
    p_09 = models.FloatField()
    pr_09 = models.FloatField()
    pro_09 = models.FloatField()
    mgr_09 = models.FloatField()
    mhi_09 = models.FloatField()
    mpv_09 = models.FloatField()
    rb_09 = models.FloatField()
    pw_09 = models.FloatField()
    paa_09 = models.FloatField()
    ph_09 = models.FloatField()
    pai_09 = models.FloatField()
    pa_09 = models.FloatField()
    pnp_09 = models.FloatField()
    pm_09 = models.FloatField()
    po_09 = models.FloatField()
    roh_09 = models.FloatField()
    ef_09 = models.FloatField()
    e_09 = models.FloatField()
    er_09 = models.FloatField()
    efr_09 = models.FloatField()
    imputed_09 = models.FloatField()
    subbed_09 = models.FloatField()
    p_10 = models.FloatField()
    pr_10 = models.FloatField()
    pro_10 = models.FloatField()
    mgr_10 = models.FloatField()
    mhi_10 = models.FloatField()
    mpv_10 = models.FloatField()
    rb_10 = models.FloatField()
    pw_10 = models.FloatField()
    paa_10 = models.FloatField()
    ph_10 = models.FloatField()
    pai_10 = models.FloatField()
    pa_10 = models.FloatField()
    pnp_10 = models.FloatField()
    pm_10 = models.FloatField()
    po_10 = models.FloatField()
    roh_10 = models.FloatField()
    ef_10 = models.FloatField()
    e_10 = models.FloatField()
    er_10 = models.FloatField()
    efr_10 = models.FloatField()
    imputed_10 = models.FloatField()
    subbed_10 = models.FloatField()
    p_11 = models.FloatField()
    pr_11 = models.FloatField()
    pro_11 = models.FloatField()
    mgr_11 = models.FloatField()
    mhi_11 = models.FloatField()
    mpv_11 = models.FloatField()
    rb_11 = models.FloatField()
    pw_11 = models.FloatField()
    paa_11 = models.FloatField()
    ph_11 = models.FloatField()
    pai_11 = models.FloatField()
    pa_11 = models.FloatField()
    pnp_11 = models.FloatField()
    pm_11 = models.FloatField()
    po_11 = models.FloatField()
    roh_11 = models.FloatField()
    ef_11 = models.FloatField()
    e_11 = models.FloatField()
    er_11 = models.FloatField()
    efr_11 = models.FloatField()
    imputed_11 = models.FloatField()
    subbed_11 = models.FloatField()
    p_12 = models.FloatField()
    pr_12 = models.FloatField()
    pro_12 = models.FloatField()
    mgr_12 = models.FloatField()
    mhi_12 = models.FloatField()
    mpv_12 = models.FloatField()
    rb_12 = models.FloatField()
    pw_12 = models.FloatField()
    paa_12 = models.FloatField()
    ph_12 = models.FloatField()
    pai_12 = models.FloatField()
    pa_12 = models.FloatField()
    pnp_12 = models.FloatField()
    pm_12 = models.FloatField()
    po_12 = models.FloatField()
    roh_12 = models.FloatField()
    ef_12 = models.FloatField()
    e_12 = models.FloatField()
    er_12 = models.FloatField()
    efr_12 = models.FloatField()
    imputed_12 = models.FloatField()
    subbed_12 = models.FloatField()
    p_13 = models.FloatField()
    pr_13 = models.FloatField()
    pro_13 = models.FloatField()
    mgr_13 = models.FloatField()
    mhi_13 = models.FloatField()
    mpv_13 = models.FloatField()
    rb_13 = models.FloatField()
    pw_13 = models.FloatField()
    paa_13 = models.FloatField()
    ph_13 = models.FloatField()
    pai_13 = models.FloatField()
    pa_13 = models.FloatField()
    pnp_13 = models.FloatField()
    pm_13 = models.FloatField()
    po_13 = models.FloatField()
    roh_13 = models.FloatField()
    ef_13 = models.FloatField()
    e_13 = models.FloatField()
    er_13 = models.FloatField()
    efr_13 = models.FloatField()
    imputed_13 = models.FloatField()
    subbed_13 = models.FloatField()
    p_14 = models.FloatField()
    pr_14 = models.FloatField()
    pro_14 = models.FloatField()
    mgr_14 = models.FloatField()
    mhi_14 = models.FloatField()
    mpv_14 = models.FloatField()
    rb_14 = models.FloatField()
    pw_14 = models.FloatField()
    paa_14 = models.FloatField()
    ph_14 = models.FloatField()
    pai_14 = models.FloatField()
    pa_14 = models.FloatField()
    pnp_14 = models.FloatField()
    pm_14 = models.FloatField()
    po_14 = models.FloatField()
    roh_14 = models.FloatField()
    ef_14 = models.FloatField()
    e_14 = models.FloatField()
    er_14 = models.FloatField()
    efr_14 = models.FloatField()
    imputed_14 = models.FloatField()
    subbed_14 = models.FloatField()
    p_15 = models.FloatField()
    pr_15 = models.FloatField()
    pro_15 = models.FloatField()
    mgr_15 = models.FloatField()
    mhi_15 = models.FloatField()
    mpv_15 = models.FloatField()
    rb_15 = models.FloatField()
    pw_15 = models.FloatField()
    paa_15 = models.FloatField()
    ph_15 = models.FloatField()
    pai_15 = models.FloatField()
    pa_15 = models.FloatField()
    pnp_15 = models.FloatField()
    pm_15 = models.FloatField()
    po_15 = models.FloatField()
    roh_15 = models.FloatField()
    ef_15 = models.FloatField()
    e_15 = models.FloatField()
    er_15 = models.FloatField()
    efr_15 = models.FloatField()
    imputed_15 = models.FloatField()
    subbed_15 = models.FloatField()
    p_16 = models.FloatField()
    pr_16 = models.FloatField()
    pro_16 = models.FloatField()
    mgr_16 = models.FloatField()
    mhi_16 = models.FloatField()
    mpv_16 = models.FloatField()
    rb_16 = models.FloatField()
    pw_16 = models.FloatField()
    paa_16 = models.FloatField()
    ph_16 = models.FloatField()
    pai_16 = models.FloatField()
    pa_16 = models.FloatField()
    pnp_16 = models.FloatField()
    pm_16 = models.FloatField()
    po_16 = models.FloatField()
    roh_16 = models.FloatField()
    ef_16 = models.FloatField()
    e_16 = models.FloatField()
    er_16 = models.FloatField()
    efr_16 = models.FloatField()
    imputed_16 = models.FloatField()
    subbed_16 = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'blockgroups_el'


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


class Census2000(models.Model):
    # TODO: Move census data into its own app
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
    # TODO: Move census data into its own app
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


class Neighborhoods(models.Model):
    # TODO: Double check this one once the table is recreated
    fid = models.IntegerField()
    name = models.CharField(max_length=60)
    area = models.FloatField()
    sqmiles = models.FloatField()
    geom = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'neighborhoods'


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
