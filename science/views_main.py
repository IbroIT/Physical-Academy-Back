# This file is deprecated and kept only for backward compatibility
# All views are now split between views_main.py and views/ package
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import (
    Publication,
    PublicationStats,
    VestnikIssue,
    VestnikArticle,
    VestnikStats,
)
from .serializers_main import (
    PublicationSerializer,
    PublicationStatsSerializer,
    PublicationsPageSerializer,
    VestnikIssueSerializer,
    VestnikArticleSerializer,
    VestnikStatsSerializer,
    VestnikPageSerializer,
)


# Other views are imported from views/ package (will be migrated later)
from .views import (
    NTSCommitteeRoleViewSet,
    NTSResearchDirectionViewSet,
    NTSCommitteeMemberViewSet,
    NTSCommitteePageView,
    ScopusMetricsViewSet,
    ScopusDocumentTypeViewSet,
    ScopusPublicationViewSet,
    ScopusStatsViewSet,
    ScopusPageView,
    WebOfScienceTimeRangeViewSet,
    WebOfScienceMetricViewSet,
    WebOfScienceCategoryViewSet,
    WebOfScienceCollaborationViewSet,
    WebOfScienceJournalQuartileViewSet,
    WebOfScienceAdditionalMetricViewSet,
    WebOfScienceSectionViewSet,
    WebOfSciencePageView,
)

__all__ = [
    "PublicationsViewSet",
    "PublicationStatsViewSet",
    "PublicationsPageView",
    "VestnikIssuesViewSet",
    "VestnikArticlesViewSet",
    "VestnikStatsViewSet",
    "VestnikPageView",
    "NTSCommitteeRoleViewSet",
    "NTSResearchDirectionViewSet",
    "NTSCommitteeMemberViewSet",
    "NTSCommitteePageView",
    "ScopusMetricsViewSet",
    "ScopusDocumentTypeViewSet",
    "ScopusPublicationViewSet",
    "ScopusStatsViewSet",
    "ScopusPageView",
    "WebOfScienceTimeRangeViewSet",
    "WebOfScienceMetricViewSet",
    "WebOfScienceCategoryViewSet",
    "WebOfScienceCollaborationViewSet",
    "WebOfScienceJournalQuartileViewSet",
    "WebOfScienceAdditionalMetricViewSet",
    "WebOfScienceSectionViewSet",
    "WebOfSciencePageView",
]


# ==================== PUBLICATION VIEWS ====================


class PublicationsViewSet(viewsets.ModelViewSet):
    """ViewSet for managing publications"""

    queryset = Publication.objects.all().order_by("order", "-year", "-id")
    serializer_class = PublicationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by type if specified
        pub_type = self.request.query_params.get("type")
        if pub_type:
            queryset = queryset.filter(publication_type=pub_type)

        # Filter by search term if provided
        search = self.request.query_params.get("search")
        if search:
            # Search across all language versions
            queryset = queryset.filter(
                Q(title_ru__icontains=search)
                | Q(title_en__icontains=search)
                | Q(title_kg__icontains=search)
                | Q(author_ru__icontains=search)
                | Q(author_en__icontains=search)
                | Q(author_kg__icontains=search)
            )

        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class PublicationStatsViewSet(viewsets.ModelViewSet):
    """ViewSet for managing publication statistics"""

    queryset = PublicationStats.objects.all().order_by("order")
    serializer_class = PublicationStatsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class PublicationsPageView(generics.GenericAPIView):
    """View for the complete publications page data"""

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="lang",
                description="Language code (ru, en, kg)",
                required=False,
                type=str,
                default="ru",
            ),
            OpenApiParameter(
                name="type",
                description="Filter by publication type",
                required=False,
                type=str,
            ),
            OpenApiParameter(
                name="search",
                description="Search term for filtering publications",
                required=False,
                type=str,
            ),
        ]
    )
    def get(self, request):
        # Get stats
        stats = PublicationStats.objects.all().order_by("order")

        # Get featured publications
        featured = Publication.objects.filter(is_featured=True).order_by(
            "order", "-year", "-id"
        )

        # Get regular publications with filters
        publications = Publication.objects.filter(is_featured=False).order_by(
            "order", "-year", "-id"
        )

        # Apply type filter if specified
        pub_type = request.query_params.get("type")
        if pub_type:
            publications = publications.filter(publication_type=pub_type)

        # Apply search filter if specified
        search = request.query_params.get("search")
        if search:
            publications = publications.filter(
                Q(title_ru__icontains=search)
                | Q(title_en__icontains=search)
                | Q(title_kg__icontains=search)
                | Q(author_ru__icontains=search)
                | Q(author_en__icontains=search)
                | Q(author_kg__icontains=search)
            )

        # Prepare context with language
        context = {
            "request": request,
            "language": request.query_params.get("lang", "ru"),
        }

        # Serialize all components
        serializer = PublicationsPageSerializer(
            {"stats": stats, "featured": featured, "publications": publications},
            context=context,
        )

        return Response(serializer.data)


