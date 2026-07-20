"""
Digital Evidence Management System (DEMS)

Module:
    Accounts

File:
    serializers.py

Purpose:
    Serializers for authentication and user management.
"""

from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User
from .services import UserService


class UserSerializer(serializers.ModelSerializer):
    """
    Read-only user profile serializer.
    """

    department = serializers.StringRelatedField()
    role = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "employee_number",
            "badge_number",
            "phone_number",
            "department",
            "role",
            "profile_image",
            "is_active",
            "date_joined",
        )
        read_only_fields = fields


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating personal profile information.
    """

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "profile_image",
        )


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for administrator-created users.
    """

    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={"input_type": "password"},
    )

    confirm_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )

    class Meta:
        model = User

        fields = (
            "username",
            "email",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
            "employee_number",
            "badge_number",
            "phone_number",
            "department",
            "role",
        )

    def validate(self, attrs):

        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "confirm_password":
                    "Passwords do not match."
                }
            )

        return attrs

    def create(self, validated_data):
        return UserService.register(validated_data)


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )

    def validate(self, attrs):

        user = authenticate(
            username=attrs["username"],
            password=attrs["password"],
        )

        if user is None:
            raise serializers.ValidationError(
                "Invalid username or password."
            )

        attrs["user"] = user

        return attrs


class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(
        write_only=True
    )

    new_password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    confirm_password = serializers.CharField(
        write_only=True,
    )

    def validate(self, attrs):

        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "confirm_password":
                    "Passwords do not match."
                }
            )

        return attrs