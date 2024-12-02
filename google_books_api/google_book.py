class GoogleBook:
    def __init__(self, item: dict):
        self.title = item.get("volumeInfo", {}).get("title", "")
        self.google_id = item.get("id", "")
