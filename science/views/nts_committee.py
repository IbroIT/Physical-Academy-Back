from rest_framework import viewsets, generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from ..models import (
    NTSCommitteeMember,
    NTSCommitteeRole,
    NTSResearchDirection,
    NTSCommitteeSection,
)
from ..serializers import (
    NTSCommitteeMemberSerializer,
    NTSCommitteeRoleSerializer,
    NTSResearchDirectionSerializer,
    NTSCommitteeSectionSerializer,
)


class NTSCommitteeRoleViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for retrieving NTS Committee roles"""

    queryset = NTSCommitteeRole.objects.all()
    serializer_class = NTSCommitteeRoleSerializer


class NTSResearchDirectionViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for retrieving NTS Research Directions"""

    queryset = NTSResearchDirection.objects.all()
    serializer_class = NTSResearchDirectionSerializer


class NTSCommitteeMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for retrieving NTS Committee members"""

    queryset = NTSCommitteeMember.objects.filter(is_active=True).order_by(
        "order", "name_ru"
    )
    serializer_class = NTSCommitteeMemberSerializer


@extend_schema(
    description="Get full NTS Committee page content",
    responses={
        200: {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "subtitle": {"type": "string"},
                "chairman": {
                    "$ref": "#/components/schemas/NTSCommitteeMemberSerializer"
                },
                "vice_chairman": {
                    "$ref": "#/components/schemas/NTSCommitteeMemberSerializer"
                },
                "secretary": {
                    "$ref": "#/components/schemas/NTSCommitteeMemberSerializer"
                },
                "members": {
                    "type": "array",
                    "items": {
                        "$ref": "#/components/schemas/NTSCommitteeMemberSerializer"
                    },
                },
                "research_directions": {
                    "type": "array",
                    "items": {
                        "$ref": "#/components/schemas/NTSResearchDirectionSerializer"
                    },
                },
            },
        }
    },
)
class NTSCommitteePageView(generics.GenericAPIView):
    """View for complete NTS Committee page data"""

    def get(self, request):
        """Get all NTS Committee page content"""
        try:
            # Try to find the chairman, vice-chairman and secretary
            chairman = NTSCommitteeMemberSerializer(
                NTSCommitteeMember.objects.filter(
                    role__name_ru__icontains="председатель", is_active=True
                ).first()
            ).data

            vice_chairman = NTSCommitteeMemberSerializer(
                NTSCommitteeMember.objects.filter(
                    role__name_ru__icontains="заместитель", is_active=True
                ).first()
            ).data

            secretary = NTSCommitteeMemberSerializer(
                NTSCommitteeMember.objects.filter(
                    role__name_ru__icontains="секретарь", is_active=True
                ).first()
            ).data

            # Get regular members (exclude chairman, vice-chairman and secretary)
            excluded_ids = []
            if chairman:
                excluded_ids.append(chairman["id"])
            if vice_chairman:
                excluded_ids.append(vice_chairman["id"])
            if secretary:
                excluded_ids.append(secretary["id"])

            members = NTSCommitteeMemberSerializer(
                NTSCommitteeMember.objects.filter(is_active=True)
                .exclude(id__in=excluded_ids)
                .order_by("order", "name_ru"),
                many=True,
            ).data

            # Get research directions
            research_directions = NTSResearchDirectionSerializer(
                NTSResearchDirection.objects.all(), many=True
            ).data

            # Get section content
            sections = {}
            section_objects = NTSCommitteeSection.objects.all()

            for section in section_objects:
                sections[section.section_key] = {
                    "title": section.get_title(),
                    "description": section.get_description(),
                }

            # Get specific sections for page elements
            footer_section = sections.get(
                "footer",
                {
                    "title": "Scientific and Technical Council",
                    "description": "Coordinating scientific research and development",
                },
            )

            vision_section = sections.get(
                "vision",
                {
                    "title": "Our Vision",
                    "description": "Advancing scientific research at the Academy",
                },
            )

            mission_section = sections.get(
                "mission",
                {
                    "title": "Our Mission",
                    "description": "Supporting innovation and development",
                },
            )

            response_data = {
                "title": "Scientific and Technical Council",
                "subtitle": "Coordinating scientific research and technical development of the Academy",
                "chairman": chairman,
                "vice_chairman": vice_chairman,
                "secretary": secretary,
                "members": members,
                "research_directions": research_directions,
                "footer_text": footer_section.get("description"),
                "footer_title": footer_section.get("title"),
                "vision": vision_section.get("description"),
                "vision_title": vision_section.get("title"),
                "mission": mission_section.get("description"),
                "sections": sections,
            }

            return Response(response_data)

        except Exception as e:
            return Response(
                {
                    "title": "Scientific and Technical Council",
                    "subtitle": "Coordinating scientific research and technical development of the Academy",
                    "error": str(e),
                }
            )
