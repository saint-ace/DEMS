"""
Project-specific exceptions.
"""


class DEMSError(Exception):
    """
    Base exception.
    """


class EvidenceNotFoundError(DEMSError):
    pass


class CaseNotFoundError(DEMSError):
    pass


class UnauthorizedActionError(DEMSError):
    pass