from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClubViewSet, ClubCategoryViewSet, ClubLeaderViewSet, ClubStatsViewSet

router = DefaultRouter()
router.register(r'clubs', ClubViewSet, basename='club')
router.register(r'categories', ClubCategoryViewSet, basename='club-category')
router.register(r'leaders', ClubLeaderViewSet, basename='club-leader')
router.register(r'stats', ClubStatsViewSet, basename='club-stats')

urlpatterns = [
    path('', include(router.urls)),
]
