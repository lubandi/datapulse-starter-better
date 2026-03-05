"""Quality checks router - STUB: All endpoints need implementation."""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def run_checks(request, dataset_id):
    """Run all applicable validation checks on a dataset.

    TODO: Implement this endpoint.

    Steps:
    1. Fetch dataset by ID (404 if not found)
    2. Get DatasetFile, read file path
    3. Load file with file_parser (parse_csv or parse_json)
    4. Fetch active ValidationRules matching dataset type
    5. Init ValidationEngine, call run_all_checks(df, rules)
    6. Create CheckResult records for each check
    7. Calculate quality score via scoring_service
    8. Create QualityScore record
    9. Update dataset status (VALIDATED or FAILED)
    10. Return score and results summary
    """
    return Response(
        {"detail": "POST /api/checks/run not implemented"},
        status=status.HTTP_501_NOT_IMPLEMENTED,
    )


@api_view(["GET"])
def get_check_results(request, dataset_id):
    """Get all check results for a dataset.

    TODO: Implement this endpoint.

    Steps:
    1. Query CheckResult table by dataset_id
    2. Order by checked_at descending
    3. Return list of results
    """
    return Response(
        {"detail": "GET /api/checks/results not implemented"},
        status=status.HTTP_501_NOT_IMPLEMENTED,
    )
