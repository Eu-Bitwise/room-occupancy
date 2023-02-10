from rest_framework import serializers 
from occupancy_app.models import * 

# A serializer is used to convert the models data into a JSON response

class PeopleCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleCounter 
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor 
        fields = '__all__'