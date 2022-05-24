from django.test import Client, TestCase
from django.urls import reverse

class TestServicesViews(TestCase):
    def setUp(self) :
        self.client = Client()

    def test_get_services_page(self):
        url = reverse("services:get-services-page")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "public/services/services.html")

    def test_get_service(self):
        url = reverse("services:get-service")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "public/services/get-services.html")
