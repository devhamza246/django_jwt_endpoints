import jwt
from datetime import datetime, timedelta
from django.conf import settings

SECRET_KEY = settings.SECRET_KEY  # Replace with a secure key from settings


def generate_jwt(user):
    payload = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "exp": datetime.utcnow() + timedelta(hours=1),  # Token expiry time
        "iat": datetime.utcnow(),
    }
    return jwt.encode(payload, settings.JWT_KEY, algorithm="HS256")


def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.JWT_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
