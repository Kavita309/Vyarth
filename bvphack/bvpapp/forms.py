

from django import forms

from . models import Child

class Generator(forms.ModelForm):

    class Meta:
        model = Genertor
        fields = ('name', 'email','communityName','contact','address')

class Collector(forms.ModelForm):

    class Meta:
        model = Collector
        fields = ('name','address','contact','email')
