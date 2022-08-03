from django.db import models


# Create your models here.

class full_Details(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(max_length=255)