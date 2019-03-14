from django.test import TestCase
from django.test import Client


class ConferenceListTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_no_conferences(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_jakkolwiek(self):
        #powinien stworzyc sb jedna kofenrencje
        #potem sciagnac response
        #i sprawdzic czy nazwa konferencji jest w response.content