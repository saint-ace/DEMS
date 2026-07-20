"""
Digital Evidence Management System (DEMS)

Module:
    Storage

Purpose:
    Secure file storage management.
"""

from django.apps import AppConfig


class StorageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.storage"
    verbose_name = "Storage"

    def ready(self):
        import apps.storage.signals