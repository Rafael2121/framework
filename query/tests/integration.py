from django.test import TestCase
from query.connection import JsonPlaceholderConnection


class ConnectionTestCase(TestCase):

    def setUp(self) -> None:
        self.conn = JsonPlaceholderConnection()

    def test_get_result_should_be_a_list(self):
        result = self.conn.get("todos")

        self.assertEqual(list, type(result))