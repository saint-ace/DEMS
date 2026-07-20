from django.contrib import admin

from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):

    list_display = (
        "report_number",
        "title",
        "report_type",
        "status",
        "generated_by",
        "generated_at",
    )

    list_filter = (
        "report_type",
        "status",
    )

    search_fields = (
        "report_number",
        "title",
    )

    ordering = (
        "-generated_at",
    )