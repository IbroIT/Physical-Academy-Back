from rest_framework import serializers
from django.utils.translation import get_language
from drf_spectacular.utils import extend_schema_field

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

    @extend_schema_field(serializers.CharField())
    def get_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.title_en:
            return obj.title_en
        elif lang == "kg" and obj.title_kg:
            return obj.title_kg
        return obj.title_ru

    @extend_schema_field(serializers.CharField())
    def get_subtitle(self, obj):
        lang = get_language()
        if lang == "en" and obj.subtitle_en:
            return obj.subtitle_en
        elif lang == "kg" and obj.subtitle_kg:
            return obj.subtitle_kg
        return obj.subtitle_ru

    @extend_schema_field(serializers.CharField())
    def get_about_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.about_title_en:
            return obj.about_title_en
        elif lang == "kg" and obj.about_title_kg:
            return obj.about_title_kg
        return obj.about_title_ru

    @extend_schema_field(serializers.CharField())
    def get_about_description(self, obj):
        lang = get_language()
        if lang == "en" and obj.about_description_en:
            return obj.about_description_en
        elif lang == "kg" and obj.about_description_kg:
            return obj.about_description_kg
        return obj.about_description_ru

    @extend_schema_field(serializers.CharField())
    def get_projects_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.projects_title_en:
            return obj.projects_title_en
        elif lang == "kg" and obj.projects_title_kg:
            return obj.projects_title_kg
        return obj.projects_title_ru

    @extend_schema_field(serializers.CharField())
    def get_events_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.events_title_en:
            return obj.events_title_en
        elif lang == "kg" and obj.events_title_kg:
            return obj.events_title_kg
        return obj.events_title_ru

    @extend_schema_field(serializers.CharField())
    def get_join_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.join_title_en:
            return obj.join_title_en
        elif lang == "kg" and obj.join_title_kg:
            return obj.join_title_kg
        return obj.join_title_ru

    @extend_schema_field(serializers.CharField())
    def get_leadership_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.leadership_title_en:
            return obj.leadership_title_en
        elif lang == "kg" and obj.leadership_title_kg:
            return obj.leadership_title_kg
        return obj.leadership_title_ru

    @extend_schema_field(serializers.CharField())
    def get_contacts_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.contacts_title_en:
            return obj.contacts_title_en
        elif lang == "kg" and obj.contacts_title_kg:
            return obj.contacts_title_kg
        return obj.contacts_title_ru

    @extend_schema_field(serializers.CharField())
    def get_upcoming_events_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.upcoming_events_title_en:
            return obj.upcoming_events_title_en
        elif lang == "kg" and obj.upcoming_events_title_kg:
            return obj.upcoming_events_title_kg
        return obj.upcoming_events_title_ru


class StudentScientificSocietyStatSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyStat
        fields = ["id", "label", "value"]

    @extend_schema_field(serializers.CharField())
    def get_label(self, obj):
        lang = get_language()
        if lang == "en" and obj.label_en:
            return obj.label_en
        elif lang == "kg" and obj.label_kg:
            return obj.label_kg
        return obj.label_ru


class StudentScientificSocietyFeatureSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyFeature
        fields = ["id", "title", "description", "icon"]

    @extend_schema_field(serializers.CharField())
    def get_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.title_en:
            return obj.title_en
        elif lang == "kg" and obj.title_kg:
            return obj.title_kg
        return obj.title_ru

    @extend_schema_field(serializers.CharField())
    def get_description(self, obj):
        lang = get_language()
        if lang == "en" and obj.description_en:
            return obj.description_en
        elif lang == "kg" and obj.description_kg:
            return obj.description_kg
        return obj.description_ru


class ProjectTagSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyProjectTag
        fields = ["id", "name"]

    @extend_schema_field(serializers.CharField())
    def get_name(self, obj):
        lang = get_language()
        if lang == "en" and obj.name_en:
            return obj.name_en
        elif lang == "kg" and obj.name_kg:
            return obj.name_kg
        return obj.name_ru


class StudentScientificSocietyProjectSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    tags = ProjectTagSerializer(many=True, read_only=True)

    class Meta:
        model = StudentScientificSocietyProject
        fields = ["id", "name", "short_description", "description", "icon", "tags"]

    @extend_schema_field(serializers.CharField())
    def get_name(self, obj):
        lang = get_language()
        if lang == "en" and obj.name_en:
            return obj.name_en
        elif lang == "kg" and obj.name_kg:
            return obj.name_kg
        return obj.name_ru

    @extend_schema_field(serializers.CharField())
    def get_short_description(self, obj):
        lang = get_language()
        if lang == "en" and obj.short_description_en:
            return obj.short_description_en
        elif lang == "kg" and obj.short_description_kg:
            return obj.short_description_kg
        return obj.short_description_ru

    @extend_schema_field(serializers.CharField())
    def get_description(self, obj):
        lang = get_language()
        if lang == "en" and obj.description_en:
            return obj.description_en
        elif lang == "kg" and obj.description_kg:
            return obj.description_kg
        return obj.description_ru


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

    @extend_schema_field(serializers.CharField())
    def get_name(self, obj):
        lang = get_language()
        if lang == "en" and obj.name_en:
            return obj.name_en
        elif lang == "kg" and obj.name_kg:
            return obj.name_kg
        return obj.name_ru

    @extend_schema_field(serializers.CharField())
    def get_description(self, obj):
        lang = get_language()
        if lang == "en" and obj.description_en:
            return obj.description_en
        elif lang == "kg" and obj.description_kg:
            return obj.description_kg
        return obj.description_ru

    @extend_schema_field(serializers.CharField())
    def get_status_display(self, obj):
        lang = get_language()
        if obj.status == StudentScientificSocietyEvent.UPCOMING:
            if lang == "en":
                return "Upcoming"
            elif lang == "kg":
                return "Келе жаткан"
            return "Предстоящее"
        else:
            if lang == "en":
                return "Completed"
            elif lang == "kg":
                return "Аяктады"
            return "Завершено"


class StudentScientificSocietyJoinStepSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyJoinStep
        fields = ["id", "step", "title", "description"]

    @extend_schema_field(serializers.CharField())
    def get_title(self, obj):
        lang = get_language()
        if lang == "en" and obj.title_en:
            return obj.title_en
        elif lang == "kg" and obj.title_kg:
            return obj.title_kg
        return obj.title_ru

    @extend_schema_field(serializers.CharField())
    def get_description(self, obj):
        lang = get_language()
        if lang == "en" and obj.description_en:
            return obj.description_en
        elif lang == "kg" and obj.description_kg:
            return obj.description_kg
        return obj.description_ru


class StudentScientificSocietyLeaderSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyLeader
        fields = ["id", "name", "position", "department"]

    @extend_schema_field(serializers.CharField())
    def get_name(self, obj):
        lang = get_language()
        if lang == "en" and obj.name_en:
            return obj.name_en
        elif lang == "kg" and obj.name_kg:
            return obj.name_kg
        return obj.name_ru

    @extend_schema_field(serializers.CharField())
    def get_position(self, obj):
        lang = get_language()
        if lang == "en" and obj.position_en:
            return obj.position_en
        elif lang == "kg" and obj.position_kg:
            return obj.position_kg
        return obj.position_ru

    @extend_schema_field(serializers.CharField())
    def get_department(self, obj):
        lang = get_language()
        if lang == "en" and obj.department_en:
            return obj.department_en
        elif lang == "kg" and obj.department_kg:
            return obj.department_kg
        return obj.department_ru


class StudentScientificSocietyContactSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    class Meta:
        model = StudentScientificSocietyContact
        fields = ["id", "label", "value", "icon"]

    @extend_schema_field(serializers.CharField())
    def get_label(self, obj):
        lang = get_language()
        if lang == "en" and obj.label_en:
            return obj.label_en
        elif lang == "kg" and obj.label_kg:
            return obj.label_kg
        return obj.label_ru


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
