"""
Digital Evidence Management System (DEMS)

Module:
    RBAC

File:
    admin.py
"""

from django.contrib import admin

from .models import (
    Permission,
    Role,
    RolePermission,
    UserRole,
)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
    )

    search_fields = (
        "name",
    )


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
    )

    search_fields = (
        "code",
        "name",
    )


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):

    list_display = (
        "role",
        "permission",
    )


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "role",
    )

    search_fields = (
        "user__username",
        "role__name",
    )