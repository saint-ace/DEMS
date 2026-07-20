"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    tests.py
"""

from django.test import TestCase

from .models import Evidence


class EvidenceModelTest(TestCase):

    def test_model_exists(self):
        self.assertIsNotNone(Evidence)