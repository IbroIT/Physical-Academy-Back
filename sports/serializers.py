from rest_framework import serializers
from .models import (
    SportSection,
    SportSectionTranslation,
    TrainingSchedule,
    Achievement,
    AchievementTranslation,
    Infrastructure,
    InfrastructureTranslation,
    InfrastructureCategory,
    InfrastructureCategoryTranslation,
    InfrastructureObject,
    InfrastructureObjectTranslation,
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

    # Поля, которые будут заполнены из переводов
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    contact_info = serializers.CharField(read_only=True)

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

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"

        # Получаем перевод
        translation = instance.translations.filter(language=language).first()

        if not translation:
            # Fallback на русский
            translation = instance.translations.filter(language="ru").first()

        if not translation:
            # Fallback на первый доступный
            translation = instance.translations.first()

        if translation:
            data["name"] = translation.name
            data["description"] = translation.description
            data["contact_info"] = translation.contact_info

        # Добавляем информацию о тренере
        data["coach"] = instance.coach_name
        data["trainer"] = instance.coach_name  # Альтернативное имя
        data["coach_info"] = {
            "name": instance.coach_name,
            "full_name": instance.coach_name,
            "rank": instance.coach_rank,
            "title": instance.coach_rank,
            "contacts": instance.coach_contacts,
            "phone": instance.coach_contacts,
        }

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
    name = serializers.CharField(source="athlete_name", read_only=True)
    description = serializers.CharField(read_only=True)
    details = serializers.JSONField(read_only=True)  # Используем JSONField напрямую

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

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"

        # Получаем перевод
        translation = instance.translations.filter(language=language).first()

        if not translation:
            translation = instance.translations.filter(language="ru").first()

        if not translation:
            translation = instance.translations.first()

        if translation:
            data["description"] = translation.description

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
        data["event_date"] = instance.date.isoformat() if instance.date else None
        data["photo"] = data["image"]

        return data


# ==================== Infrastructure ====================


class InfrastructureObjectTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfrastructureObjectTranslation
        fields = ["name", "description"]


class InfrastructureObjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    features = serializers.JSONField(read_only=True)  # Используем JSONField напрямую
    amenities = serializers.SerializerMethodField()

    class Meta:
        model = InfrastructureObject
        fields = ["id", "name", "description", "image", "features", "amenities"]

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def get_amenities(self, obj):
        """Альтернативное название для features"""
        return obj.features or []

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"

        # Получаем перевод
        translation = instance.translations.filter(language=language).first()

        if not translation:
            translation = instance.translations.filter(language="ru").first()

        if not translation:
            translation = instance.translations.first()

        if translation:
            data["name"] = translation.name
            data["title"] = translation.name
            data["description"] = translation.description

        # features уже в формате JSON
        data["features"] = instance.features or []
        data["amenities"] = instance.features or []

        return data

        if translation:
            data["name"] = translation.name
            data["title"] = translation.name
            data["description"] = translation.description

        return data


class InfrastructureCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    objects = InfrastructureObjectSerializer(many=True, read_only=True)
    items = serializers.SerializerMethodField()

    class Meta:
        model = InfrastructureCategory
        fields = ["id", "slug", "name", "icon", "color", "objects", "items"]

    def get_items(self, obj):
        """Альтернативное название для objects"""
        request = self.context.get("request")
        objects = obj.objects.filter(is_active=True)
        serializer = InfrastructureObjectSerializer(
            objects, many=True, context={"request": request}
        )
        return serializer.data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"

        # Получаем перевод
        translation = instance.translations.filter(language=language).first()

        if not translation:
            translation = instance.translations.filter(language="ru").first()

        if not translation:
            translation = instance.translations.first()

        if translation:
            data["name"] = translation.name
            data["title"] = translation.name

        # Фильтруем активные объекты
        objects = instance.objects.filter(is_active=True)
        data["objects"] = InfrastructureObjectSerializer(
            objects, many=True, context={"request": request}
        ).data

        return data


class InfrastructureSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    stats = serializers.SerializerMethodField()
    categories = InfrastructureCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Infrastructure
        fields = ["name", "title", "description", "badge", "stats", "categories"]

    def get_stats(self, obj):
        """Формируем массив статистики"""
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"

        # Получаем перевод
        translation = obj.translations.filter(language=language).first()

        if not translation:
            translation = obj.translations.filter(language="ru").first()

        if not translation:
            translation = obj.translations.first()

        if translation:
            return [
                {
                    "label": translation.stat_1_label,
                    "value": obj.stat_1_value,
                    "icon": obj.stat_1_icon,
                },
                {
                    "label": translation.stat_2_label,
                    "value": obj.stat_2_value,
                    "icon": obj.stat_2_icon,
                },
                {
                    "label": translation.stat_3_label,
                    "value": obj.stat_3_value,
                    "icon": obj.stat_3_icon,
                },
                {
                    "label": translation.stat_4_label,
                    "value": obj.stat_4_value,
                    "icon": obj.stat_4_icon,
                },
            ]
        return []

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"

        # Получаем перевод
        translation = instance.translations.filter(language=language).first()

        if not translation:
            translation = instance.translations.filter(language="ru").first()

        if not translation:
            translation = instance.translations.first()

        if translation:
            data["name"] = translation.name
            data["title"] = translation.name
            data["description"] = translation.description

        return data
