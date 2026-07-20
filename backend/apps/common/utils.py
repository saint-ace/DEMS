"""
Shared utility functions.
"""

from datetime import datetime


def generate_reference(prefix, number):

    year = datetime.now().year

    return f"{prefix}-{year}-{number:06d}"