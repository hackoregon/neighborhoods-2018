from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from civic_sandbox import views
from civic_sandbox import packages_view


urlpatterns = [
    url(r'^slides/bikeparking/', views.bikeparking),
    url(r'^slides/bikelanes/', views.bikelanes), 
    url(r'^slides/parks/', views.parks),
    url(r'^slides/parkstrails/', views.parkstrails),
    url(r'^slides/multiusetrails/', views.multiusetrails),
    url(r'^slides/communitygardens/', views.communitygardens),
    url(r'^slides/bikegreenways/', views.bikegreenways),
    url(r'^slides/railstops/', views.railstops),
    url(r'^slides/demolitions/(?P<date_filter>\d+)', views.demolitions),
    url(r'^slides/demolitions/', views.demolitions),
    url(r'^slides/campsweeps/(?P<date_filter>\w+)', views.campsweeps),
    url(r'^slides/campsweeps/', views.campsweeps),
    url(r'^slides/campreports/(?P<date_filter>\d+)', views.campreports),
    url(r'^slides/campreports/', views.campreports),
    url(r'^slides/retailgrocers/', views.retailgrocers),
    url(r'^slides/trees/(?P<date_filter>\d+)', views.trees),
    url(r'^slides/trees/', views.trees),
    url(r'^slides/busstops/', views.busstops),
    url(r'^foundations/under18/(?P<date_filter>\d+)', views.under18),
    url(r'^foundations/under18/', views.under18),
    url(r'^foundations/over65/(?P<date_filter>\d+)', views.over65),
    url(r'^foundations/over65/', views.over65),
    url(r'^foundations/population/(?P<date_filter>\d+)', views.population),
    url(r'^foundations/population/', views.population),
    url(r'^foundations/owneroccupied/(?P<date_filter>\d+)', views.owneroccupied),
    url(r'^foundations/owneroccupied/', views.owneroccupied),
    url(r'^foundations/livingalone/(?P<date_filter>\d+)', views.livingalone),
    url(r'^foundations/livingalone/', views.livingalone),
    url(r'^foundations/income/(?P<date_filter>\d+)', views.income),
    url(r'^foundations/income/', views.income),
    url(r'^foundations/evictions/(?P<date_filter>\d+)', views.evictions),
    url(r'^foundations/evictions/', views.evictions),
    url(r'^foundations/grossrent/(?P<date_filter>\d+)', views.grossrent),
    url(r'^foundations/grossrent/', views.grossrent),
    url(r'^foundations/pctrenteroccupied/(?P<date_filter>\d+)', views.pctrenteroccupied),
    url(r'^foundations/pctrenteroccupied/', views.pctrenteroccupied),
    url(r'^foundations/rentburden/(?P<date_filter>\d+)', views.rentburden),
    url(r'^foundations/rentburden/', views.rentburden),
    url(r'^foundations/renteroccupied/(?P<date_filter>\d+)', views.renteroccupied),
    url(r'^foundations/renteroccupied/', views.renteroccupied),
    url(r'^foundations/renteroccupied/(?P<date_filter>\d+)', views.renteroccupied),
    url(r'^foundations/renteroccupied/', views.renteroccupied), 
    url(r'^foundations/voters18to25/(?P<date_filter>\d+)', views.voters18to25),
    url(r'^foundations/voters18to25/', views.voters18to25),
    url(r'^foundations/voters26to32/(?P<date_filter>\d+)', views.voters26to32),
    url(r'^foundations/voters26to32/', views.voters26to32),
    url(r'^foundations/voters33to39/(?P<date_filter>\d+)', views.voters33to39),
    url(r'^foundations/voters33to39/', views.voters33to39),
    url(r'^foundations/voters40to49/(?P<date_filter>\d+)', views.voters40to49),
    url(r'^foundations/voters40to49/', views.voters40to49),
    url(r'^foundations/voters50plus/(?P<date_filter>\d+)', views.voters50plus),
    url(r'^foundations/voters50plus/', views.voters50plus),
    url(r'^foundations/reportsbymonth/(?P<date_filter>\w+)', views.reportsbymonth), 
    url(r'^foundations/reportsbymonth/', views.reportsbymonth),
    url(r'^slides/bikecounts/', views.bikecounts),
    url(r'^slides/bikeestimates/', views.bikeestimates),
    url(r'^foundations/evictionrate/(?P<date_filter>\d+)', views.evictionrate),
    url(r'^foundations/evictionrate/', views.evictionrate),
    url(r'^foundations/povertyrate/(?P<date_filter>\d+)', views.povertyrate),
    url(r'^foundations/povertyrate/', views.povertyrate),
    url(r'^package_info/', packages_view.packages_view, name='package_info'),

]
urlpatterns = format_suffix_patterns(urlpatterns)

