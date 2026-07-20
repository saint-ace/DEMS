from django.contrib import admin

from .models import Sequence


@admin.register(Sequence)
class SequenceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "year",
        "current_value",
    )

    list_filter = (
        "year",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
        "year",
    )