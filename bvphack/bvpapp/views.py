from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms

class GeneratorView(CreateView):
    model = Generator
    form_class = forms.Generator
    success_url = reverse_lazy('home')
    template_name = 'Generator.html'


class CollectorView(CreateView):
    model = Collector
    form_class = forms.Collector
    success_url = reverse_lazy('home')
    template_name = 'Collector.html'

############# KAVITA CHECK


class LoginView(TemplateView):
    template_name = 'login.html'

class SubmitWasteView(CreateView):
    model = SubmitWaste
    form_class= forms.SubmitWaste
    #success_url
    #template_name='thankyou.html'

class CollectWasteView(TemplateView):
    model = SubmitWaste
    form_class= forms.CollectWaste
    #success_url
    #template_name='thankyou.html'
