# This file is deprecated. All council views have been moved to views/council.py
# Please use the implementation in views/council.py instead

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models_council import CouncilMember, CouncilInitiative, CouncilEvent, CouncilStats
from .serializers_council import (
    CouncilMemberSerializer,
    CouncilInitiativeSerializer,
    CouncilEventSerializer,
    CouncilStatsSerializer,
)


class CouncilMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for student council members"""

    queryset = CouncilMember.objects.all().order_by("order", "role", "name_ru")
    serializer_class = CouncilMemberSerializer

    def get_serializer_context(self):
        """Add language to serializer context based on query parameter"""
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context


class CouncilInitiativeViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for student council initiatives"""

    queryset = CouncilInitiative.objects.all().order_by("order", "status", "start_date")
    serializer_class = CouncilInitiativeSerializer

    def get_serializer_context(self):
        """Add language to serializer context based on query parameter"""
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context


class CouncilEventViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for student council events"""

    queryset = CouncilEvent.objects.all().order_by("order", "status", "date")
    serializer_class = CouncilEventSerializer

    def get_serializer_context(self):
        """Add language to serializer context based on query parameter"""
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context


class CouncilStatsViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoints for student council statistics"""

    queryset = CouncilStats.objects.all().order_by("order")
    serializer_class = CouncilStatsSerializer

    def get_serializer_context(self):
        """Add language to serializer context based on query parameter"""
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"
        context["language"] = lang
        return context


class CouncilPageDataViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """API endpoint to get all council page data in a single request"""

    def list(self, request):
        lang = request.query_params.get("lang", "ru")
        # Validate language
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"

        # Get all needed data
        members = CouncilMember.objects.all().order_by("order", "role", "name_ru")
        initiatives = CouncilInitiative.objects.all().order_by(
            "order", "status", "start_date"
        )
        events = CouncilEvent.objects.all().order_by("order", "status", "date")
        stats = CouncilStats.objects.all().order_by("order")

        # Prepare context with language
        context = {"language": lang}

        # Serialize each component
        members_serializer = CouncilMemberSerializer(
            members, many=True, context=context
        )
        initiatives_serializer = CouncilInitiativeSerializer(
            initiatives, many=True, context=context
        )
        events_serializer = CouncilEventSerializer(events, many=True, context=context)
        stats_serializer = CouncilStatsSerializer(stats, many=True, context=context)

        # Combine data
        data = {
            "members": members_serializer.data,
            "initiatives": initiatives_serializer.data,
            "events": events_serializer.data,
            "stats": stats_serializer.data,
        }

        return Response(data)
