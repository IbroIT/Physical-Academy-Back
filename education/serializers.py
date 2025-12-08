from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import (
    MasterProgramsSerializer,
    FacultySerializer,
    CollegeProgramsSerializer,
    PhdProgramsSerializer,
    FacultyNamesSerializer,
    FacultyPublicPageSerializer,
)
from .models import MasterPrograms, Faculty, CollegePrograms, PhdPrograms


class FacultyNamesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultyNamesSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


# Create your views here.
class MasterProgramsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MasterPrograms.objects.all()
    serializer_class = MasterProgramsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class PhdProgramsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PhdPrograms.objects.all()
    serializer_class = MasterProgramsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class CollegeProgramsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CollegePrograms.objects.all()
    serializer_class = MasterProgramsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class FacultyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    # Use slug for lookup so router resolves URLs like /faculties/<slug>/
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


# Universal Faculty Public Page View
class FacultyPublicPageAPIView(APIView):
    """
    Universal API view for faculty public pages.
    Supports language selection via ?lang=ru|en|kg parameter.
    """

    def get(self, request, slug):
        """
        Retrieve faculty page by slug with localization.

        URL: /api/education/faculties/<slug>/
        Query params: ?lang=ru (default: ru, options: ru|en|kg)
        """
        # Get language from query params (default: ru)
        lang = request.query_params.get("lang", "ru")
        if lang not in ["ru", "en", "kg"]:
            lang = "ru"

        # Fetch faculty by slug
        faculty = get_object_or_404(
            Faculty.objects.prefetch_related("public_sections__items"),
            slug=slug,
            is_active=True,
        )

        # Serialize with language context
        serializer = FacultyPublicPageSerializer(faculty, context={"language": lang})

        return Response(serializer.data, status=status.HTTP_200_OK)