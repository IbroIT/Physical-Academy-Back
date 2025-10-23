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

    class Meta:
        model = NTSCommitteeRole
        fields = ["id", "name"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_name(language)


class NTSResearchDirectionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = NTSResearchDirection
        fields = ["id", "name", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class NTSCommitteeMemberSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

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
            "is_active",
            "order",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_position(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_position(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_bio(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_bio(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_role(self, obj):
        language = self.context.get("language", "ru")
        if obj.role:
            return obj.role.get_name(language)
        return ""


class NTSCommitteeSectionSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = NTSCommitteeSection
        fields = ["id", "section_key", "title", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_description(language)
