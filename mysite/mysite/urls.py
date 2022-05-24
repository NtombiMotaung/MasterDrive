from django.conf import settings
from django.conf.urls.static import staticw
from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    [
        path("staff/", admin.site.urls),
        path("services/", include("services.urls", namespace="services")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
