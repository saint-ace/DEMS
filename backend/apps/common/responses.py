"""
Digital Evidence Management System (DEMS)

Module:
    Common

File:
    responses.py

Purpose:
    Standard API response helpers.
"""

from rest_framework.response import Response


def success_response(
    data=None,
    message="Success",
    status_code=200,
):
    """
    Return a standardized success response.
    """
    return Response(
        {
            "success": True,
            "message": message,
            "data": data,
        },
        status=status_code,
    )


def error_response(
    message="An error occurred.",
    errors=None,
    status_code=400,
):
    """
    Return a standardized error response.
    """
    return Response(
        {
            "success": False,
            "message": message,
            "errors": errors,
        },
        status=status_code,
    )