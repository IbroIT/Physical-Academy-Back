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
    StudentContactInfoViewSet,
    SocialNetworkAccountViewSet,
    SocialCommunityViewSet,
    ContactSocialPageDataViewSet,
)
from .views_ebilim import (
    EbilimStatViewSet,
    EbilimQuickLinkViewSet,
    EbilimSystemStatusViewSet,
    EbilimPageDataView,
    EbilimPageDataViewSet,
)
from .views_scholarship_visa import (
    ScholarshipProgramViewSet,
    ScholarshipRequiredDocumentViewSet,
    ScholarshipPageDataViewSet,
    VisaSupportServiceViewSet,
    VisaSupportContactViewSet,
    VisaSupportPageDataViewSet,
)
from .views_exchange import (
    ExchangeRegionViewSet,
    ExchangeDurationTypeViewSet,
    ExchangeProgramViewSet,
    ExchangeProgramRequirementViewSet,
    ExchangeProgramBenefitViewSet,
    ExchangeProgramCourseViewSet,
    ExchangePageStatViewSet,
    ExchangeDeadlineViewSet,
    ExchangePageDataViewSet,
)
from .views_instructions import (
    InstructionCategoryViewSet,
    InstructionDocumentViewSet,
    ImportantUpdateViewSet,
    InstructionsPageDataViewSet,
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

# Ebilim endpoints
router.register(r"ebilim", EbilimPageDataViewSet, basename="ebilim")
router.register(r"ebilim/stats", EbilimStatViewSet, basename="ebilim-stats")
router.register(
    r"ebilim/quick-links", EbilimQuickLinkViewSet, basename="ebilim-quick-links"
)
router.register(
    r"ebilim/system-status", EbilimSystemStatusViewSet, basename="ebilim-system-status"
)

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
    r"disabilities/resources", DisabilityResourceViewSet, basename="disability-resource"
)
router.register(
    r"disabilities/emergency",
    DisabilityEmergencyContactViewSet,
    basename="disability-emergency",
)
router.register(
    r"disabilities-page", DisabilitiesPageDataViewSet, basename="disabilities-page"
)
router.register(
    r"disabilities-pages", DisabilityPageViewSet, basename="disability-pages"
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

# Exchange programs endpoints
router.register(r"exchange/regions", ExchangeRegionViewSet, basename="exchange-region")
router.register(
    r"exchange/durations", ExchangeDurationTypeViewSet, basename="exchange-duration"
)
router.register(
    r"exchange/programs", ExchangeProgramViewSet, basename="exchange-program"
)
router.register(
    r"exchange/requirements",
    ExchangeProgramRequirementViewSet,
    basename="exchange-requirement",
)
router.register(
    r"exchange/benefits", ExchangeProgramBenefitViewSet, basename="exchange-benefit"
)
router.register(
    r"exchange/courses", ExchangeProgramCourseViewSet, basename="exchange-course"
)
router.register(r"exchange/stats", ExchangePageStatViewSet, basename="exchange-stat")
router.register(
    r"exchange/deadlines", ExchangeDeadlineViewSet, basename="exchange-deadline"
)
router.register(r"exchange-page", ExchangePageDataViewSet, basename="exchange-page")

# Instructions endpoints
router.register(
    r"instructions/categories",
    InstructionCategoryViewSet,
    basename="instruction-category",
)
router.register(
    r"instructions/documents",
    InstructionDocumentViewSet,
    basename="instruction-document",
)
router.register(
    r"instructions/updates", ImportantUpdateViewSet, basename="instruction-update"
)
router.register(
    r"instructions-page", InstructionsPageDataViewSet, basename="instructions-page"
)

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
    path("ebilim/", EbilimPageDataView.as_view(), name="ebilim-page-data"),
]
