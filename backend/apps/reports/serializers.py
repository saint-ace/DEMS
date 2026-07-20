"""
Digital Evidence Management System (DEMS)

Module:
    Reports

File:
    serializers.py
"""

from rest_framework import serializers

from .models import Report, ReportType


class ReportListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing reports.
    """

    generated_by = serializers.CharField(
        source="generated_by.username",
        read_only=True,
    )

    class Meta:
        model = Report

        fields = (
            "id",
            "report_number",
            "title",
            "report_type",
            "status",
            "generated_by",
            "generated_at",
        )


class ReportDetailSerializer(serializers.ModelSerializer):
    """
    Detailed report serializer.
    """

    generated_by = serializers.CharField(
        source="generated_by.username",
        read_only=True,
    )

    file_name = serializers.CharField(
        source="stored_file.original_name",
        read_only=True,
    )

    file_size = serializers.IntegerField(
        source="stored_file.file_size",
        read_only=True,
    )

    sha256_hash = serializers.CharField(
        source="stored_file.sha256_hash",
        read_only=True,
    )

    class Meta:
        model = Report

        fields = (
            "id",
            "report_number",
            "title",
            "report_type",
            "status",
            "generated_by",
            "generated_at",
            "notes",
            "file_name",
            "file_size",
            "sha256_hash",
        )


class ReportGenerateSerializer(serializers.Serializer):
    """
    Serializer used when generating reports.
    """

    report_type = serializers.ChoiceField(
        choices=ReportType.choices
    )

    object_id = serializers.UUIDField()

    title = serializers.CharField(
        max_length=255,
    )

    notes = serializers.CharField(
        required=False,
        allow_blank=True,
    )