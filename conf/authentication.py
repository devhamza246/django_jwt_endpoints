import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api.models import CustomUser
from django.conf import settings


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_token = request.headers.get("Authorization")
        if not jwt_token:
            return None

        try:
            # Assuming the JWT token comes as 'Bearer <token>'
            token = jwt_token.split(" ")[1]
            # Replace 'your_secret_key' with the secret key used for signing the JWT in PHP
            payload = jwt.decode(token, settings.JWT_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired. Please log in again.")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token. Please log in again.")
        except IndexError:
            raise AuthenticationFailed("Invalid provided. Please log in again.")

        user_id = payload.get("id")
        if not user_id:
            raise AuthenticationFailed("Invalid token payload. Please log in again.")
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed("No such user.")

        return (user, None)
