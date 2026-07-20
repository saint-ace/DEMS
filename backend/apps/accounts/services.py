"""
Digital Evidence Management System (DEMS)

Module:
    Accounts

File:
    services.py

Purpose:
    Business logic for authentication and user management.
"""

from typing import Dict

from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, UserActivity


class AuthenticationService:
    """
    Handles authentication operations.
    """

    @staticmethod
    def generate_tokens(user: User) -> Dict[str, str]:
        """
        Generate JWT access and refresh tokens.
        """
        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    @staticmethod
    def login(username: str, password: str) -> Dict:
        """
        Authenticate a user and return JWT tokens.
        """
        user = authenticate(
            username=username,
            password=password,
        )

        if user is None:
            raise AuthenticationFailed(
                "Invalid username or password."
            )

        if not user.is_active:
            raise AuthenticationFailed(
                "User account is disabled."
            )

        tokens = AuthenticationService.generate_tokens(user)

        from django.contrib.auth.models import update_last_login

        update_last_login(None, user)

        return {
        "user": user,
        "tokens": tokens,
    }


class UserService:
    """
    Handles user-related business logic.
    """

    @staticmethod
    @transaction.atomic
    def register(validated_data: dict) -> User:
        """
        Create a new user.
        """
        password = validated_data.pop("password")
        validated_data.pop("confirm_password", None)

        if User.objects.filter(
            employee_number=validated_data["employee_number"]
        ).exists():
            raise ValidationError(
                {
                    "employee_number": "Employee number already exists."
                }
            )

        user = User.objects.create_user(
            password=password,
            **validated_data,
    )

        UserActivity.objects.create(
            user=user,
            action="Account Created",
        )

        return user

    @staticmethod
    def update_profile(user: User, validated_data: dict) -> User:
        """
        Update user profile information.
        """
        for field, value in validated_data.items():
            setattr(user, field, value)

        user.save()

        UserActivity.objects.create(
            user=user,
            action="Profile Updated",
        )

        return user

    @staticmethod
    def change_password(
        user: User,
        old_password: str,
        new_password: str,
    ) -> None:
        """
        Change the user's password.
        """
        if not user.check_password(old_password):
            raise ValidationError(
                {"old_password": "Incorrect password."}
            )

        user.set_password(new_password)
        user.save()

        UserActivity.objects.create(
            user=user,
            action="Password Changed",
        )

    @staticmethod
    def deactivate(user: User) -> None:
        """
        Soft delete (deactivate) a user.
        """
        user.is_active = False
        user.save(update_fields=["is_active"])

        UserActivity.objects.create(
            user=user,
            action="Account Deactivated",
        )