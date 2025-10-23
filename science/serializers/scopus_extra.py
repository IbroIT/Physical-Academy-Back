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
            return (
                getattr(obj.publication, f"title_{language}", obj.publication.title_ru)
                or obj.publication.title_ru
            )
        return ""


class ScopusDocumentTypeSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    class Meta:
        model = ScopusDocumentType
        fields = ["id", "code", "label"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj) -> str:
        language = self.context.get("language", "ru")
        return getattr(obj, f"label_{language}", obj.label_ru) or obj.label_ru


class ScopusStatsSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    class Meta:
        model = ScopusStats
        # ScopusStats model fields: label_*, value, order
        fields = ["id", "value", "label", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj) -> str:
        language = self.context.get("language", "ru")
        return getattr(obj, f"label_{language}", obj.label_ru) or obj.label_ru


class ScopusSectionSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = ScopusSection
        fields = ["id", "section_key", "title", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        language = self.context.get("language", "ru")
        return getattr(obj, f"title_{language}", obj.title_ru) or obj.title_ru

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return (
            getattr(obj, f"description_{language}", obj.description_ru)
            or obj.description_ru
        )
