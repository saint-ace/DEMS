"""
Digital Evidence Management System (DEMS)

Module:
    Cases

File:
    signals.py

Purpose:
    Signal handlers for the Cases module.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Case


@receiver(post_save, sender=Case)
def case_created(sender, instance, created, **kwargs):
    """
    Perform actions immediately after a case is created.
    """
    if created:
        # Future:
        # - Create audit log entry
        # - Send notifications
        # - Create initial timeline event
        print(f"New case created: {instance.case_number}")


@receiver(post_save, sender=Case)
def case_updated(sender, instance, created, **kwargs):
    """
    Perform actions after a case is updated.
    """
    if not created:
        # Future:
        # - Log changes
        # - Notify assigned investigators
        # - Update dashboard statistics
        print(f"Case updated: {instance.case_number}")