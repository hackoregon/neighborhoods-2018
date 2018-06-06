from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('1990', views.Census1990List.as_view()),
    path('2000', views.Census2000List.as_view()),
    path('2010', views.Census2010List.as_view()),
    path('ims', views.ImsNbrhdDemographicsList.as_view()),
    path('evictions_blockgroups', views.EvictionsBlockgroupsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
