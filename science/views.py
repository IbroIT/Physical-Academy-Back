# This file is kept for backward compatibility
# All views are now imported from their respective modules in the views/ package

from .views.publication import (
    PublicationsViewSet,
    PublicationStatsViewSet,
    PublicationsPageView,
)
from .views.vestnik import (
    VestnikIssuesViewSet,
    VestnikArticlesViewSet,
    VestnikStatsViewSet,
    VestnikPageView,
)
from .views.nts_committee import (
    NTSCommitteeRoleViewSet,
    NTSResearchDirectionViewSet,
    NTSCommitteeMemberViewSet,
    NTSCommitteePageView,
)
from .views.scopus import (
    ScopusMetricsViewSet,
    ScopusDocumentTypeViewSet,
    ScopusPublicationViewSet,
    ScopusStatsViewSet,
    ScopusPageView,
)