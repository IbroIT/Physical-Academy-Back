from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from ..models import (
    Publication,
    PublicationStats,
    VestnikArticle,
    VestnikIssue,
    VestnikStats,
)


class PublicationStatsSerializer(serializers.ModelSerializer):
    """Serializer for publication statistics"""

    label = serializers.SerializerMethodField()

    class Meta:
        model = PublicationStats
        fields = ["id", "label", "value", "icon", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj) -> str:
        language = self.context.get("language", "ru")
        if language == "kg" and obj.label_kg:
            return obj.label_kg
        elif language == "en" and obj.label_en:
            return obj.label_en
        return obj.label_ru


class VestnikArticleSerializer(serializers.ModelSerializer):
    """Serializer for Vestnik articles"""

    title = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    abstract = serializers.SerializerMethodField()
    keywords = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = VestnikArticle
        fields = [
            "id",
            "title",
            "author",
            "abstract",
            "keywords",
            "pages_from",
            "pages_to",
            "page_range",
            "doi",
            "pdf_url",
            "article_type",
            "citation_count",
            "order",
            # Include all language versions for admin
            "title_ru",
            "title_en",
            "title_kg",
            "author_ru",
            "author_en",
            "author_kg",
            "abstract_ru",
            "abstract_en",
            "abstract_kg",
            "keywords_ru",
            "keywords_en",
            "keywords_kg",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        language = self.context.get("language", "ru")
        if language == "kg" and obj.title_kg:
            return obj.title_kg
        elif language == "en" and obj.title_en:
            return obj.title_en
        return obj.title_ru

    @extend_schema_field(OpenApiTypes.STR)
    def get_author(self, obj) -> str:
        language = self.context.get("language", "ru")
        if language == "kg" and obj.author_kg:
            return obj.author_kg
        elif language == "en" and obj.author_en:
            return obj.author_en
        return obj.author_ru

    @extend_schema_field(OpenApiTypes.STR)
    def get_abstract(self, obj) -> str:
        language = self.context.get("language", "ru")
        if language == "kg" and obj.abstract_kg:
            return obj.abstract_kg
        elif language == "en" and obj.abstract_en:
            return obj.abstract_en
        return obj.abstract_ru

    @extend_schema_field(OpenApiTypes.STR)
    def get_keywords(self, obj) -> str:
        language = self.context.get("language", "ru")
        if language == "kg" and obj.keywords_kg:
            return obj.keywords_kg
        elif language == "en" and obj.keywords_en:
            return obj.keywords_en
        return obj.keywords_ru or ""

    @extend_schema_field(OpenApiTypes.STR)
    def get_pdf_url(self, obj) -> str:
        if obj.pdf_file:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.pdf_file.url)
        return None


class VestnikStatsSerializer(serializers.ModelSerializer):
    """Serializer for Vestnik statistics"""

    label = serializers.SerializerMethodField()

    class Meta:
        model = VestnikStats
        fields = ["id", "label", "value", "icon", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj) -> str:
        language = self.context.get("language", "ru")
        if language == "kg" and obj.label_kg:
            return obj.label_kg
        elif language == "en" and obj.label_en:
            return obj.label_en
        return obj.label_ru


class PublicationsPageSerializer(serializers.Serializer):
    """Serializer for entire publications page data"""

    stats = PublicationStatsSerializer(many=True)
    featured = serializers.SerializerMethodField()
    publications = serializers.SerializerMethodField()

    def get_featured(self, obj):
        from .publication import PublicationSerializer

        return PublicationSerializer(many=True).data

    def get_publications(self, obj):
        from .publication import PublicationSerializer

        return PublicationSerializer(many=True).data


class VestnikPageSerializer(serializers.Serializer):
    """Serializer for entire Vestnik page data"""

    stats = VestnikStatsSerializer(many=True)
    featured_issues = serializers.SerializerMethodField()
    recent_issues = serializers.SerializerMethodField()
    recent_articles = VestnikArticleSerializer(many=True)

    def get_featured_issues(self, obj):
        from .science import VestnikIssueSerializer

        return VestnikIssueSerializer(many=True).data

    def get_recent_issues(self, obj):
        from .science import VestnikIssueSerializer

        return VestnikIssueSerializer(many=True).data
