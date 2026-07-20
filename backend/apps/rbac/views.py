"""
Digital Evidence Management System (DEMS)

Module:
    RBAC

File:
    views.py
"""

from rest_framework.generics import ListAPIView

from .models import Permission, Role, UserRole
from .permissions import HasPermission
from .serializers import (
    PermissionSerializer,
    RoleSerializer,
    UserRoleSerializer,
)


class RBACManagePermission(HasPermission):
    required_permission = "rbac.manage"


class RoleListView(ListAPIView):
    """
    List all roles.
    """

    queryset = Role.objects.all().order_by("name")

    serializer_class = RoleSerializer

    permission_classes = [RBACManagePermission]


class PermissionListView(ListAPIView):
    """
    List all permissions.
    """

    queryset = Permission.objects.all().order_by("code")

    serializer_class = PermissionSerializer

    permission_classes = [RBACManagePermission]


class UserRoleListView(ListAPIView):
    """
    List all user-role assignments.
    """

    queryset = (
        UserRole.objects
        .select_related("user", "role")
        .order_by("user__username")
    )

    serializer_class = UserRoleSerializer

    permission_classes = [RBACManagePermission]