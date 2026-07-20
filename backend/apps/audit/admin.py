"""
Digital Evidence Management System (DEMS)

Module:
    Audit

File:
    admin.py

Purpose:
    Django admin configuration for Audit Logs.
"""

from django.contrib import admin

from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        "created_at",
        "user",
        "module",
        "action",
        "object_type",
        "object_id",
    )

    list_filter = (
        "action",
        "module",
        "created_at",
    )

    search_fields = (
        "description",
        "object_id",
        "object_type",
        "user__username",
        "user__email",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    date_hierarchy = "created_at"

    list_per_page = 25