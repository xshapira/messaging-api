from rest_framework import authentication


class TokenCookieAuthentication(authentication.TokenAuthentication):
    def authenticate(self, request):
        # Check for token in cookies first
        token = request.COOKIES.get("authToken")

        if token:
            return self.authenticate_credentials(token)

        # Otherwise check normal auth sources
        return super().authenticate(request)
