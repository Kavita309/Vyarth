from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms

class GeneratorView(CreateView):
    form_class = forms.Generator
    success_url = reverse_lazy('home')
    template_name = 'generator.html'


class CollectorView(CreateView):
    form_class = forms.Collector
    success_url = reverse_lazy('home')
    template_name = 'Collector.html'


class LoginView(TemplateView):
    template_name = 'login.html'
