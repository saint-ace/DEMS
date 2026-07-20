"""
Digital Evidence Management System (DEMS)

Module:
    Storage

File:
    services.py

Purpose:
    Secure storage service.
"""

from django.db import transaction

from .models import StorageFile
from .utils import FileUtility


class StorageService:
    """
    Handles secure storage of uploaded files.
    """

    @staticmethod
    @transaction.atomic
    def store_file(uploaded_file, uploaded_by):
        """
        Store a file and record its metadata.
        """

        original_name = uploaded_file.name

        hashes = FileUtility.calculate_hashes(
            uploaded_file
        )

        stored_name = FileUtility.generate_storage_name(
            original_name
        )

        uploaded_file.name = stored_name

        storage = StorageFile.objects.create(
            file=uploaded_file,
            original_name=original_name,
            stored_name=stored_name,
            mime_type=FileUtility.get_mime_type(
                original_name
            ),
            extension=FileUtility.get_extension(
                original_name
            ),
            file_size=uploaded_file.size,
            md5_hash=hashes["md5"],
            sha1_hash=hashes["sha1"],
            sha256_hash=hashes["sha256"],
            uploaded_by=uploaded_by,
        )

        return storage