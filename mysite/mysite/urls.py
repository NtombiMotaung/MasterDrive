from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from gallery.models import BackgroundImage

def index(request):
    bg = BackgroundImage.objects.last()
    context = {
        "bg": bg,
    }
    return render(request, "public/index.html", context)

urlpatterns = (
    [
        path("staff/", admin.site.urls),
        path("services/", include("services.urls", namespace="services")),
        path("contacts/", include("contacts.urls", namespace = "contacts")),
        path("gallery/", include("gallery.urls", namespace= "gallery") ),
        path("",  index),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
