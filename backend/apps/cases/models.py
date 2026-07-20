"""
Digital Evidence Management System (DEMS)

Module:
    Cases

File:
    models.py

Purpose:
    Database models for case management.
"""

from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.common.models import BaseModel
from apps.common.utils import generate_reference

class CaseType(BaseModel):
    """
    Configurable investigation categories.
    """

    code = models.CharField(
        max_length=30,
        unique=True,
    )

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Case Type"
        verbose_name_plural = "Case Types"

    def __str__(self):
        return self.name

class CaseStatus(BaseModel):
    """
    Configurable workflow status.
    """

    code = models.CharField(
        max_length=30,
        unique=True,
    )

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    color = models.CharField(
        max_length=20,
        default="#0d6efd",
    )

    order = models.PositiveIntegerField(
        default=1,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Case Status"
        verbose_name_plural = "Case Statuses"

    def __str__(self):
        return self.name

class CasePriority(BaseModel):
    """
    Configurable priority levels.
    """

    code = models.CharField(
        max_length=20,
        unique=True,
    )

    name = models.CharField(
        max_length=50,
        unique=True,
    )

    color = models.CharField(
        max_length=20,
        default="#198754",
    )

    order = models.PositiveIntegerField(
        default=1,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Case Priority"
        verbose_name_plural = "Case Priorities"

    def __str__(self):
        return self.name

class Case(BaseModel):
    """
    Represents an investigation case within the Digital Evidence
    Management System.
    """

    case_number = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        help_text="Automatically generated unique case number.",
    )

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField()

    case_type = models.ForeignKey(
        CaseType,
        on_delete=models.PROTECT,
        related_name="cases",
    )

    status = models.ForeignKey(
        CaseStatus,
        on_delete=models.PROTECT,
        related_name="cases",
    )

    priority = models.ForeignKey(
        CasePriority,
        on_delete=models.PROTECT,
        related_name="cases",
    )

    lead_investigator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="lead_cases",
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_cases",
    )

    department = models.ForeignKey(
        "accounts.Department",
        on_delete=models.PROTECT,
        related_name="cases",
    )

    court_reference = models.CharField(
        max_length=150,
        blank=True,
    )

    incident_location = models.CharField(
        max_length=255,
        blank=True,
    )

    incident_date = models.DateField(
        null=True,
        blank=True,
    )

    date_opened = models.DateField()

    date_closed = models.DateField(
        null=True,
        blank=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Case"
        verbose_name_plural = "Cases"

    def __str__(self):
        return f"{self.case_number} - {self.title}"

    def save(self, *args, **kwargs):
        """
        Automatically generate a unique case number when creating
        a new case.
        """
        if not self.case_number:
            year = timezone.now().year

            last_case = (
                Case.objects.filter(
                    case_number__startswith=f"CASE-{year}"
                )
                .order_by("-case_number")
                .first()
            )

            if last_case:
                try:
                    last_number = int(
                        last_case.case_number.split("-")[-1]
                    )
                except (ValueError, IndexError):
                    last_number = 0
            else:
                last_number = 0

            self.case_number = generate_reference(
                "CASE",
                last_number + 1,
            )

        super().save(*args, **kwargs)
class CaseAssignment(BaseModel):
    """
    Assignment of users to investigations.
    """

    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        related_name="assignments",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="case_assignments_created",
    )

    assigned_at = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("case", "user")

    def __str__(self):
        return f"{self.case.case_number} - {self.user.username}"


class CaseNote(BaseModel):
    """
    Investigation notes.
    """

    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        related_name="notes",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    note = models.TextField()

    def __str__(self):
        return f"{self.case.case_number} Note"


class CaseAttachment(BaseModel):
    """
    Files attached to a case.
    """

    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        related_name="attachments",
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    file = models.FileField(
        upload_to="cases/",
    )

    description = models.CharField(
        max_length=255,
        blank=True,
    )

    def __str__(self):
        return self.file.name