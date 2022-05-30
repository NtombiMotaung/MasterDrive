from django.shortcuts import render
from gallery.models import ContactImages

# Create your views here.
def gallery(request):
    image = ContactImages.objects.last()
    context = {
            "code8" : image

    }
    return render(request, "public/gallery/gallery.html", context)
