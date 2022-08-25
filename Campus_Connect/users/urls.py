from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.prof),
    path('blog/', views.blog, name="blog")
]
