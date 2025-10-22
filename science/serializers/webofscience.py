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
        # Обрабатываем как объект модели, так и словарь
        if isinstance(obj, dict):
            lang = get_language()
            if lang == "en" and obj.get('label_en'):
                return obj['label_en']
            elif lang == "kg" and obj.get('label_kg'):
                return obj['label_kg']
            return obj.get('label_ru', '')
        else:
            # Обычная обработка для объекта модели
            lang = get_language()
            if lang == "en" and obj.label_en:
                return obj.label_en
            elif lang == "kg" and obj.label_kg:
                return obj.label_kg
            return obj.label_ru

    @extend_schema_field(serializers.CharField())
    def get_description(self, obj):
        # Аналогичная обработка для description
        if isinstance(obj, dict):
            lang = get_language()
            if lang == "en" and obj.get('description_en'):
                return obj['description_en']
            elif lang == "kg" and obj.get('description_kg'):
                return obj['description_kg']
            return obj.get('description_ru', '')
        else:
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
        # Аналогичное исправление для категорий
        if isinstance(obj, dict):
            lang = get_language()
            if lang == "en" and obj.get('name_en'):
                return obj['name_en']
            elif lang == "kg" and obj.get('name_kg'):
                return obj['name_kg']
            return obj.get('name_ru', '')
        else:
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
        # Аналогичное исправление для collaborations
        if isinstance(obj, dict):
            lang = get_language()
            if lang == "en" and obj.get('country_en'):
                return obj['country_en']
            elif lang == "kg" and obj.get('country_kg'):
                return obj['country_kg']
            return obj.get('country_ru', '')
        else:
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
        fields = ['id', 'key', 'value', 'title', 'description', 'icon', 'order']  # Убрал 'time_range'

    def get_title(self, obj):
        # Обрабатываем как объект модели, так и словарь
        if isinstance(obj, dict):
            lang = get_language()
            if lang == "en" and obj.get('title_en'):
                return obj['title_en']
            elif lang == "kg" and obj.get('title_kg'):
                return obj['title_kg']
            return obj.get('title_ru', '')
        else:
            # Обычная обработка для объекта модели
            lang = get_language()
            if lang == "en" and obj.title_en:
                return obj.title_en
            elif lang == "kg" and obj.title_kg:
                return obj.title_kg
            return obj.title_ru

    def get_description(self, obj):
        # Аналогичная обработка для description
        if isinstance(obj, dict):
            lang = get_language()
            if lang == "en" and obj.get('description_en'):
                return obj['description_en']
            elif lang == "kg" and obj.get('description_kg'):
                return obj['description_kg']
            return obj.get('description_ru', '')
        else:
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
    metrics = WebOfScienceMetricSerializer(many=True, read_only=True)
    timeRanges = serializers.SerializerMethodField()
    collaborations = WebOfScienceCollaborationSerializer(many=True, read_only=True)
    additionalMetrics = WebOfScienceAdditionalMetricSerializer(many=True, read_only=True)

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