from tokenize import Name
from xml.sax import make_parser
from django.shortcuts import render
from django.http import HttpResponse

from . models import profile, tags, blog
from django.contrib.auth.models import User



def prof(request):
#     users=User.objects.get(id=1)
    profiles=profile.objects.all()
    
    blogs=blog.objects.all()
    tagss=tags.objects.all()
    context={
                "tag":tagss,
                "title":blogs,
                "name" : profiles,
                "blog":blogs
        }
    return render(request, "club.html",context)

def blogs(request):
        
        return render(request, "blog.html")


