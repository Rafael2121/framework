

import re
from query.services import JsonPlaceholderService
from .services import JsonPlaceholderService
from .facades import QueryFacade


class QueryRepository:
    
    def __init__(self) -> None:
        self.service = JsonPlaceholderService()

    def fetch(self):
        result = self.service.fetch_all()

        if not len(result) > 5:
            raise Exception("Response has less than five results")

        return [QueryFacade(r).parse() for r in result[:5]]
