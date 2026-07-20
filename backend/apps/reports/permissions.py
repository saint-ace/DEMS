"""
Digital Evidence Management System (DEMS)

Module:
    Reports

File:
    permissions.py
"""

from rest_framework.permissions import BasePermission


class CanViewReports(BasePermission):
    """
    Allows viewing reports.
    """

    def has_permission(self, request, view):
        return request.user.has_perm("reports.view_report")


class CanGenerateReports(BasePermission):
    """
    Allows generating reports.
    """

    def has_permission(self, request, view):
        return request.user.has_perm("reports.generate_report")


class CanDeleteReports(BasePermission):
    """
    Allows deleting reports.
    """

    def has_permission(self, request, view):
        return request.user.has_perm("reports.delete_report")