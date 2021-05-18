from django.contrib.gis.db import models

class County(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)   # PointField is aGeoDjango specificgeometricfieldforstoring a GEOS point
    capital = models.CharField(max_length=50)
    population = models.IntegerField()

class counties(models.Model):
    county_1 = models.CharField(max_length=25)
    county_1_2 = models.CharField(max_length=254)
    id = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return 'Name: %s' % self.name
