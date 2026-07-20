"""
Digital Evidence Management System (DEMS)

Module:
    Accounts

File:
    views.py

Purpose:
    REST API views for authentication and user management.
"""

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .permissions import (
    IsAdministrator,
    IsAuthenticatedAndActive,
)
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    UserUpdateSerializer,
    ChangePasswordSerializer,
)
from .services import AuthenticationService, UserService


class RegisterView(CreateAPIView):
    """
    Register a new user.
    """

    serializer_class = RegisterSerializer
    permission_classes = [IsAdministrator]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response(
            {
                "success": True,
                "message": "User registered successfully.",
                "data": UserSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    """
    Authenticate a user.
    """

    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = AuthenticationService.login(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        return Response(
            {
                "success": True,
                "message": "Login successful.",
                "data": {
                    "user": UserSerializer(result["user"]).data,
                    "tokens": result["tokens"],
                },
            }
        )


class ProfileView(RetrieveAPIView):
    """
    Return the authenticated user's profile.
    """

    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticatedAndActive,
    ]

    def get_object(self):
        return self.request.user


class UpdateProfileView(UpdateAPIView):

    serializer_class = UserUpdateSerializer

    permission_classes = [
        IsAuthenticatedAndActive,
    ]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            self.get_object(),
            data=request.data,
            partial=True,
        )

        serializer.is_valid(raise_exception=True)

        user = UserService.update_profile(
            request.user,
            serializer.validated_data,
        )

        return Response(
            {
                "success": True,
                "message": "Profile updated successfully.",
                "data": UserSerializer(user).data,
            }
        )   

    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticatedAndActive,
    ]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.get_object(),
            data=request.data,
            partial=True,
        )

        serializer.is_valid(raise_exception=True)

        user = UserService.update_profile(
            self.request.user,
            serializer.validated_data,
        )

        return Response(
            {
                "success": True,
                "message": "Profile updated successfully.",
                "data": UserSerializer(user).data,
            }
        )


class ChangePasswordView(APIView):
    """
    Change the authenticated user's password.
    """

    permission_classes = [
        IsAuthenticatedAndActive,
    ]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        UserService.change_password(
            user=request.user,
            old_password=serializer.validated_data["old_password"],
            new_password=serializer.validated_data["new_password"],
        )

        return Response(
            {
                "success": True,
                "message": "Password changed successfully.",
            }
        )


class UserListView(ListAPIView):
    """
    List all users.
    """

    queryset = User.objects.select_related(
        "department",
        "role",
    )

    serializer_class = UserSerializer

    permission_classes = [
        IsAdministrator,
    ]