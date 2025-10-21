from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.utils.translation import get_language
from django.db.models import F

from ..models import (
    WebOfScienceTimeRange,
    WebOfScienceMetric,
    WebOfScienceCategory,
    WebOfScienceCollaboration,
    WebOfScienceJournalQuartile,
    WebOfScienceAdditionalMetric,
    WebOfScienceSection,
)
from ..serializers import (
    WebOfScienceTimeRangeSerializer,
    WebOfScienceMetricSerializer,
    WebOfScienceCategorySerializer,
    WebOfScienceCollaborationSerializer,
    WebOfScienceJournalQuartileSerializer,
    WebOfScienceAdditionalMetricSerializer,
    WebOfScienceSectionSerializer,
    WebOfSciencePageSerializer,
)


class WebOfScienceTimeRangeViewSet(viewsets.ModelViewSet):
    """API endpoint for Web of Science time ranges."""

    queryset = WebOfScienceTimeRange.objects.all().order_by("order")
    serializer_class = WebOfScienceTimeRangeSerializer


class WebOfScienceMetricViewSet(viewsets.ModelViewSet):
    """API endpoint for Web of Science metrics."""

    queryset = WebOfScienceMetric.objects.all().order_by("time_range", "order")
    serializer_class = WebOfScienceMetricSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        time_range_key = self.request.query_params.get("time_range", None)

        if time_range_key:
            queryset = queryset.filter(time_range__key=time_range_key)

        return queryset


class WebOfScienceCategoryViewSet(viewsets.ModelViewSet):
    """API endpoint for Web of Science categories."""

    queryset = WebOfScienceCategory.objects.all().order_by("time_range", "order")
    serializer_class = WebOfScienceCategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        time_range_key = self.request.query_params.get("time_range", None)

        if time_range_key:
            queryset = queryset.filter(time_range__key=time_range_key)

        return queryset


class WebOfScienceCollaborationViewSet(viewsets.ModelViewSet):
    """API endpoint for Web of Science collaborations."""

    queryset = WebOfScienceCollaboration.objects.all().order_by("time_range", "order")
    serializer_class = WebOfScienceCollaborationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        time_range_key = self.request.query_params.get("time_range", None)

        if time_range_key:
            queryset = queryset.filter(time_range__key=time_range_key)

        return queryset


class WebOfScienceJournalQuartileViewSet(viewsets.ModelViewSet):
    """API endpoint for Web of Science journal quartiles."""

    queryset = WebOfScienceJournalQuartile.objects.all().order_by("time_range", "order")
    serializer_class = WebOfScienceJournalQuartileSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        time_range_key = self.request.query_params.get("time_range", None)

        if time_range_key:
            queryset = queryset.filter(time_range__key=time_range_key)

        return queryset


class WebOfScienceAdditionalMetricViewSet(viewsets.ModelViewSet):
    """API endpoint for Web of Science additional metrics."""

    queryset = WebOfScienceAdditionalMetric.objects.all().order_by(
        "time_range", "order"
    )
    serializer_class = WebOfScienceAdditionalMetricSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        time_range_key = self.request.query_params.get("time_range", None)

        if time_range_key:
            queryset = queryset.filter(time_range__key=time_range_key)

        return queryset


class WebOfScienceSectionViewSet(viewsets.ModelViewSet):
    """API endpoint for Web of Science sections."""

    queryset = WebOfScienceSection.objects.all().order_by("order")
    serializer_class = WebOfScienceSectionSerializer


