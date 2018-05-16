from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from . import models, serializers

@api_view
def crimes_list(request):
    crimes = models.Crime.objects.all()

class CrimesList(ListAPIView):
    queryset = models.Crime.objects.all()
    serializer_class = serializers.CrimeSerializer