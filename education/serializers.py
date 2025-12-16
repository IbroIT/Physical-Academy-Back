from rest_framework import serializers
from .models import (
    CollegePrograms,
    PhdPrograms,
    MasterPrograms,
)


class MasterProgramsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = MasterPrograms
        fields = [
            "id",
            "emoji",
            "name",
            "description",
            "features",
            "duration_years",
            "offline",
            "tuition_fee",
        ]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)

    def get_features(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_features(lang)


class CollegeProgramsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = CollegePrograms
        fields = [
            "id",
            "emoji",
            "name",
            "description",
            "features",
            "duration_years",
            "offline",
            "tuition_fee",
        ]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)

    def get_features(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_features(lang)


class PhdProgramsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()

    class Meta:
        model = PhdPrograms
        fields = [
            "id",
            "emoji",
            "name",
            "description",
            "features",
            "duration_years",
            "offline",
            "tuition_fee",
        ]

    def get_name(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_name(lang)

    def get_description(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_description(lang)

    def get_features(self, obj):
        lang = self.context.get("language", "ru")
        return obj.get_features(lang)
