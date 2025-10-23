from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.db.models import F
from rest_framework import status

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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class WebOfScienceSectionViewSet(viewsets.ModelViewSet):
    """API endpoint for Web of Science sections."""

    queryset = WebOfScienceSection.objects.all().order_by("order")
    serializer_class = WebOfScienceSectionSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["language"] = self.request.query_params.get("lang", "ru")
        return context


class WebOfSciencePageView(generics.RetrieveAPIView):
    """API endpoint for Web of Science page data."""

    def get(self, request, *args, **kwargs):
        try:
            # Get the requested time range or default to 'all'
            time_range_key = self.request.query_params.get("time_range", "all")

            try:
                time_range = WebOfScienceTimeRange.objects.get(key=time_range_key)
            except WebOfScienceTimeRange.DoesNotExist:
                # If the requested time range doesn't exist, get the default one
                time_range = WebOfScienceTimeRange.objects.filter(
                    is_default=True
                ).first()
                if not time_range:
                    # If no default time range exists, get the first one
                    time_range = WebOfScienceTimeRange.objects.first()

            # Get language from query parameters
            language = self.request.query_params.get("lang", "ru")

            # Get all sections for the text content
            sections = {}
            for section in WebOfScienceSection.objects.all():
                sections[section.section_key] = section.get_text(language)

            # Get data as querysets
            metrics = WebOfScienceMetric.objects.filter(time_range=time_range).order_by(
                "order"
            )
            subject_categories = WebOfScienceCategory.objects.filter(
                time_range=time_range
            ).order_by("-count")[:8]

            source_categories = WebOfScienceCategory.objects.filter(
                time_range=time_range
            ).order_by("-count")[:6]

            collaborations = WebOfScienceCollaboration.objects.filter(
                time_range=time_range
            ).order_by("-publications")

            journal_quartiles = WebOfScienceJournalQuartile.objects.filter(
                time_range=time_range
            ).order_by("order")

            additional_metrics = WebOfScienceAdditionalMetric.objects.filter(
                time_range=time_range
            ).order_by("order")

            # Sample time series data
            year_labels = ["2018", "2019", "2020", "2021", "2022", "2023"]
            publication_data = [18, 22, 25, 31, 28, 32]
            citation_data = [145, 203, 275, 390, 420, 439]

            # Prepare chart data
            colors = [
                "rgba(16, 185, 129, 0.8)",
                "rgba(59, 130, 246, 0.8)",
                "rgba(99, 102, 241, 0.8)",
                "rgba(139, 92, 246, 0.8)",
                "rgba(236, 72, 153, 0.8)",
                "rgba(244, 63, 94, 0.8)",
                "rgba(234, 88, 12, 0.8)",
                "rgba(22, 163, 74, 0.8)",
                "rgba(6, 182, 212, 0.8)",
                "rgba(168, 85, 247, 0.8)",
            ]

            # Subject categories data for chart
            subject_categories_data = {
                "labels": [],
                "datasets": [{"data": [], "backgroundColor": []}],
            }

            for i, category in enumerate(subject_categories):
                subject_categories_data["labels"].append(category.get_name(language))
                subject_categories_data["datasets"][0]["data"].append(category.count)
                if i < len(colors):
                    subject_categories_data["datasets"][0]["backgroundColor"].append(
                        colors[i]
                    )

            # Source categories data for chart
            source_categories_data = {
                "labels": [],
                "datasets": [{"data": [], "backgroundColor": []}],
            }

            for i, category in enumerate(source_categories):
                source_categories_data["labels"].append(category.get_name(language))
                source_categories_data["datasets"][0]["data"].append(category.count)
                if i < len(colors):
                    source_categories_data["datasets"][0]["backgroundColor"].append(
                        colors[i]
                    )

            # Journal quartiles data for chart
            journal_quartiles_data = {
                "labels": [jq.quartile for jq in journal_quartiles],
                "datasets": [
                    {
                        "data": [jq.count for jq in journal_quartiles],
                        "backgroundColor": [
                            "rgba(16, 185, 129, 0.8)",
                            "rgba(59, 130, 246, 0.8)",
                            "rgba(139, 92, 246, 0.8)",
                            "rgba(244, 63, 94, 0.8)",
                        ][: len(journal_quartiles)],
                        "borderColor": [
                            "rgba(16, 185, 129, 1)",
                            "rgba(59, 130, 246, 1)",
                            "rgba(139, 92, 246, 1)",
                            "rgba(244, 63, 94, 1)",
                        ][: len(journal_quartiles)],
                    }
                ],
            }

            # Language context for serializers
            context = {"language": language}

            # Сериализуем данные
            metrics_serializer = WebOfScienceMetricSerializer(
                metrics, many=True, context=context
            )
            collaborations_serializer = WebOfScienceCollaborationSerializer(
                collaborations, many=True, context=context
            )
            additional_metrics_serializer = WebOfScienceAdditionalMetricSerializer(
                additional_metrics, many=True, context=context
            )

            # Формируем финальные данные в формате, ожидаемом фронтендом
            formatted_data = {
                "pageData": {
                    "title": sections.get("title", "Web of Science Publications"),
                    "subtitle": sections.get(
                        "subtitle", "Publications in Web of Science indexed journals"
                    ),
                    "titleIcon": "📊",
                    "categoriesIcon": "📈",
                    "collaborationsIcon": "🌍",
                    "topJournalsIcon": "⭐",
                    "timeRanges": {"5years": "5 Years", "10years": "10 Years"},
                    "collaborationsInstitutions": sections.get(
                        "collaborationsInstitutions", "institutions"
                    ),
                    "collaborationsPublications": sections.get(
                        "collaborationsPublications", "publications"
                    ),
                    "topJournalsTitle": sections.get(
                        "topJournalsTitle", "Publications by Journal Quartile"
                    ),
                    "categoriesTitle": sections.get(
                        "categoriesTitle", "Publications by Category"
                    ),
                    "collaborationsTitle": sections.get(
                        "collaborationsTitle", "International Collaboration"
                    ),
                    "additionalMetrics": additional_metrics_serializer.data,
                },
                "metrics": {
                    "5years": {
                        "main": {},
                        "categories": subject_categories_data,
                        "collaborations": collaborations_serializer.data,
                        "topJournals": journal_quartiles_data,
                    }
                },
            }

            # Заполняем основные метрики
            for i, metric_data in enumerate(metrics_serializer.data):
                if metric_data and metric_data.get("key"):
                    formatted_data["metrics"]["5years"]["main"][metric_data["key"]] = {
                        "value": metric_data.get("value", "0"),
                        "label": metric_data.get("label", ""),
                        "icon": metric_data.get("icon", "📊"),
                        "description": metric_data.get("description", ""),
                    }

            return Response(formatted_data)

        except Exception as e:
            print(f"Error in WebOfSciencePageView: {str(e)}")
            import traceback

            traceback.print_exc()
            return Response(
                {"error": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
