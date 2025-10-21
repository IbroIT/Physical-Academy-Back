# This file is kept for backward compatibility
# All views are now imported from their respective modules in the views/ package

from .views.clubs import (
    BaseLanguageViewSet,
    ClubCategoryViewSet,
    ClubViewSet,
    ClubLeaderViewSet,
    ClubStatsViewSet,
    StudentProfileViewSet,
    ClubMembershipViewSet,
)
from .views.disabilities import (
    DisabilitySupportServiceViewSet,
    DisabilityContactPersonViewSet,
    DisabilityResourceViewSet,
    DisabilityEmergencyContactViewSet,
    DisabilitiesPageDataViewSet,
)
from .views.disability_page import DisabilityPageViewSet
from .views.council import (
    CouncilMemberViewSet,
    CouncilInitiativeViewSet,
    CouncilEventViewSet,
    CouncilStatsViewSet,
    CouncilPageDataViewSet,
)
from .views.scholarship_visa import (
    ScholarshipProgramViewSet,
    ScholarshipRequiredDocumentViewSet,
    ScholarshipPageDataViewSet,
    VisaSupportServiceViewSet,
    VisaSupportContactViewSet,
    VisaSupportPageDataViewSet,
)
from .views.contact_social import (
    StudentContactInfoViewSet,
    SocialNetworkAccountViewSet,
    SocialCommunityViewSet,
    ContactSocialPageDataViewSet,
)
