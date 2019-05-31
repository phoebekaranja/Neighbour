from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 500)
    count = models.PositiveIntegerField()
