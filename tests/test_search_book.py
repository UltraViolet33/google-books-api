import unittest
from unittest.mock import patch, MagicMock
from requests.models import Response
from requests.structures import CaseInsensitiveDict
from google_books_api.google_books_api import GoogleBookApi


class TestSearchBook(unittest.TestCase):

    @patch("requests.request")
    def test_search_book(self, mock_request):
        book_goggle_api = GoogleBookApi("https://www.googleapis.com/books/v1/")
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
        book_goggle_api = GoogleBookApi("https://www.googleapis.com/books/v1/")
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
