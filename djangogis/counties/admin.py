from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from .models import County

from leaflet.admin import LeafletGeoAdmin

@admin.register(County)
# class CountyAdmin(OSMGeoAdmin):
class CountyAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
