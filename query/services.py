from .connection import JsonPlaceholderConnection


class JsonPlaceholderService:

    def __init__(self) -> None:
        self.conn = JsonPlaceholderConnection()

    def fetch_all(self):
        endpoint = "todos"

        return self.conn.get(endpoint=endpoint)
