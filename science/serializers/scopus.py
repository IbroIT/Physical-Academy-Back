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
    class Meta:
        model = ScopusAuthor
        fields = ["id", "scopus_id", "name", "first_name", "last_name", "h_index"]


class ScopusJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScopusJournal
        fields = [
            "id",
            "scopus_id",
            "title",
            "publisher",
            "issn",
            "eissn",
            "source_id",
            "cite_score",
            "sjr",
            "snip",
        ]


class ScopusPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScopusPublisher
        fields = ["id", "scopus_id", "name"]


class ScopusPublicationAuthorSerializer(serializers.ModelSerializer):
    author = ScopusAuthorSerializer()

    class Meta:
        model = ScopusPublicationAuthor
        fields = ["id", "author", "seq", "is_corresponding"]


class ScopusPublicationSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    journal = ScopusJournalSerializer()

    class Meta:
        model = ScopusPublication
        fields = [
            "id",
            "scopus_id",
            "title",
            "abstract",
            "authors",
            "year",
            "month",
            "day",
            "volume",
            "issue",
            "pages",
            "doi",
            "journal",
            "url",
            "citation_count",
            "source",
            "is_active",
        ]

    @extend_schema_field(ScopusPublicationAuthorSerializer(many=True))
    def get_authors(self, obj):
        publication_authors = obj.scopuspublicationauthor_set.all().order_by("seq")
        return ScopusPublicationAuthorSerializer(publication_authors, many=True).data
