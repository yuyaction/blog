from django.contrib.gis.db import models

# Create your models here.

class Mtmap(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField('Climbed date')
    Mtposition = models.PointField('Position',srid=4326)
    photo = models.ImageField(upload_to='mountain/')

    def __str__(self):
        return self.name
    
