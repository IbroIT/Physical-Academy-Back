from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from ..models import (
    ScopusAuthor,
    ScopusPublication,
    ScopusPublicationAuthor,
    ScopusJournal,
    ScopusPublisher,
)


class ScopusAuthorSerializer(serializers.ModelSerializer):
    # Добавляем свойства для обратной совместимости
    name = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return f"{obj.family_name_ru} {obj.given_name_ru}".strip()

    def get_first_name(self, obj):
        return obj.given_name_ru

    def get_last_name(self, obj):
        return obj.family_name_ru

    class Meta:
        model = ScopusAuthor
        fields = [
            "id",
            "scopus_id",
            "name",
            "first_name",
            "last_name",
            "given_name_ru",
            "family_name_ru",
            "given_name_en",
            "family_name_en",
            "given_name_kg",
            "family_name_kg",
        ]


class ScopusJournalSerializer(serializers.ModelSerializer):
    # Добавляем свойство для обратной совместимости
    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.title_ru

    class Meta:
        model = ScopusJournal
        fields = [
            "id",
            "title",
            "title_ru",
            "title_en",
            "title_kg",
            "publisher",
            "issn",
        ]


class ScopusPublisherSerializer(serializers.ModelSerializer):
    # Добавляем свойство для обратной совместимости
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name_ru

    class Meta:
        model = ScopusPublisher
        fields = ["id", "name", "name_ru", "name_en", "name_kg", "country"]


class ScopusPublicationAuthorSerializer(serializers.ModelSerializer):
    # For read operations we want the nested author representation. For
    # write operations allow passing an `author_id` primary key.
    author = ScopusAuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author", queryset=ScopusAuthor.objects.all(), write_only=True
    )

    class Meta:
        model = ScopusPublicationAuthor
        # model fields: id, publication, author, author_position
        fields = ["id", "author", "author_id", "publication", "author_position"]


class ScopusPublicationSerializer(serializers.ModelSerializer):
    # Expose a localized title, computed authors list and journal display
    title = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()
    journal_name = serializers.SerializerMethodField()
    citation_count = serializers.SerializerMethodField()

    class Meta:
        model = ScopusPublication
        fields = [
            "id",
            "title",
            "title_ru",
            "title_en",
            "title_kg",
            "year",
            "authors",
            "journal",
            "journal_name",
            "doi",
            "url",
            "citation_count",
            "abstract_ru",
            "abstract_en",
            "abstract_kg",
        ]

    @extend_schema_field(ScopusPublicationAuthorSerializer(many=True))
    def get_authors(self, obj):
        # use related_name defined on ScopusPublicationAuthor: authors
        publication_authors = obj.authors.all().order_by("author_position")
        return ScopusPublicationAuthorSerializer(publication_authors, many=True).data

    def get_title(self, obj):
        return obj.title_ru or obj.title_en or obj.title_kg

    def get_citation_count(self, obj):
        # Получаем значение citation_count из связанной модели ScopusMetrics, если она существует
        try:
            return obj.metrics.citation_count
        except:
            return 0

    def get_journal_name(self, obj):
        # Возвращаем название журнала из связанного объекта, если он есть
        if obj.journal:
            return obj.journal.title_ru
        return ""
