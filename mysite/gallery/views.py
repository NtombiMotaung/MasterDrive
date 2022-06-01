from django.shortcuts import render

from gallery.models import GalleryImages, BackgroundImage


# Create your views here.
def gallery(request):
    image = GalleryImages.objects.all()
    bg = BackgroundImage.objects.last()
    context = {
        "image" : image,
        "bg" : bg,

    }
    
    return render(request, "public/gallery/gallery.html", context)

    
    



