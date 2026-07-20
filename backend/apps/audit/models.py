"""
Digital Evidence Management System (DEMS)

Module:
    Audit

File:
    models.py

Purpose:
    Stores all system audit events.
"""

from django.conf import settings
from django.db import models

from apps.common.models import BaseModel


class AuditAction(models.TextChoices):
    CREATE = "CREATE", "Create"
    UPDATE = "UPDATE", "Update"
    DELETE = "DELETE", "Delete"
    VIEW = "VIEW", "View"
    LOGIN = "LOGIN", "Login"
    LOGOUT = "LOGOUT", "Logout"
    DOWNLOAD = "DOWNLOAD", "Download"
    VERIFY = "VERIFY", "Verify"
    ASSIGN = "ASSIGN", "Assign"
    CLOSE = "CLOSE", "Close"
    ARCHIVE = "ARCHIVE", "Archive"


class AuditLog(BaseModel):
    """
    Records every important action performed in the system.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_logs",
    )

    action = models.CharField(
        max_length=30,
        choices=AuditAction.choices,
    )

    module = models.CharField(
        max_length=100,
    )

    object_type = models.CharField(
        max_length=100,
    )

    object_id = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    user_agent = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Audit Log"
        verbose_name_plural = "Audit Logs"

    def __str__(self):
        username = self.user.username if self.user else "System"
        return f"{username} - {self.action}"