from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from .models import County
from .models import counties



# class CountyAdmin(OSMGeoAdmin):
@admin.register(County)
class CountyAdmin(LeafletGeoAdmin): 
    list_display = ('name', 'location')

@admin.register(counties)
class countiesAdmin(LeafletGeoAdmin):
    list_display = ('county_1', 'id')


