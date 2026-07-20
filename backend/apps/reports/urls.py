"""
Digital Evidence Management System (DEMS)

Module:
    Reports

File:
    urls.py
"""

from django.urls import path

from .views import (
    DeleteReportView,
    GenerateReportView,
    ReportDetailView,
    ReportListView,
)

urlpatterns = [
    path(
        "",
        ReportListView.as_view(),
        name="report-list",
    ),
    path(
        "generate/",
        GenerateReportView.as_view(),
        name="report-generate",
    ),
    path(
        "<uuid:report_id>/",
        ReportDetailView.as_view(),
        name="report-detail",
    ),
    path(
        "<uuid:report_id>/delete/",
        DeleteReportView.as_view(),
        name="report-delete",
    ),
]