"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    signals.py
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Evidence


@receiver(post_save, sender=Evidence)
def evidence_saved(sender, instance, created, **kwargs):

    if created:
        print(
            f"Evidence created: {instance.evidence_number}"
        )