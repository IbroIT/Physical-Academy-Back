from rest_framework import viewsets, generics
from rest_framework.response import Response

from ..models import (
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
from ..serializers import (
    StudentScientificSocietyInfoSerializer,
    StudentScientificSocietyStatSerializer,
    StudentScientificSocietyFeatureSerializer,
    StudentScientificSocietyProjectSerializer,
    ProjectTagSerializer,
    StudentScientificSocietyEventSerializer,
    StudentScientificSocietyJoinStepSerializer,
    StudentScientificSocietyLeaderSerializer,
    StudentScientificSocietyContactSerializer,
    StudentScientificSocietyPageSerializer,
)


class StudentScientificSocietyInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Student Scientific Society basic information."""

    queryset = StudentScientificSocietyInfo.objects.all()
    serializer_class = StudentScientificSocietyInfoSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class StudentScientificSocietyStatViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Student Scientific Society statistics."""

    queryset = StudentScientificSocietyStat.objects.all().order_by("order")
    serializer_class = StudentScientificSocietyStatSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class StudentScientificSocietyFeatureViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Student Scientific Society features."""

    queryset = StudentScientificSocietyFeature.objects.all().order_by("order")
    serializer_class = StudentScientificSocietyFeatureSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class StudentScientificSocietyProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Student Scientific Society projects."""

    queryset = StudentScientificSocietyProject.objects.all().order_by("order")
    serializer_class = StudentScientificSocietyProjectSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class StudentScientificSocietyEventViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Student Scientific Society events."""

    queryset = StudentScientificSocietyEvent.objects.all().order_by("date", "order")
    serializer_class = StudentScientificSocietyEventSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get("status", None)

        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class StudentScientificSocietyJoinStepViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Student Scientific Society join steps."""

    queryset = StudentScientificSocietyJoinStep.objects.all().order_by("order", "step")
    serializer_class = StudentScientificSocietyJoinStepSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class StudentScientificSocietyLeaderViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Student Scientific Society leadership."""

    queryset = StudentScientificSocietyLeader.objects.all().order_by("order")
    serializer_class = StudentScientificSocietyLeaderSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class StudentScientificSocietyContactViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Student Scientific Society contacts."""

    queryset = StudentScientificSocietyContact.objects.all().order_by("order")
    serializer_class = StudentScientificSocietyContactSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class StudentScientificSocietyPageView(generics.RetrieveAPIView):
    """API endpoint for the complete Student Scientific Society page."""

    serializer_class = StudentScientificSocietyPageSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context

    def get_object(self):
        # Get or create the info object (should only be one)
        info, _ = StudentScientificSocietyInfo.objects.get_or_create(pk=1)

        # Get stats
        stats = StudentScientificSocietyStat.objects.all().order_by("order")

        # Get features
        about_features = StudentScientificSocietyFeature.objects.all().order_by("order")

        # Get projects
        projects = StudentScientificSocietyProject.objects.all().order_by("order")

        # Get all events
        events = StudentScientificSocietyEvent.objects.all().order_by("date", "order")

        # Get upcoming events
        upcoming_events = StudentScientificSocietyEvent.objects.filter(
            status=StudentScientificSocietyEvent.UPCOMING
        ).order_by("date", "order")

        # Get join steps
        join_steps = StudentScientificSocietyJoinStep.objects.all().order_by(
            "order", "step"
        )

        # Get leadership
        leadership = StudentScientificSocietyLeader.objects.all().order_by("order")

        # Get contacts
        contacts = StudentScientificSocietyContact.objects.all().order_by("order")

        # Construct and return page data
        return {
            "info": info,
            "stats": stats,
            "about_features": about_features,
            "projects": projects,
            "events": events,
            "upcoming_events": upcoming_events,
            "join_steps": join_steps,
            "leadership": leadership,
            "contacts": contacts,
        }
