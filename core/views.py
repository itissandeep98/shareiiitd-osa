import json
from datetime import datetime

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def ResetPasswordView(request):
    """
    Send a reset password request to user email.
    """

    username = json.loads(request.body)['username']
    try:
        user = User.objects.get(username=username)
        token = default_token_generator.make_token(user)
        send_mail(subject="Password Reset Request for OSAIIITD",
                  message="Your token is " + token, recipient_list=[user.username], from_email='')
    except Exception as e:
        return Response(e.__str__())
    return Response()


@api_view(['POST'])
@permission_classes([AllowAny])
def ChangePasswordView(request):
    """
    Set new password for the user.
    """

    post_data = json.loads(request.body)
    username = post_data['username']
    token = post_data['token']
    password = post_data['password']
    try:
        user = User.objects.get(username=username)
        if default_token_generator.check_token(user, token):
            user.set_password(password)
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise Exception("Invalid token!")
    except Exception as e:
        return Response(e.__str__())
    return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditProfileView(request):
    """
    Edit user profile first_name, last_name, email
    """

    post_data = json.loads(request.body)
    username = post_data['username']
    first_name = post_data['first_name']
    last_name = post_data['last_name']
    try:
        request.user.username = username
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.save()
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.__str__())
    return Response()


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(
            data={"username_osa": request.data['username'] +
                  "-" + str(datetime.now().date()), **request.data}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
