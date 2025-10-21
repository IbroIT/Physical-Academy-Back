# This file is kept for backward compatibility
# All serializers are now imported from their respective modules in the serializers/ package

from .serializers.clubs import (
    ClubCategorySerializer,
    ClubLeaderSerializer,
    ClubListSerializer,
    ClubDetailSerializer,
    ClubStatsSerializer,
)

from .serializers.students import (
    StudentProfileSerializer,
    StudentProfileCreateSerializer,
    StudentProfileListSerializer,
    ClubMembershipSerializer,
    ClubMembershipCreateSerializer,
    StudentClubsSerializer,
)

# Other serializers
from rest_framework import serializers
from .serializers.clubs import (
    ClubStatsSerializer,
    ClubListSerializer,
    ClubCategorySerializer,
)


# ClubPageSerializer and other composite serializers
class ClubPageSerializer(serializers.Serializer):
    """Сериализатор для всей страницы клубов с заголовками и статистикой"""

    title = serializers.CharField()
    subtitle = serializers.CharField()
    stats = ClubStatsSerializer(many=True)
    categories = ClubCategorySerializer(many=True)
    clubs = ClubListSerializer(many=True)
