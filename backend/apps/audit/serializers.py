"""
Digital Evidence Management System (DEMS)

Module:
    Audit

File:
    serializers.py
"""

from rest_framework import serializers

from .models import AuditLog


class AuditLogSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True,
    )

    class Meta:
        model = AuditLog

        fields = (
            "id",
            "created_at",
            "username",
            "module",
            "action",
            "object_type",
            "object_id",
            "description",
            "ip_address",
            "user_agent",
        )

        read_only_fields = fields