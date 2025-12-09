from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import TabCategory, Card, TimelineEvent, AboutFaculty


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


class TimelineEventSerializer(serializers.ModelSerializer):
    """Сериализатор для событий истории"""

    image = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()

    class Meta:
        model = TimelineEvent
        fields = ["id", "image", "event", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_event(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_event(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_image(self, obj) -> str:
        if not obj.image:
            return None

        try:
            return obj.image.url
        except Exception:
            return str(obj.image)


class TabCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий/табов"""

    title = serializers.SerializerMethodField()

    class Meta:
        model = TabCategory
        fields = ["id", "key", "title", "icon", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_title(language)


class FacultyDataSerializer(serializers.Serializer):
    """Общий сериализатор для всех данных факультета"""

    tabs = TabCategorySerializer(many=True)


class AboutFacultySerializer(serializers.ModelSerializer):
    """Сериализатор для текста 'О факультете'"""

    text = serializers.SerializerMethodField()

    class Meta:
        model = AboutFaculty
        fields = ["id", "text", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_text(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_text(language)
