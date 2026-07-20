"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    permissions.py
"""

from apps.rbac.permissions import HasPermission


class CanViewEvidence(HasPermission):
    required_permission = "evidence.view"


class CanUploadEvidence(HasPermission):
    required_permission = "evidence.upload"


class CanUpdateEvidence(HasPermission):
    required_permission = "evidence.update"


class CanVerifyEvidence(HasPermission):
    required_permission = "evidence.verify"


class CanDownloadEvidence(HasPermission):
    required_permission = "evidence.download"


class CanDeleteEvidence(HasPermission):
    required_permission = "evidence.delete"