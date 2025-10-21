from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from ..models import (
    ScopusMetrics,
    ScopusDocumentType,
    ScopusStats,
    ScopusSection,
)


class ScopusMetricsSerializer(serializers.ModelSerializer):
    publication_title = serializers.SerializerMethodField()

    class Meta:
        model = ScopusMetrics
        fields = ["id", "citation_count", "h_index", "publication_title"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_publication_title(self, obj) -> str:
        if obj.publication:
            language = self.context.get("language", "ru")
            if language == "kg" and obj.publication.title_kg:
                return obj.publication.title_kg
            elif language == "en" and obj.publication.title_en:
                return obj.publication.title_en
            return obj.publication.title_ru
        return ""


class ScopusDocumentTypeSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    class Meta:
        model = ScopusDocumentType
        fields = ["id", "code", "label"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj) -> str:
        language = self.context.get("language", "ru")
        if language == "kg" and obj.label_kg:
            return obj.label_kg
        elif language == "en" and obj.label_en:
            return obj.label_en
        return obj.label_ru


class ScopusStatsSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    class Meta:
        model = ScopusStats
        # ScopusStats model fields: label_*, value, order
        fields = ["id", "value", "label", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj) -> str:
        language = self.context.get("language", "ru")
        if language == "kg" and obj.label_kg:
            return obj.label_kg
        elif language == "en" and obj.label_en:
            return obj.label_en
        return obj.label_ru


class ScopusSectionSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = ScopusSection
        fields = ["id", "section_key", "title", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        language = self.context.get("language", "ru")
        if language == "kg" and obj.title_kg:
            return obj.title_kg
        elif language == "en" and obj.title_en:
            return obj.title_en
        return obj.title_ru

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        if language == "kg" and obj.description_kg:
            return obj.description_kg
        elif language == "en" and obj.description_en:
            return obj.description_en
        return obj.description_ru
