"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    validators.py

Purpose:
    Validation utilities for uploaded evidence files.
"""

import os

from django.core.exceptions import ValidationError

# Maximum upload size (2 GB)
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024

# Allowed evidence file extensions
ALLOWED_EXTENSIONS = {
    # Documents
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".csv",
    ".xlsx",

    # Images
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".gif",
    ".tif",
    ".tiff",

    # Video
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",

    # Audio
    ".wav",
    ".mp3",

    # Archives
    ".zip",
    ".7z",
    ".rar",
    ".tar",
    ".gz",

    # Disk Images
    ".dd",
    ".img",
    ".iso",
    ".e01",
    ".001",

    # Memory Dumps
    ".raw",
    ".mem",

    # Network Captures
    ".pcap",
    ".pcapng",

    # Mobile
    ".ufdr",
}


def validate_file_size(file):
    """
    Validate the uploaded file size.
    """

    if file.size > MAX_FILE_SIZE:
        raise ValidationError(
            f"File exceeds the maximum size of "
            f"{MAX_FILE_SIZE // (1024 * 1024)} MB."
        )


def validate_file_extension(file):
    """
    Validate the uploaded file extension.
    """

    extension = os.path.splitext(file.name)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValidationError(
            f"Unsupported file type: {extension}"
        )


def validate_evidence_file(file):
    """
    Run all evidence validation checks.
    """

    validate_file_size(file)
    validate_file_extension(file)