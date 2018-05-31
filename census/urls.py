from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('census_2000', views.Census2000List.as_view()),
    path('census_2010', views.Census2010List.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
