from audioop import reverse
from unittest.mock import patch
from django.test import Client
from django.test import TestCase
from query.connection import JsonPlaceholderConnection


class QueryListingTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()

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


class ConnectionTestCase(TestCase):

    def setUp(self) -> None:
        self.conn = JsonPlaceholderConnection()

    def test_get_result_should_be_a_list(self):
        result = self.conn.get("todos")

        self.assertEqual(list, type(result))
