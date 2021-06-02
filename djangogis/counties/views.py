from django.shortcuts import render
from django.views.generic import TemplateView

from django.core.serializers import serialize
from django.http import HttpResponse
from .models import County, counties


# Create your views here.
class HomePageView(TemplateView):
    template_name= 'index.html'

def county_points(request):
	countypoints = serialize('geojson', County.objects.all())
	return HttpResponse(countypoints,content_type='application/json')

def county_datasets(request):
	countiesdata = serialize('geojson', counties.objects.all())
	return HttpResponse(countiesdata,content_type='application/json')