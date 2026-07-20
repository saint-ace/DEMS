"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    permissions.py
"""

from apps.rbac.permissions import HasPermission


class CanViewCustody(HasPermission):
    required_permission = "custody.view"


class CanCreateCustody(HasPermission):
    required_permission = "custody.create"


class CanUpdateCustody(HasPermission):
    required_permission = "custody.update"


class CanDeleteCustody(HasPermission):
    required_permission = "custody.delete"


class CanTransferEvidence(HasPermission):
    required_permission = "custody.transfer"


class CanReceiveEvidence(HasPermission):
    required_permission = "custody.receive"


class CanVerifyCustody(HasPermission):
    required_permission = "custody.verify"