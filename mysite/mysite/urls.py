from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('staff/', admin.site.urls),
    path('services/', include("services.urls", namespace = "services"))
]
