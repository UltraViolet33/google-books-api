from easy_http_requests.easy_http_request import EasyHttpRequest
from google_books_api.google_books_api_params import GoogleBooksApiParams
from google_books_api.google_books_api_result import GoogleBooksApiResult


class GoogleBookApi:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.http_request: EasyHttpRequest = EasyHttpRequest(self.base_url)

    def search_book(self, search_params: dict) -> GoogleBooksApiResult:
        response = self.http_request.get(f"volumes", search_params)
        return GoogleBooksApiResult(response.body)

    def search_by_title(self, title: str, max_results: int = 5) -> GoogleBooksApiResult:
        params = {
            "q": GoogleBooksApiParams.IN_TITLE + title,
            GoogleBooksApiParams.MAX_RESULTS: max_results,
        }
        return self.search_book(search_params=params)
