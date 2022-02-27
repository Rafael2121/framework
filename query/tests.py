from http import client
from unittest import skip
from django.test import TestCase
from .services import JsonPlaceholderService
from .connection import JsonPlaceholderConnection


class ServiceTestCase(TestCase):

    def setUp(self) -> None:
        self.service = JsonPlaceholderService()

    def test_fetch_all(self):

        result = self.service.fetch_all()

        self.assertTrue(result)


class ConnectionTestCase(TestCase):

    def setUp(self) -> None:
        self.conn = JsonPlaceholderConnection()

    def test_get_result_should_be_a_list(self):
        result = self.conn.get("todos")

        self.assertEqual(list, type(result))

