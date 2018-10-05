from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from myapp.models import SubmitWaste,CollectWaste
from . import forms
from geopy.geocoders import Nominatim
from geopy import distance
from operator import itemgetter
from tabulate import tabulate

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

class Result(TemplateView):
    template_name='result.html'
geolocator = Nominatim(user_agent="specify_your_app_name_here")
def new_view(request):
    form=forms.CollectWasteForm()
    if request.method=='POST':
        form=forms.CollectWasteForm(request.POST)
        if form.is_valid():
            print("hello")
            a=form.cleaned_data['typerequired']
            b=form.cleaned_data['address']
            b=geolocator.geocode(b)
            lat=b.latitude
            lon=b.longitude
            tup1=(lat,lon)
            print(lat,lon,"hello")
            print(a)
            v=SubmitWaste.objects.filter(typeofwaste=a).values_list()
            print(v)
            list1=[]
            rt=[]
            for i in v:
                temp=[]
                temp.append(i[4])
                temp.append(i[5])
                print(i[4])
                list1.append(geolocator.geocode(i[4],timeout=10))
                rt.append(temp)
            dist=[]
            for ele in list1:
                tup2=(ele.latitude,ele.longitude)
                dist.append(distance.distance(tup1, tup2).km)
            print(dist)
            j=0
            for m in dist:
                rt[j].append(m)
                j=j+1

            rt=sorted(rt, key=itemgetter(2))
            print(rt)

        return render(request,'result.html',{'val':rt})
    return render(request,'SignupC.html',{'form':form})
