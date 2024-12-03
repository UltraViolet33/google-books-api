import unittest
from google_books_api.models import GoogleBook, GoogleBookBuilder


class TestBook(unittest.TestCase):
    BOOK_ITEM = {
        "id": "123",
        "volumeInfo": {
            "title": "The Great Gatsby",
            "description": "A book",
            "publishedDate": "1925",
        },
    }

    def test_create_google_book_builder(self):
        builder = GoogleBookBuilder([self.BOOK_ITEM])
        books = builder.build()
        self.assertEqual(len(books), 1)
        book = books[0]
        self.assertEqual(book.title, "The Great Gatsby")
        self.assertEqual(book.google_id, "123")
        self.assertEqual(book.description, "A book")

    def test_parse_authors(self):
        authors = ["F. Scott Fitzgerald"]
        item = {"volumeInfo": {"authors": authors}}
        book = GoogleBookBuilder([item]).build()[0]
        self.assertEqual(len(book.authors), 1)
        self.assertEqual(book.authors[0].name, "F. Scott Fitzgerald")

    def test_parse_isbn(self):
        isbn_13 = "9780743273565"
        isbn_10 = "0743273567"
        item = {
            "volumeInfo": {
                "industryIdentifiers": [
                    {"type": "ISBN_13", "identifier": isbn_13},
                    {"type": "ISBN_10", "identifier": isbn_10},
                ]
            }
        }
        book = GoogleBookBuilder([item]).build()[0]
        self.assertEqual(book.isbn_13, isbn_13)
        self.assertEqual(book.isbn_10, isbn_10)

    def parse_categories(self):
        categories = ["Fiction"]
        item = {"volumeInfo": {"categories": categories}}
        book = GoogleBookBuilder([item]).build()[0]
        self.assertEqual(len(book.categories), 1)
        self.assertEqual(book.categories[0].name, "Fiction")
