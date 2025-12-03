from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import TabCategory, Card, TimelineEvent


class CardSerializer(serializers.ModelSerializer):
    """Сериализатор для карточек"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ["id", "title", "description", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)


class TabCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий/табов с карточками"""

    title = serializers.SerializerMethodField()
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = TabCategory
        fields = ["id", "key", "title", "icon", "order", "cards"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_title(language)

    def to_representation(self, instance):
        language = self.context.get("language", "ru")
        self.fields["cards"].context.update({"language": language})
        return super().to_representation(instance)


class TimelineEventSerializer(serializers.ModelSerializer):
    """Сериализатор для событий истории"""

    event = serializers.SerializerMethodField()

    class Meta:
        model = TimelineEvent
        fields = ["id", "year", "event", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_event(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_event(language)


class FacultyDataSerializer(serializers.Serializer):
    """Общий сериализатор для всех данных факультета"""

    tabs = TabCategorySerializer(many=True)
    timeline = TimelineEventSerializer(many=True)
