"""
Admin configuration for the Accounts module.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Department, Role, User, UserActivity


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "employee_number",
        "department",
        "role",
        "is_active",
        "is_staff",
    )

    list_filter = (
        "department",
        "role",
        "is_active",
        "is_staff",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "DEMS Information",
            {
                "fields": (
                    "employee_number",
                    "badge_number",
                    "phone_number",
                    "department",
                    "role",
                    "profile_image",
                )
            },
        ),
    )


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "action",
        "ip_address",
        "created_at",
    )

    list_filter = (
        "action",
        "created_at",
    )

    readonly_fields = (
        "created_at",
    )

    search_fields = (
        "user__username",
        "ip_address",
    )