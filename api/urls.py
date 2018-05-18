from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('crimes', views.CrimesList.as_view()),
    path('affordable_housing', views.AffordableHousingList.as_view()),
    path('camp_cleanups', views.CampCleanupsList.as_view()),
    path('dat_crime_neigh', views.DatCrimeNeighList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
