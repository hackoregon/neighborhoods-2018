from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^slides/bikeparking/', views.bikeparking),
    url(r'^slides/bikelanes/', views.bikelanes), 
    url(r'^foundations/taxlotblockgroups/(?P<date_filter>\d+)', views.taxlotblockgroups),
    url(r'^foundations/taxlotblockgroups/', views.taxlotblockgroups),
    url(r'^slides/parks/', views.parks),
    #TODO: url(r'^slides/parkstrails/', views.parkstrails),
    url(r'^slides/multiusetrails/', views.multiusetrails),
    url(r'^slides/communitygardens/', views.communitygardens),
    url(r'^slides/bikegreenways/', views.bikegreenways),
    url(r'^slides/railstops/', views.railstops),
    url(r'^slides/demolitions/(?P<date_filter>\d+)', views.demolitions),
    url(r'^slides/demolitions/', views.demolitions),
    url(r'^slides/campsweeps/(?P<date_filter>\d+)', views.campsweeps),
    url(r'^slides/campsweeps/', views.campsweeps),
    url(r'^slides/campreports/(?P<date_filter>\d+)', views.campreports),
    url(r'^slides/campreports/', views.campreports),
]
urlpatterns = format_suffix_patterns(urlpatterns)

