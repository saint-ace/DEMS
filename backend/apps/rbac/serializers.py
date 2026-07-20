"""
Digital Evidence Management System (DEMS)

Module:
    RBAC

File:
    serializers.py
"""

from rest_framework import serializers

from .models import (
    Permission,
    Role,
    UserRole,
)


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = "__all__"


class UserRoleSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True,
    )

    role_name = serializers.CharField(
        source="role.name",
        read_only=True,
    )

    class Meta:
        model = UserRole

        fields = (
            "id",
            "username",
            "role_name",
            "created_at",
        )