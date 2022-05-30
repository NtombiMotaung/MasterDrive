from gallery.models import BackgroundImage
from django.shortcuts import render 

def index(request):
    bg = BackgroundImage.objects.last()
    context = {
        "bg": bg,
    }
    return render(request, "public/index.html", context)