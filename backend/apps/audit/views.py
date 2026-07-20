"""
Digital Evidence Management System (DEMS)

Module:
    Audit

File:
    views.py

Purpose:
    REST API views for Audit Logs.
"""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .filters import AuditLogFilter
from .models import AuditLog
from .permissions import CanViewAuditLogs
from .serializers import AuditLogSerializer


class AuditLogListView(ListAPIView):
    """
    List audit logs.
    """

    queryset = (
        AuditLog.objects
        .select_related("user")
        .order_by("-created_at")
    )

    serializer_class = AuditLogSerializer
    permission_classes = [CanViewAuditLogs]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = AuditLogFilter

    search_fields = [
        "description",
        "module",
        "object_type",
        "object_id",
        "user__username",
    ]

    ordering_fields = [
        "created_at",
        "module",
        "action",
    ]

    ordering = [
        "-created_at",
    ]


class AuditLogDetailView(RetrieveAPIView):
    """
    Retrieve a single audit log.
    """

    queryset = AuditLog.objects.select_related("user")

    serializer_class = AuditLogSerializer

    permission_classes = [CanViewAuditLogs]