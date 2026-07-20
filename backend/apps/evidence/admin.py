"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    admin.py
"""

from django.contrib import admin

from .models import Evidence


@admin.register(Evidence)
class EvidenceAdmin(admin.ModelAdmin):

    list_display = (
        "evidence_number",
        "title",
        "case",
        "evidence_type",
        "status",
        "collected_by",
        "created_at",
    )

    search_fields = (
        "evidence_number",
        "title",
        "stored_file__original_name",
        "stored_file__sha256_hash",
    )

    list_filter = (
        "status",
        "evidence_type",
        "created_at",
    )

    readonly_fields = (
        "get_original_filename",
        "get_file_size",
        "get_mime_type",
        "get_sha256_hash",
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    @admin.display(description="Original Filename")
    def get_original_filename(self, obj):
        return (
            obj.stored_file.original_name
            if obj.stored_file
            else "-"
        )

    @admin.display(description="File Size")
    def get_file_size(self, obj):
        return (
            obj.stored_file.file_size
            if obj.stored_file
            else "-"
        )

    @admin.display(description="MIME Type")
    def get_mime_type(self, obj):
        return (
            obj.stored_file.mime_type
            if obj.stored_file
            else "-"
        )

    @admin.display(description="SHA-256")
    def get_sha256_hash(self, obj):
        return (
            obj.stored_file.sha256_hash
            if obj.stored_file
            else "-"
        )