from django.core.serializers import serialize
from .models import Mtmap, GPXsave

def Pointjson():
    serialize('geojson', Mtmap.objects.all(),geometry_field='point',fields=('name',))

def Routejson():
    serialize('geojson', GPXsave.objects.all())

