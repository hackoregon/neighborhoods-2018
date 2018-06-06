from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^bikeparking/', views.bikeparking),
    url(r'^bikelanes/', views.bikelanes),
    url(r'^taxlotblockgroups/(?P<date_filter>\d+)', views.taxlotblockgroups),
    url(r'^taxlotblockgroups/', views.taxlotblockgroups),
    url(r'^parks/', views.parks),
]
urlpatterns = format_suffix_patterns(urlpatterns)

