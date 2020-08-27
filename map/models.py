from django.contrib.gis.db import models

# Create your models here.

class Mtmap(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField('Climbed date')
    Mtposition = models.PointField('Position',srid=4326)
    photo1 = models.ImageField(upload_to='mountain/', blank=True)
    photo2 = models.ImageField(upload_to='mountain/', blank=True)
    photo3 = models.ImageField(upload_to='mountain/', blank=True)
    photo4 = models.ImageField(upload_to='mountain/', blank=True)
    photo5 = models.ImageField(upload_to='mountain/', blank=True)

    def __str__(self):
        return self.name

class GPXsave(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Bike ride date')
    gpx_file = models.FileField(upload_to='gpx_files/')

    def __str__(self):
        return self.name
