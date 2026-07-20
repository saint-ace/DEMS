"""
Digital Evidence Management System (DEMS)

Module:
    Cases

File:
    serializers.py

Purpose:
    Serializers for Case Management.
"""

from rest_framework import serializers

from .models import (
    Case,
    CaseAssignment,
    CaseAttachment,
    CaseNote,
    CasePriority,
    CaseStatus,
    CaseType,
)


# =========================================================
# Lookup Serializers
# =========================================================

class CaseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseType
        fields = (
            "id",
            "code",
            "name",
            "description",
            "is_active",
        )
        read_only_fields = ("id",)


class CaseStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = CaseStatus
        fields = (
            "id",
            "code",
            "name",
            "color",
            "order",
            "is_active",
        )
        read_only_fields = ("id",)


class CasePrioritySerializer(serializers.ModelSerializer):

    class Meta:
        model = CasePriority
        fields = (
            "id",
            "code",
            "name",
            "color",
            "order",
            "is_active",
        )
        read_only_fields = ("id",)


# =========================================================
# Assignment
# =========================================================

class CaseAssignmentSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(
        source="user.get_full_name",
        read_only=True,
    )

    assigned_by_name = serializers.CharField(
        source="assigned_by.get_full_name",
        read_only=True,
    )

    class Meta:
        model = CaseAssignment
        fields = (
            "id",
            "user",
            "user_name",
            "assigned_by",
            "assigned_by_name",
            "assigned_at",
            "active",
        )

        read_only_fields = (
            "id",
            "assigned_at",
        )


# =========================================================
# Notes
# =========================================================

class CaseNoteSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(
        source="author.get_full_name",
        read_only=True,
    )

    class Meta:
        model = CaseNote

        fields = (
            "id",
            "author",
            "author_name",
            "note",
            "created_at",
        )

        read_only_fields = (
            "id",
            "created_at",
        )


# =========================================================
# Attachments
# =========================================================

class CaseAttachmentSerializer(serializers.ModelSerializer):

    uploaded_by_name = serializers.CharField(
        source="uploaded_by.get_full_name",
        read_only=True,
    )

    class Meta:
        model = CaseAttachment

        fields = (
            "id",
            "file",
            "description",
            "uploaded_by",
            "uploaded_by_name",
            "created_at",
        )

        read_only_fields = (
            "id",
            "created_at",
        )


# =========================================================
# Case List
# =========================================================

class CaseListSerializer(serializers.ModelSerializer):

    case_type = serializers.StringRelatedField()

    status = serializers.StringRelatedField()

    priority = serializers.StringRelatedField()

    lead_investigator = serializers.StringRelatedField()

    class Meta:

        model = Case

        fields = (
            "id",
            "case_number",
            "title",
            "case_type",
            "status",
            "priority",
            "lead_investigator",
            "date_opened",
        )


# =========================================================
# Case Details
# =========================================================

class CaseDetailSerializer(serializers.ModelSerializer):

    case_type = CaseTypeSerializer(read_only=True)

    status = CaseStatusSerializer(read_only=True)

    priority = CasePrioritySerializer(read_only=True)

    assignments = CaseAssignmentSerializer(
        many=True,
        read_only=True,
    )

    notes = CaseNoteSerializer(
        many=True,
        read_only=True,
    )

    attachments = CaseAttachmentSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = Case

        fields = "__all__"


# =========================================================
# Create
# =========================================================

class CaseCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Case

        exclude = (
            "case_number",
            "created_at",
            "updated_at",
        )


# =========================================================
# Update
# =========================================================

class CaseUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Case

        exclude = (
            "case_number",
            "created_at",
            "updated_at",
            "created_by",
        )