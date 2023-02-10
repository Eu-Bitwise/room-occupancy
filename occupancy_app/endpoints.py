from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from occupancy_app.serializers import *

import datetime

# -- Functions --
def count_occupants_inside(data):
    people_inside_count = data['inside'] - data['out']
    return people_inside_count if people_inside_count >= 0 else 0

def string_to_datetime(string):
    return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M')

# -- Endpoints --
class MyEndpoint(APIView):

    def get(self, request):
        data = {'message': 'Hello World!'}
        return Response(data)

class RoomOccupancy(APIView):

    def post(self, request):
        serializer = PeopleCounterSerializer(data=request.data)
        if serializer.is_valid():
            people_counter_object = serializer.save()
            data_sensor_name = request.data['sensor_name']
            # Check if the sensor exists
            if Sensor.objects.filter(sensor_name=data_sensor_name).exists():
                # Update the sensor
               sensor_object = Sensor.objects.get(sensor_name=data_sensor_name)         
            else:
                # Create a new sensor
                sensor_object = Sensor.objects.create(sensor_name=data_sensor_name)
            # Add the new people counter relation to sensor
            sensor_object.people_counter.add(people_counter_object)
            sensor_object.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, sensor_name=None, date_time=None):
        if sensor_name:
            # Fetch a sensor by its name
            sensor_cursor = Sensor.objects.filter(sensor_name=sensor_name)
            if sensor_cursor:
                serializer = SensorSerializer(sensor_cursor, many=True)
                sensor_cursor = serializer.data[0]

                # Fetch sensor counter with a datetime
                if date_time:
                    date_time = string_to_datetime(date_time)
                    sensor_people_counter = PeopleCounter.objects.filter(id__in=sensor_cursor['people_counter'], sensor_name=sensor_name, timestamp__lte=date_time).order_by('-timestamp')
                # Fetch the sensor's most recent data counter by default
                else:
                    sensor_people_counter = PeopleCounter.objects.filter(id__in=sensor_cursor['people_counter'], sensor_name=sensor_name).order_by('-timestamp')
               
                # Return the sensor inside counter
                if sensor_people_counter:
                    serializer = PeopleCounterSerializer(sensor_people_counter, many=True)
                    return Response({'inside': count_occupants_inside(serializer.data[0])})
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        # Return all sensor list
        else:
            sensors_cursor = Sensor.objects.all()
            if sensors_cursor:
                serializer = SensorSerializer(sensors_cursor, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)