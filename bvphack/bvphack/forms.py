from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from bvpapp.models import Generator, Collector, SubmitWaste


class GeneratorForm(forms.ModelForm):
    class Meta:
        model = Generator
        fields = ['name','communityName','address','contact','email']





class CollectorForm(forms.ModelForm):
    class Meta:
        model = Collector
        fields = ['name','email','address','contact']

class SubmitWasteForm(forms.ModelForm):
    class Meta:
        model= SubmitWaste
        fields = ['typeofwaste','quantityofwaste']
