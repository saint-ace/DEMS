"""
Digital Evidence Management System (DEMS)

Module:
    Chain of Custody

File:
    serializers.py
"""

from rest_framework import serializers

from .models import CustodyRecord


class CustodyListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing custody records.
    """

    evidence_number = serializers.CharField(
        source="evidence.evidence_number",
        read_only=True,
    )

    from_user = serializers.CharField(
        source="from_user.username",
        read_only=True,
        allow_null=True,
    )

    to_user = serializers.CharField(
        source="to_user.username",
        read_only=True,
    )

    class Meta:
        model = CustodyRecord
        fields = (
            "id",
            "evidence_number",
            "action",
            "from_user",
            "to_user",
            "location",
            "transferred_at",
        )


class CustodyDetailSerializer(serializers.ModelSerializer):
    """
    Detailed custody record serializer.
    """

    evidence_number = serializers.CharField(
        source="evidence.evidence_number",
        read_only=True,
    )

    from_username = serializers.CharField(
        source="from_user.username",
        read_only=True,
        allow_null=True,
    )

    to_username = serializers.CharField(
        source="to_user.username",
        read_only=True,
    )

    class Meta:
        model = CustodyRecord
        fields = "__all__"


class CustodyTransferSerializer(serializers.ModelSerializer):
    """
    Serializer used to transfer evidence.
    """

    class Meta:
        model = CustodyRecord
        fields = (
            "evidence",
            "to_user",
            "action",
            "location",
            "reason",
            "remarks",
        )