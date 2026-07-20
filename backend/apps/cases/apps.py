"""
Digital Evidence Management System (DEMS)

Module:
    Cases

File:
    apps.py
"""

from django.apps import AppConfig


class CasesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.cases"
    verbose_name = "Case Management"

    def ready(self):
        import apps.cases.signals