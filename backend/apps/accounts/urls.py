"""
Digital Evidence Management System (DEMS)

Module:
    Accounts

File:
    urls.py

Purpose:
    URL routing for authentication endpoints.
"""

from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView

from .views import (
    ChangePasswordView,
    LoginView,
    ProfileView,
    RegisterView,
    UpdateProfileView,
    UserListView,
)

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/update/", UpdateProfileView.as_view(), name="profile-update"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("register/", RegisterView.as_view(), name="register"),
    path("users/", UserListView.as_view(), name="user-list"),
]