class GoogleBook:
    def __init__(self, item: dict):
        self.title = item.get("volumeInfo", {}).get("title", "")
        self.google_id = item.get("id", "")
        self.description = item.get("volumeInfo", {}).get("description", "")
        self.published_date = item.get("volumeInfo", {}).get("publishedDate", "")