"""
Digital Evidence Management System (DEMS)

Module:
    RBAC

File:
    apps.py
"""

from django.apps import AppConfig


class RBACConfig(AppConfig):

    default_auto_field = "django.db.models.BigAutoField"

    name = "apps.rbac"

    verbose_name = "Role-Based Access Control"

    def ready(self):

        import apps.rbac.signals