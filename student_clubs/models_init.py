"""
This module initializer helps to properly load the student models
and integrate them with the existing models.

Usage:
    from student_clubs.models import Club, ClubCategory  # Base models
    from student_clubs.models_students import StudentProfile, ClubMembership  # Student models
"""

# Import main models first
from .models import Club, ClubCategory, ClubLeader, ClubStats

# Import student models when available
try:
    from .models_students import StudentProfile, ClubMembership

    __all__ = [
        "Club",
        "ClubCategory",
        "ClubLeader",
        "ClubStats",
        "StudentProfile",
        "ClubMembership",
    ]
except ImportError:
    __all__ = ["Club", "ClubCategory", "ClubLeader", "ClubStats"]
