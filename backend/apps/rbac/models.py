"""
Digital Evidence Management System (DEMS)

Module:
    RBAC

File:
    models.py
"""

from django.conf import settings
from django.db import models

from apps.common.models import BaseModel


class Role(BaseModel):
    """
    User role.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name


class Permission(BaseModel):
    """
    System permission.
    """

    code = models.CharField(
        max_length=100,
        unique=True,
    )

    name = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name


class RolePermission(BaseModel):
    """
    Maps permissions to roles.
    """

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="permissions",
    )

    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (
            "role",
            "permission",
        )


class UserRole(BaseModel):
    """
    Assigns roles to users.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assigned_roles",
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (
            "user",
            "role",
        )