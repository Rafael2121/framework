import json
from django.test import TestCase
from unittest.mock import MagicMock, patch
from query.services import JsonPlaceholderService
from query.repository import QueryRepository
from query.facades import QueryFacade


def read_mock():
    with open("query/tests/response_mock.json") as fileContent:
        return json.load(fileContent)


class RepositoryTestCase(TestCase):

    @patch("query.connection.JsonPlaceholderConnection.get")
    def test_fetch_should_have_five_results(self, mock_get):
        mock_get.return_value = read_mock()
        
        repository = QueryRepository()

        result = repository.fetch()

        expected = 5

        self.assertEqual(expected, len(result))

    @patch("query.connection.JsonPlaceholderConnection.get")
    def test_fetch_should_return_correct_data_format(self, mock_get):
        mock_get.return_value = read_mock()

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
            repository.fetch()


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


@patch("query.connection.JsonPlaceholderConnection.get")
class ServiceTestCase(TestCase):

    def setUp(self) -> None:
        self.service = JsonPlaceholderService()

    def test_fetch_all(self, mock_get):

        mock_get.return_value = read_mock()

        result = self.service.fetch_all()

        self.assertEqual(list, type(result))
