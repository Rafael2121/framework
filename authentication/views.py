from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@api_view(['POST'])
def create_auth(request):

    username = request.data["username"]
    password = request.data["pass"]

    user = User.objects.get_or_create(username=username, password=password)

    token = Token.objects.get_or_create(user=user[0])

    response = {
        "token": token[0].key 
    }

    return Response(response, status=status.HTTP_201_CREATED
                    if user[1] else status.HTTP_200_OK)
