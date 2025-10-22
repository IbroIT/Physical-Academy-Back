from django.contrib import admin
from .models_scholarship_visa import (
    ScholarshipProgram,
    ScholarshipRequiredDocument,
    VisaSupportService,
    VisaSupportContact,
)
from .models_disabilities import (
    DisabilitySupportService,
    DisabilityContactPerson,
    DisabilityResource,
    DisabilityEmergencyContact,
    DisabilityPage
)
from .models_council import CouncilMember, CouncilInitiative, CouncilEvent, CouncilStats

admin.site.register(ScholarshipProgram)
admin.site.register(ScholarshipRequiredDocument)
admin.site.register(VisaSupportService)
admin.site.register(VisaSupportContact)
admin.site.register(DisabilitySupportService)
admin.site.register(DisabilityContactPerson)
admin.site.register(DisabilityResource)
admin.site.register(DisabilityEmergencyContact)
admin.site.register(DisabilityPage)
admin.site.register(CouncilMember)
admin.site.register(CouncilInitiative)
admin.site.register(CouncilEvent)
admin.site.register(CouncilStats)
