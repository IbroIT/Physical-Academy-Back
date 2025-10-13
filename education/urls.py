from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MasterProgramsViewSet, FacultyViewSet

router = DefaultRouter()
router.register(r'master-programs', MasterProgramsViewSet, basename='master-programs')
router.register(r'faculties', FacultyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]