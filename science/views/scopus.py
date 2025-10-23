from rest_framework import viewsets, generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from ..models import (
    ScopusMetrics,
    ScopusDocumentType,
    ScopusPublication,
    ScopusStats,
    ScopusSection,
    ScopusAuthor,
    ScopusJournal,
    ScopusPublisher,
    ScopusPublicationAuthor,
)
from ..serializers import (
    ScopusMetricsSerializer,
    ScopusDocumentTypeSerializer,
    ScopusPublicationSerializer,
    ScopusStatsSerializer,
    ScopusSectionSerializer,
    ScopusAuthorSerializer,
    ScopusJournalSerializer,
    ScopusPublisherSerializer,
    ScopusPublicationAuthorSerializer,
)


class ScopusMetricsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for retrieving Scopus metrics"""

    queryset = ScopusMetrics.objects.all()
    serializer_class = ScopusMetricsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class ScopusDocumentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for retrieving Scopus document types"""

    queryset = ScopusDocumentType.objects.all()
    serializer_class = ScopusDocumentTypeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class ScopusPublicationViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Scopus publications (list/retrieve/create/update/delete)"""

    # Order by existing fields on ScopusPublication. "order" and
    # "citation_count" are stored on related models, so use title/year here.
    queryset = ScopusPublication.objects.all().order_by("-year", "title_ru")
    serializer_class = ScopusPublicationSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class ScopusAuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Scopus authors (list/retrieve/create/update/delete)"""

    queryset = ScopusAuthor.objects.all().order_by("family_name_ru", "given_name_ru")
    serializer_class = ScopusAuthorSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class ScopusJournalViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Scopus journals (list/retrieve/create/update/delete)"""

    queryset = ScopusJournal.objects.all().order_by("title_ru")
    serializer_class = ScopusJournalSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class ScopusPublisherViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Scopus publishers (list/retrieve/create/update/delete)"""

    queryset = ScopusPublisher.objects.all().order_by("name_ru")
    serializer_class = ScopusPublisherSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class ScopusPublicationAuthorViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Scopus publication-author relationships (list/retrieve/create/update/delete)"""

    queryset = ScopusPublicationAuthor.objects.all().order_by("author_position")
    serializer_class = ScopusPublicationAuthorSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class ScopusStatsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for retrieving Scopus stats"""

    queryset = ScopusStats.objects.all()
    serializer_class = ScopusStatsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class ScopusSectionViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for retrieving Scopus sections"""

    queryset = ScopusSection.objects.all().order_by("order")
    serializer_class = ScopusSectionSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


@extend_schema(
    description="Get full Scopus page content",
    responses={
        200: {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "subtitle": {"type": "string"},
                "metrics": {
                    "type": "array",
                    "items": {"$ref": "#/components/schemas/ScopusMetricsSerializer"},
                },
                "document_types": {
                    "type": "array",
                    "items": {
                        "$ref": "#/components/schemas/ScopusDocumentTypeSerializer"
                    },
                },
                "publications": {
                    "type": "array",
                    "items": {
                        "$ref": "#/components/schemas/ScopusPublicationSerializer"
                    },
                },
                "stats": {
                    "type": "array",
                    "items": {"$ref": "#/components/schemas/ScopusStatsSerializer"},
                },
            },
        }
    },
)
class ScopusPageView(generics.GenericAPIView):
    """View for complete Scopus page data"""

    def get(self, request):
        """Get all Scopus page content"""
        # Prepare context with language
        language = request.query_params.get("lang", "ru")
        context = {
            "request": request,
            "language": language,
        }

        # Metrics model doesn't have `order`; sort by citation_count (desc)
        metrics = ScopusMetricsSerializer(
            ScopusMetrics.objects.all().order_by("-citation_count"),
            many=True,
            context=context,
        ).data

        # ScopusDocumentType does not have `count`; order by label_ru for stable order
        document_types = ScopusDocumentTypeSerializer(
            ScopusDocumentType.objects.all().order_by("label_ru"),
            many=True,
            context=context,
        ).data

        # Use title_ru and year for ordering; citation_count is in ScopusMetrics
        publications = ScopusPublicationSerializer(
            ScopusPublication.objects.all().order_by("-year", "title_ru")[:10],
            many=True,
            context=context,
        ).data

        stats = ScopusStatsSerializer(
            ScopusStats.objects.all().order_by("order"), many=True, context=context
        ).data

        # Get section content
        sections = {}
        section_objects = ScopusSection.objects.all()

        for section in section_objects:
            sections[section.section_key] = {
                "title": section.get_title(language),
                "description": section.get_description(language),
            }

        # Get specific sections for page elements
        header_section = sections.get(
            "header",
            {
                "title": "Scopus Publication Database",
                "description": "Information about our institution's Scopus publications and metrics",
            },
        )

        footer_section = sections.get(
            "footer",
            {
                "title": "About Scopus",
                "description": "Scopus is one of the largest abstract and citation databases of peer-reviewed literature",
            },
        )

        response_data = {
            "title": header_section.get("title", "Scopus Publication Database"),
            "subtitle": header_section.get(
                "description",
                "Information about our institution's Scopus publications and metrics",
            ),
            "metrics": metrics,
            "document_types": document_types,
            "publications": publications,
            "stats": stats,
            "footer_text": footer_section.get("description"),
            "footer_title": footer_section.get("title"),
            "sections": sections,
        }

        return Response(response_data)
