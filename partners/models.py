from django.db import models
from django.utils import timezone


# Create your models here.
class Partner(models.Model):
    dni = models.CharField(max_length=9, null=False)
    email = models.EmailField(max_length=200, null=False)
    name = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    postal_code = models.CharField(max_length=5, null=False)
    created_date = models.DateTimeField(default=timezone.now)
