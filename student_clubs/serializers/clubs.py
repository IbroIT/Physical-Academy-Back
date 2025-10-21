from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from ..models import Club, ClubCategory, ClubLeader, ClubStats


class ClubCategorySerializer(serializers.ModelSerializer):
    """Сериализатор категорий с поддержкой языков"""

    name = serializers.SerializerMethodField()

    class Meta:
        model = ClubCategory
        fields = ["id", "slug", "name", "name_ru", "name_en", "name_kg", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        """Возвращает название на языке из контекста запроса"""
        language = self.context.get("language", "ru")
        return obj.get_name(language)


class ClubLeaderSerializer(serializers.ModelSerializer):
    """Сериализатор руководителей клубов"""

    name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = ClubLeader
        fields = [
            "id",
            "name",
            "role",
            "email",
            "phone",
            "photo",
            "name_ru",
            "name_en",
            "name_kg",
            "role_ru",
            "role_en",
            "role_kg",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("name", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_role(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("role", language)


class ClubListSerializer(serializers.ModelSerializer):
    """Краткий сериализатор для списка клубов"""

    category = ClubCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ClubCategory.objects.all(), source="category", write_only=True
    )

    name = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    meetings = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = [
            "id",
            "category",
            "category_id",
            "icon",
            "status",
            "members_count",
            "name",
            "short_description",
            "description",
            "meetings",
            "tags",
            "join_link",
            "created_at",
            "updated_at",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("name", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_short_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("short_description", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("description", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_meetings(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("meetings", language)


class ClubDetailSerializer(serializers.ModelSerializer):
    """Полный сериализатор клуба со всеми деталями"""

    category = ClubCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ClubCategory.objects.all(), source="category", write_only=True
    )
    leaders = ClubLeaderSerializer(many=True, read_only=True)

    # Локализованные поля
    name = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    goals = serializers.SerializerMethodField()
    motivation = serializers.SerializerMethodField()
    meetings = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = [
            "id",
            "category",
            "category_id",
            "icon",
            "status",
            "members_count",
            "name",
            "short_description",
            "description",
            "goals",
            "motivation",
            "meetings",
            "tags",
            "join_link",
            "leaders",
            "created_at",
            "updated_at",
            # Исходные поля для админки
            "name_ru",
            "name_en",
            "name_kg",
            "short_description_ru",
            "short_description_en",
            "short_description_kg",
            "description_ru",
            "description_en",
            "description_kg",
            "goals_ru",
            "goals_en",
            "goals_kg",
            "motivation_ru",
            "motivation_en",
            "motivation_kg",
            "meetings_ru",
            "meetings_en",
            "meetings_kg",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("name", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_short_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("short_description", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("description", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_goals(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("goals", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_motivation(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("motivation", language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_meetings(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_field("meetings", language)


class ClubStatsSerializer(serializers.ModelSerializer):
    """Сериализатор статистики клубов"""

    label = serializers.SerializerMethodField()

    class Meta:
        model = ClubStats
        fields = ["id", "value", "label", "icon", "order", "is_active"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_label(language)
