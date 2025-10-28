from django.urls import path
from .views import (
    SportSectionListAPIView,
    SportSectionDetailAPIView,
    AchievementListAPIView,
    AchievementDetailAPIView,
    InfrastructureAPIView,
    SportStatisticsAPIView,
)

app_name = "sports"

urlpatterns = [
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
]