class WebOfSciencePageView(generics.RetrieveAPIView):
    """API endpoint for Web of Science page data."""

    serializer_class = WebOfSciencePageSerializer

    def get_object(self):
        # Get the requested time range or default to 'all'
        time_range_key = self.request.query_params.get("time_range", "all")

        try:
            time_range = WebOfScienceTimeRange.objects.get(key=time_range_key)
        except WebOfScienceTimeRange.DoesNotExist:
            # If the requested time range doesn't exist, get the default one
            time_range = WebOfScienceTimeRange.objects.filter(is_default=True).first()
            if not time_range:
                # If no default time range exists, get the first one
                time_range = WebOfScienceTimeRange.objects.first()

        # Get all sections for the text content
        sections = {}
        for section in WebOfScienceSection.objects.all():
            lang_suffix = ""
            if get_language() == "en":
                lang_suffix = "_en"
            elif get_language() == "kg":
                lang_suffix = "_kg"
            else:
                lang_suffix = "_ru"

            sections[section.section_key] = (
                getattr(section, f"text{lang_suffix}", "") or section.text_ru
            )

        # Get metrics for the selected time range
        metrics = WebOfScienceMetric.objects.filter(time_range=time_range).order_by(
            "order"
        )
        metrics_serializer = WebOfScienceMetricSerializer(metrics, many=True)

        # Get categories for the selected time range - filter subject categories
        subject_categories = WebOfScienceCategory.objects.filter(
            time_range=time_range
        ).order_by("-count")[
            :8
        ]  # Limit to 8 for readability
        subject_cats_serializer = WebOfScienceCategorySerializer(
            subject_categories, many=True
        )

        # Get source categories
        source_categories = WebOfScienceCategory.objects.filter(
            time_range=time_range
        ).order_by("-count")[
            :6
        ]  # Limit to 6 for readability
        source_cats_serializer = WebOfScienceCategorySerializer(
            source_categories, many=True
        )

        # Get collaborations for the selected time range
        collaborations = WebOfScienceCollaboration.objects.filter(
            time_range=time_range
        ).order_by("-publications")
        collaborations_serializer = WebOfScienceCollaborationSerializer(
            collaborations, many=True
        )

        # Get journal quartiles for the selected time range
        journal_quartiles = WebOfScienceJournalQuartile.objects.filter(
            time_range=time_range
        ).order_by("order")
        journal_quartiles_serializer = WebOfScienceJournalQuartileSerializer(
            journal_quartiles, many=True
        )

        # Get additional metrics for the selected time range
        additional_metrics = WebOfScienceAdditionalMetric.objects.filter(
            time_range=time_range
        ).order_by("order")
        additional_metrics_serializer = WebOfScienceAdditionalMetricSerializer(
            additional_metrics, many=True
        )

        # Sample time series data (should be replaced with real data from models)
        # In a real implementation, this would come from a separate model with year-by-year data
        # For now, we'll just use mock data similar to what's in the frontend component
        year_labels = ["2018", "2019", "2020", "2021", "2022", "2023"]
        publication_data = [18, 22, 25, 31, 28, 32]
        citation_data = [145, 203, 275, 390, 420, 439]

        # Assemble the page data
        page_data = {
            "title": sections.get("title", "Web of Science Publications"),
            "subtitle": sections.get(
                "subtitle", "Publications in Web of Science indexed journals"
            ),
            "metrics": metrics_serializer.data,
            "year_labels": year_labels,
            "publication_data": publication_data,
            "citation_data": citation_data,
            "subject_categories": subject_cats_serializer.data,
            "source_categories": source_cats_serializer.data,
            "collaborations": collaborations_serializer.data,
            "journal_quartiles": journal_quartiles_serializer.data,
            "additionalMetrics": additional_metrics_serializer.data,
            # Translation strings
            "categoriesTitle": sections.get(
                "categoriesTitle", "Publications by Category"
            ),
            "collaborationsTitle": sections.get(
                "collaborationsTitle", "International Collaborations"
            ),
            "collaborationsInstitutions": sections.get(
                "collaborationsInstitutions", "institutions"
            ),
            "collaborationsPublications": sections.get(
                "collaborationsPublications", "publications"
            ),
            "topJournalsTitle": sections.get(
                "topJournalsTitle", "Publications by Journal Quartile"
            ),
            "topJournalsPublications": sections.get(
                "topJournalsPublications", "publications"
            ),
            "timelineTitle": sections.get(
                "timelineTitle", "Publications & Citations Over Time"
            ),
        }

        return page_data
