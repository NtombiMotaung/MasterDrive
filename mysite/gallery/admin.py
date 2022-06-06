from django.contrib import admin
from gallery.models import GalleryBackground, GalleryImages, HomePicture

# Register your models here.

admin.site.register(GalleryBackground)
admin.site.register(GalleryImages)
admin.site.register(HomePicture)

