from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutStatisticsViewSet, AboutPhotosViewSet, AcademyInfrastructureViewSet, HistoryStepViewSet, ImportantDatesViewSet, MissionViewSet, AccreditationViewSet, AcademyAchievementsViewSet, AcademyStatisticsViewSet

router = DefaultRouter()
router.register(r'about-statistics', AboutStatisticsViewSet)
router.register(r'about-photos', AboutPhotosViewSet)
router.register(r'history-steps', HistoryStepViewSet)
router.register(r'important-dates', ImportantDatesViewSet)
router.register(r'missions', MissionViewSet)
router.register(r'accreditations', AccreditationViewSet)
router.register(r'achievements', AcademyAchievementsViewSet)
router.register(r'statistics', AcademyStatisticsViewSet)
router.register(r'infrastructure', AcademyInfrastructureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
