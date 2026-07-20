"""
Digital Evidence Management System (DEMS)

Module:
    Audit

File:
    tests.py
"""

from django.test import TestCase

from .models import AuditLog


class AuditLogModelTest(TestCase):

    def test_model_exists(self):
        """
        Basic test to verify the AuditLog model is available.
        """
        self.assertIsNotNone(AuditLog)