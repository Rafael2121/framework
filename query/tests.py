from http import client
from unittest import skip
from unittest.mock import MagicMock
from django.test import TestCase
from .services import JsonPlaceholderService
from .connection import JsonPlaceholderConnection
from .repository import QueryRepository
from .facades import QueryFacade


class RepositoryTestCase(TestCase):

    def test_fetch_should_have_five_results(self):
        repository = QueryRepository()

        result = repository.fetch()

        expected = 5

        self.assertEqual(expected, len(result))

    def test_fetch_should_return_correct_data_format(self):
        repository = QueryRepository()

        result = repository.fetch()

        expected = {
            "id": 1,
            "title": "delectus aut autem"
        }

        self.assertEqual(expected, result[0])
    
    def test_fetch_with_less_than_five_results_should_raise_exception(self):
        repository = QueryRepository()

        repository.service = MagicMock(get=MagicMock(return_value=[]))

        with self.assertRaises(Exception):
            result = repository.fetch()


class FacadeTestCase(TestCase):

    def test_parse_return(self):
        entry = {
            "userId": 99,
            "id": 99,
            "title": "Elden Ring é sensacional",
            "completed": False
        }

        facade = QueryFacade(entry)

        result = facade.parse()

        expected = {
            "id": 99,
            "title": "Elden Ring é sensacional"
        }

        self.assertEqual(expected, result)

    def test_parse_with_missing_data_should_raise_exception(self):
        entry = {
            "title": "Elden Ring é sensacional"
        }

        facade = QueryFacade(entry)

        with self.assertRaises(Exception):
            result = facade.parse()


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

