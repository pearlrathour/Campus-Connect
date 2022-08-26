from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("domain", views.domains, name="domain"),
    path("login", views.login_page, name="login-page"),
    path("result", views.result, name="Result"),
    path('', views.land, name="Home"),
    path('trending', views.trending, name="trend")
]