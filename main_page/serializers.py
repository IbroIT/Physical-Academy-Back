from rest_framework import serializers
from .models import (
    AcademyInfrastructure,
    AcademyStatistics,
    AcademyAchievements,
    Accreditation,
    AccreditationType,
    Mission,
    MissionCategory,
    aboutStatistics,
    AboutPhotos,
    ImportantDates,
    HistoryStep,
)


class AboutStatisticsSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = aboutStatistics
        fields = ["id", "titleInt", "description", "emoji"]

    def get_description(self, obj):
        return obj.get_description(self.context.get("language", "ru"))


class AboutPhotosSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = AboutPhotos
        fields = ["id", "photo", "description"]

    def get_description(self, obj):
        return obj.get_description(self.context.get("language", "ru"))


class HistoryStepSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()

    class Meta:
        model = HistoryStep
        fields = [
            "id",
            "year",
            "title",
            "description",
            "buildings",
            "students",
            "programs",
            "achievements",
        ]

    def get_title(self, obj):
        return obj.get_title(self.context.get("language", "ru"))

    def get_description(self, obj):
        return obj.get_description(self.context.get("language", "ru"))

    def get_achievements(self, obj):
        language = self.context.get("language", "ru")
        return (
            obj.achievements_ru
            if language == "ru"
            else obj.achievements_en if language == "en" else obj.achievements_kg
        )


class ImportantDatesSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = ImportantDates
        fields = ["id", "year", "titleInt", "description"]

    def get_description(self, obj):
        return obj.get_description(self.context.get("language", "ru"))


class MissionCategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = MissionCategory
        fields = ["id", "name"]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)


class MissionSerializer(serializers.ModelSerializer):
    category = MissionCategorySerializer(read_only=True)
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Mission
        fields = ["id", "category", "title", "description"]

    def get_title(self, obj):
        return obj.get_title(self.context.get("language", "ru"))

    def get_description(self, obj):
        return obj.get_description(self.context.get("language", "ru"))


class AccreditationTypeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = AccreditationType
        fields = ["id", "name"]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)


class AccreditationSerializer(serializers.ModelSerializer):
    accreditation_type = AccreditationTypeSerializer(read_only=True)
    organization = serializers.SerializerMethodField()
    validity = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Accreditation
        fields = [
            "id",
            "accreditation_type",
            "organization",
            "validity",
            "description",
            "photo",
            "logo",
            "certificate_number",
        ]

    def get_organization(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_organization(lang)

    def get_validity(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_validity(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)


class AcademyStatisticsSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = AcademyStatistics
        fields = ["id", "title", "description", "titleInt"]

    def get_title(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_title(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)


class AcademyAchievementsSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = AcademyAchievements
        fields = [
            "title",
            "description",
            "year",
        ]

    def get_title(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_title(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)


class AcademyInfrastructureSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = AcademyInfrastructure
        fields = ["id", "titleInt", "description", "emoji"]

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)
