from django.shortcuts import render

from gallery.models import GalleryImages, GalleryBackground


# Create your views here.
def gallery(request):
    image = GalleryImages.objects.all()
    bg = GalleryBackground.objects.last()
    context = {
        "image" : image,
        "bg" : bg,

    }
    
    return render(request, "public/gallery/gallery.html", context)

    
    



