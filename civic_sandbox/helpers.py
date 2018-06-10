import json 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString


def sandbox_view_factory(model_class, serializer_class, multi_geom_class, geom_field, attributes, dates):
    @api_view(['GET'])
    def sandbox_function(request, date_filter=dates['default_date_filter'], format=None): 

        ## get data ##
        try:
            if not dates['date_attribute']: 
                dataset= model_class.objects.all()
            else:
                variable_column = dates['date_attribute']
                filter = variable_column + '__contains'
                dataset= model_class.objects.filter(**{ filter: date_filter })
        
        # calculate limit boundary meta #
            coords = []
            for each in dataset: 
                geom = getattr(each, geom_field)
                ## converts MultiPolygons to Polygons ##
                if isinstance(geom, MultiPolygon):
                    coords.append(geom.convex_hull)
                elif isinstance(geom, MultiLineString):
                    coords.append(geom.union)
                else: 
                    coords.append(geom)
            
            multi = multi_geom_class(coords)
            limit_boundary = multi.convex_hull.json

            # calculate date meta #
            
            min_date = None
            max_date = None
            if dates['date_attribute'] is not None: 
                min_date = min(dates['date_attribute'])
                max_date = max(['date_attribute'])
    
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
