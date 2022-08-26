from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.prof, name ="club"),
    path('blog/', views.blogs, name="blog")
    
]
