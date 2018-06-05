from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^bikeparking', views.bikeparking),
    url(r'^bikelanes', views.bikelanes),
    url(r'^taxlotblockgroups', views.taxlotblockgroups),
]
urlpatterns = format_suffix_patterns(urlpatterns)

