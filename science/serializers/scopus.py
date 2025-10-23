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
    # Return only localized name based on ?lang= parameter
    name = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        language = self.context.get("language", "ru")
        given = (
            getattr(obj, f"given_name_{language}", obj.given_name_ru)
            or obj.given_name_ru
        )
        family = (
            getattr(obj, f"family_name_{language}", obj.family_name_ru)
            or obj.family_name_ru
        )
        return f"{family} {given}".strip()

    class Meta:
        model = ScopusAuthor
        fields = [
            "id",
            "scopus_id",
            "name",
        ]


class ScopusJournalSerializer(serializers.ModelSerializer):
    # Return only localized title based on ?lang= parameter
    title = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"title_{language}", obj.title_ru) or obj.title_ru

    class Meta:
        model = ScopusJournal
        fields = [
            "id",
            "title",
            "publisher",
            "issn",
        ]


class ScopusPublisherSerializer(serializers.ModelSerializer):
    # Return only localized name based on ?lang= parameter
    name = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"name_{language}", obj.name_ru) or obj.name_ru

    class Meta:
        model = ScopusPublisher
        fields = ["id", "name", "country"]


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
    # Return only localized fields based on ?lang= parameter
    title = serializers.SerializerMethodField()
    abstract = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()
    journal_name = serializers.SerializerMethodField()
    citation_count = serializers.SerializerMethodField()

    class Meta:
        model = ScopusPublication
        fields = [
            "id",
            "title",
            "abstract",
            "year",
            "authors",
            "journal",
            "journal_name",
            "doi",
            "url",
            "citation_count",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"title_{language}", obj.title_ru) or obj.title_ru

    @extend_schema_field(OpenApiTypes.STR)
    def get_abstract(self, obj):
        language = self.context.get("language", "ru")
        return getattr(obj, f"abstract_{language}", obj.abstract_ru) or obj.abstract_ru

    @extend_schema_field(ScopusPublicationAuthorSerializer(many=True))
    def get_authors(self, obj):
        # use related_name defined on ScopusPublicationAuthor: authors
        publication_authors = obj.authors.all().order_by("author_position")
        context = self.context
        return ScopusPublicationAuthorSerializer(
            publication_authors, many=True, context=context
        ).data

    @extend_schema_field(OpenApiTypes.INT)
    def get_citation_count(self, obj):
        # Получаем значение citation_count из связанной модели ScopusMetrics, если она существует
        try:
            return obj.metrics.citation_count
        except:
            return 0

    @extend_schema_field(OpenApiTypes.STR)
    def get_journal_name(self, obj):
        # Возвращаем название журнала из связанного объекта, если он есть
        if obj.journal:
            language = self.context.get("language", "ru")
            return (
                getattr(obj.journal, f"title_{language}", obj.journal.title_ru)
                or obj.journal.title_ru
            )
        return ""
