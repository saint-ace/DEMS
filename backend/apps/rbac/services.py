"""
Digital Evidence Management System (DEMS)

Module:
    RBAC

File:
    services.py

Purpose:
    Business logic for Role-Based Access Control (RBAC).
"""

from django.db import transaction

from apps.common.services import BaseService

from .models import (
    Permission,
    Role,
    RolePermission,
    UserRole,
)
from .seed import DEFAULT_PERMISSIONS


class RBACService(BaseService):
    """
    Business logic for managing roles, permissions,
    and user-role assignments.
    """

    # --------------------------------------------------
    # Role Management
    # --------------------------------------------------

    @staticmethod
    @transaction.atomic
    def create_role(name, description=""):
        """
        Create a role if it does not already exist.
        """

        role, _ = Role.objects.get_or_create(
            name=name,
            defaults={
                "description": description,
            },
        )

        return role

    @staticmethod
    def get_roles():
        """
        Return all roles.
        """

        return Role.objects.all().order_by("name")

    # --------------------------------------------------
    # Permission Management
    # --------------------------------------------------

    @staticmethod
    @transaction.atomic
    def create_permission(code, name, description=""):
        """
        Create a permission if it does not already exist.
        """

        permission, _ = Permission.objects.get_or_create(
            code=code,
            defaults={
                "name": name,
                "description": description,
            },
        )

        return permission

    @staticmethod
    def get_permissions():
        """
        Return all permissions.
        """

        return Permission.objects.all().order_by("code")

    @staticmethod
    @transaction.atomic
    def initialize_permissions():
        """
        Create all default system permissions.
        Safe to run multiple times.
        """

        for code, name in DEFAULT_PERMISSIONS:

            Permission.objects.get_or_create(
                code=code,
                defaults={
                    "name": name,
                },
            )

    @staticmethod
    @transaction.atomic
    def initialize_roles():
        """
        Create the default system roles.
        Safe to run multiple times.
        """

        from .seed import DEFAULT_ROLES

        for name, description in DEFAULT_ROLES:

            Role.objects.get_or_create(
                name=name,
                defaults={
                    "description": description,
                },
            )

    @staticmethod
    @transaction.atomic
    def initialize_role_permissions():
        """
        Assign default permissions to roles.
        Safe to run multiple times.
        """

        from .seed import DEFAULT_ROLE_PERMISSIONS

        for role_name, permission_codes in DEFAULT_ROLE_PERMISSIONS.items():

            role = Role.objects.filter(
                name=role_name
            ).first()

            if role is None:
                continue

            if "*" in permission_codes:

                permissions = Permission.objects.all()

            else:

                permissions = Permission.objects.filter(
                    code__in=permission_codes
                )

            for permission in permissions:

                RolePermission.objects.get_or_create(
                    role=role,
                    permission=permission,
                )
    # --------------------------------------------------
    # Role ↔ Permission
    # --------------------------------------------------

    @staticmethod
    @transaction.atomic
    def assign_permission(role, permission):
        """
        Assign a permission to a role.
        """

        assignment, _ = RolePermission.objects.get_or_create(
            role=role,
            permission=permission,
        )

        return assignment

    @staticmethod
    @transaction.atomic
    def remove_permission(role, permission):
        """
        Remove a permission from a role.
        """

        RolePermission.objects.filter(
            role=role,
            permission=permission,
        ).delete()

    # --------------------------------------------------
    # User ↔ Role
    # --------------------------------------------------

    @staticmethod
    @transaction.atomic
    def assign_role(user, role):
        """
        Assign a role to a user.
        """

        assignment, _ = UserRole.objects.get_or_create(
            user=user,
            role=role,
        )

        return assignment

    @staticmethod
    @transaction.atomic
    def remove_role(user, role):
        """
        Remove a role from a user.
        """

        UserRole.objects.filter(
            user=user,
            role=role,
        ).delete()

    @staticmethod
    def get_user_roles(user):
        """
        Return all roles assigned to a user.
        """

        return Role.objects.filter(
            userrole__user=user
        ).distinct()

    # --------------------------------------------------
    # Permission Checking
    # --------------------------------------------------

    @staticmethod
    def get_user_permissions(user):
        """
        Return all permissions assigned to a user.
        """

        if user.is_superuser:
            return Permission.objects.all()

        return Permission.objects.filter(
            rolepermission__role__userrole__user=user
        ).distinct()

    @staticmethod
    def user_has_permission(user, permission_code):
        """
        Check whether a user has a specific permission.
        """

        if not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        return Permission.objects.filter(
            code=permission_code,
            rolepermission__role__userrole__user=user,
        ).exists()

    # --------------------------------------------------
    # Utility Methods
    # --------------------------------------------------

    @staticmethod
    def user_has_role(user, role_name):
        """
        Check whether a user has a specific role.
        """

        if user.is_superuser:
            return True

        return Role.objects.filter(
            name=role_name,
            userrole__user=user,
        ).exists()