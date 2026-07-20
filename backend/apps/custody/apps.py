"""
Digital Evidence Management System (DEMS)

Module:
    Chain of Custody

Purpose:
    Chain of Custody Management.
"""

from django.apps import AppConfig


class CustodyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.custody"
    verbose_name = "Chain of Custody"

    def ready(self):
        import apps.custody.signals