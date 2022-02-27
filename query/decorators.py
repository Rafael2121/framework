from rest_framework.response import Response
from rest_framework import status


def exception_handling(func):

    def wrapper(*args, **kwargs):

        try:

            return func(*args, **kwargs)

        except Exception as e:
            data = {
                "error": {
                    "reason": str(e)
                }
            }

            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return wrapper
