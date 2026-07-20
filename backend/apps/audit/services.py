"""
Digital Evidence Management System (DEMS)

Module:
    Audit

File:
    services.py
"""
from .models import AuditLog


class AuditService:
    """
    Centralized audit logging service.
    """

    @staticmethod
    def log(
        *,
        user,
        action,
        module,
        object_type,
        object_id,
        description,
        ip_address=None,
        user_agent="",
    ):
        """
        Create an audit log entry.
        """

        return AuditLog.objects.create(
            user=user,
            action=action,
            module=module,
            object_type=object_type,
            object_id=str(object_id),
            description=description,
            ip_address=ip_address,
            user_agent=user_agent,
        )