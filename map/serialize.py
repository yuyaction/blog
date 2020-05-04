from django.core.serializers import serialize
from .models import Mtmap

def Pointjson():
    serialize('geojson', Mtmap.objects.all(),geometry_field='point',fields=('name',))
