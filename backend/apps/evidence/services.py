"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    services.py
"""

from django.db import transaction
from django.utils import timezone

from apps.audit.models import AuditAction
from apps.audit.services import AuditService
from apps.common.numbering import NumberGenerator
from apps.common.services import BaseService
from apps.storage.services import StorageService

from .models import Evidence


class EvidenceService(BaseService):
    """
    Business logic for evidence management.
    """

    @staticmethod
    def _store_file(uploaded_file, uploaded_by):
        """
        Store the uploaded file.
        """
        return StorageService.store_file(
            uploaded_file=uploaded_file,
            uploaded_by=uploaded_by,
        )

    @staticmethod
    def _create_evidence(
        *,
        case,
        stored_file,
        uploaded_by,
        title,
        description,
        evidence_type,
        notes,
    ):
        """
        Create an evidence record.
        """

        return Evidence.objects.create(
            case=case,
            evidence_number=NumberGenerator.generate_evidence_number(),
            title=title,
            description=description,
            evidence_type=evidence_type,
            stored_file=stored_file,
            collected_by=uploaded_by,
            collected_at=timezone.now(),
            notes=notes,
        )

    @staticmethod
    def _log_audit(evidence, user, request=None):
        """
        Record the audit event.
        """

        AuditService.log(
            user=user,
            action=AuditAction.CREATE,
            module="Evidence",
            object_type="Evidence",
            object_id=str(evidence.id),
            description=(
                f"Uploaded evidence {evidence.evidence_number}"
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

    @staticmethod
    def _create_initial_custody(evidence, user):
        """
        Placeholder for the first chain-of-custody record.

        This will be connected to the Custody module.
        """
        pass

    @staticmethod
    @transaction.atomic
    def upload_evidence(
        *,
        case,
        uploaded_file,
        uploaded_by,
        title,
        description="",
        evidence_type,
        notes="",
        request=None,
    ):
        """
        Complete evidence upload workflow.
        """

        stored_file = EvidenceService._store_file(
            uploaded_file,
            uploaded_by,
        )

        evidence = EvidenceService._create_evidence(
            case=case,
            stored_file=stored_file,
            uploaded_by=uploaded_by,
            title=title,
            description=description,
            evidence_type=evidence_type,
            notes=notes,
        )

        EvidenceService._log_audit(
            evidence,
            uploaded_by,
            request,
        )

        EvidenceService._create_initial_custody(
            evidence,
            uploaded_by,
        )

        return evidence

    @staticmethod
    def list_evidence():
        """
        Return all evidence.
        """

        return (
            Evidence.objects
            .select_related(
                "case",
                "stored_file",
                "collected_by",
            )
            .order_by("-created_at")
        )

    @staticmethod
    def get_evidence(pk):
        """
        Return one evidence item.
        """

        return (
            Evidence.objects
            .select_related(
                "case",
                "stored_file",
                "collected_by",
            )
            .get(pk=pk)
        )