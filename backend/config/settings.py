"""
Digital Evidence Management System (DEMS)

File:
    config/settings.py

Purpose:
    Global Django configuration for the DEMS backend.

Author:
    DEMS Development Team
"""

from pathlib import Path
from datetime import timedelta
import os

from dotenv import load_dotenv

# ---------------------------------------------------------------------
# PATHS
# ---------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# ---------------------------------------------------------------------
# SECURITY
# ---------------------------------------------------------------------

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-change-this-in-production"
)

DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
]

# ---------------------------------------------------------------------
# APPLICATIONS
# ---------------------------------------------------------------------

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "django_filters",
    "corsheaders",
    "drf_spectacular",
]


INSTALLED_APPS = [
    # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_spectacular",
    "drf_spectacular_sidecar",

    # Third-party Apps
    "rest_framework",
    "django_filters",

    # Local Apps
    "apps.common",
    "apps.accounts",
    "apps.cases",
    "apps.audit",
    "apps.evidence",
    "apps.custody",
    "apps.rbac",
    "apps.storage",
    "apps.reports",
]

# ---------------------------------------------------------------------
# MIDDLEWARE
# ---------------------------------------------------------------------

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ---------------------------------------------------------------------
# URLS
# ---------------------------------------------------------------------

ROOT_URLCONF = "config.urls"

# ---------------------------------------------------------------------
# TEMPLATES
# ---------------------------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ---------------------------------------------------------------------
# WSGI
# ---------------------------------------------------------------------

WSGI_APPLICATION = "config.wsgi.application"

# ---------------------------------------------------------------------
# DATABASE
# ---------------------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": os.getenv(
            "DB_ENGINE",
            "django.db.backends.sqlite3"
        ),

        "NAME": os.getenv(
            "DB_NAME",
            BASE_DIR / "db.sqlite3"
        ),

        "USER": os.getenv("DB_USER", ""),

        "PASSWORD": os.getenv("DB_PASSWORD", ""),

        "HOST": os.getenv("DB_HOST", ""),

        "PORT": os.getenv("DB_PORT", ""),
    }
}

# ---------------------------------------------------------------------
# PASSWORD VALIDATION
# ---------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ---------------------------------------------------------------------
# CUSTOM USER MODEL
# ---------------------------------------------------------------------

AUTH_USER_MODEL = "accounts.User"

# ---------------------------------------------------------------------
# INTERNATIONALIZATION
# ---------------------------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# ---------------------------------------------------------------------
# STATIC FILES
# ---------------------------------------------------------------------

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# ---------------------------------------------------------------------
# MEDIA FILES
# ---------------------------------------------------------------------

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------------------------------------------------
# DEFAULT PRIMARY KEY
# ---------------------------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------------------------
# DJANGO REST FRAMEWORK
# ---------------------------------------------------------------------

# ---------------------------------------------------------
# Django REST Framework
# ---------------------------------------------------------

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),

    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),

    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
    "DEFAULT_SCHEMA_CLASS": (
    "drf_spectacular.openapi.AutoSchema",
    ),
}

# ---------------------------------------------------------------------
# JWT SETTINGS
# ---------------------------------------------------------------------

SIMPLE_JWT = {

    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),

    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),

    "ROTATE_REFRESH_TOKENS": True,

    "BLACKLIST_AFTER_ROTATION": True,

    "UPDATE_LAST_LOGIN": True,
}

# ---------------------------------------------------------------------
# CORS
# ---------------------------------------------------------------------

CORS_ALLOW_ALL_ORIGINS = DEBUG

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

# ---------------------------------------------------------------------
# API DOCUMENTATION
# ---------------------------------------------------------------------

SPECTACULAR_SETTINGS = {

    "TITLE": "Digital Evidence Management System API",

    "DESCRIPTION":
        "REST API for the Digital Evidence Management System.",

    "VERSION": "1.0.0",
}

# ---------------------------------------------------------------------
# LOGGING
# ---------------------------------------------------------------------

LOGGING = {

    "version": 1,

    "disable_existing_loggers": False,

    "handlers": {

        "console": {

            "class": "logging.StreamHandler",

        },

    },

    "root": {

        "handlers": ["console"],

        "level": "INFO",

    },
}