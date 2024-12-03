import unittest
import requests
from unittest.mock import patch, MagicMock
from requests.models import Response
from requests.structures import CaseInsensitiveDict
from google_books_api.google_books_api import GoogleBookApi


class TestSearchBook(unittest.TestCase):

    GOOGLE_BASE_URL = "FAKE_URL"

    @patch("requests.request")
    def test_search_book(self, mock_request):
        book_goggle_api = GoogleBookApi(self.GOOGLE_BASE_URL)
        mock_response = MagicMock(spec=Response)
        mock_response.json.return_value = {
            "totalItems": 100,
            "items": [{"volumeInfo": {"title": "The Great Gatsby"}}],
        }
        mock_response.headers = CaseInsensitiveDict(
            {"content-type": "application/json"}
        )
        mock_request.return_value = mock_response

        search_params = {"q": "The Great Gatsby"}
        result = book_goggle_api.search_book(search_params)

        self.assertEqual(result.total_items, 100)

    @patch("requests.request")
    def test_search_book_by_title(self, mock_request):
        book_goggle_api = GoogleBookApi(self.GOOGLE_BASE_URL)
        mock_response = MagicMock(spec=Response)
        mock_response.json.return_value = {
            "totalItems": 100,
            "items": [{"volumeInfo": {"title": "The Great Gatsby"}}],
        }
        mock_response.headers = CaseInsensitiveDict(
            {"content-type": "application/json"}
        )
        mock_request.return_value = mock_response

        response = book_goggle_api.search_by_title("The Great Gatsby", 1)

        self.assertEqual(response.total_items, 100)

    @patch("requests.request")
    def test_get_book_by_id(self, mock_request):
        book_goggle_api = GoogleBookApi(self.GOOGLE_BASE_URL)
        mock_response = MagicMock(spec=Response)
        mock_response.json.return_value = {
            "id": "123",
            "volumeInfo": {
                "title": "The Great Gatsby",
                "description": "A book",
                "publishedDate": "1925",
            },
        }
        mock_response.headers = CaseInsensitiveDict(
            {"content-type": "application/json"}
        )
        mock_request.return_value = mock_response

        book = book_goggle_api.get_by_id("123")

        self.assertEqual(book.title, "The Great Gatsby")
        self.assertEqual(book.google_id, "123")
        self.assertEqual(book.description, "A book")

    @patch("requests.request")
    def test_make_request(self, mock_request):
        book_goggle_api = GoogleBookApi(self.GOOGLE_BASE_URL)
        mock_response = MagicMock(spec=Response)
        mock_response.json.return_value = {
            "id": "123",
            "volumeInfo": {
                "title": "The Great Gatsby",
                "description": "A book",
                "publishedDate": "1925",
            },
        }
        mock_response.headers = CaseInsensitiveDict(
            {"content-type": "application/json"}
        )
        mock_request.return_value = mock_response

        response = book_goggle_api._make_get_request(
            "volumes", {"q": "The Great Gatsby"}
        )

        self.assertEqual(response.body, mock_response.json())

    @patch("requests.request")
    def test_make_request_error(self, mock_request):
        book_goggle_api = GoogleBookApi(self.GOOGLE_BASE_URL)
        mock_request.side_effect = requests.exceptions.RequestException(
            "HTTP request failed"
        )
        mock_response = MagicMock(spec=Response)
        mock_response.json.return_value = {
            "error": "An error occurred",
        }
        mock_response.headers = CaseInsensitiveDict(
            {"content-type": "application/json"}
        )
        mock_request.return_value = mock_response

        with self.assertRaises(Exception):
            book_goggle_api._make_get_request("volumes", {"q": "The Great Gatsby"})
