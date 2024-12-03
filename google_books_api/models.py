class GoogleBook:
    def __init__(self, item: dict):
        self.title = item.get("volumeInfo", {}).get("title", "")
        self.google_id = item.get("id", "")
        self.description = item.get("volumeInfo", {}).get("description", "")
        self.published_date = item.get("volumeInfo", {}).get("publishedDate", "")
        self.authors = self.parse_authors(item)

    def parse_authors(self, item: dict):
        authors = item.get("volumeInfo", {}).get("authors", [])
        return [Author(author) for author in authors]


class Author:
    def __init__(self, name):
        self.name = name
