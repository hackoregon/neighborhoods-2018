import coreapi
from django_filters.rest_framework import DjangoFilterBackend

from . import models


class SchoolDemographicsFilter(DjangoFilterBackend):
    class Meta:
        model = models.SchoolDemographics
        fields = ['year', 'type']

    def get_schema_fields(self, view):
        year = coreapi.Field(
            name="year",
            location="query",
            description="YYYY",
            type="integer"
        )
        type = coreapi.Field(
            name="type",
            location="query",
            description="Type of School.  One of: (O, M, H, E, C)",
            type="string"
        )
        name = coreapi.Field(
            name='name',
            location='query',
            description='School Name',
            type='string'
        )
        return [year, type, name]

class SchoolClassSizeFilter(DjangoFilterBackend):
    class Meta:
        model = models.SchoolDemographics
        fields = ('year',)

    def get_schema_fields(self, view):
        year = coreapi.Field(
            name="year",
            location="query",
            description="YYYY",
            type="integer"
        )
        return [year]