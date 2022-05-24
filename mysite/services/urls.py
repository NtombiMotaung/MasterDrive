from django.urls import path
from services.views import get_services


app_name = "services"

urlpatterns = [path("", get_services, name="get-services-page")]
