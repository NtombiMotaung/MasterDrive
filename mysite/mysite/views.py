from gallery.models import  HomePicture, WelcomePicture
from django.shortcuts import render 

def index(request):
    bg = HomePicture.objects.last()
    welcome_pic = WelcomePicture.objects.last()
    context = {
        "bg": bg,
        "wp" : welcome_pic,
    }
    return render(request, "public/index.html", context)