from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from ..models import Publication, PublicationTypeOptions


class PublicationSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    abstract = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()
    # Backwards-compatible single-author field used by frontend
    author = serializers.SerializerMethodField()
    journal = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()
    pub_type_display = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = [
            "id",
            "title",
            "abstract",
            "authors",
            "author",
            "year",
            "publication_date",
            "pdf_url",
            "image_url",
            "year",
            # "volume",
            # "issue",
            # "pages",
            "doi",
            "journal",
            "publisher",
            "url",
            # "file",
            # "pub_type",
            "publication_type",
            "pub_type_display",
            "citation_count",
            "impact_factor",
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
        return PublicationTypeOptions(obj.publication_type).label

    @extend_schema_field(OpenApiTypes.STR)
    def get_pdf_url(self, obj):
        if obj.pdf_file:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.pdf_file.url)
        return None

    @extend_schema_field(OpenApiTypes.STR)
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
        return None

    @extend_schema_field(OpenApiTypes.STR)
    def get_author(self, obj):
        # keep compatibility with frontend which expects `author`
        return obj.get_authors()
