"""
Digital Evidence Management System (DEMS)

File:
    config/urls.py

Purpose:
    Root URL configuration for the DEMS backend.

Author:
    DEMS Development Team
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # -----------------------------------------------------------------
    # Django Admin
    # -----------------------------------------------------------------
    path("admin/", admin.site.urls),

    # -----------------------------------------------------------------
    # Authentication APIs
    # -----------------------------------------------------------------
    path("api/cases/",include("apps.cases.urls"),),
    path(
    "api/audit/",
    include("apps.audit.urls"),
    ),

    path("api/auth/", include("apps.accounts.urls")),

    # -----------------------------------------------------------------
    # API Documentation
    # -----------------------------------------------------------------
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),

    path(
        "api/redoc/",
        SpectacularRedocView.as_view(
            url_name="schema"
        ),
        name="redoc",
    ),

    path(
    "api/evidence/",
    include("apps.evidence.urls"),
    ),

    path(
    "api/custody/",
    include("apps.custody.urls"),
    ),

    path(
    "api/rbac/",
    include("apps.rbac.urls"),
    ),

    path(
    "api/storage/",
    include("apps.storage.urls"),
    ),

    path(
    "api/reports/",
    include("apps.reports.urls"),
    ),
    
]

# ---------------------------------------------------------------------
# Serve Media Files During Development
# ---------------------------------------------------------------------

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )