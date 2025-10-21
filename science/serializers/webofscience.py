from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from django.utils.translation import get_language

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

    @extend_schema_field(serializers.CharField())
    def get_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.title_en:
            return obj.title_en
        elif lang == "kg" and obj.title_kg:
            return obj.title_kg
        return obj.title_ru


class WebOfScienceMetricSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = WebOfScienceMetric
        fields = ["id", "key", "value", "label", "description", "icon", "order"]

    @extend_schema_field(serializers.CharField())
    def get_label(self, obj):
        lang = get_language()
        if lang == "en" and obj.label_en:
            return obj.label_en
        elif lang == "kg" and obj.label_kg:
            return obj.label_kg
        return obj.label_ru

    @extend_schema_field(serializers.CharField())
    def get_description(self, obj):
        lang = get_language()
        if lang == "en" and obj.description_en:
            return obj.description_en
        elif lang == "kg" and obj.description_kg:
            return obj.description_kg
        return obj.description_ru


class WebOfScienceCategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = WebOfScienceCategory
        fields = ["id", "name", "count", "order"]

    @extend_schema_field(serializers.CharField())
    def get_name(self, obj):
        lang = get_language()
        if lang == "en" and obj.name_en:
            return obj.name_en
        elif lang == "kg" and obj.name_kg:
            return obj.name_kg
        return obj.name_ru


class WebOfScienceCollaborationSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    class Meta:
        model = WebOfScienceCollaboration
        fields = ["id", "country", "flag", "institutions", "publications", "order"]

    @extend_schema_field(serializers.CharField())
    def get_country(self, obj):
        lang = get_language()
        if lang == "en" and obj.country_en:
            return obj.country_en
        elif lang == "kg" and obj.country_kg:
            return obj.country_kg
        return obj.country_ru


class WebOfScienceJournalQuartileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebOfScienceJournalQuartile
        fields = ["id", "quartile", "count", "order"]


class WebOfScienceAdditionalMetricSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = WebOfScienceAdditionalMetric
        fields = ["id", "key", "value", "title", "description", "icon", "order"]

    @extend_schema_field(serializers.CharField())
    def get_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.title_en:
            return obj.title_en
        elif lang == "kg" and obj.title_kg:
            return obj.title_kg
        return obj.title_ru

    @extend_schema_field(serializers.CharField())
    def get_description(self, obj):
        lang = get_language()
        if lang == "en" and obj.description_en:
            return obj.description_en
        elif lang == "kg" and obj.description_kg:
            return obj.description_kg
        return obj.description_ru


class WebOfScienceSectionSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    class Meta:
        model = WebOfScienceSection
        fields = ["id", "section_key", "text", "order"]

    @extend_schema_field(serializers.CharField())
    def get_text(self, obj):
        lang = get_language()
        if lang == "en" and obj.text_en:
            return obj.text_en
        elif lang == "kg" and obj.text_kg:
            return obj.text_kg
        return obj.text_ru


class WebOfSciencePageSerializer(serializers.Serializer):
    title = serializers.CharField()
    subtitle = serializers.CharField()
    metrics = WebOfScienceMetricSerializer(many=True)
    timeRanges = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    sourceCategories = serializers.SerializerMethodField()
    collaborations = WebOfScienceCollaborationSerializer(many=True)
    topJournals = serializers.SerializerMethodField()
    additionalMetrics = WebOfScienceAdditionalMetricSerializer(many=True)

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

    @extend_schema_field(serializers.DictField())
    def get_categories(self, obj):
        # Format for Chart.js pie chart - subject categories
        categories = obj.get("subject_categories", [])
        return {
            "labels": [cat.get("name") for cat in categories],
            "datasets": [
                {
                    "data": [cat.get("count") for cat in categories],
                    "backgroundColor": [
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
                    ][: len(categories)],
                }
            ],
        }

    @extend_schema_field(serializers.DictField())
    def get_sourceCategories(self, obj):
        # Format for Chart.js pie chart - source categories (journals)
        categories = obj.get("source_categories", [])
        return {
            "labels": [cat.get("name") for cat in categories],
            "datasets": [
                {
                    "data": [cat.get("count") for cat in categories],
                    "backgroundColor": [
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
                    ][: len(categories)],
                }
            ],
        }

    @extend_schema_field(serializers.DictField())
    def get_topJournals(self, obj):
        # Format for Chart.js bar chart - journal quartiles
        journal_quartiles = obj.get("journal_quartiles", [])
        return {
            "labels": [jq.get("quartile") for jq in journal_quartiles],
            "datasets": [
                {
                    "data": [jq.get("count") for jq in journal_quartiles],
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
