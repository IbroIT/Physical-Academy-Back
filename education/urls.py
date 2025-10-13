from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MasterProgramsViewSet, FacultyViewSet, PhdProgramsViewSet, CollegeProgramsViewSet

router = DefaultRouter()
router.register(r'master-programs', MasterProgramsViewSet, basename='master-programs')
router.register(r'faculties', FacultyViewSet)
router.register(r'phd-programs', PhdProgramsViewSet, basename='phd-programs')
router.register(r'college-programs', CollegeProgramsViewSet, basename='college-programs')

urlpatterns = [
    path('', include(router.urls)),
]