from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CollegeAdmissionRequirementsViewSet, CollegeAdmissionStepsViewSet, CollegeProgramsViewSet, CollegeSoonEventsViewSet, CollegeStatisticsViewSet, DoctorAdmissionStepsViewSet, DoctorSoonEventsViewSet, DoctorStatisticsViewSet, QuotaTypeViewSet, QuotaStatsViewSet, AdditionalSupportViewSet,
    ProcessStepViewSet, BachelorQuotasViewSet, MasterDocumentsViewSet, 
    MasterProgramsViewSet, MasterMainDateViewSet, MasterRequirementsViewSet,
    AspirantDocumentsViewSet, AspirantProgramsViewSet, AspirantMainDateViewSet, AspirantRequirementsViewSet, DoctorAdmissionStepsViewSet, DoctorStatisticsViewSet,
    DoctorProgramsViewSet
)

# Создаем роутер для API
router = DefaultRouter()
router.register(r'quota-types', QuotaTypeViewSet, basename='quota-types')
router.register(r'quota-stats', QuotaStatsViewSet, basename='quota-stats')
router.register(r'additional-support', AdditionalSupportViewSet, basename='additional-support')
router.register(r'process-steps', ProcessStepViewSet, basename='process-steps')
router.register(r'bachelor-quotas', BachelorQuotasViewSet, basename='bachelor-quotas')

router.register(r'master-documents', MasterDocumentsViewSet, basename='master-documents')
router.register(r'master-programs', MasterProgramsViewSet, basename='master-programs')
router.register(r'master-main-dates', MasterMainDateViewSet, basename='master-main-dates')
router.register(r'master-requirements', MasterRequirementsViewSet, basename='master-requirements')
router.register(r'aspirant-documents', AspirantDocumentsViewSet, basename='aspirant-documents')
router.register(r'aspirant-programs', AspirantProgramsViewSet, basename='aspirant-programs')
router.register(r'aspirant-main-dates', AspirantMainDateViewSet, basename='aspirant-main-dates')
router.register(r'aspirant-requirements', AspirantRequirementsViewSet, basename='aspirant-requirements')
router.register(r'doctor-soon-events', DoctorSoonEventsViewSet, basename='doctor-soon-events')
router.register(r'doctor-admission-steps', DoctorAdmissionStepsViewSet, basename='doctor-admission-steps')
router.register(r'doctor-statistics', DoctorStatisticsViewSet, basename='doctor-statistics')
router.register(r'college-soon-events', CollegeSoonEventsViewSet, basename='college-soon-events')
router.register(r'college-admission-steps', CollegeAdmissionStepsViewSet, basename='college-admission-steps')
router.register(r'college-admission-requirements', CollegeAdmissionRequirementsViewSet, basename='college-admission-requirements')
router.register(r'college-statistics', CollegeStatisticsViewSet, basename='college-statistics')

doctor_programs_list = DoctorProgramsViewSet.as_view({'get': 'list'})
college_programs_list = CollegeProgramsViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('', include(router.urls)),
    path('doctor-programs/', doctor_programs_list, name='doctor-programs'),
    path('college-programs/', college_programs_list, name='college-programs'),
]