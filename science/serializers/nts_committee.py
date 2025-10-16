from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from ..models import (
    NTSCommitteeMember,
    NTSCommitteeRole,
    NTSResearchDirection,
    NTSCommitteeSection,
)


class NTSCommitteeRoleSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = NTSCommitteeRole
        fields = ["id", "name", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        return obj.get_name()

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        return obj.get_description()


class NTSResearchDirectionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = NTSResearchDirection
        fields = ["id", "name", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        return obj.get_name()

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        return obj.get_description()


class NTSCommitteeMemberSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    role = NTSCommitteeRoleSerializer(allow_null=True, read_only=True)
    # Убираем неиспользуемое поле research_direction
    # research_direction = NTSResearchDirectionSerializer()

    class Meta:
        model = NTSCommitteeMember
        fields = [
            "id",
            "name",
            "position",
            "bio",
            "email",
            "phone",
            "photo",
            "role",
            # "research_direction", # Убираем поле, которого нет в модели
            "is_active",
            "order",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        return obj.get_name()

    @extend_schema_field(OpenApiTypes.STR)
    def get_position(self, obj):
        return obj.get_position()

    @extend_schema_field(OpenApiTypes.STR)
    def get_bio(self, obj):
        return obj.get_bio()


class NTSCommitteeSectionSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = NTSCommitteeSection
        fields = ["id", "section_key", "title", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        return obj.get_title()

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        return obj.get_description()
