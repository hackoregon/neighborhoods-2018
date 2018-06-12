import json 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString


def sandbox_view_factory(model_class, serializer_class, multi_geom_class, geom_field, attributes, dates):
    @api_view(['GET'])
    def sandbox_function(request, date_filter=dates['default_date_filter'], format=None): 

        ## get data ##
        try:
            # full_dataset = model_class.objects.all()
            if not dates['date_attribute']: 
                dataset= model_class.objects.all()
            else:
                variable_column = dates['date_attribute']
                filter = variable_column + '__contains'
                dataset= model_class.objects.filter(**{ filter: date_filter })
                if settings.DEBUG: print('---------------------------------------')
                if settings.DEBUG: print(filter)
                if settings.DEBUG: print(date_filter)


            if settings.DEBUG: print('made queryset')
        
        # calculate limit boundary meta #
            coords = []
            for each in dataset: 
                geom = getattr(each, geom_field)
                ## converts MultiPolygons to Polygons ##
                if isinstance(geom, MultiPolygon):
                    coords.append(geom.convex_hull)

                #TODO merge multilinestring to linestring(https://docs.djangoproject.com/en/2.0/ref/contrib/gis/geos/#django.contrib.gis.geos.MultiLineString.merged)
                # elif isinstance(geom, MultiLineString):
                #     merged = geom.merged
                #     coords.append(merged)

                else: 
                    coords.append(geom)
            
            multi = multi_geom_class(coords)
            limit_boundary = multi.convex_hull.json

            if settings.DEBUG: print('boundary calculation complete')

            # # calculate date meta #
            # if dates['date_attribute'] is not None: 
            #     date_list = []
            #     for each in full_dataset: 
            #         date = getattr(each, dates['date_attribute'])
            #         date_list.append(date)
            #     min_date = min(date_list)
            #     max_date = max(date_list)
            # else: 
            min_date = None
            max_date = None

        except model_class.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializer_class(dataset, many=True)

        response= { 
            'slide_meta': {
                'boundary': [json.loads(limit_boundary)],
                'dates': {
                    'min_date': min_date, 
                    'max_date': max_date, 
                    'date_granularity': dates['date_granularity'],
                },
                'attributes': attributes
                },
            'slide_data': serializer.data
        
        }
        return Response(response)

    return sandbox_function
