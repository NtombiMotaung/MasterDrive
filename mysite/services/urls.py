from django.urls import path
from services.views import get_services, get_service


app_name = "services"

urlpatterns = [

    path("", get_services, name="get-services-page"),
    path("<id>/", get_service, name="get-service"),


]
