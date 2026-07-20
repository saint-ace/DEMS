"""
Digital Evidence Management System (DEMS)

Module:
    Common

File:
    apps.py

Purpose:
    Registers the Common application.
"""

from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.common"
    verbose_name = "Common"