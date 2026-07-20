"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

Purpose:
    Digital Evidence Management.
"""

from django.apps import AppConfig


class EvidenceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.evidence"
    verbose_name = "Evidence Management"

    def ready(self):
        import apps.evidence.signals