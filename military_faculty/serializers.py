from rest_framework import serializers
from .models import TabCategory, Card, TimelineEvent


class CardSerializer(serializers.ModelSerializer):
    """Сериализатор для карточек"""

    class Meta:
        model = Card
        fields = ["id", "title", "description", "order"]


class TabCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий/табов с карточками"""

    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = TabCategory
        fields = ["id", "key", "title", "icon_svg", "order", "cards"]


class TimelineEventSerializer(serializers.ModelSerializer):
    """Сериализатор для событий истории"""

    class Meta:
        model = TimelineEvent
        fields = ["id", "year", "event", "order"]


class FacultyDataSerializer(serializers.Serializer):
    """Общий сериализатор для всех данных факультета"""

    tabs = TabCategorySerializer(many=True)
    timeline = TimelineEventSerializer(many=True)
