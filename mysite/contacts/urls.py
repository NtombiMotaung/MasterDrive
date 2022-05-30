from django.urls import path
from contacts.views import contact_page


app_name = "contacts"

urlpatterns = [

    path("", contact_page, name="get-contacts-page"),
]