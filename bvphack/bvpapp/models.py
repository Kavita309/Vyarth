from django.db import models

# Create your models here.

class Generator(models.Model):
    name=models.CharField(max_length=256)
    communityName=models.TextField(max_length=256)
    address=models.TextField(max_length=1024)
    # email=models.EmailFeild()
    contact=models.CharField(null=True,max_length=256)

class Collector(models.Model):
    name=models.CharField(max_length=256)
    address=models.TextField(max_length=1024)
    email=models.EmailField()
    contact=models.CharField(null=True,max_length=256)
