from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SportSectionViewSet,
    AchievementViewSet,
    InfrastructureViewSet,
    SportStatisticsAPIView,
)

app_name = "sports"

# Создаем роутер для ViewSets
router = DefaultRouter()
router.register(r"sections", SportSectionViewSet, basename="section")
router.register(r"achievements", AchievementViewSet, basename="achievement")
router.register(r"infrastructure", InfrastructureViewSet, basename="infrastructure")

urlpatterns = [
    # ViewSet URLs
    path("", include(router.urls)),
    # Statistics
    path("statistics/", SportStatisticsAPIView.as_view(), name="statistics"),
]
