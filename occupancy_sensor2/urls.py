"""occupancy_sensor2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from occupancy_app import views
from occupancy_app.endpoints import *

urlpatterns = [
    # Default
    path('admin/', admin.site.urls),
    # Validation
    path('hello/', views.hello),
    path('my-endpoint/', MyEndpoint.as_view()),
    # App
    path('', views.occupancy),
    path('occupancy/', views.occupancy),
    # Endpoints
    path('api/room-occupancy/', RoomOccupancy.as_view()),
    path('api/room-occupancy/<str:sensor_name>', RoomOccupancy.as_view()),
    path('api/room-occupancy/<str:sensor_name>/<str:date_time>', RoomOccupancy.as_view()),
]
