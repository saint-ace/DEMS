"""
Digital Evidence Management System (DEMS)

Module:
    Common

File:
    numbering.py

Purpose:
    Enterprise sequence generator.
"""

from django.db import transaction
from django.db.models import F
from django.utils import timezone

from apps.common.models import Sequence


class NumberGenerator:
    """
    Generates unique sequential numbers.
    """

    @staticmethod
    @transaction.atomic
    def _next(sequence_name):
        """
        Atomically allocate the next sequence number.
        """

        year = timezone.now().year

        sequence, _ = Sequence.objects.select_for_update().get_or_create(
            name=sequence_name,
            year=year,
            defaults={
                "current_value": 0,
            },
        )

        sequence.current_value = F("current_value") + 1
        sequence.save(update_fields=["current_value"])

        sequence.refresh_from_db()

        return sequence.current_value

    @staticmethod
    def generate_evidence_number():
        number = NumberGenerator._next("EVIDENCE")
        year = timezone.now().year
        return f"EV-{year}-{number:06d}"

    @staticmethod
    def generate_case_number():
        number = NumberGenerator._next("CASE")
        year = timezone.now().year
        return f"CASE-{year}-{number:06d}"

    @staticmethod
    def generate_report_number():
        number = NumberGenerator._next("REPORT")
        year = timezone.now().year
        return f"REP-{year}-{number:06d}"

    @staticmethod
    def generate_custody_number():
        number = NumberGenerator._next("CUSTODY")
        year = timezone.now().year
        return f"CUST-{year}-{number:06d}"