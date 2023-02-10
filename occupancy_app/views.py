from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from occupancy_app.forms import SensorDataForm
from occupancy_app.models import * 

import requests
import urllib.parse


def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def occupancy(request):
    form = SensorDataForm()
    if request.method == 'POST':
        data = request.POST
        # Forge the url pattern to call the endpoint
        sensor_name = data['select_sensor'] 
        args = urllib.parse.quote(sensor_name) # str to url format

        if data['date'] and data['time']:
            date_time = data['date'] + ' ' + data['time']
            args += urllib.parse.quote('/' + date_time)

        # Make the API call
        url = 'http://localhost:8080/api/room-occupancy/' + args
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return render(request, 'occupancy.html', {'form': form, 'inside': data['inside']})
        elif response.status_code == 404:
            return render(request, 'occupancy.html', {'form': form, 'inside': -1})
        else:
            print('Error:', response.status_code)

    return render(request, 'occupancy.html', {'form': form})