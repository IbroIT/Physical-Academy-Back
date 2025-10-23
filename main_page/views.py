from django.shortcuts import render
from rest_framework import viewsets
from .models import (
    AcademyInfrastructure,
    Mission,
    aboutStatistics,
    AboutPhotos,
    HistoryStep,
    ImportantDates,
    Accreditation,
    AcademyAchievements,
    AcademyStatistics,
)

from .serializers import (
    AboutPhotosSerializer,
    AboutStatisticsSerializer,
    HistoryStepSerializer,
    ImportantDatesSerializer,
    MissionSerializer,
    AccreditationSerializer,
    AcademyAchievementsSerializer,
    AcademyStatisticsSerializer,
    AcademyInfrastructureSerializer,
)

# Create your views here.


class AboutStatisticsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = aboutStatistics.objects.all()
    serializer_class = AboutStatisticsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class AboutPhotosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutPhotos.objects.all()
    serializer_class = AboutPhotosSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class HistoryStepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HistoryStep.objects.all().order_by("year")
    serializer_class = HistoryStepSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class ImportantDatesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ImportantDates.objects.all().order_by("year")
    serializer_class = ImportantDatesSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class MissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class AccreditationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Accreditation.objects.all()
    serializer_class = AccreditationSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class AcademyStatisticsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AcademyStatistics.objects.all()
    serializer_class = AcademyStatisticsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class AcademyAchievementsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AcademyAchievements.objects.all()
    serializer_class = AcademyAchievementsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class AcademyInfrastructureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AcademyInfrastructure.objects.all()
    serializer_class = AcademyInfrastructureSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context
