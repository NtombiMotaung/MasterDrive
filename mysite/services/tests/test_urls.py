from django.test import TestCase
from django.urls import reverse


class TestServicesUrls(TestCase):
    def test_get_services_page(self):
        url = reverse("services:get-services-page")
        self.assertEqual(url , "/services/")

    def test_get_service(self):
        url = reverse("services:get-service", kwargs={"id": "1"})
        self.assertEqual(url , "/services/1/")
