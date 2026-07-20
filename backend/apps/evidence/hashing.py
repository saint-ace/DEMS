"""
Digital Evidence Management System (DEMS)

Module:
    Evidence

File:
    hashing.py

Purpose:
    Cryptographic hashing utilities for digital evidence.
"""

import hashlib


CHUNK_SIZE = 1024 * 1024  # 1 MB


def _calculate_hash(file_object, algorithm):
    """
    Calculate a hash using the specified algorithm.

    Args:
        file_object: Django UploadedFile or file-like object.
        algorithm: hashlib hash object.

    Returns:
        Hexadecimal digest.
    """

    algorithm = algorithm()

    file_object.seek(0)

    while True:
        chunk = file_object.read(CHUNK_SIZE)

        if not chunk:
            break

        algorithm.update(chunk)

    file_object.seek(0)

    return algorithm.hexdigest()


def generate_sha256(file_object):
    """
    Generate a SHA-256 hash.
    """
    return _calculate_hash(file_object, hashlib.sha256)


def generate_sha1(file_object):
    """
    Generate a SHA-1 hash.
    """
    return _calculate_hash(file_object, hashlib.sha1)


def generate_md5(file_object):
    """
    Generate an MD5 hash.
    """
    return _calculate_hash(file_object, hashlib.md5)


def verify_sha256(file_object, expected_hash):
    """
    Verify the SHA-256 hash of a file.

    Returns:
        True if the hash matches, otherwise False.
    """

    calculated_hash = generate_sha256(file_object)

    return calculated_hash.lower() == expected_hash.lower()