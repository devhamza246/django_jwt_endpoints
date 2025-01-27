from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from conf.utils import generate_jwt
from rest_framework.permissions import IsAuthenticated
from conf.authentication import JWTAuthentication
from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):

    @swagger_auto_schema(
        request_body=UserSerializer,
        operation_description="Save quotes from the provided API URL.",
    )
    @action(detail=False, methods=["post"])
    def signup(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User created successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=UserSerializer,
        operation_description="Save quotes from the provided API URL.",
    )
    @action(detail=False, methods=["post"])
    def login(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = CustomUser.objects.filter(email=email).first()
        if user and user.check_password(password):
            token = generate_jwt(user)
            return Response({"token": token}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Invalid email or password."}, status=status.HTTP_400_BAD_REQUEST
        )


class PublicEndpointView(viewsets.ViewSet):

    def list(self, request):
        return Response(
            {"message": "Hello, this is the public endpoint."},
            status=status.HTTP_200_OK,
        )


class ProtectedEndpointView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        return Response(
            {"id": user.id, "username": user.username, "email": user.email},
            status=status.HTTP_200_OK,
        )
