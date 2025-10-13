from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PublicationsViewSet,
    PublicationStatsViewSet,
    PublicationsPageView,
    VestnikIssuesViewSet,
    VestnikArticlesViewSet,
    VestnikStatsViewSet,
    VestnikPageView,
    ScopusMetricsViewSet,
    ScopusDocumentTypeViewSet,
    ScopusPublicationViewSet,
    ScopusStatsViewSet,
    ScopusPageView,
    NTSCommitteeRoleViewSet,
    NTSResearchDirectionViewSet,
    NTSCommitteeMemberViewSet,
    NTSCommitteePageView,
)

# Create router and register viewsets
router = DefaultRouter()
router.register(r"publications", PublicationsViewSet)
router.register(r"publication-stats", PublicationStatsViewSet)
router.register(r"vestnik-issues", VestnikIssuesViewSet)
router.register(r"vestnik-articles", VestnikArticlesViewSet)
router.register(r"vestnik-stats", VestnikStatsViewSet)
# Scopus API endpoints
router.register(r"scopus-metrics", ScopusMetricsViewSet)
router.register(r"scopus-document-types", ScopusDocumentTypeViewSet)
router.register(r"scopus-publications", ScopusPublicationViewSet)
router.register(r"scopus-stats", ScopusStatsViewSet)
# NTS Committee API endpoints
router.register(r"nts-committee-roles", NTSCommitteeRoleViewSet)
router.register(r"nts-research-directions", NTSResearchDirectionViewSet)
router.register(r"nts-committee-members", NTSCommitteeMemberViewSet)

urlpatterns = [
    # ViewSet routes
    path("", include(router.urls)),
    # Additional views
    path(
        "publications-page/", PublicationsPageView.as_view(), name="publications-page"
    ),
    path("vestnik-page/", VestnikPageView.as_view(), name="vestnik-page"),
    # Scopus page view
    path("scopus-page/", ScopusPageView.as_view(), name="scopus-page"),
    # NTS Committee page view
    path(
        "nts-committee-page/", NTSCommitteePageView.as_view(), name="nts-committee-page"
    ),
]