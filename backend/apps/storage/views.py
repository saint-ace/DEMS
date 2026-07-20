"""
Digital Evidence Management System (DEMS)

Module:
    Storage

File:
    views.py
"""

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import StorageFile
from .permissions import CanViewStorage
from .serializers import StorageFileSerializer


class StorageFileListView(ListAPIView):
    """
    List all stored files.
    """

    queryset = (
        StorageFile.objects
        .select_related("uploaded_by")
        .order_by("-created_at")
    )

    serializer_class = StorageFileSerializer

    permission_classes = [CanViewStorage]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        "original_name",
        "mime_type",
        "sha256_hash",
    ]

    ordering_fields = [
        "created_at",
        "file_size",
    ]


class StorageFileDetailView(RetrieveAPIView):
    """
    Retrieve a stored file.
    """

    queryset = StorageFile.objects.select_related(
        "uploaded_by"
    )

    serializer_class = StorageFileSerializer

    permission_classes = [CanViewStorage]