"""
Digital Evidence Management System (DEMS)

Module:
    Storage

File:
    serializers.py
"""

from rest_framework import serializers

from .models import StorageFile


class StorageFileSerializer(serializers.ModelSerializer):

    uploaded_by = serializers.CharField(
        source="uploaded_by.username",
        read_only=True,
    )

    class Meta:
        model = StorageFile

        fields = (
            "id",
            "original_name",
            "mime_type",
            "extension",
            "file_size",
            "md5_hash",
            "sha1_hash",
            "sha256_hash",
            "uploaded_by",
            "verified",
            "created_at",
        )