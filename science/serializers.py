# This file is kept for backward compatibility
# All serializers are now imported from their respective modules in the serializers/ package

from .serializers.science import (
    ScientificDirectionSerializer,
    DissertationSpecializationSerializer,
    DissertationSecretarySerializer,
    DissertationCouncilSerializer,
    DissertationCouncilDocumentsSerializer,
    DissertationCouncilAdminStaffSerializer,
    DissertationDefenseSerializer,
    ConferenceNoticeSerializer,
    VestnikSerializer,
    VestnikIssueSerializer,
)
from .serializers.nts_committee import (
    NTSCommitteeRoleSerializer,
    NTSResearchDirectionSerializer,
    NTSCommitteeMemberSerializer,
    NTSCommitteeSectionSerializer,
)
from .serializers.scopus import (
    ScopusAuthorSerializer,
    ScopusJournalSerializer,
    ScopusPublisherSerializer,
    ScopusPublicationAuthorSerializer,
    ScopusPublicationSerializer,
)
from .serializers.publication import PublicationSerializer
from .serializers.vestnik_stats import (
    PublicationStatsSerializer,
    VestnikArticleSerializer,
    VestnikStatsSerializer,
    PublicationsPageSerializer,
    VestnikPageSerializer,
)