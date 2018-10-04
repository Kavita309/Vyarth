from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from myapp.models import SubmitWaste,CollectWaste
from . import forms

class HomePage(TemplateView):
    template_name = "index.html"

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class GenView(CreateView):
    model = SubmitWaste
    form_class= forms.SubmitWasteForm
    success_url = reverse_lazy("home")
    template_name = "SignupG.html"
    #success_url
    #template_name='thankyou.html'

class ColView(CreateView):
    model = CollectWaste
    form_class= forms.CollectWasteForm
    success_url = reverse_lazy("home")
    template_name = "SignupC.html"


    #success_url
    #template_name='thankyou.html'
