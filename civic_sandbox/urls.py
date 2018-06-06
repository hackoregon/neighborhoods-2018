from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^slides/bikeparking/', views.bikeparking),
    url(r'^slides/bikelanes/', views.bikelanes), 
    url(r'^foundations/taxlotblockgroups/(?P<date_filter>\d+)', views.taxlotblockgroups),
    url(r'^foundations/taxlotblockgroups/', views.taxlotblockgroups),
    url(r'^slides/parks/', views.parks),
    url(r'^slides/parkstrails/', views.parks),
    url(r'^slides/multiusetrails/', views.multiusetrails),
    url(r'^slides/communitygardens/', views.communitygardens),
]
urlpatterns = format_suffix_patterns(urlpatterns)

