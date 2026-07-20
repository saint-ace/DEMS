"""
Digital Evidence Management System (DEMS)

Module:
    Accounts

File:
    models.py

Purpose:
    Models for authentication, roles, departments and user activity.
"""

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.models import BaseModel
from .managers import UserManager


class Department(BaseModel):
    """
    Organizational departments.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


class Role(BaseModel):
    """
    System roles.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    Custom authentication model.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    email = models.EmailField(unique=True)

    employee_number = models.CharField(
        max_length=30,
        unique=True,
    )

    badge_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )

    objects = UserManager()

    REQUIRED_FIELDS = [
        "email",
        "employee_number",
    ]

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.employee_number})"


class UserActivity(BaseModel):
    """
    Tracks user activity.
    """

    ACTION_CHOICES = [
        ("LOGIN", "Login"),
        ("LOGOUT", "Logout"),
        ("CREATE", "Account Created"),
        ("UPDATE", "Profile Updated"),
        ("PASSWORD", "Password Changed"),
        ("DEACTIVATE", "Account Deactivated"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="activities",
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES,
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    user_agent = models.TextField(
        blank=True,
    )

    details = models.JSONField(
        default=dict,
        blank=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.get_action_display()}"