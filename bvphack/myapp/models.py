from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

    def get_absolute_url(self):
        return reverse("home")

class SubmitWaste(models.Model):
    WASTE_CHOICES= [
        ('plastic', 'Plastic'),
        ('paper', 'Paper'),
        ('metal', 'Metal'),
        ('glass', 'Glass'),
         ('organic','Organic')
        ]
    contact=models.IntegerField(null=True)

    COMMUNITY_CHOICES= [
            ('household', 'Household'),
            ('industry', 'Industry'),
            ('market', 'Market'),
            ('office', 'Office'),
            ]
    communityName= models.CharField(max_length=1024,choices=COMMUNITY_CHOICES,default='household')
    typeofwaste= models.CharField(max_length=1024,choices=WASTE_CHOICES,default='organic')
    #typeofwaste=models.CharField(max_length=1024)
    address=models.TextField(max_length=1024, blank=True)
    quantityofwaste=models.IntegerField()

class CollectWaste(models.Model):
    WASTE_CHOICES= [
        ('plastic', 'Plastic'),
        ('paper', 'Paper'),
        ('metal', 'Metal'),
        ('glass', 'Glass'),
        ]
    typerequired=models.CharField(max_length=1024,choices=WASTE_CHOICES,default='plastic')
    contact=models.IntegerField(null=True)
    address=models.TextField(max_length=1024, blank=True)
