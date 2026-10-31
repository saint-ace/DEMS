"""
Digital Evidence Management System (DEMS)

Module:
    Reports

File:
    views.py
"""

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import (
    CanDeleteReports,
    CanGenerateReports,
    CanViewReports,
)
from .serializers import (
    ReportDetailSerializer,
    ReportGenerateSerializer,
    ReportListSerializer,
)
from .services import ReportService


@extend_schema(
    responses={200: ReportListSerializer(many=True)},
)
class ReportListView(APIView):
    """
    List all reports.
    """

    permission_classes = [CanViewReports]

    def get(self, request):
        reports = ReportService.list_reports()

        serializer = ReportListSerializer(
            reports,
            many=True,
        )

        return Response(serializer.data)


@extend_schema(
    responses={200: ReportDetailSerializer},
)
class ReportDetailView(APIView):
    """
    Retrieve a report.
    """

    permission_classes = [CanViewReports]

    def get(self, request, report_id):
        report = ReportService.get_report(report_id)

        serializer = ReportDetailSerializer(report)

        return Response(serializer.data)


@extend_schema(
    request=ReportGenerateSerializer,
    responses={201: ReportDetailSerializer},
)
class GenerateReportView(APIView):
    """
    Generate a report.
    """

    permission_classes = [CanGenerateReports]

    def post(self, request):
        serializer = ReportGenerateSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        report = ReportService.generate_report(
            title=serializer.validated_data["title"],
            report_type=serializer.validated_data["report_type"],
            object_id=serializer.validated_data["object_id"],
            generated_by=request.user,
            notes=serializer.validated_data.get(
                "notes",
                "",
            ),
            request=request,
        )

        output = ReportDetailSerializer(report)

        return Response(
            output.data,
            status=status.HTTP_201_CREATED,
        )


@extend_schema(
    responses={204: None},
)
class DeleteReportView(APIView):
    """
    Delete a report.
    """

    permission_classes = [CanDeleteReports]

    def delete(self, request, report_id):
        report = ReportService.get_report(report_id)

        ReportService.delete_report(report)

        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )