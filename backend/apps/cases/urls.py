"""
Digital Evidence Management System (DEMS)

Module:
    Cases

File:
    urls.py

Purpose:
    URL routing for the Cases module.
"""

from django.urls import path

from .views import (
    ArchiveCaseView,
    CaseCreateView,
    CaseDeleteView,
    CaseDetailView,
    CaseListView,
    CaseUpdateView,
    CloseCaseView,
    ReopenCaseView,
)

app_name = "cases"

urlpatterns = [
    # ======================================================
    # Case CRUD
    # ======================================================

    path(
        "",
        CaseListView.as_view(),
        name="case-list",
    ),

    path(
        "create/",
        CaseCreateView.as_view(),
        name="case-create",
    ),

    path(
        "<uuid:pk>/",
        CaseDetailView.as_view(),
        name="case-detail",
    ),

    path(
        "<uuid:pk>/update/",
        CaseUpdateView.as_view(),
        name="case-update",
    ),

    path(
        "<uuid:pk>/delete/",
        CaseDeleteView.as_view(),
        name="case-delete",
    ),

    # ======================================================
    # Case Actions
    # ======================================================

    path(
        "<uuid:pk>/close/",
        CloseCaseView.as_view(),
        name="case-close",
    ),

    path(
        "<uuid:pk>/reopen/",
        ReopenCaseView.as_view(),
        name="case-reopen",
    ),

    path(
        "<uuid:pk>/archive/",
        ArchiveCaseView.as_view(),
        name="case-archive",
    ),
]