"""
Digital Evidence Management System (DEMS)

Module:
    RBAC

File:
    urls.py
"""

from django.urls import path

from .views import (
    PermissionListView,
    RoleListView,
    UserRoleListView,
)

app_name = "rbac"

urlpatterns = [

    path(
        "roles/",
        RoleListView.as_view(),
        name="roles",
    ),

    path(
        "permissions/",
        PermissionListView.as_view(),
        name="permissions",
    ),

    path(
        "assignments/",
        UserRoleListView.as_view(),
        name="assignments",
    ),

]