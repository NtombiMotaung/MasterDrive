from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request, "public/gallery/gallery.html")

