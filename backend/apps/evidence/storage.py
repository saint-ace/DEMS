"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    storage.py

Purpose:
    Custom storage path generation for evidence files.
"""

import os
from pathlib import Path


def evidence_upload_path(instance, filename):
    """
    Generate a structured upload path.

    Example:

    media/
        evidence/
            CASE-2026-000001/
                EVID-000001/
                    disk_image.E01
    """

    extension = Path(filename).suffix

    safe_filename = (
        f"{instance.evidence_number}{extension}"
    )

    return os.path.join(
        "evidence",
        instance.case.case_number,
        instance.evidence_number,
        safe_filename,
    )