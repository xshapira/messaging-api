from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


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
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(
                {"detail": "Logged in successfully."},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"detail": "Invalid username or password."},
            status=status.HTTP_401_UNAUTHORIZED,
        )
