from gallery.models import GalleryBackground
from django.shortcuts import render 

def index(request):
    bg = GalleryBackground.objects.last()
    context = {
        "bg": bg,
    }
    return render(request, "public/gallery/gallery.html", context)