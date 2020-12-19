from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import MyModel


@admin.register(MyModel)
class MyModelAdmin(OSMGeoAdmin):
    default_lon = 0
    default_lat = 0
    default_zoom = 1
