from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BoardOfTrusteesViewSet, BoardOfTrusteesStatsViewSet,
    AuditCommissionViewSet, AuditCommissionStatisticsViewSet,
    AcademicCouncilViewSet,
    TradeUnionBenefitViewSet, TradeUnionEventViewSet, TradeUnionStatsViewSet,
    CommissionViewSet,
    AdministrativeDepartmentViewSet, AdministrativeUnitViewSet,
    LeadershipViewSet, OrganizationStructureViewSet, DocumentViewSet
)

router = DefaultRouter()

# Board of Trustees
router.register(r'board-of-trustees', BoardOfTrusteesViewSet, basename='board-of-trustees')
router.register(r'board-of-trustees-stats', BoardOfTrusteesStatsViewSet, basename='board-of-trustees-stats')

# Audit Commission
router.register(r'audit-commission', AuditCommissionViewSet, basename='audit-commission')
router.register(r'audit-commission-statistics', AuditCommissionStatisticsViewSet, basename='audit-commission-statistics')

# Academic Council
router.register(r'academic-council', AcademicCouncilViewSet, basename='academic-council')

# Trade Union
router.register(r'trade-union/benefits', TradeUnionBenefitViewSet, basename='trade-union-benefits')
router.register(r'trade-union/events', TradeUnionEventViewSet, basename='trade-union-events')
router.register(r'trade-union/stats', TradeUnionStatsViewSet, basename='trade-union-stats')

# Commissions
router.register(r'commissions', CommissionViewSet, basename='commissions')

# Administrative Structure
router.register(r'administrative/departments', AdministrativeDepartmentViewSet, basename='administrative-departments')
router.register(r'administrative/units', AdministrativeUnitViewSet, basename='administrative-units')

# New APIs for missing endpoints
router.register(r'leadership', LeadershipViewSet, basename='leadership')
router.register(r'organization-structure', OrganizationStructureViewSet, basename='organization-structure')
router.register(r'documents', DocumentViewSet, basename='documents')

urlpatterns = [
    path('', include(router.urls)),
]
