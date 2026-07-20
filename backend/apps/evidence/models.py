"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    models.py
"""

import uuid

from django.conf import settings
from django.db import models

from apps.cases.models import Case
from apps.common.models import BaseModel


class EvidenceStatus(models.TextChoices):
    COLLECTED = "COLLECTED", "Collected"
    IN_ANALYSIS = "IN_ANALYSIS", "In Analysis"
    ANALYZED = "ANALYZED", "Analyzed"
    PRESENTED = "PRESENTED", "Presented"
    ARCHIVED = "ARCHIVED", "Archived"
    DISPOSED = "DISPOSED", "Disposed"


class EvidenceType(models.TextChoices):
    DISK_IMAGE = "DISK_IMAGE", "Disk Image"
    MEMORY_DUMP = "MEMORY_DUMP", "Memory Dump"
    DOCUMENT = "DOCUMENT", "Document"
    IMAGE = "IMAGE", "Image"
    VIDEO = "VIDEO", "Video"
    AUDIO = "AUDIO", "Audio"
    NETWORK_CAPTURE = "NETWORK_CAPTURE", "Network Capture"
    MOBILE_EXTRACTION = "MOBILE_EXTRACTION", "Mobile Extraction"
    OTHER = "OTHER", "Other"


class Evidence(BaseModel):
    """
    Represents a digital evidence item.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        related_name="evidence_items",
    )

    evidence_number = models.CharField(
        max_length=50,
        unique=True,
    )

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
    )

    evidence_type = models.CharField(
        max_length=30,
        choices=EvidenceType.choices,
    )

    status = models.CharField(
        max_length=30,
        choices=EvidenceStatus.choices,
        default=EvidenceStatus.COLLECTED,
    )

    stored_file = models.OneToOneField(
        "storage.StorageFile",
    on_delete=models.PROTECT,
    related_name="evidence",
)

    collected_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="collected_evidence",
    )

    collected_at = models.DateTimeField()

    notes = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Evidence"
        verbose_name_plural = "Evidence"

    def __str__(self):
        return f"{self.evidence_number} - {self.title}"