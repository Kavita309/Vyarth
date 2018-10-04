from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms


class HomePage(TemplateView):
    template_name = "index.html"


class SignUpG(CreateView):
    form_class = forms.GeneratorForm
    success_url = reverse_lazy("login")
    template_name = "signupG.html"

class SignUpC(CreateView):
    form_class = forms.CollectorForm
    success_url = reverse_lazy("login")
    template_name = "SignupC.html"

class Submitkarowaste(CreateView):
    form_class=forms.SubmitWasteForm
    #success_url=
    template_name="Generator.html"
