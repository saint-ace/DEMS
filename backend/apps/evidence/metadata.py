"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    metadata.py

Purpose:
    Extract metadata from uploaded evidence files.
"""

import mimetypes
import os
from pathlib import Path


def get_file_extension(file_object):
    """
    Return the file extension.
    """

    return Path(file_object.name).suffix.lower()


def get_original_filename(file_object):
    """
    Return the original filename.
    """

    return os.path.basename(file_object.name)


def get_mime_type(file_object):
    """
    Determine the MIME type.
    """

    mime_type, _ = mimetypes.guess_type(file_object.name)

    return mime_type or "application/octet-stream"


def get_file_size(file_object):
    """
    Return file size in bytes.
    """

    return file_object.size


def extract_metadata(file_object):
    """
    Extract standard metadata from an uploaded file.
    """

    return {
        "original_filename": get_original_filename(file_object),
        "extension": get_file_extension(file_object),
        "mime_type": get_mime_type(file_object),
        "file_size": get_file_size(file_object),
    }