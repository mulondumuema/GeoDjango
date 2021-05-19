from django.contrib.gis.utils import LayerMapping
from .models import counties
from djangogis.settings import BASE_DIRe

counties_mapping = {
    'county_1': 'County_1',
    'county_1_2': 'County_1_2',
    'id': 'ID',
    'geom': 'MULTIPOLYGON',
}

county_shp = folder_path = os.path.join(BASE_DIRe, 'data/counties/counties.shp')

def run(verbose=True): 
    lm = LayerMapping(counties, county_shp, mapping)
    lm.save(verbose=True)