"""
Digital Evidence Management System (DEMS)

Module:
    Cases

File:
    admin.py

Purpose:
    Django admin configuration for Case Management.
"""

from django.contrib import admin

from .models import (
    Case,
    CaseAssignment,
    CaseAttachment,
    CaseNote,
    CasePriority,
    CaseStatus,
    CaseType,
)


# ---------------------------------------------------------
# Inline Models
# ---------------------------------------------------------

class CaseAssignmentInline(admin.TabularInline):
    model = CaseAssignment
    extra = 0
    autocomplete_fields = ("user", "assigned_by")


class CaseNoteInline(admin.TabularInline):
    model = CaseNote
    extra = 0
    autocomplete_fields = ("author",)


class CaseAttachmentInline(admin.TabularInline):
    model = CaseAttachment
    extra = 0
    autocomplete_fields = ("uploaded_by",)


# ---------------------------------------------------------
# Lookup Tables
# ---------------------------------------------------------

@admin.register(CaseType)
class CaseTypeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )


@admin.register(CaseStatus)
class CaseStatusAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )

@admin.register(CasePriority)
class CasePriorityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )

# ---------------------------------------------------------
# Case
# ---------------------------------------------------------

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):

    list_display = (
        "case_number",
        "title",
        "case_type",
        "status",
        "priority",
        "lead_investigator",
        "department",
        "date_opened",
    )

    list_filter = (
        "status",
        "priority",
        "case_type",
        "department",
        "date_opened",
    )

    search_fields = (
        "case_number",
        "title",
        "description",
        "court_reference",
    )

    autocomplete_fields = (
        "lead_investigator",
        "created_by",
        "department",
        "case_type",
        "status",
        "priority",
    )

    readonly_fields = (
        "case_number",
        "created_at",
        "updated_at",
    )

    date_hierarchy = "date_opened"

    ordering = (
        "-created_at",
    )

    inlines = [
        CaseAssignmentInline,
        CaseNoteInline,
        CaseAttachmentInline,
    ]

    actions = (
        "archive_cases",
        "close_cases",
    )

    @admin.action(description="Archive selected cases")
    def archive_cases(self, request, queryset):
        archived = CaseStatus.objects.filter(
            name__iexact="Archived"
        ).first()

        if archived:
            queryset.update(status=archived)

    @admin.action(description="Close selected cases")
    def close_cases(self, request, queryset):
        closed = CaseStatus.objects.filter(
            name__iexact="Closed"
        ).first()

        if closed:
            queryset.update(status=closed)


# ---------------------------------------------------------
# Case Assignment
# ---------------------------------------------------------

@admin.register(CaseAssignment)
class CaseAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        "case",
        "user",
        "assigned_by",
        "assigned_at",
        "active",
    )

    list_filter = (
        "active",
    )

    autocomplete_fields = (
        "case",
        "user",
        "assigned_by",
    )


# ---------------------------------------------------------
# Case Notes
# ---------------------------------------------------------

@admin.register(CaseNote)
class CaseNoteAdmin(admin.ModelAdmin):

    list_display = (
        "case",
        "author",
        "created_at",
    )

    autocomplete_fields = (
        "case",
        "author",
    )


# ---------------------------------------------------------
# Case Attachments
# ---------------------------------------------------------

@admin.register(CaseAttachment)
class CaseAttachmentAdmin(admin.ModelAdmin):

    list_display = (
        "case",
        "uploaded_by",
        "created_at",
    )

    autocomplete_fields = (
        "case",
        "uploaded_by",
    )