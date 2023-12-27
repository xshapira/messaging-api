from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer, UserSignupSerializer


class SignupView(APIView):
    """
    Register a new user account.

    Handle POST requests by validating user data, creating a new user,
    and returning a token upon successful registration.

    Returns 201 response with token on success.
    Returns 400 response with errors on failure.
    """

    # allow open access for creating new accounts
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "User created successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Authenticate and login a user.

    Handle POST request to log a user in by validating the
    provided credentials and returning a proper response.

    On successful login, a 200 response is returned indicating success.
    Otherwise, a 401 response is returned for invalid credentials.
    """

    def post(self, request: Request) -> Response:
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user)
            response = Response({"user": serializer.data})
            response.set_cookie(
                key="authToken",
                value=token.key,
            )
            return response

        return Response(
            {"detail": "Invalid username or password."},
            status=status.HTTP_401_UNAUTHORIZED,
        )
