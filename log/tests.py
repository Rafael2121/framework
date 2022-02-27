from django.test import Client
from django.test import TestCase
from .models import Log


class LoggingTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.client.get("/")
    
    def test_api_call_should_create_log(self):
        self.assertTrue(Log.objects.exists())