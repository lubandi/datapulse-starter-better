"""Reports router - STUB: All endpoints need implementation."""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_dataset_report(request, dataset_id):
    """Get a full quality report for a dataset.

    TODO: Implement using report_service.generate_report().

    Steps:
    1. Fetch dataset by ID (404 if not found)
    2. Fetch latest QualityScore for this dataset
    3. Fetch all CheckResults from latest check run
    4. Compose QualityReport with dataset info, score, results
    5. Return the report
    """
    return Response(
        {"detail": "GET /api/reports/{id} not implemented"},
        status=status.HTTP_501_NOT_IMPLEMENTED,
    )


@api_view(["GET"])
def get_quality_trends(request):
    """Get quality score trends over time.

    TODO: Implement using report_service.get_trend_data().

    Steps:
    1. Calculate start_date = now - days
    2. Query QualityScore after start_date
    3. Order by checked_at ascending
    4. Return scores showing quality trends
    """
    return Response(
        {"detail": "GET /api/reports/trends not implemented"},
        status=status.HTTP_501_NOT_IMPLEMENTED,
    )
