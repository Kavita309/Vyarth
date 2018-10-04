from django.db import models

# Create your models here.



class Generator(models.Model):
    name=models.CharField(max_length=256)
    communityName=models.TextField(max_length=256)
    address=models.TextField(max_length=1024)
    email=models.EmailField(max_length=1024,null=True, blank=True)
    contact=models.CharField(null=True,max_length=256)
    # FRUIT_CHOICES= [
    #     ('orange', 'Oranges'),
    #     ('cantaloupe', 'Cantaloupes'),
    #     ('mango', 'Mangoes'),
    #     ('honeydew', 'Honeydews'),
    #     ]
    # favorite_fruit= models.CharField(max_length=1024,choices=FRUIT_CHOICES,default='orange')


class Collector(models.Model):
    name=models.CharField(max_length=256)
    address=models.TextField(max_length=1024)
    email=models.EmailField(max_length=1024,null=True, blank=True)
    contact=models.CharField(null=True,max_length=256)

class SubmitWaste(models.Model):
    typeofwaste=models.CharField(max_length=1024)
    quantityofwaste=models.IntegerField(max_length=1024)
