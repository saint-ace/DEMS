"""
Digital Evidence Management System (DEMS)

Module:
    Chain of Custody

File:
    signals.py
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustodyRecord


@receiver(post_save, sender=CustodyRecord)
def custody_created(sender, instance, created, **kwargs):

    if created:
        print(
            f"Custody record created for "
            f"{instance.evidence.evidence_number}"
        )