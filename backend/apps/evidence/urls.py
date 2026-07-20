"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    urls.py
"""

from django.urls import path

from .views import (
    EvidenceDetailView,
    EvidenceListView,
    EvidenceUploadView,
)

app_name = "evidence"

urlpatterns = [

    path(
        "",
        EvidenceListView.as_view(),
        name="list",
    ),

    path(
        "upload/",
        EvidenceUploadView.as_view(),
        name="upload",
    ),

    path(
        "<uuid:pk>/",
        EvidenceDetailView.as_view(),
        name="detail",
    ),

]