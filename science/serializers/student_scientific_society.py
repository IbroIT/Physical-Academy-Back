from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from ..models import (
    StudentScientificSocietyInfo,
    StudentScientificSocietyStat,
    StudentScientificSocietyFeature,
    StudentScientificSocietyProject,
    StudentScientificSocietyProjectTag,
    StudentScientificSocietyEvent,
    StudentScientificSocietyJoinStep,
    StudentScientificSocietyLeader,
    StudentScientificSocietyContact,
)


class StudentScientificSocietyInfoSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    subtitle = serializers.SerializerMethodField()
    about_title = serializers.SerializerMethodField()
    about_description = serializers.SerializerMethodField()
    projects_title = serializers.SerializerMethodField()
    events_title = serializers.SerializerMethodField()
    join_title = serializers.SerializerMethodField()
    leadership_title = serializers.SerializerMethodField()
    contacts_title = serializers.SerializerMethodField()
    upcoming_events_title = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyInfo
        fields = [
            "id",
            "title",
            "subtitle",
            "about_title",
            "about_description",
            "projects_title",
            "events_title",
            "join_title",
            "leadership_title",
            "contacts_title",
            "upcoming_events_title",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_subtitle(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_subtitle(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_about_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_about_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_about_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_about_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_projects_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_projects_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_events_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_events_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_join_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_join_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_leadership_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_leadership_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_contacts_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_contacts_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_upcoming_events_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_upcoming_events_title(language)


class StudentScientificSocietyStatSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyStat
        fields = ["id", "label", "value"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_label(language)


class StudentScientificSocietyFeatureSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyFeature
        fields = ["id", "title", "description", "icon"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class ProjectTagSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyProjectTag
        fields = ["id", "name"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_name(language)


class StudentScientificSocietyProjectSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    tags = ProjectTagSerializer(many=True, read_only=True)

    class Meta:
        model = StudentScientificSocietyProject
        fields = ["id", "name", "short_description", "description", "icon", "tags"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_short_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_short_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class StudentScientificSocietyEventSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    days_left = serializers.IntegerField(read_only=True)
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyEvent
        fields = [
            "id",
            "name",
            "description",
            "icon",
            "date",
            "time",
            "status",
            "status_display",
            "days_left",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_status_display(self, obj):
        language = self.context.get("language", "ru")
        status_translations = {
            StudentScientificSocietyEvent.UPCOMING: {
                "en": "Upcoming",
                "kg": "Келе жаткан",
                "ru": "Предстоящее",
            },
            StudentScientificSocietyEvent.COMPLETED: {
                "en": "Completed",
                "kg": "Аяктады",
                "ru": "Завершено",
            },
        }
        return status_translations.get(obj.status, {}).get(
            language, status_translations.get(obj.status, {}).get("ru", "")
        )


class StudentScientificSocietyJoinStepSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyJoinStep
        fields = ["id", "step", "title", "description"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class StudentScientificSocietyLeaderSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyLeader
        fields = ["id", "name", "position", "department"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_position(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_position(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_department(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_department(language)


class StudentScientificSocietyContactSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyContact
        fields = ["id", "label", "value", "icon"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj):
        language = self.context.get("language", "ru")
        return obj.get_label(language)


class StudentScientificSocietyPageSerializer(serializers.Serializer):
    """Serializer for the full Student Scientific Society page."""

    info = StudentScientificSocietyInfoSerializer(read_only=True)
    stats = StudentScientificSocietyStatSerializer(many=True, read_only=True)
    about_features = StudentScientificSocietyFeatureSerializer(
        many=True, read_only=True
    )
    projects = StudentScientificSocietyProjectSerializer(many=True, read_only=True)
    events = StudentScientificSocietyEventSerializer(many=True, read_only=True)
    join_steps = StudentScientificSocietyJoinStepSerializer(many=True, read_only=True)
    leadership = StudentScientificSocietyLeaderSerializer(many=True, read_only=True)
    contacts = StudentScientificSocietyContactSerializer(many=True, read_only=True)
    upcoming_events = StudentScientificSocietyEventSerializer(many=True, read_only=True)
