# room-occupancy-sensor
This is a Django app that can count the number of people in a room using sensors.

# Description
Check the pdf to get an insight of the complete subject.

This include Front/Back and an API using Django Rest Framework

# Installation
`sudo apt-get install python3`
`pip install django`

# Usage
## Run the server
`python3 manager.py runserver 0.0.0.0:8080`

## Run unit testing
`python3 manager.py test`
(Server must be running)

## API Endpoints
### Get
`/api/room-occupancy/` show all available room sensors

`api/room-occupancy/<sensor_name>` fetch a room sensor latest occupancy data

`api/room-occupancy/<sensor_name>/<date_time>` fetch a room sensor occupancy data at a specific datetime

### Post

`/api/room-occupancy/` used by the room sensor to send the occupancy count

e.g:
`curl --header "Content-Type: application/json"
--request POST --data
'{ "sensor_name": "sensor name", "timestamp": "2023-01-01 10:00", "inside": "25", "out": "5" }'
http://localhost:8080/api/room-occupancy/`







