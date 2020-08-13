from django.shortcuts import render
from django.http import HttpResponse
from .models import Mtmap, GPXsave 
from django.core.serializers import serialize

# Create your views here.

def Mtmap_view(request):
    context = {}
    return render(request, 'map/Mtmap_view.html', context)

def Mtpoints_view(request):
    points_as_geojson = serialize('geojson', Mtmap.objects.all())
    return HttpResponse(points_as_geojson, content_type='json')

def Cyclemap_view(request):
    context = {}
    return render(request, 'map/Cyclemap_view.html', context)

def Cycleroute_view(request):
    routes_as_geojson = serialize('geojson', GPXsave.objects.all())
    return HttpResponse(routes_as_geojson, content_type='json')

