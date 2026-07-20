"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    filters.py
"""

import django_filters

from .models import Evidence


class EvidenceFilter(django_filters.FilterSet):

    evidence_number = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    title = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    status = django_filters.CharFilter()

    evidence_type = django_filters.CharFilter()

    collected_after = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="gte",
    )

    collected_before = django_filters.DateTimeFilter(
        field_name="created_at",
        lookup_expr="lte",
    )

    class Meta:
        model = Evidence

        fields = [
            "status",
            "evidence_type",
            "case",
        ]