from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .views import (
    SportSectionListAPIView,
    SportSectionDetailAPIView,
    AchievementListAPIView,
    AchievementDetailAPIView,
    InfrastructureAPIView,
    SportStatisticsAPIView,
    SportTypeListAPIView,
)

app_name = "sports"


@api_view(["GET"])
def api_root(request, format=None):
    base = request.build_absolute_uri(request.path)
    # Ensure base ends with '/'
    if not base.endswith("/"):
        base += "/"
    return Response(
        {
            "sections": base + "sections/",
            "achievements": base + "achievements/",
            "infrastructure": base + "infrastructure/",
            "statistics": base + "statistics/",
            "types": base + "types/",
        }
    )


urlpatterns = [
    path("", api_root, name="sports-root"),
    # Sport Sections
    path("sections/", SportSectionListAPIView.as_view(), name="section-list"),
    path(
        "sections/<int:id>/", SportSectionDetailAPIView.as_view(), name="section-detail"
    ),
    # Achievements
    path("achievements/", AchievementListAPIView.as_view(), name="achievement-list"),
    path(
        "achievements/<int:id>/",
        AchievementDetailAPIView.as_view(),
        name="achievement-detail",
    ),
    # Infrastructure
    path("infrastructure/", InfrastructureAPIView.as_view(), name="infrastructure"),
    # Statistics
    path("statistics/", SportStatisticsAPIView.as_view(), name="statistics"),
    # Sport types (catalog)
    path("types/", SportTypeListAPIView.as_view(), name="types-list"),
]
