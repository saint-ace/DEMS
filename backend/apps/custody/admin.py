"""
Digital Evidence Management System (DEMS)

Module:
    Chain of Custody

File:
    admin.py
"""

from django.contrib import admin

from .models import CustodyRecord


@admin.register(CustodyRecord)
class CustodyRecordAdmin(admin.ModelAdmin):

    list_display = (
        "evidence",
        "action",
        "from_user",
        "to_user",
        "location",
        "transferred_at",
    )

    list_filter = (
        "action",
        "transferred_at",
    )

    search_fields = (
        "evidence__evidence_number",
        "location",
        "reason",
    )

    readonly_fields = (
        "transferred_at",
        "created_at",
        "updated_at",
    )

    ordering = (
        "-transferred_at",
    )