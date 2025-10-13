from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from ..models import Publication, PublicationTypeOptions


class PublicationSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    abstract = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()
    journal = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()
    pub_type_display = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = [
            "id",
            "title",
            "abstract",
            "authors",
            "year",
            "volume",
            "issue",
            "pages",
            "doi",
            "journal",
            "publisher",
            "url",
            "file",
            "pub_type",
            "pub_type_display",
            "citation_count",
            "is_active",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        return obj.get_title()

    @extend_schema_field(OpenApiTypes.STR)
    def get_abstract(self, obj):
        return obj.get_abstract()

    @extend_schema_field(OpenApiTypes.STR)
    def get_authors(self, obj):
        return obj.get_authors()

    @extend_schema_field(OpenApiTypes.STR)
    def get_journal(self, obj):
        return obj.get_journal()

    @extend_schema_field(OpenApiTypes.STR)
    def get_publisher(self, obj):
        return obj.get_publisher()

    @extend_schema_field(OpenApiTypes.STR)
    def get_pub_type_display(self, obj):
        return PublicationTypeOptions(obj.pub_type).label