# ==================== VESTNIK VIEWS ====================


class VestnikIssuesViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Vestnik issues"""

    queryset = (
        VestnikIssue.objects.filter(is_published=True)
        .prefetch_related("articles")
        .order_by("-year", "-volume_number", "-issue_number")
    )
    serializer_class = VestnikIssueSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by featured if specified
        is_featured = self.request.query_params.get("is_featured")
        if is_featured is not None:
            is_featured_bool = is_featured.lower() in ["true", "1", "yes"]
            queryset = queryset.filter(is_featured=is_featured_bool)

        # Filter by year if specified
        year = self.request.query_params.get("year")
        if year:
            queryset = queryset.filter(year=year)

        # Filter by volume if specified
        volume = self.request.query_params.get("volume")
        if volume:
            queryset = queryset.filter(volume_number=volume)

        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class VestnikArticlesViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Vestnik articles"""

    queryset = VestnikArticle.objects.select_related("issue").filter(
        issue__is_published=True
    )
    serializer_class = VestnikArticleSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by issue if specified
        issue_id = self.request.query_params.get("issue")
        if issue_id:
            queryset = queryset.filter(issue_id=issue_id)

        # Filter by article type if specified
        article_type = self.request.query_params.get("type")
        if article_type:
            queryset = queryset.filter(article_type=article_type)

        # Filter by search term if provided
        search = self.request.query_params.get("search")
        if search:
            queryset = queryset.filter(
                Q(title_ru__icontains=search)
                | Q(title_en__icontains=search)
                | Q(title_kg__icontains=search)
                | Q(author_ru__icontains=search)
                | Q(author_en__icontains=search)
                | Q(author_kg__icontains=search)
                | Q(abstract_ru__icontains=search)
                | Q(abstract_en__icontains=search)
                | Q(abstract_kg__icontains=search)
            )

        return queryset.order_by(
            "issue__year", "issue__volume_number", "issue__issue_number", "order"
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class VestnikStatsViewSet(viewsets.ModelViewSet):
    """ViewSet for managing Vestnik statistics"""

    queryset = VestnikStats.objects.all().order_by("order")
    serializer_class = VestnikStatsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class VestnikPageView(generics.GenericAPIView):
    """View for the complete Vestnik page data"""

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="lang",
                description="Language code (ru, en, kg)",
                required=False,
                type=str,
                default="ru",
            ),
            OpenApiParameter(
                name="year",
                description="Filter by publication year",
                required=False,
                type=int,
            ),
        ]
    )
    def get(self, request):
        # Get stats
        stats = VestnikStats.objects.all().order_by("order")

        # Get featured issues
        featured_issues = VestnikIssue.objects.filter(
            is_featured=True, is_published=True
        ).order_by("-year", "-volume_number", "-issue_number")[:3]

        # Get recent issues with filters
        recent_issues = VestnikIssue.objects.filter(is_published=True).order_by(
            "-year", "-volume_number", "-issue_number"
        )

        # Apply year filter if specified
        year = request.query_params.get("year")
        if year:
            recent_issues = recent_issues.filter(year=year)

        recent_issues = recent_issues[:6]

        # Get recent articles from latest issues
        recent_articles = (
            VestnikArticle.objects.select_related("issue")
            .filter(issue__is_published=True)
            .order_by(
                "-issue__year", "-issue__volume_number", "-issue__issue_number", "order"
            )[:10]
        )

        # Prepare context with language
        context = {
            "request": request,
            "language": request.query_params.get("lang", "ru"),
        }

        # Serialize all components
        serializer = VestnikPageSerializer(
            {
                "stats": stats,
                "featured_issues": featured_issues,
                "recent_issues": recent_issues,
                "recent_articles": recent_articles,
            },
            context=context,
        )

        return Response(serializer.data)
