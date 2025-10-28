from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import (
    SportSection,
    TrainingSchedule,
    Achievement,
    Infrastructure,
    InfrastructureStatistic,
    InfrastructureCategory,
    InfrastructureObject,
)
from django.utils import translation


# ==================== Sport Sections ====================


class TrainingScheduleSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = TrainingSchedule
        fields = ["day", "time_start", "time_end", "location"]

    def get_location(self, obj):
        request = self.context.get("request")
        language = self.context.get("language") or (
            request.query_params.get("language") if request else "ru"
        )
        return obj.get_location(language)

    def get_day(self, obj):
        request = self.context.get("request")
        language = self.context.get("language") or (
            request.query_params.get("language") if request else "ru"
        )
        prev = translation.get_language()
        try:
            translation.activate(language)
            return obj.get_day_of_week_display()
        finally:
            translation.activate(prev)


class SportSectionSerializer(serializers.ModelSerializer):
    """Сериализатор для спортивных секций с многоязычной поддержкой"""

    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    contact_info = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    schedule = serializers.SerializerMethodField()
    training_schedule_details = TrainingScheduleSerializer(
        source="training_schedules", many=True, read_only=True
    )
    coach_info = serializers.SerializerMethodField()
    # Compatibility fields expected by frontend
    coach = serializers.CharField(source="coach_name", read_only=True)
    trainer = serializers.CharField(source="coach_name", read_only=True)

    class Meta:
        model = SportSection
        fields = [
            "id",
            "name",
            "sport_type",
            "image",
            "coach",
            "trainer",
            "schedule",
            "description",
            "contact_info",
            "coach_info",
            "training_schedule_details",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_contact_info(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_contact_info(language)

    def get_image(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    def get_coach_info(self, obj):
        request = self.context.get("request")
        language = self.context.get("language") or (
            request.query_params.get("language") if request else "ru"
        )
        return {
            "name": obj.get_coach_name(language),
            "full_name": obj.get_coach_name(language),
            "rank": obj.get_coach_rank(language),
            "title": obj.get_coach_rank(language),
            "contacts": obj.coach_contacts,
            "phone": obj.coach_contacts,
        }

    @extend_schema_field(OpenApiTypes.STR)
    def get_schedule(self, obj):
        request = self.context.get("request")
        language = self.context.get("language") or (
            request.query_params.get("language") if request else "ru"
        )
        return obj.get_schedule(language)

    def to_representation(self, instance):
        # Получаем язык из контекста
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"
        self.context["language"] = language

        data = super().to_representation(instance)

        # Добавляем альтернативные имена полей
        data["coach"] = instance.get_coach_name(language)
        data["trainer"] = instance.get_coach_name(language)
        # Локализованное расписание
        data["schedule"] = instance.get_schedule(language)

        return data


# ==================== Achievements ====================


class AchievementSerializer(serializers.ModelSerializer):
    """Сериализатор для спортивных достижений с многоязычной поддержкой"""

    description = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    name = serializers.CharField(source="athlete_name", read_only=True)

    class Meta:
        model = Achievement
        fields = [
            "id",
            "name",
            "athlete_name",
            "sport",
            "sport_type",
            "competition",
            "event",
            "result",
            "place",
            "achievement",
            "date",
            "event_date",
            "image",
            "photo",
            "description",
            "category",
            "details",
        ]

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    def get_image(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    def to_representation(self, instance):
        # Получаем язык из контекста
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"
        self.context["language"] = language

        data = super().to_representation(instance)

        # Добавляем альтернативные имена полей для совместимости с фронтендом
        data["name"] = instance.athlete_name
        data["athlete_name"] = instance.athlete_name
        data["sport_type"] = instance.sport
        data["event"] = instance.competition
        data["place"] = instance.result
        data["achievement"] = instance.result
        data["event_date"] = instance.date.isoformat() if instance.date else None
        data["photo"] = data["image"]

        return data


# ==================== Infrastructure ====================


class InfrastructureStatisticSerializer(serializers.ModelSerializer):
    """Сериализатор для статистики инфраструктуры"""

    label = serializers.SerializerMethodField()

    class Meta:
        model = InfrastructureStatistic
        fields = ["id", "label", "value", "icon", "order"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_label(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_label(language)


class InfrastructureObjectSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов инфраструктуры"""

    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    amenities = serializers.SerializerMethodField()

    class Meta:
        model = InfrastructureObject
        fields = ["id", "name", "description", "image", "features", "amenities"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    def get_image(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    def get_amenities(self, obj):
        """Альтернативное название для features"""
        return obj.features or []

    def to_representation(self, instance):
        # Получаем язык из контекста
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"
        self.context["language"] = language

        data = super().to_representation(instance)

        # Добавляем альтернативные имена
        data["title"] = data["name"]

        return data


class InfrastructureCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий инфраструктуры"""

    name = serializers.SerializerMethodField()
    objects = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = InfrastructureCategory
        fields = ["id", "slug", "name", "icon", "color", "objects", "items"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    def get_objects(self, obj):
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"

        active_objects = obj.objects.filter(is_active=True)
        serializer = InfrastructureObjectSerializer(
            active_objects,
            many=True,
            context={"request": request, "language": language},
        )
        return serializer.data

    def get_items(self, obj):
        """Альтернативное название для objects"""
        return self.get_objects(obj)

    def to_representation(self, instance):
        # Получаем язык из контекста
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"
        self.context["language"] = language

        data = super().to_representation(instance)

        # Добавляем альтернативные имена
        data["title"] = data["name"]

        return data


class InfrastructureSerializer(serializers.ModelSerializer):
    """Сериализатор для спортивной инфраструктуры"""

    name = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    stats = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Infrastructure
        fields = ["name", "title", "description", "badge", "stats", "categories"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        """Альтернативное название для name"""
        return self.get_name(obj)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    def get_stats(self, obj):
        """Получаем статистику из связанной модели InfrastructureStatistic"""
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"

        active_stats = obj.statistics.filter(is_active=True).order_by("order")
        serializer = InfrastructureStatisticSerializer(
            active_stats, many=True, context={"request": request, "language": language}
        )
        return serializer.data

    def get_categories(self, obj):
        """Получаем категории инфраструктуры"""
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"

        categories = obj.categories.all().order_by("order")
        serializer = InfrastructureCategorySerializer(
            categories, many=True, context={"request": request, "language": language}
        )
        return serializer.data

    def to_representation(self, instance):
        # Получаем язык из контекста
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"
        self.context["language"] = language

        data = super().to_representation(instance)

        return data
