import json


class QueryFacade:

    expected_fields = ["id", "title"]

    def __init__(self, json_data) -> None:
        self.json_data = json_data

    def parse(self):

        for field in self.expected_fields:
            if field not in self.json_data:
                raise Exception(f"Field '{field}' not found in '{json.dumps(self.json_data)}'")

        return dict(id=self.json_data["id"],
                    title=self.json_data["title"])
