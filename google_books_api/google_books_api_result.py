from google_books_api.google_book import GoogleBook


class GoogleBooksApiResult:
    def __init__(self, result: dict):
        self.parse_result(result)

    def parse_result(self, result: dict):
        self.total_items: int = result.get("totalItems", 0)
        self.items: list = result.get("items", [])
        self.books: list[GoogleBook] = [GoogleBook(item) for item in self.items]
