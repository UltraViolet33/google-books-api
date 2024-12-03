import unittest
from google_books_api.models import GoogleBook


class TestBook(unittest.TestCase):
    BOOK_ITEM = {
        "id": "123",
        "volumeInfo": {
            "title": "The Great Gatsby",
            "description": "A book",
            "publishedDate": "1925",
        },
    }

    def test_create_google_book(self):
        book = GoogleBook(self.BOOK_ITEM)
        self.assertEqual(book.title, "The Great Gatsby")
        self.assertEqual(book.google_id, "123")
        self.assertEqual(book.description, "A book")
        self.assertEqual(book.published_date, "1925")

    def test_parse_authors(self):
        authors = ["F. Scott Fitzgerald"]
        item = {"volumeInfo": {"authors": authors}}
        book = GoogleBook(item)
        self.assertEqual(len(book.authors), 1)
        self.assertEqual(book.authors[0].name, "F. Scott Fitzgerald")
