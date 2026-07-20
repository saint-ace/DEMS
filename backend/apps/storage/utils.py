"""
Digital Evidence Management System (DEMS)

Module:
    Storage

File:
    utils.py

Purpose:
    File utility functions.
"""

import hashlib
import mimetypes
import os
import uuid


class FileUtility:
    """
    Utility methods for uploaded files.
    """

    CHUNK_SIZE = 8192

    @staticmethod
    def calculate_hashes(uploaded_file):
        """
        Calculate MD5, SHA1 and SHA256 hashes.
        """

        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()

        uploaded_file.seek(0)

        while chunk := uploaded_file.read(FileUtility.CHUNK_SIZE):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

        uploaded_file.seek(0)

        return {
            "md5": md5.hexdigest(),
            "sha1": sha1.hexdigest(),
            "sha256": sha256.hexdigest(),
        }

    @staticmethod
    def get_extension(filename):

        return os.path.splitext(filename)[1].lower()

    @staticmethod
    def get_mime_type(filename):

        mime, _ = mimetypes.guess_type(filename)

        return mime or "application/octet-stream"

    @staticmethod
    def generate_storage_name(filename):

        extension = FileUtility.get_extension(filename)

        return f"{uuid.uuid4().hex}{extension}"