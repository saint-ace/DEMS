"""
Digital Evidence Management System (DEMS)

Module:
    Common

File:
    models.py

Purpose:
    Shared abstract models used throughout the project.
"""

import uuid

from django.db import models
from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides created and updated timestamps.
    """

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """
    Abstract base model that provides a UUID primary key.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class BaseModel(UUIDModel, TimeStampedModel):
    """
    Base model used by all project models.
    """

    class Meta:
        abstract = True

class Sequence(models.Model):
    """
    Stores sequential numbers for different entities.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
    )

    year = models.PositiveIntegerField(
        default=timezone.now().year,
    )

    current_value = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        unique_together = ("name", "year")
        verbose_name = "Sequence"
        verbose_name_plural = "Sequences"

    def __str__(self):
        return f"{self.name} ({self.year})"