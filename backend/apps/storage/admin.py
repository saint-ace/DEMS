"""
Digital Evidence Management System (DEMS)

Module:
    Storage

File:
    admin.py
"""

from django.contrib import admin

from .models import StorageFile


@admin.register(StorageFile)
class StorageFileAdmin(admin.ModelAdmin):

    list_display = (
        "original_name",
        "uploaded_by",
        "file_size",
        "verified",
        "created_at",
    )

    list_filter = (
        "verified",
        "encrypted",
        "created_at",
    )

    search_fields = (
        "original_name",
        "sha256_hash",
        "md5_hash",
    )

    readonly_fields = (
        "md5_hash",
        "sha1_hash",
        "sha256_hash",
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )