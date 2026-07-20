"""
Digital Evidence Management System (DEMS)

Module:
    Chain of Custody

File:
    models.py
"""

from django.conf import settings
from django.db import models

from apps.common.models import BaseModel
from apps.evidence.models import Evidence


class CustodyAction(models.TextChoices):
    COLLECTED = "COLLECTED", "Collected"
    TRANSFERRED = "TRANSFERRED", "Transferred"
    RECEIVED = "RECEIVED", "Received"
    ANALYZED = "ANALYZED", "Analyzed"
    RETURNED = "RETURNED", "Returned"
    ARCHIVED = "ARCHIVED", "Archived"


class CustodyRecord(BaseModel):
    """
    Immutable custody history for evidence.
    """

    evidence = models.ForeignKey(
        Evidence,
        on_delete=models.CASCADE,
        related_name="custody_records",
    )

    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="custody_transfers_sent",
        null=True,
        blank=True,
    )

    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="custody_transfers_received",
    )

    action = models.CharField(
        max_length=30,
        choices=CustodyAction.choices,
    )

    location = models.CharField(
        max_length=255,
    )

    reason = models.TextField()

    transferred_at = models.DateTimeField(
        auto_now_add=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = [
            "-transferred_at",
        ]

        verbose_name = "Custody Record"

        verbose_name_plural = "Custody Records"

    def __str__(self):
        return (
            f"{self.evidence.evidence_number} "
            f"-> {self.to_user.username}"
        )