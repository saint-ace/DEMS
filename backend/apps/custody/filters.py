"""
Digital Evidence Management System (DEMS)

Module:
    Chain of Custody

File:
    filters.py
"""

import django_filters

from .models import CustodyRecord


class CustodyFilter(django_filters.FilterSet):

    action = django_filters.CharFilter(
        lookup_expr="iexact",
    )

    location = django_filters.CharFilter(
        lookup_expr="icontains",
    )

    transferred_after = django_filters.DateTimeFilter(
        field_name="transferred_at",
        lookup_expr="gte",
    )

    transferred_before = django_filters.DateTimeFilter(
        field_name="transferred_at",
        lookup_expr="lte",
    )

    class Meta:
        model = CustodyRecord

        fields = [
            "action",
            "evidence",
            "from_user",
            "to_user",
        ]