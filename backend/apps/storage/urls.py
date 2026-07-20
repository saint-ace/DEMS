"""
Digital Evidence Management System (DEMS)

Module:
    Storage

File:
    urls.py
"""

from django.urls import path

from .views import (
    StorageFileDetailView,
    StorageFileListView,
)

app_name = "storage"

urlpatterns = [

    path(
        "",
        StorageFileListView.as_view(),
        name="storage-list",
    ),

    path(
        "<uuid:pk>/",
        StorageFileDetailView.as_view(),
        name="storage-detail",
    ),

]