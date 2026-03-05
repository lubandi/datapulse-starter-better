"""Checks URL configuration."""

from django.urls import path
from checks import views

urlpatterns = [
    path("run/<int:dataset_id>", views.run_checks, name="checks-run"),
    path("results/<int:dataset_id>", views.get_check_results, name="checks-results"),
]
