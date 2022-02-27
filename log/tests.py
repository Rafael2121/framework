from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from .models import Log


class LoggingTestCase(TestCase):

    def setUp(self) -> None:
        token = self.create_token()

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def create_token(self):
        user = User.objects.create(username="test_root")

        token = Token.objects.get_or_create(user=user)

        return token[0]
    
    def test_api_call_should_create_log(self):
        response = self.client.get("/")

        self.assertEqual(200, response.status_code)
        self.assertTrue(Log.objects.exists())