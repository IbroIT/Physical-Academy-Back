from .science import (
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
from .nts_committee import (
    NTSCommitteeRoleSerializer,
    NTSResearchDirectionSerializer,
    NTSCommitteeMemberSerializer,
    NTSCommitteeSectionSerializer,
)
from .scopus import (
    ScopusAuthorSerializer,
    ScopusJournalSerializer,
    ScopusPublisherSerializer,
    ScopusPublicationAuthorSerializer,
    ScopusPublicationSerializer,
)
from .scopus_extra import (
    ScopusMetricsSerializer,
    ScopusDocumentTypeSerializer,
    ScopusStatsSerializer,
    ScopusSectionSerializer,
)
from .publication import PublicationSerializer
from .vestnik_stats import (
    PublicationStatsSerializer,
    VestnikArticleSerializer,
    VestnikStatsSerializer,
    PublicationsPageSerializer,
    VestnikPageSerializer,
)
