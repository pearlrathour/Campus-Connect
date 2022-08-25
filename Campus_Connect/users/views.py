from tokenize import Name
from xml.sax import make_parser
from django.shortcuts import render
from django.http import HttpResponse

from . models import profile
from django.contrib.auth.models import User


def prof(request):
#     users=User.objects.get(id=1)
    profiles=profile.objects.get(id=7)
    
    context={
        "name" : profiles.Name,
    }
    return render(request, "club.html",context)

def blog(request):
        return render(request, "blog.html")


