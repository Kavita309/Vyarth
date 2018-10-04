"""vyarth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"^login/$", auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    url(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"^signup/$", views.SignUp.as_view(), name="signup"),
    url(r"^gview/$", views.GenView.as_view(), name="gview"),
    url(r"^cview/$", views.ColView.as_view(), name="cview"),
    url(r'^result/$',views.Result.as_view(),name='result'),
    url(r"^new_view/$", views.new_view, name="new_view"),

]
