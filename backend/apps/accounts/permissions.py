"""
Digital Evidence Management System (DEMS)

Module:
    Accounts

File:
    permissions.py

Purpose:
    Custom permission classes for Role-Based Access Control (RBAC).
"""

from rest_framework.permissions import BasePermission


class IsAuthenticatedAndActive(BasePermission):
    """
    Allows access only to authenticated and active users.
    """

    message = "Your account is inactive or you are not authenticated."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_active
        )


class BaseRolePermission(BasePermission):
    """
    Base permission for checking user roles.
    """

    allowed_roles = []

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if not user.is_active:
            return False

        if user.is_superuser:
            return True

        if user.role is None:
            return False

        return user.role.name in self.allowed_roles


class IsAdministrator(BaseRolePermission):
    """
    Administrator access only.
    """

    allowed_roles = [
        "Administrator",
    ]


class IsLeadInvestigator(BaseRolePermission):
    """
    Lead Investigator access.
    """

    allowed_roles = [
        "Lead Investigator",
    ]


class IsInvestigator(BaseRolePermission):
    """
    Investigator access.
    """

    allowed_roles = [
        "Investigator",
    ]


class IsEvidenceCustodian(BaseRolePermission):
    """
    Evidence Custodian access.
    """

    allowed_roles = [
        "Evidence Custodian",
    ]


class IsForensicAnalyst(BaseRolePermission):
    """
    Forensic Analyst access.
    """

    allowed_roles = [
        "Forensic Analyst",
    ]


class IsAuditor(BaseRolePermission):
    """
    Auditor access.
    """

    allowed_roles = [
        "Auditor",
    ]


class IsProsecutor(BaseRolePermission):
    """
    Prosecutor access.
    """

    allowed_roles = [
        "Prosecutor",
    ]


class IsAdministratorOrLeadInvestigator(BaseRolePermission):
    """
    Administrator or Lead Investigator.
    """

    allowed_roles = [
        "Administrator",
        "Lead Investigator",
    ]


class IsInvestigatorOrAnalyst(BaseRolePermission):
    """
    Investigator or Forensic Analyst.
    """

    allowed_roles = [
        "Investigator",
        "Forensic Analyst",
    ]