to checkout the layer in the python manage.py shell:
1. get into the shell while in the virtualenvironment:
```
$ python manage.py shell
```
2. In the shell import the Datasource library and run the commands to checkout the layers:

```
>>> from django.contrib.gis.gdal import DataSource
>>> ds = DataSource("djangogis/data/counties/counties.shp")
>>> layer= ds[0]
>>> print(layer.fields)
>>> print(len(layer))
>>> print(layer.srs)
>>> print(layer.geom_type)
```
To generate a mapping model, use ogrinspect management command
```
$ python manage.py ogrinspect [options] <data_source> <model_name> [options]
```
data_source is the path to the GDAL-supported data source and model_name is the name to use for the model. Command-line options may be used to further define how the model is generated.

For example:

```
$ python manage.py ogrinspect djangogis/data/counties/counties.shp counties --srid=4326 --mapping --multi
```

A few notes about the command-line options given above:

- The --srid=4326 option sets the SRID for the geographic field.
- The --mapping option tells ogrinspect to also generate a mapping dictionary for use with LayerMapping.
- The --multi option is specified so that the geographic field is a MultiPolygonField instead of just a PolygonField.

The command produces the following output, which may be copied directly into the models.py of a GeoDjango application:

```
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class counties(models.Model):
    county_1 = models.CharField(max_length=25)
    county_1_2 = models.CharField(max_length=254)
    id = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)


# Auto-generated `LayerMapping` dictionary for counties model
counties_mapping = {
    'county_1': 'County_1',
    'county_1_2': 'County_1_2',
    'id': 'ID',
    'geom': 'MULTIPOLYGON',
}
(geod
```