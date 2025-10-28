from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from .models import (
    SportSection,
    TrainingSchedule,
    Achievement,
    Infrastructure,
    InfrastructureCategory,
    InfrastructureObject,
)


# ==================== Sport Sections ====================


class TrainingScheduleSerializer(serializers.ModelSerializer):
    day = serializers.CharField(source="get_day_of_week_display", read_only=True)

    class Meta:
        model = TrainingSchedule
        fields = ["day", "time_start", "time_end", "location"]


class SportSectionSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    training_schedule_details = TrainingScheduleSerializer(
        source="training_schedules", many=True, read_only=True
    )

    # Поля, которые будут заполнены через SerializerMethodField
    coach_info = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    contact_info = serializers.SerializerMethodField()

    class Meta:
        model = SportSection
        fields = [
            "id",
            "name",
            "sport_type",
            "image",
            "schedule",
            "description",
            "contact_info",
            "coach_info",
            "training_schedule_details",
        ]

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def get_coach_info(self, obj):
        return {
            "name": obj.coach_name,
            "full_name": obj.coach_name,
            "rank": obj.coach_rank,
            "title": obj.coach_rank,
            "contacts": obj.coach_contacts,
            "phone": obj.coach_contacts,
        }

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        """Получить название секции на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание секции на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_contact_info(self, obj) -> str:
        """Получить контактную информацию на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_contact_info(language)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Добавляем дополнительные поля для совместимости
        data["coach"] = instance.coach_name
        data["trainer"] = instance.coach_name

        # Форматируем расписание тренировок
        schedules = instance.training_schedules.all()
        if schedules:
            data["training_schedule_details"] = [
                {
                    "day": schedule.get_day_of_week_display(),
                    "time": f"{schedule.time_start.strftime('%H:%M')}-{schedule.time_end.strftime('%H:%M')}",
                    "location": schedule.location,
                }
                for schedule in schedules
            ]
        else:
            data["training_schedule_details"] = []

        return data


# ==================== Achievements ====================


class AchievementSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Achievement
        fields = [
            "id",
            "athlete_name",
            "sport",
            "competition",
            "result",
            "date",
            "image",
            "photo",
            "description",
            "category",
            "details",
        ]

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def get_photo(self, obj):
        # Альтернативное имя для image
        return self.get_image(obj)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание достижения на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Добавляем альтернативные имена полей для совместимости
        data["name"] = instance.athlete_name
        data["athlete_name"] = instance.athlete_name
        data["sport_type"] = instance.sport
        data["event"] = instance.competition
        data["place"] = instance.result
        data["achievement"] = instance.result
        data["event_date"] = instance.date.isoformat() if instance.date else None
        data["photo"] = data["image"]

        # details уже в формате JSON, просто используем как есть
        data["details"] = instance.details or {}

        return data


# ==================== Infrastructure ====================


class InfrastructureObjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    features = serializers.JSONField(read_only=True)
    amenities = serializers.SerializerMethodField()

    class Meta:
        model = InfrastructureObject
        fields = ["id", "name", "description", "image", "features", "amenities"]

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        """Получить название объекта на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание объекта на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    def get_amenities(self, obj):
        """Альтернативное название для features"""
        return obj.features or []

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Добавляем альтернативное имя для name
        data["title"] = data["name"]

        # features уже в формате JSON
        data["features"] = instance.features or []
        data["amenities"] = instance.features or []

        return data


class InfrastructureCategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    objects = InfrastructureObjectSerializer(many=True, read_only=True)
    items = serializers.SerializerMethodField()

    class Meta:
        model = InfrastructureCategory
        fields = ["id", "slug", "name", "icon", "color", "objects", "items"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        """Получить название категории на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    def get_items(self, obj):
        """Альтернативное название для objects"""
        language = self.context.get("language", "ru")
        objects = obj.objects.filter(is_active=True)
        serializer = InfrastructureObjectSerializer(
            objects, many=True, context={"language": language}
        )
        return serializer.data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        language = self.context.get("language", "ru")

        # Добавляем альтернативное имя для name
        data["title"] = data["name"]

        # Фильтруем активные объекты
        objects = instance.objects.filter(is_active=True)
        data["objects"] = InfrastructureObjectSerializer(
            objects, many=True, context={"language": language}
        ).data

        return data


class InfrastructureSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    stats = serializers.SerializerMethodField()
    categories = InfrastructureCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Infrastructure
        fields = ["name", "title", "description", "badge", "stats", "categories"]

    @extend_schema_field(OpenApiTypes.STR)
    def get_name(self, obj) -> str:
        """Получить название инфраструктуры на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_title(self, obj) -> str:
        """Получить название инфраструктуры на нужном языке (альтернатива)"""
        language = self.context.get("language", "ru")
        return obj.get_name(language)

    @extend_schema_field(OpenApiTypes.STR)
    def get_description(self, obj) -> str:
        """Получить описание инфраструктуры на нужном языке"""
        language = self.context.get("language", "ru")
        return obj.get_description(language)

    def get_stats(self, obj):
        """Формируем массив статистики"""
        language = self.context.get("language", "ru")

        return [
            {
                "label": obj.get_stat_label(1, language),
                "value": obj.stat_1_value,
                "icon": obj.stat_1_icon,
            },
            {
                "label": obj.get_stat_label(2, language),
                "value": obj.stat_2_value,
                "icon": obj.stat_2_icon,
            },
            {
                "label": obj.get_stat_label(3, language),
                "value": obj.stat_3_value,
                "icon": obj.stat_3_icon,
            },
            {
                "label": obj.get_stat_label(4, language),
                "value": obj.stat_4_value,
                "icon": obj.stat_4_icon,
            },
        ]
