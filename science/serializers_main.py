from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from .models import (
    Publication,
    PublicationStats,
    Vestnik,
    VestnikArticle,
    VestnikIssue,
    VestnikStats,
)


from .serializers.nts_committee import (
    NTSCommitteeRoleSerializer,
    NTSResearchDirectionSerializer,
    NTSCommitteeMemberSerializer,
    NTSCommitteeSectionSerializer,
)
from .serializers.scopus import (
    ScopusAuthorSerializer,
    ScopusJournalSerializer,
    ScopusPublisherSerializer,
    ScopusPublicationAuthorSerializer,
    ScopusPublicationSerializer,
)

# ==================== PUBLICATION SERIALIZERS ====================


class PublicationSerializer(serializers.ModelSerializer):
    """Сериализатор для научных публикаций с поддержкой многоязычности"""

    title = serializers.SerializerMethodField()
    abstract = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()
    pub_type_display = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = [
            "id",
            "title",
            "authors",
            "abstract",
            "journal",
            "year",
            "doi",
            "url",
            "citation_count",
            "publication_type",
            "pub_type_display",
            "pdf_url",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_abstract(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_abstract(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_authors(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_authors(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_pub_type_display(self, obj):
        """Возвращает читаемое название типа публикации на выбранном языке"""
        type_mapping = {
            "article": {
                "ru": "Журнальная статья",
                "en": "Journal Article",
                "kg": "Журнал макаласы",
            },
            "conference": {
                "ru": "Конференция",
                "en": "Conference Paper",
                "kg": "Конференция",
            },
            "book": {"ru": "Книга/Глава", "en": "Book/Chapter", "kg": "Китеп/Бөлүм"},
            "patent": {"ru": "Патент", "en": "Patent", "kg": "Патент"},
        }
        language = self.context.get("language", "ru")
        return type_mapping.get(obj.publication_type, {}).get(
            language, obj.publication_type
        )

    @extend_schema_field(OpenApiTypes.STR)
    def get_pdf_url(self, obj):
        """Возвращает полный URL для PDF файла"""
        if obj.pdf_file:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.pdf_file.url)
        return None


# ==================== PUBLICATION STATS SERIALIZERS ====================


class PublicationStatsSerializer(serializers.ModelSerializer):
    """Сериализатор для статистики публикаций"""

    label = serializers.SerializerMethodField()

    class Meta:
        model = PublicationStats
        fields = ["id", "label", "value", "icon", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"label_{language}", obj.label_ru)


class PublicationsPageSerializer(serializers.Serializer):
    """Сериализатор для полной страницы публикаций со статистикой"""

    stats = PublicationStatsSerializer(many=True)
    featured = serializers.SerializerMethodField()
    publications = serializers.SerializerMethodField()

    def get_featured(self, obj):
        # obj ожидается как словарь с ключом 'featured'
        featured_qs = obj.get("featured", [])
        serializer = PublicationSerializer(featured_qs, many=True, context=self.context)
        return serializer.data

    def get_publications(self, obj):
        pubs_qs = obj.get("publications", [])
        serializer = PublicationSerializer(pubs_qs, many=True, context=self.context)
        return serializer.data


# ==================== VESTNIK SERIALIZERS ====================


class VestnikSerializer(serializers.ModelSerializer):
    """Сериализатор для журнала Vestnik"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    issn = serializers.CharField()

    class Meta:
        model = Vestnik
        fields = ["id", "title", "description", "issn", "image", "is_active"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class VestnikIssueSerializer(serializers.ModelSerializer):
    """Сериализатор для выпусков журнала Vestnik с поддержкой многоязычности"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    articles_count = serializers.IntegerField(read_only=True)
    pdf_url = serializers.SerializerMethodField()
    cover_image_url = serializers.SerializerMethodField()

    class Meta:
        model = VestnikIssue
        fields = [
            "id",
            "volume_number",
            "issue_number",
            "year",
            "title",
            "description",
            "pdf_file",
            "pdf_url",
            "cover_image",
            "cover_image_url",
            "issn_print",
            "issn_online",
            "articles_count",
            "is_featured",
            "is_published",
            "publication_date",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_pdf_url(self, obj):
        """Возвращает полный URL для PDF файла"""
        if obj.pdf_file:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.pdf_file.url)
        return None

    @extend_schema_field(OpenApiTypes.STR)
    def get_cover_image_url(self, obj):
        """Возвращает полный URL для обложки"""
        if obj.cover_image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
        return None


class VestnikArticleSerializer(serializers.ModelSerializer):
    """Сериализатор для статей журнала Vestnik"""

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
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"title_{language}", obj.title_ru)

    @extend_schema_field(OpenApiTypes.STR)
    def get_author(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"author_{language}", obj.author_ru)

    @extend_schema_field(OpenApiTypes.STR)
    def get_abstract(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"abstract_{language}", obj.abstract_ru)

    @extend_schema_field(OpenApiTypes.STR)
    def get_keywords(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"keywords_{language}", obj.keywords_ru or "")

    @extend_schema_field(OpenApiTypes.STR)
    def get_pdf_url(self, obj):
        if obj.pdf_file:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.pdf_file.url)
        return None


class VestnikStatsSerializer(serializers.ModelSerializer):
    """Сериализатор для статистики Vestnik"""

    label = serializers.SerializerMethodField()

    class Meta:
        model = VestnikStats
        fields = ["id", "label", "value", "icon", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"label_{language}", obj.label_ru)


class VestnikPageSerializer(serializers.Serializer):
    """Сериализатор для полной страницы Vestnik"""

    stats = VestnikStatsSerializer(many=True)
    featured_issues = serializers.SerializerMethodField()
    recent_issues = serializers.SerializerMethodField()
    recent_articles = VestnikArticleSerializer(many=True)

    def get_featured_issues(self, obj):
        featured_qs = obj.get("featured_issues", [])
        serializer = VestnikIssueSerializer(
            featured_qs, many=True, context=self.context
        )
        return serializer.data

    def get_recent_issues(self, obj):
        recent_qs = obj.get("recent_issues", [])
        serializer = VestnikIssueSerializer(recent_qs, many=True, context=self.context)
        return serializer.data
