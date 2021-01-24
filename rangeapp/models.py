from django.db import models

# Create your models here.

class Aircraft(models.Model):
    aircraft_name = models.CharField(max_length=99)
