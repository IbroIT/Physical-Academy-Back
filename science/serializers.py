# This file is deprecated and kept only for backward compatibility
# All serializers are now in serializers_main.py

# Import from serializers_main for backward compatibility
from .serializers_main import (
    # Publication serializers
    PublicationSerializer,
    PublicationStatsSerializer,
    PublicationsPageSerializer,
    # Vestnik serializers
    VestnikSerializer,
    VestnikIssueSerializer,
    VestnikArticleSerializer,
    VestnikStatsSerializer,
    VestnikPageSerializer,
)

# Import from old files (will be removed after full migration)

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

__all__ = [
    # Publication serializers
    "PublicationSerializer",
    "PublicationStatsSerializer",
    "PublicationsPageSerializer",
    # Vestnik serializers
    "VestnikSerializer",
    "VestnikIssueSerializer",
    "VestnikArticleSerializer",
    "VestnikStatsSerializer",
    "VestnikPageSerializer",
    # Science serializers (from old files)
    "ScientificDirectionSerializer",
    "DissertationSpecializationSerializer",
    "DissertationSecretarySerializer",
    "DissertationCouncilSerializer",
    "DissertationCouncilDocumentsSerializer",
    "DissertationCouncilAdminStaffSerializer",
    "DissertationDefenseSerializer",
    "ConferenceNoticeSerializer",
    # NTS Committee serializers
    "NTSCommitteeRoleSerializer",
    "NTSResearchDirectionSerializer",
    "NTSCommitteeMemberSerializer",
    "NTSCommitteeSectionSerializer",
    # Scopus serializers
    "ScopusAuthorSerializer",
    "ScopusJournalSerializer",
    "ScopusPublisherSerializer",
    "ScopusPublicationAuthorSerializer",
    "ScopusPublicationSerializer",
]


# ==================== OLD CODE REMOVED ====================
# All serializers moved to serializers_main.py
