"""
Digital Evidence Management System (DEMS)

Module:
    Storage

File:
    tests.py
"""

from django.test import TestCase

from .models import StorageFile


class StorageFileModelTest(TestCase):

    def test_model_exists(self):
        self.assertIsNotNone(StorageFile)