from django.shortcuts import render
from django.http import HttpResponse
from .models import Mtmap
from django.core.serializers import serialize

# Create your views here.

def Mtmap_view(request):
    context = {"maps":Mtmap.objects.get(pk=1)}
    return render(request, 'map/Mtmap_view.html', context)

def Mtpoints_view(request):
    points_as_geojson = serialize('geojson', Mtmap.objects.all())
    return HttpResponse(points_as_geojson, content_type='json')
