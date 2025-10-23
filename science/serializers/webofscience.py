from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from ..models import (
    WebOfScienceTimeRange,
    WebOfScienceMetric,
    WebOfScienceCategory,
    WebOfScienceCollaboration,
    WebOfScienceJournalQuartile,
    WebOfScienceAdditionalMetric,
    WebOfScienceSection,
)


class WebOfScienceTimeRangeSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = WebOfScienceTimeRange
        fields = ["id", "key", "title", "order", "is_default"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_title(language)


class WebOfScienceMetricSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = WebOfScienceMetric
        fields = ["id", "key", "value", "label", "description", "icon", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_label(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class WebOfScienceCategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = WebOfScienceCategory
        fields = ["id", "name", "count", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_name(language)


class WebOfScienceCollaborationSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    class Meta:
        model = WebOfScienceCollaboration
        fields = ["id", "country", "flag", "institutions", "publications", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_country(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_country(language)


class WebOfScienceJournalQuartileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebOfScienceJournalQuartile
        fields = ["id", "quartile", "count", "order"]


class WebOfScienceAdditionalMetricSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = WebOfScienceAdditionalMetric
        fields = [
            "id",
            "key",
            "value",
            "title",
            "description",
            "icon",
            "order",
        ]  # Убрал 'time_range'

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class WebOfScienceSectionSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    class Meta:
        model = WebOfScienceSection
        fields = ["id", "section_key", "text", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_text(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_text(language)


class WebOfSciencePageSerializer(serializers.Serializer):
    title = serializers.CharField()
    subtitle = serializers.CharField()
    metrics = WebOfScienceMetricSerializer(many=True, read_only=True)
    timeRanges = serializers.SerializerMethodField()
    collaborations = WebOfScienceCollaborationSerializer(many=True, read_only=True)
    additionalMetrics = WebOfScienceAdditionalMetricSerializer(
        many=True, read_only=True
    )

    # Translated text fields
    categoriesTitle = serializers.CharField()
    collaborationsTitle = serializers.CharField()
    collaborationsInstitutions = serializers.CharField()
    collaborationsPublications = serializers.CharField()
    topJournalsTitle = serializers.CharField()
    topJournalsPublications = serializers.CharField()
    timelineTitle = serializers.CharField()

    @extend_schema_field(serializers.DictField())
    def get_timeRanges(self, obj):
        # Format for Chart.js timeline
        return {
            "labels": obj.get("year_labels", []),
            "datasets": [
                {
                    "label": "Publications",
                    "data": obj.get("publication_data", []),
                    "borderColor": "rgba(16, 185, 129, 1)",
                    "backgroundColor": "rgba(16, 185, 129, 0.2)",
                },
                {
                    "label": "Citations",
                    "data": obj.get("citation_data", []),
                    "borderColor": "rgba(59, 130, 246, 1)",
                    "backgroundColor": "rgba(59, 130, 246, 0.2)",
                },
            ],
        }
