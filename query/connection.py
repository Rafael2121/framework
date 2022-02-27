import requests
from decouple import config


class JsonPlaceholderConnection:

    def __init__(self) -> None:
        self.base_url = config("JSON_PLACEHOLDER_URL")

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"

        response = requests.get(url=url)

        return response.json() 
