from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from Users.models import profile
from django.contrib.auth.models import User
from django.contrib import messages
from Users.models import profile, tags, blog


def land(request):
    return render(request, "landing ori.html")


def result(request):
    return render(request, "landing.html")

def login_page(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            # messages.success(request, "success")
            return redirect('home')
        else:
            
            messages.error(request, "error")
            
    return render(request, "login.html")

def domains(request):
    tag=tags.objects.all()
    
    context={
       "web": profile.objects.filter(tags=tag[0]),
        "AI/ML":profile.objects.filter(tags=tag[1]),
        "AR/VR":profile.objects.filter(tags=tag[2]),
        "app":profile.objects.filter(tags=tag[3]),
        "block":profile.objects.filter(tags=tag[4]),
    }

    return render(request,"domain.html", context)



