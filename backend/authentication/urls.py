"""Authentication URL configuration."""

from django.urls import path
from authentication import views

urlpatterns = [
    path("register", views.register, name="auth-register"),
    path("login", views.login, name="auth-login"),
]
