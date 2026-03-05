"""Rules URL configuration."""

from django.urls import path
from rules import views

urlpatterns = [
    path("", views.rules_root, name="rules-root"),
    path("<int:rule_id>", views.rule_detail, name="rule-detail"),
]
