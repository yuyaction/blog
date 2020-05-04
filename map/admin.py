from django.contrib.gis import admin
from .models import Mtmap
# Register your models here.

admin.site.register(Mtmap,admin.OSMGeoAdmin)
