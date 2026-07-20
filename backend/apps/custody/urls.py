"""
Digital Evidence Management System (DEMS)

Module:
    Chain of Custody

File:
    urls.py
"""

from django.urls import path

from .views import (
    CustodyDetailView,
    CustodyListView,
    CustodyTransferView,
)

app_name = "custody"

urlpatterns = [

    path(
        "",
        CustodyListView.as_view(),
        name="custody-list",
    ),

    path(
        "transfer/",
        CustodyTransferView.as_view(),
        name="custody-transfer",
    ),

    path(
        "<uuid:pk>/",
        CustodyDetailView.as_view(),
        name="custody-detail",
    ),

]