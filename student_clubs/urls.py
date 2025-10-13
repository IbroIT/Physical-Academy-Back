from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClubViewSet,
    ClubCategoryViewSet,
    ClubLeaderViewSet,
    ClubStatsViewSet,
    StudentProfileViewSet,
    ClubMembershipViewSet,
    DisabilitySupportServiceViewSet,
    DisabilityContactPersonViewSet,
    DisabilityResourceViewSet,
    DisabilityEmergencyContactViewSet,
    DisabilitiesPageDataViewSet,
    DisabilityPageViewSet,
    CouncilMemberViewSet,
    CouncilInitiativeViewSet,
    CouncilEventViewSet,
    CouncilStatsViewSet,
    CouncilPageDataViewSet,
    ScholarshipProgramViewSet,
    ScholarshipRequiredDocumentViewSet,
    ScholarshipPageDataViewSet,
    VisaSupportServiceViewSet,
    VisaSupportContactViewSet,
    VisaSupportPageDataViewSet,
    StudentContactInfoViewSet,
    SocialNetworkAccountViewSet,
    SocialCommunityViewSet,
    ContactSocialPageDataViewSet,
)

router = DefaultRouter()
# Основные эндпоинты для клубов
router.register(r"clubs", ClubViewSet, basename="club")
router.register(r"categories", ClubCategoryViewSet, basename="club-category")
router.register(r"leaders", ClubLeaderViewSet, basename="club-leader")
router.register(r"stats", ClubStatsViewSet, basename="club-stats")

# Новые эндпоинты для студентов
router.register(r"students", StudentProfileViewSet, basename="student-profile")
router.register(r"memberships", ClubMembershipViewSet, basename="club-membership")

# Disabilities endpoints
router.register(
    r"disabilities/services",
    DisabilitySupportServiceViewSet,
    basename="disability-service",
)
router.register(
    r"disabilities/contacts",
    DisabilityContactPersonViewSet,
    basename="disability-contact",
)
router.register(
    r"disabilities/resources",
    DisabilityResourceViewSet,
    basename="disability-resource",
)
router.register(
    r"disabilities/emergency",
    DisabilityEmergencyContactViewSet,
    basename="disability-emergency",
)
router.register(
    r"disabilities-page",
    DisabilitiesPageDataViewSet,
    basename="disabilities-page",
)
router.register(
    r"disabilities-pages",
    DisabilityPageViewSet,
    basename="disability-pages",
)

# Council endpoints
router.register(r"council/members", CouncilMemberViewSet, basename="council-member")
router.register(
    r"council/initiatives", CouncilInitiativeViewSet, basename="council-initiative"
)
router.register(r"council/events", CouncilEventViewSet, basename="council-event")
router.register(r"council/stats", CouncilStatsViewSet, basename="council-stats")
router.register(r"council-page", CouncilPageDataViewSet, basename="council-page")

# Scholarship endpoints
router.register(
    r"scholarship/programs", ScholarshipProgramViewSet, basename="scholarship-program"
)
router.register(
    r"scholarship/documents",
    ScholarshipRequiredDocumentViewSet,
    basename="scholarship-document",
)
router.register(
    r"scholarship-page", ScholarshipPageDataViewSet, basename="scholarship-page"
)

# Visa support endpoints
router.register(r"visa/services", VisaSupportServiceViewSet, basename="visa-service")
router.register(r"visa/contacts", VisaSupportContactViewSet, basename="visa-contact")
router.register(r"visa-page", VisaSupportPageDataViewSet, basename="visa-page")

# Contact and social endpoints
router.register(
    r"contact-info", StudentContactInfoViewSet, basename="student-contact-info"
)
router.register(
    r"social-accounts", SocialNetworkAccountViewSet, basename="social-network-account"
)
router.register(
    r"social-communities", SocialCommunityViewSet, basename="social-community"
)
router.register(
    r"contact-social-page", ContactSocialPageDataViewSet, basename="contact-social-page"
)

urlpatterns = [
    path("", include(router.urls)),
]
