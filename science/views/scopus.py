from rest_framework import viewsets, generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from ..models import (
    ScopusMetrics,
    ScopusDocumentType,
    ScopusPublication,
    ScopusStats,
    ScopusSection,
)
from ..serializers import (
    ScopusMetricsSerializer,
    ScopusDocumentTypeSerializer,
    ScopusPublicationSerializer,
    ScopusStatsSerializer,
    ScopusSectionSerializer,
)


class ScopusMetricsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for retrieving Scopus metrics"""

    queryset = ScopusMetrics.objects.all()
    serializer_class = ScopusMetricsSerializer


class ScopusDocumentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for retrieving Scopus document types"""

    queryset = ScopusDocumentType.objects.all()
    serializer_class = ScopusDocumentTypeSerializer


class ScopusPublicationViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for retrieving Scopus publications"""

    queryset = ScopusPublication.objects.all().order_by(
        "-year", "order", "-citation_count"
    )
    serializer_class = ScopusPublicationSerializer


class ScopusStatsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for retrieving Scopus stats"""

    queryset = ScopusStats.objects.all()
    serializer_class = ScopusStatsSerializer


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
        metrics = ScopusMetricsSerializer(
            ScopusMetrics.objects.all().order_by("order"), many=True
        ).data

        document_types = ScopusDocumentTypeSerializer(
            ScopusDocumentType.objects.all().order_by("-count"), many=True
        ).data

        publications = ScopusPublicationSerializer(
            ScopusPublication.objects.all().order_by(
                "-year", "order", "-citation_count"
            )[:10],
            many=True,
        ).data

        stats = ScopusStatsSerializer(
            ScopusStats.objects.all().order_by("order"), many=True
        ).data

        # Get section content
        sections = {}
        section_objects = ScopusSection.objects.all()

        for section in section_objects:
            sections[section.section_key] = {
                "title": section.get_title(),
                "description": section.get_description(),
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
