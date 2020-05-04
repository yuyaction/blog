from django.shortcuts import render
from django.http import HttpResponse
from .models import Mtmap

# Create your views here.

def Mtmap_view(request):
    context = {"maps":Mtmap.objects.get(pk=1)}
    return render(request, 'map/Mtmap_view.html', context)
