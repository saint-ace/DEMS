"""
Digital Evidence Management System (DEMS)

Module:
    Chain of Custody

File:
    tests.py
"""

from django.test import TestCase

from .models import CustodyRecord


class CustodyRecordModelTest(TestCase):

    def test_model_exists(self):
        self.assertIsNotNone(CustodyRecord)