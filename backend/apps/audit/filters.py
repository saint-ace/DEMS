"""
Digital Evidence Management System (DEMS)

Module:
    Audit

File:
    filters.py
"""

import django_filters

from .models import AuditLog


class AuditLogFilter(django_filters.FilterSet):

    username = django_filters.CharFilter(
        field_name="user__username",
        lookup_expr="icontains",
    )

    module = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    action = django_filters.CharFilter(
        lookup_expr="iexact",
    )

    object_type = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    created_after = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="gte",
    )

    created_before = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="lte",
    )

    class Meta:
        model = AuditLog

        fields = [
            "module",
            "action",
            "object_type",
        ]