"""
Digital Evidence Management System (DEMS)

Module:
    Storage

File:
    models.py
"""

import uuid

from django.conf import settings
from django.db import models

from apps.common.models import BaseModel


class StorageFile(BaseModel):
    """
    Stores metadata for uploaded files.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    file = models.FileField(
        upload_to="evidence/",
    )

    original_name = models.CharField(
        max_length=255,
    )

    stored_name = models.CharField(
        max_length=255,
        unique=True,
    )

    mime_type = models.CharField(
        max_length=100,
    )

    extension = models.CharField(
        max_length=20,
    )

    file_size = models.BigIntegerField()

    md5_hash = models.CharField(
        max_length=32,
        db_index=True,
    )

    sha1_hash = models.CharField(
        max_length=40,
        db_index=True,
    )

    sha256_hash = models.CharField(
        max_length=64,
        db_index=True,
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="uploaded_files",
    )

    encrypted = models.BooleanField(
        default=False,
    )

    verified = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = [
            "-created_at",
        ]

        verbose_name = "Stored File"

        verbose_name_plural = "Stored Files"

    def __str__(self):
        return self.original_name