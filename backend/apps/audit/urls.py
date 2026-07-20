"""
Digital Evidence Management System (DEMS)

Module:
    Audit

File:
    urls.py
"""

from django.urls import path

from .views import (
    AuditLogDetailView,
    AuditLogListView,
)

urlpatterns = [
    path(
        "",
        AuditLogListView.as_view(),
        name="audit-list",
    ),
    path(
        "<uuid:pk>/",
        AuditLogDetailView.as_view(),
        name="audit-detail",
    ),
]