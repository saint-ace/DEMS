"""
Digital Evidence Management System (DEMS)

Module:
    RBAC

File:
    permissions.py
"""

from rest_framework.permissions import BasePermission

from .services import RBACService


class HasPermission(BasePermission):
    """
    Generic permission checker.
    """

    required_permission = None

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if self.required_permission is None:
            return False

        return RBACService.user_has_permission(
            request.user,
            self.required_permission,
        )