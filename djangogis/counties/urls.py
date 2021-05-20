from django.urls import path
from .views import HomePageView, county_points

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('countypoints/', county_points, name="countypoints"),
]