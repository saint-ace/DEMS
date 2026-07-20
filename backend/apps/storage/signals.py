"""
Digital Evidence Management System (DEMS)

Module:
    Storage

File:
    signals.py
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import StorageFile


@receiver(post_save, sender=StorageFile)
def storage_file_created(sender, instance, created, **kwargs):
    """
    Placeholder for future storage events.
    """

    if created:
        pass