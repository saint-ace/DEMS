"""
Digital Evidence Management System (DEMS)

Module:
    Cases

File:
    services.py

Purpose:
    Business logic for Case Management.
"""

from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from apps.common.services import BaseService

from .models import (
    Case,
    CaseAssignment,
)


class CaseService(BaseService):
    """
    Business logic for managing investigation cases.
    """

    @staticmethod
    @transaction.atomic
    def create_case(validated_data, created_by):
        """
        Create a new investigation case.
        """

        lead_investigator = validated_data.get("lead_investigator")

        case = Case.objects.create(
            **validated_data,
            created_by=created_by,
        )

        if lead_investigator:
            CaseAssignment.objects.create(
                case=case,
                user=lead_investigator,
                assigned_by=created_by,
                active=True,
            )

        return case

    @staticmethod
    @transaction.atomic
    def assign_user(
        case,
        user,
        assigned_by,
    ):
        """
        Assign a user to a case.
        """

        assignment, created = CaseAssignment.objects.get_or_create(
            case=case,
            user=user,
            defaults={
                "assigned_by": assigned_by,
                "active": True,
            },
        )

        if not created and assignment.active:
            raise ValidationError(
                "User is already assigned to this case."
            )

        assignment.active = True
        assignment.assigned_by = assigned_by
        assignment.save()

        return assignment

    @staticmethod
    @transaction.atomic
    def unassign_user(case, user):
        """
        Remove a user from a case.
        """

        try:
            assignment = CaseAssignment.objects.get(
                case=case,
                user=user,
            )
        except CaseAssignment.DoesNotExist:
            raise ValidationError(
                "Assignment does not exist."
            )

        assignment.active = False
        assignment.save()

        return assignment

    @staticmethod
    @transaction.atomic
    def close_case(case):
        """
        Close a case.
        """

        if case.date_closed:
            raise ValidationError(
                "Case is already closed."
            )

        closed_status = case.status.__class__.objects.filter(
            code="CLOSED"
        ).first()

        if closed_status is None:
            raise ValidationError(
                "Closed status has not been configured."
            )

        case.status = closed_status
        case.date_closed = timezone.now().date()

        case.save()

        return case

    @staticmethod
    @transaction.atomic
    def reopen_case(case):
        """
        Reopen a closed case.
        """

        open_status = case.status.__class__.objects.filter(
            code="OPEN"
        ).first()

        if open_status is None:
            raise ValidationError(
                "Open status has not been configured."
            )

        case.status = open_status
        case.date_closed = None

        case.save()

        return case

    @staticmethod
    @transaction.atomic
    def archive_case(case):
        """
        Archive a case.
        """

        archived_status = case.status.__class__.objects.filter(
            code="ARCHIVED"
        ).first()

        if archived_status is None:
            raise ValidationError(
                "Archived status has not been configured."
            )

        case.status = archived_status
        case.save()

        return case

    @staticmethod
    def update_case(case, validated_data):
        """
        Update a case.
        """

        if case.status.code == "ARCHIVED":
            raise ValidationError(
                "Archived cases cannot be modified."
            )

        for field, value in validated_data.items():
            setattr(case, field, value)

        case.save()

        return case