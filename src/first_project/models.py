import sys
sys.path.append('.')
from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=True)

class Sport(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=True)

class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=False)

class Customer(models.Model):
    name = models.CharField(max_length=100, null=False)
    num_doc = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=20, null=True)
