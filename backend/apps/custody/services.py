"""
Digital Evidence Management System (DEMS)

Module:
    Chain of Custody

File:
    services.py
"""

from django.db import transaction

from apps.audit.models import AuditAction
from apps.audit.services import AuditService
from apps.common.services import BaseService

from .models import CustodyRecord


class CustodyService(BaseService):
    """
    Business logic for Chain of Custody.
    """

    @staticmethod
    @transaction.atomic
    def transfer_evidence(
        *,
        evidence,
        from_user,
        to_user,
        action,
        location,
        reason,
        remarks="",
        request=None,
    ):
        """
        Create a custody transfer record.
        """

        custody = CustodyRecord.objects.create(
            evidence=evidence,
            from_user=from_user,
            to_user=to_user,
            action=action,
            location=location,
            reason=reason,
            remarks=remarks,
        )

        AuditService.log(
            user=from_user,
            action=AuditAction.UPDATE,
            module="Custody",
            object_type="Evidence",
            object_id=evidence.id,
            description=(
                f"Transferred "
                f"{evidence.evidence_number} "
                f"to {to_user.username}"
            ),
            ip_address=(
                request.META.get("REMOTE_ADDR")
                if request else None
            ),
            user_agent=(
                request.META.get("HTTP_USER_AGENT", "")
                if request else ""
            ),
        )

        return custody