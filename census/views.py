from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import models, serializers


class Census1990List(ListAPIView):
    queryset = models.Census1990.objects.all()
    serializer_class = serializers.Census1990Serializer


class Census2000List(ListAPIView):
    queryset = models.Census2000.objects.all()
    serializer_class = serializers.Census2000Serializer


class Census2010List(ListAPIView):
    queryset = models.Census2010.objects.all()
    serializer_class = serializers.Census2010Serializer


class ImsNbrhdDemographicsList(ListAPIView):
    queryset = models.ImsNbrhdDemographics.objects.all()
    serializer_class = serializers.ImsNbrhdDemograpicsSerializer


class EvictionsBlockgroupsList(ListAPIView):
    queryset = models.EvictionsBlockgroups.objects.all()
    serializer_class = serializers.EvictionsBlockgroupsSerializer
