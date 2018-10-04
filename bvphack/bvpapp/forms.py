

from django import forms

from . models import Generator,Collector,SubmitWaste, CollectWaste


class Generator(forms.ModelForm):

    class Meta:
        model = Genertor
        fields = ['name', 'email','communityName','contact','address']

class Collector(forms.ModelForm):

    class Meta:
        model = Collector
        fields = ['name','address','contact','email']

class SubmitWaste(forms.ModelForm):

    class Meta:
        model= SubmitWaste
        fields = ['typeofwaste','quantityofwaste']

class CollectWasteForm(forms.ModelForm):

    class Meta:
        model= CollectWaste
        field = ['typerequired']
