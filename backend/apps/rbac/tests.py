"""
Digital Evidence Management System (DEMS)

Module:
    RBAC

File:
    tests.py
"""

from django.test import TestCase

from .models import Role


class RoleModelTest(TestCase):

    def test_role_model_exists(self):
        self.assertIsNotNone(Role)