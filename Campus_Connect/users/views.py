from xml.sax import make_parser
from django.shortcuts import render
from django.http import HttpResponse

from . models import profile

def prof(request):
    profiles=profile.objects.get(id=3)
    context={"name": profiles.Name,
            "college": profiles.college,}
    return render(request, "club.html", context)

