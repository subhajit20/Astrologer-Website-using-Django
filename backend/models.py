from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date  = models.DateField()
    time  = models.TimeField()
    place = models.CharField(max_length=100)
    lat  = models.DecimalField(max_digits=10, decimal_places=6)
    lon  = models.DecimalField(max_digits=10, decimal_places=6)
    tzone = models.CharField(max_length=100)