


class QueryFacade:

    def __init__(self, json_data) -> None:
        self.json_data = json_data

    def parse(self):
        return dict(id=self.json_data["id"],
                    title=self.json_data["title"])
