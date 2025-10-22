from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from ..models import (
    ScientificDirection,
    DissertationCouncil,
    DissertationSpecialization,
    DissertationDefense,
    DissertationSecretary,
    DissertationCouncilDocuments,
    DissertationCouncilAdminStaff,
    ConferenceNotice,
    Vestnik,
    VestnikIssue,
)


class ScientificDirectionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = ScientificDirection
        fields = ["id", "name", "description", "is_active"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        return obj.get_name()

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        return obj.get_description()


class DissertationSpecializationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    degree = serializers.SerializerMethodField()

    class Meta:
        model = DissertationSpecialization
        fields = ["id", "code", "name", "degree"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        return obj.get_name()

    @extend_schema_field(OpenApiTypes.STR)
    def get_degree(self, obj):
        return obj.get_degree()


class DissertationSecretarySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()

    class Meta:
        model = DissertationSecretary
        fields = [
            "id",
            "name",
            "position",
            "bio",
            "email",
            "phone",
            "photo",
            "is_active",
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


class DissertationCouncilSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    specializations = DissertationSpecializationSerializer(many=True)
    secretary = DissertationSecretarySerializer()

    class Meta:
        model = DissertationCouncil
        fields = [
            "id",
            "name",
            "description",
            "secretary",
            "specializations",
            "order_number",
            "from_date",
            "to_date",
            "is_active",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        return obj.get_name()

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        return obj.get_description()


class DissertationCouncilDocumentsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = DissertationCouncilDocuments
        fields = ["id", "name", "description", "file", "is_active"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        return obj.get_name()

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        return obj.get_description()


class DissertationCouncilAdminStaffSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()

    class Meta:
        model = DissertationCouncilAdminStaff
        fields = [
            "id",
            "name",
            "position",
            "bio",
            "email",
            "phone",
            "photo",
            "is_active",
            "council",
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


class DissertationDefenseSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    applicant = serializers.SerializerMethodField()
    abstract = serializers.SerializerMethodField()
    specializations = DissertationSpecializationSerializer(many=True)
    council = DissertationCouncilSerializer()

    class Meta:
        model = DissertationDefense
        fields = [
            "id",
            "title",
            "applicant",
            "abstract",
            "specializations",
            "defense_date",
            "council",
            "dissertation_file",
            "abstract_file",
            "is_active",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        return obj.get_title()

    @extend_schema_field(OpenApiTypes.STR)
    def get_applicant(self, obj):
        return obj.get_applicant()

    @extend_schema_field(OpenApiTypes.STR)
    def get_abstract(self, obj):
        return obj.get_abstract()


class ConferenceNoticeSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = ConferenceNotice
        fields = [
            "id",
            "title",
            "description",
            "start_date",
            "end_date",
            "registration_deadline",
            "location",
            "organizer",
            "website",
            "is_active",
            "file",
            "contact_email",
            "contact_phone",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        return obj.get_title()

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        return obj.get_description()


class VestnikSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    issn = serializers.CharField()

    class Meta:
        model = Vestnik
        fields = ["id", "title", "description", "issn", "image", "is_active"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        return obj.get_title()

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        return obj.get_description()


class VestnikIssueSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    # Remove vestnik field as it doesn't appear to be in the model
    # vestnik = VestnikSerializer()

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
            "cover_image",
            "is_featured",
            "is_published",
            "publication_date",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        if language == "kg" and obj.title_kg:
            return obj.title_kg
        elif language == "en" and obj.title_en:
            return obj.title_en
        return obj.title_ru

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        language = self.context.get("language", "ru")
        if language == "kg" and obj.description_kg:
            return obj.description_kg
        elif language == "en" and obj.description_en:
            return obj.description_en
        return obj.description_ru
