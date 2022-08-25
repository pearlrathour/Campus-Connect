from xml.sax import make_parser
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def prof(request):
    return HttpResponse("hello")
