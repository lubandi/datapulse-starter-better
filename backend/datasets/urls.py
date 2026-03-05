"""Datasets URL configuration."""

from django.urls import path
from datasets import views

urlpatterns = [
    path("upload", views.upload_dataset, name="dataset-upload"),
    path("", views.list_datasets, name="dataset-list"),
]
