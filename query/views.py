from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .repository import QueryRepository
from .decorators import exception_handling
from log.decorators import enable_logging


class QueryListingView(APIView):

    @enable_logging
    @exception_handling
    def get(self, request, format=None):
        repository = QueryRepository()

        fetch_data = repository.fetch()

        return Response(fetch_data, status=status.HTTP_200_OK)
