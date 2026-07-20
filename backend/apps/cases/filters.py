"""
Digital Evidence Management System (DEMS)

Module:
    Cases

File:
    filters.py

Purpose:
    Filtering and searching for investigation cases.
"""

import django_filters

from .models import Case


class CaseFilter(django_filters.FilterSet):
    """
    Filters for investigation cases.
    """

    case_number = django_filters.CharFilter(
        field_name="case_number",
        lookup_expr="icontains",
    )

    title = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
    )

    case_type = django_filters.CharFilter(
        field_name="case_type__name",
        lookup_expr="icontains",
    )

    status = django_filters.CharFilter(
        field_name="status__code",
        lookup_expr="iexact",
    )

    priority = django_filters.CharFilter(
        field_name="priority__code",
        lookup_expr="iexact",
    )

    department = django_filters.CharFilter(
        field_name="department__name",
        lookup_expr="icontains",
    )

    investigator = django_filters.CharFilter(
        field_name="lead_investigator__username",
        lookup_expr="icontains",
    )

    opened_after = django_filters.DateFilter(
        field_name="date_opened",
        lookup_expr="gte",
    )

    opened_before = django_filters.DateFilter(
        field_name="date_opened",
        lookup_expr="lte",
    )

    incident_after = django_filters.DateFilter(
        field_name="incident_date",
        lookup_expr="gte",
    )

    incident_before = django_filters.DateFilter(
        field_name="incident_date",
        lookup_expr="lte",
    )

    class Meta:
        model = Case
        fields = [
            "case_number",
            "title",
            "case_type",
            "status",
            "priority",
            "department",
        ]