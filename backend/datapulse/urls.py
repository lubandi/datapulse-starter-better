"""DataPulse URL Configuration."""

from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def root(request):
    """Root endpoint."""
    return Response({"name": "DataPulse", "version": "1.0.0", "docs": "/docs"})


@api_view(["GET"])
def health_check(request):
    """Health check endpoint."""
    return Response({"status": "healthy"})


urlpatterns = [
    path("", root),
    path("health", health_check),
    path("api/auth/", include("authentication.urls")),
    path("api/datasets/", include("datasets.urls")),
    path("api/rules/", include("rules.urls")),
    path("api/checks/", include("checks.urls")),
    path("api/reports/", include("reports.urls")),
]
