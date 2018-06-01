from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('crimes', views.CrimesList.as_view()),
    path('affordable_housing', views.AffordableHousingList.as_view()),
    path('camp_sweeps', views.CampSweepsList.as_view()),
    path('camp_sweeps/bytime', views.camp_sweeps_by_time),
    path('camp_sweeps/by_neighborhood', views.camp_sweeps_by_neighborhood),
    path('bus_stops', views.BusStopsList.as_view()),
    path('census_2000', views.Census2000List.as_view()),
    path('census_2010', views.Census2010List.as_view()),
    path('demolitions', views.DemolitionsList.as_view()),
    path('housing_areas', views.HousingAreasList.as_view()),
    path('neighborhoods', views.NeighborhoodsList.as_view()),
    path('parks_trails', views.ParksTrailsList.as_view()),
    path('school_districts', views.SchoolDistrictsList.as_view()),
    path('transit_centers', views.TransitCentersList.as_view()),
    path('voter_precincts', views.VoterPrecinctsList.as_view()),
    path('zip_codes', views.ZipCodesList.as_view()),
    path('zoning', views.ZoningList.as_view()),
    path('blockgroups_el', views.BlockgroupsElList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
