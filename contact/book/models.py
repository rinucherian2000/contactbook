from django.db import models

# Create your models here.

class Phone(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=120)
    phone= models.PositiveIntegerField(max_length=10)
    date = models.DateField(auto_now_add=True, null=True)
