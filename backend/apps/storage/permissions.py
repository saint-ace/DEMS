"""
Digital Evidence Management System (DEMS)

Module:
    Storage

File:
    permissions.py
"""

from apps.rbac.permissions import HasPermission


class CanViewStorage(HasPermission):
    required_permission = "storage.view"


class CanUploadStorage(HasPermission):
    required_permission = "storage.upload"


class CanVerifyStorage(HasPermission):
    required_permission = "storage.verify"