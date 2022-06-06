from gallery.models import  HomePicture
from django.shortcuts import render 

def index(request):
    bg = HomePicture.objects.last()
    context = {
        "bg": bg,
    }
    return render(request, "public/index.html", context)