"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    serializers.py
"""

from rest_framework import serializers

from apps.cases.models import Case
from .models import (
    Evidence,
    EvidenceType,
)


class EvidenceUploadSerializer(serializers.Serializer):
    """
    Serializer for uploading new evidence.
    """

    case = serializers.PrimaryKeyRelatedField(
        queryset=Case.objects.all()
    )

    title = serializers.CharField(
        max_length=255
    )

    description = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    evidence_type = serializers.ChoiceField(
        choices=EvidenceType.choices
    )

    notes = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    file = serializers.FileField()


class EvidenceListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing evidence.
    """

    case_number = serializers.CharField(
        source="case.case_number",
        read_only=True,
    )

    collected_by = serializers.CharField(
        source="collected_by.username",
        read_only=True,
    )

    original_filename = serializers.CharField(
        source="stored_file.original_name",
        read_only=True,
    )

    file_size = serializers.IntegerField(
        source="stored_file.file_size",
        read_only=True,
    )

    verified = serializers.BooleanField(
        source="stored_file.verified",
        read_only=True,
    )

    class Meta:
        model = Evidence

        fields = (
            "id",
            "evidence_number",
            "title",
            "evidence_type",
            "status",
            "case_number",
            "collected_by",
            "original_filename",
            "file_size",
            "verified",
            "created_at",
        )


class EvidenceDetailSerializer(serializers.ModelSerializer):
    """
    Detailed serializer for evidence.
    """

    case_number = serializers.CharField(
        source="case.case_number",
        read_only=True,
    )

    collected_by = serializers.CharField(
        source="collected_by.username",
        read_only=True,
    )

    original_filename = serializers.CharField(
        source="stored_file.original_name",
        read_only=True,
    )

    mime_type = serializers.CharField(
        source="stored_file.mime_type",
        read_only=True,
    )

    extension = serializers.CharField(
        source="stored_file.extension",
        read_only=True,
    )

    file_size = serializers.IntegerField(
        source="stored_file.file_size",
        read_only=True,
    )

    md5_hash = serializers.CharField(
        source="stored_file.md5_hash",
        read_only=True,
    )

    sha1_hash = serializers.CharField(
        source="stored_file.sha1_hash",
        read_only=True,
    )

    sha256_hash = serializers.CharField(
        source="stored_file.sha256_hash",
        read_only=True,
    )

    verified = serializers.BooleanField(
        source="stored_file.verified",
        read_only=True,
    )

    encrypted = serializers.BooleanField(
        source="stored_file.encrypted",
        read_only=True,
    )

    class Meta:
        model = Evidence

        fields = (
            "id",
            "case",
            "case_number",
            "evidence_number",
            "title",
            "description",
            "evidence_type",
            "status",
            "collected_by",
            "collected_at",
            "notes",
            "original_filename",
            "mime_type",
            "extension",
            "file_size",
            "md5_hash",
            "sha1_hash",
            "sha256_hash",
            "verified",
            "encrypted",
            "created_at",
            "updated_at",
        )