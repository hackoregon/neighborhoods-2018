from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^slides/bikeparking/', views.bikeparking),
    url(r'^slides/bikelanes/', views.bikelanes), 
    url(r'^foundations/taxlotblockgroups/(?P<date_filter>\d+)', views.taxlotblockgroups),
    url(r'^foundations/taxlotblockgroups/', views.taxlotblockgroups),
    url(r'^slides/parks/', views.parks),
    url(r'^slides/parkstrails/', views.parkstrails),
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
    url(r'^slides/retailgrocers/', views.retailgrocers),
    url(r'^slides/trees/', views.trees),
    url(r'^slides/trees/(?P<date_filter>\d+)', views.trees),
    url(r'^slides/busstops/', views.busstops),
    url(r'^foundations/under18/', views.under18),
    url(r'^foundations/under18/(?P<date_filter>\d+)', views.under18),
    url(r'^foundations/over65/', views.over65),
    url(r'^foundations/over65/(?P<date_filter>\d+)', views.over65),
    url(r'^foundations/population/', views.population),
    url(r'^foundations/population/(?P<date_filter>\d+)', views.population),
    url(r'^foundations/owneroccupied/', views.owneroccupied),
    url(r'^foundations/owneroccupied/(?P<date_filter>\d+)', views.owneroccupied),
    url(r'^foundations/livingalone/', views.livingalone),
    url(r'^foundations/livingalone/(?P<date_filter>\d+)', views.livingalone),
    url(r'^foundations/income/', views.income),
    url(r'^foundations/income/(?P<date_filter>\d+)', views.income),
    url(r'^foundations/evictions/', views.evictions),
    url(r'^foundations/evictions/(?P<date_filter>\d+)', views.evictions),
    url(r'^foundations/grossrent/', views.grossrent),
    url(r'^foundations/grossrent/(?P<date_filter>\d+)', views.grossrent),
    url(r'^foundations/pctrenteroccupied/', views.pctrenteroccupied),
    url(r'^foundations/pctrenteroccupied/(?P<date_filter>\d+)', views.pctrenteroccupied),
    url(r'^foundations/rentburden/', views.rentburden),
    url(r'^foundations/rentburden/(?P<date_filter>\d+)', views.rentburden),
    url(r'^foundations/renteroccupied/', views.renteroccupied),
    url(r'^foundations/renteroccupied/(?P<date_filter>\d+)', views.renteroccupied),

]
urlpatterns = format_suffix_patterns(urlpatterns)

