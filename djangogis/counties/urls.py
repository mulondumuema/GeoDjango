from django.urls import path
from .views import HomePageView, county_points, county_datasets

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('countypoint/', county_points, name="countypoints"),
    path('countiesdataset/', county_datasets, name="countiesdata"),
]