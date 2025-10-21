# Import all views to make them available
from .contact_social import *
from .clubs import (
    BaseLanguageViewSet,
    ClubCategoryViewSet,
    ClubViewSet,
    ClubLeaderViewSet,
    ClubStatsViewSet,
    StudentProfileViewSet,
    ClubMembershipViewSet,
)
from .disabilities import (
    DisabilitySupportServiceViewSet,
    DisabilityContactPersonViewSet,
    DisabilityResourceViewSet,
    DisabilityEmergencyContactViewSet,
    DisabilitiesPageDataViewSet,
)
from .disability_page import DisabilityPageViewSet
from .council import (
    CouncilMemberViewSet,
    CouncilInitiativeViewSet,
    CouncilEventViewSet,
    CouncilStatsViewSet,
    CouncilPageDataViewSet,
)
from .scholarship_visa import (
    ScholarshipProgramViewSet,
    ScholarshipRequiredDocumentViewSet,
    ScholarshipPageDataViewSet,
    VisaSupportServiceViewSet,
    VisaSupportContactViewSet,
    VisaSupportPageDataViewSet,
)
