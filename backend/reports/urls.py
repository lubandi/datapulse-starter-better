"""Reports URL configuration."""

from django.urls import path
from reports import views

urlpatterns = [
    path("trends", views.get_quality_trends, name="reports-trends"),
    path("<int:dataset_id>", views.get_dataset_report, name="reports-detail"),
]
