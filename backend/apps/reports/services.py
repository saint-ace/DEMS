"""
Digital Evidence Management System (DEMS)

Module:
    Reports

File:
    services.py
"""

from django.core.files.base import ContentFile
from django.db import transaction

from apps.audit.models import AuditAction
from apps.audit.services import AuditService
from apps.common.numbering import NumberGenerator
from apps.common.services import BaseService
from apps.storage.services import StorageService

from .models import Report, ReportStatus
from .pdf import PDFReportGenerator


class ReportService(BaseService):
    """
    Business logic for report management.
    """

    @staticmethod
    def _create_report(
        *,
        title,
        report_type,
        object_id,
        generated_by,
        notes="",
    ):
        """
        Create a new report record.
        """

        return Report.objects.create(
            report_number=NumberGenerator.generate_report_number(),
            title=title,
            report_type=report_type,
            object_id=object_id,
            generated_by=generated_by,
            status=ReportStatus.GENERATING,
            notes=notes,
        )

    @staticmethod
    def _generate_pdf(report):
        """
        Generate the PDF and store it securely.
        """

        pdf_buffer = PDFReportGenerator.generate(report)

        uploaded_file = ContentFile(
            pdf_buffer.getvalue(),
            name=f"{report.report_number}.pdf",
        )

        stored_file = StorageService.store_file(
            uploaded_file,
            report.generated_by,
        )

        report.stored_file = stored_file

        report.save(
            update_fields=["stored_file"],
        )

        return stored_file

    @staticmethod
    def _log_audit(report, user, request=None):
        """
        Log report generation.
        """

        AuditService.log(
            user=user,
            action=AuditAction.CREATE,
            module="Reports",
            object_type="Report",
            object_id=str(report.id),
            description=f"Generated report {report.report_number}",
            ip_address=(
                request.META.get("REMOTE_ADDR")
                if request
                else None
            ),
            user_agent=(
                request.META.get("HTTP_USER_AGENT", "")
                if request
                else ""
            ),
        )

    @staticmethod
    @transaction.atomic
    def generate_report(
        *,
        title,
        report_type,
        object_id,
        generated_by,
        notes="",
        request=None,
    ):
        """
        Complete report generation workflow.
        """

        report = ReportService._create_report(
            title=title,
            report_type=report_type,
            object_id=object_id,
            generated_by=generated_by,
            notes=notes,
        )

        try:
            ReportService._generate_pdf(report)

            report.status = ReportStatus.COMPLETED
            report.save(update_fields=["status"])

            ReportService._log_audit(
                report,
                generated_by,
                request,
            )

        except Exception:
            report.status = ReportStatus.FAILED
            report.save(update_fields=["status"])
            raise

        return report

    @staticmethod
    def list_reports():
        """
        Return all reports.
        """

        return (
            Report.objects.select_related(
                "generated_by",
                "stored_file",
            ).order_by("-generated_at")
        )

    @staticmethod
    def get_report(report_id):
        """
        Return a single report.
        """

        return (
            Report.objects.select_related(
                "generated_by",
                "stored_file",
            ).get(pk=report_id)
        )

    @staticmethod
    def delete_report(report):
        """
        Delete a report.
        """

        report.delete()