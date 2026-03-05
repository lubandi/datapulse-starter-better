"""Validation rules router - PARTIAL implementation."""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rules.models import ValidationRule
from rules.serializers import RuleCreateSerializer, RuleResponseSerializer, RuleUpdateSerializer

VALID_TYPES = {"NOT_NULL", "DATA_TYPE", "RANGE", "UNIQUE", "REGEX"}
VALID_SEVERITIES = {"HIGH", "MEDIUM", "LOW"}


@api_view(["POST", "GET"])
def rules_root(request):
    """Handle POST (create) and GET (list) for rules."""
    if request.method == "POST":
        return create_rule(request)
    return list_rules(request)


@api_view(["PUT", "DELETE"])
def rule_detail(request, rule_id):
    """Handle PUT (update) and DELETE for a specific rule."""
    if request.method == "PUT":
        return update_rule(request, rule_id)
    return delete_rule(request, rule_id)


def create_rule(request):
    """Create a new validation rule - IMPLEMENTED."""
    serializer = RuleCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    if data["rule_type"] not in VALID_TYPES:
        return Response(
            {"detail": f"Invalid rule_type: {VALID_TYPES}"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if data["severity"] not in VALID_SEVERITIES:
        return Response(
            {"detail": f"Invalid severity: {VALID_SEVERITIES}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    rule = ValidationRule.objects.create(**data)
    return Response(
        RuleResponseSerializer(rule).data, status=status.HTTP_201_CREATED
    )


def list_rules(request):
    """List validation rules - IMPLEMENTED."""
    dataset_type = request.query_params.get("dataset_type")
    queryset = ValidationRule.objects.filter(is_active=True)
    if dataset_type:
        queryset = queryset.filter(dataset_type=dataset_type)
    return Response(
        RuleResponseSerializer(queryset, many=True).data, status=status.HTTP_200_OK
    )


def update_rule(request, rule_id):
    """Update a validation rule - TODO: Implement.

    Steps:
    1. Fetch rule by ID (404 if not found)
    2. Update non-None fields from rule_data
    3. Validate rule_type and severity if changed
    4. Commit and return updated rule
    """
    return Response(
        {"detail": "PUT /api/rules/{id} not implemented"},
        status=status.HTTP_501_NOT_IMPLEMENTED,
    )


def delete_rule(request, rule_id):
    """Soft-delete a validation rule - TODO: Implement.

    Steps:
    1. Fetch rule by ID (404 if not found)
    2. Set is_active = False
    3. Save, return 204
    """
    return Response(
        {"detail": "DELETE /api/rules/{id} not implemented"},
        status=status.HTTP_501_NOT_IMPLEMENTED,
    )
