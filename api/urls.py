from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='Hack Oregon 2018 Neighborhood Development APIs')

urlpatterns = [
    path('', schema_view),
    path('crimes', views.CrimesList.as_view()),
    path('affordable_housing', views.AffordableHousingList.as_view()),
    path('camp_sweeps', views.CampSweepsList.as_view()),
    path('bus_stops', views.BusStopsList.as_view()),
    path('demolitions', views.DemolitionsList.as_view()),
    path('housing_areas', views.HousingAreasList.as_view()),
    path('parks_trails', views.ParksTrailsList.as_view()),
    path('school_districts', views.SchoolDistrictsList.as_view()),
    path('transit_centers', views.TransitCentersList.as_view()),
    path('voter_precincts', views.VoterPrecinctsList.as_view()),
    path('zip_codes', views.ZipCodesList.as_view()),
    path('zoning', views.ZoningList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
