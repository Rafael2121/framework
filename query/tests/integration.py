from audioop import reverse
from email import header
from unittest.mock import patch
from venv import create
from django.test import Client
from django.test import TestCase
from query.connection import JsonPlaceholderConnection
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class QueryListingTestCase(TestCase):

    def setUp(self) -> None:
        token = self.create_token()

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def create_token(self):
        user = User.objects.create(username="test_root")

        token = Token.objects.get_or_create(user=user)

        return token[0]

    def test_get(self):
        response = self.client.get("/")

        self.assertEqual(200, response.status_code)

    def test_get_response(self):
        response = self.client.get("/")

        data = response.data

        self.assertEqual(list, type(data))
        self.assertEqual(["id", "title"], list(data[0].keys()))

    @patch("query.connection.JsonPlaceholderConnection.get")
    def test_get_error_format(self, mock_get):
        response = self.client.get("/")

        mock_get.return_value = []

        self.assertEqual(500, response.status_code)

        expected = {
            "error": {
                "reason": "Response has less than five results"
            }
        }
        self.assertEqual(expected, response.data)

    def test_get_error_not_authenticated_format(self):
        client = APIClient()

        response = client.get("/")

        self.assertEqual(401, response.status_code)

        expected = {
            "error": {
                "reason": "Authentication credentials were not provided."
            }
        }
        self.assertEqual(expected, response.data)


class ConnectionTestCase(TestCase):

    def setUp(self) -> None:
        self.conn = JsonPlaceholderConnection()

    def test_get_result_should_be_a_list(self):
        result = self.conn.get("todos")

        self.assertEqual(list, type(result))
