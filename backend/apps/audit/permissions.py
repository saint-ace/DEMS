"""
Digital Evidence Management System (DEMS)

Module:
    Audit

File:
    permissions.py
"""

from apps.rbac.permissions import HasPermission


class CanViewAuditLogs(HasPermission):
    """
    Permission to view audit logs.
    """

    required_permission = "audit.view"


class CanDeleteAuditLogs(HasPermission):
    """
    Permission to delete audit logs.
    """

    required_permission = "audit.delete"


class CanExportAuditLogs(HasPermission):
    """
    Permission to export audit logs.
    """

    required_permission = "audit.export"