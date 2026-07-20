"""
Digital Evidence Management System (DEMS)

Module:
    Reports

File:
    models.py
"""

import uuid

from django.conf import settings
from django.db import models

from apps.common.models import BaseModel
from apps.storage.models import StorageFile


class ReportType(models.TextChoices):
    CASE = "CASE", "Case Report"
    EVIDENCE = "EVIDENCE", "Evidence Report"
    CUSTODY = "CUSTODY", "Chain of Custody Report"
    AUDIT = "AUDIT", "Audit Report"


class ReportStatus(models.TextChoices):
    GENERATING = "GENERATING", "Generating"
    COMPLETED = "COMPLETED", "Completed"
    FAILED = "FAILED", "Failed"


class Report(BaseModel):
    """
    Stores generated reports.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    report_number = models.CharField(
        max_length=50,
        unique=True,
    )

    title = models.CharField(
        max_length=255,
    )

    report_type = models.CharField(
        max_length=20,
        choices=ReportType.choices,
    )

    object_id = models.UUIDField(
    help_text="ID of the object this report was generated for.",
    )
    status = models.CharField(
        max_length=20,
        choices=ReportStatus.choices,
        default=ReportStatus.GENERATING,
    )

    generated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="generated_reports",
    )

    stored_file = models.ForeignKey(
        StorageFile,
        on_delete=models.PROTECT,
        related_name="reports",
        null=True,
        blank=True,
    )

    generated_at = models.DateTimeField(
        auto_now_add=True,
    )

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["-generated_at"]
        verbose_name = "Report"
        verbose_name_plural = "Reports"

    def __str__(self):
        return self.report_number