import os
from django.contrib.gis.utils import LayerMapping
from .models import counties
from djangogis.settings import BASE_DIRe

counties_mapping = {
    'county_1': 'County_1',
    'county_1_2': 'County_1_2',
    'id': 'ID',
    'geom': 'MULTIPOLYGON',
}

county_shp = folder_path = os.path.join(BASE_DIRe, 'djangogis/data/counties/counties.shp')
# county_shp = folder_path = os.path.join(BASE_DIRe, 'djangogis/data/counties/counties.shp')


def run(verbose=True):
    lm = LayerMapping(counties, county_shp, counties_mapping)
    lm.save(verbose=True)
