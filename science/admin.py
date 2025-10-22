from django.contrib import admin
from .models import (
    NTSCommitteeRole,
    NTSResearchDirection,
    NTSCommitteeMember,
    NTSCommitteeSection,
    Publication,
    PublicationStats,
    VestnikIssue,
    VestnikArticle,
    VestnikStats,
    ScopusMetrics,
    ScopusDocumentType,
    ScopusPublication,
    ScopusStats,
    ScopusSection,
    ScopusAuthor,
    ScopusPublicationAuthor,
    ScopusJournal,
    ScopusPublisher,
    WebOfScienceTimeRange,
    WebOfScienceMetric,
    WebOfScienceCategory,
    WebOfScienceCollaboration,
    WebOfScienceJournalQuartile,
    WebOfScienceAdditionalMetric,
    WebOfScienceSection,
    StudentScientificSocietyInfo,
    StudentScientificSocietyStat,
    StudentScientificSocietyFeature,
    StudentScientificSocietyProject,
    StudentScientificSocietyProjectTag,
    StudentScientificSocietyEvent,
    StudentScientificSocietyJoinStep,
    StudentScientificSocietyLeader,
    StudentScientificSocietyContact,
)

admin.site.register(NTSCommitteeRole)
admin.site.register(NTSResearchDirection)
admin.site.register(NTSCommitteeMember)
admin.site.register(NTSCommitteeSection)
admin.site.register(Publication)
admin.site.register(PublicationStats)
admin.site.register(VestnikIssue)
admin.site.register(VestnikArticle)
admin.site.register(VestnikStats)
admin.site.register(ScopusMetrics)
admin.site.register(ScopusDocumentType)
admin.site.register(ScopusPublication)
admin.site.register(ScopusStats)
admin.site.register(ScopusJournal)
admin.site.register(ScopusPublisher)
admin.site.register(ScopusSection)
admin.site.register(ScopusAuthor)
admin.site.register(ScopusPublicationAuthor)

# Web of Science
admin.site.register(WebOfScienceTimeRange)
admin.site.register(WebOfScienceMetric)
admin.site.register(WebOfScienceCategory)
admin.site.register(WebOfScienceCollaboration)
admin.site.register(WebOfScienceJournalQuartile)
admin.site.register(WebOfScienceAdditionalMetric)
admin.site.register(WebOfScienceSection)

# Student Scientific Society
admin.site.register(StudentScientificSocietyInfo)
admin.site.register(StudentScientificSocietyStat)
admin.site.register(StudentScientificSocietyFeature)
admin.site.register(StudentScientificSocietyProject)
admin.site.register(StudentScientificSocietyProjectTag)
admin.site.register(StudentScientificSocietyEvent)
admin.site.register(StudentScientificSocietyJoinStep)
admin.site.register(StudentScientificSocietyLeader)
admin.site.register(StudentScientificSocietyContact)
