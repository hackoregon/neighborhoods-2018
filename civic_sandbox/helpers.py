from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BikeParking
from .serializers import BikeParkingSerializer
import json 
from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString


def sandbox_view_factory(model_class, serializer_class, multi_geom_class, geom_field, attributes, dates):
    @api_view(['GET'])
    def sandbox_function(request, format=None): 
        print('\n====================================================================================\n')
        try:
            if not dates['date_column']: 
                dataset= model_class.objects.all()
            else:
                variable_column = dates['date_column']
                filter = variable_column + '__contains'
                dataset= model_class.objects.filter(**{ filter: '2010'})
            print('got objects')   
        
        # calculate limit boundary meta #
            coords = []
            for each in dataset: 
                geom = getattr(each, geom_field)
                coords.append(geom)
            print('4 loop all done')  
            
            multi = multi_geom_class(coords)
            limit_boundary = multi.convex_hull.json
            

            print('made mps')  

            # calculate date meta #
            
            min_date = 'null'
            max_date = 'null'
    
        except model_class.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        if request.method == 'GET':
                serializer = serializer_class(dataset, many=True)
                print('done with serializer')

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

                print('got serializer.data')
                return Response(response)

    return sandbox_function
