from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User

# Import models from sub-directories
from .models_instructions import (
    InstructionCategory,
    InstructionDocument,
    ImportantUpdate,
)

# COMMENTED OUT: Ebilim models not needed - using i18n translations on frontend
# from .models_ebilim import (
#     EbilimStat,
#     EbilimQuickLink,
#     EbilimSystemStatus,
# )
from .models_disabilities import (
    DisabilitySupportService,
    DisabilityContactPerson,
    DisabilityResource,
    DisabilityEmergencyContact,
)

# from .models_disability_page import DisabilityPage

from .models_council import CouncilMember, CouncilInitiative, CouncilEvent, CouncilStats

from .models_scholarship_visa import (
    ScholarshipProgram,
    ScholarshipRequiredDocument,
    VisaSupportService,
    VisaSupportContact,
)

from .models_exchange import (
    ExchangeRegion,
    ExchangeDurationType,
    ExchangeProgram,
    ExchangeProgramRequirement,
    ExchangeProgramBenefit,
    ExchangeProgramCourse,
    ExchangePageStat,
    ExchangeDeadline,
)

# Import models from the models directory
from .models.contact_social import (
    StudentContactInfo,
    SocialNetworkAccount,
    SocialCommunity,
)

# Import models from the models/clubs.py
from .models.clubs import Club, ClubCategory, ClubLeader, ClubStats

# Import models from the models/students.py
from .models.students import StudentProfile, ClubMembership


# ClubCategory model moved to models/clubs.py


# Club model moved to models/clubs.py


# ClubLeader model moved to models/clubs.py


# ClubStats model moved to models/clubs.py


# StudentProfile model moved to models/students.py


# ClubMembership model moved to models/students.py
