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

# Map known seeded Russian placeholder strings to localized labels.
# This avoids showing untranslated placeholder text coming from demo data.
_PLACEHOLDER_MAP = {
    "Имя спортсмена/команды:": {
        "ru": "Имя спортсмена/команды:",
        "en": "Athlete name:",
        "kg": "Спортчу аты:",
    },
    "Вид спорта:": {"ru": "Вид спорта:", "en": "Sport:", "kg": "Спорт:"},
    "Соревнование:": {"ru": "Соревнование:", "en": "Competition:", "kg": "Мелдешүү:"},
    "Результат:": {"ru": "Результат:", "en": "Result:", "kg": "Жыйынтык:"},
    "Описание достижения (RU):": {
        "ru": "Описание достижения (RU):",
        "en": "Achievement description:",
        "kg": "Сипаттамасы:",
    },
}


def _localize_placeholder(value, language="ru"):
    """If value matches a known RU placeholder, return a small in-code localized string.

    This is a pragmatic fallback for seeded/demo content that stored Russian labels
    in model text fields. If the value is not a known placeholder, return it unchanged.
    """
    if not value:
        return value
    # Work with plain strings only
    try:
        s = str(value).strip()
    except Exception:
        return value

    if s in _PLACEHOLDER_MAP:
        return _PLACEHOLDER_MAP[s].get(language, _PLACEHOLDER_MAP[s].get("ru"))
    return value


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
    name = serializers.SerializerMethodField()
    athlete_name = serializers.SerializerMethodField()
    # Compatibility fields - these are added in to_representation
    sport_type = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()
    place = serializers.SerializerMethodField()
    achievement = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    event_date = serializers.SerializerMethodField()

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
        """Return localized description (handles seeded placeholder values)."""
        request = self.context.get("request")
        language = self.context.get("language", None) or (
            request.query_params.get("language") if request else "ru"
        )
        raw = obj.get_description(language)
        return _localize_placeholder(raw, language)

    def get_name(self, obj):
        request = self.context.get("request")
        language = self.context.get("language", None) or (
            request.query_params.get("language") if request else "ru"
        )
        raw = obj.get_name(language)
        return _localize_placeholder(raw, language)

    def get_athlete_name(self, obj):
        request = self.context.get("request")
        language = self.context.get("language", None) or (
            request.query_params.get("language") if request else "ru"
        )
        raw = obj.get_name(language)
        return _localize_placeholder(raw, language)

    def get_sport_type(self, obj):
        request = self.context.get("request")
        language = self.context.get("language", None) or (
            request.query_params.get("language") if request else "ru"
        )
        # Prefer model-level translated field if present
        raw = obj.get_sport(language) if hasattr(obj, "get_sport") else obj.sport
        return _localize_placeholder(raw, language)

    def get_event(self, obj):
        request = self.context.get("request")
        language = self.context.get("language", None) or (
            request.query_params.get("language") if request else "ru"
        )
        raw = (
            obj.get_competition(language)
            if hasattr(obj, "get_competition")
            else obj.competition
        )
        return _localize_placeholder(raw, language)

    def get_place(self, obj):
        request = self.context.get("request")
        language = self.context.get("language", None) or (
            request.query_params.get("language") if request else "ru"
        )
        raw = obj.get_result(language) if hasattr(obj, "get_result") else obj.result
        return _localize_placeholder(raw, language)

    def get_achievement(self, obj):
        request = self.context.get("request")
        language = self.context.get("language", None) or (
            request.query_params.get("language") if request else "ru"
        )
        raw = obj.get_result(language) if hasattr(obj, "get_result") else obj.result
        return _localize_placeholder(raw, language)

    def get_event_date(self, obj):
        return obj.date.isoformat() if getattr(obj, "date", None) else None

    def get_image(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    def get_photo(self, obj):
        # reuse same logic as image
        return self.get_image(obj)

    def to_representation(self, instance):
        # Получаем язык из контекста
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"
        self.context["language"] = language

        data = super().to_representation(instance)

        # Ensure compatibility aliases (also localized if needed)
        data["name"] = data.get("name") or data.get("athlete_name")
        data["athlete_name"] = data.get("athlete_name")
        data["sport_type"] = data.get("sport_type") or data.get("sport")
        data["event"] = data.get("event") or data.get("competition")
        data["place"] = data.get("place") or data.get("result")
        data["achievement"] = data.get("achievement") or data.get("result")
        data["event_date"] = data.get("event_date") or (
            data.get("date") if data.get("date") else None
        )
        data["photo"] = data.get("photo") or data.get("image")

        # Also localize raw model-backed fields that are still present in data
        # (these were included in Meta.fields and come from the model directly).
        for key in (
            "sport",
            "competition",
            "result",
            "athlete_name",
            "description",
            "name",
        ):
            if key in data and data.get(key):
                try:
                    data[key] = _localize_placeholder(data[key], language)
                except Exception:
                    # be conservative — leave original value on any error
                    pass

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
        """Альтернативное название для features.

        Supports two formats stored in `features` JSONField:
        - list of strings (legacy): ["Вместимость: 1500", ...]
        - list of dicts with language keys (new): [{"ru": "...", "en": "...", "kg": "..."}, ...]

        This method returns a list of strings localized for the requested language.
        """
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"

        raw = obj.features or []
        out = []
        for item in raw:
            if isinstance(item, dict):
                # try exact language, then fallbacks
                val = (
                    item.get(language)
                    or item.get("ru")
                    or next(iter(item.values()), None)
                )
                if val:
                    out.append(val)
                    continue
            # fallback: string value
            out.append(item)

        return out

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

        include_inactive = False
        if request:
            q = request.query_params.get("include_inactive", "false").lower()
            include_inactive = q in ("1", "true", "yes")

        if include_inactive:
            objects_qs = obj.objects.all()
        else:
            objects_qs = obj.objects.filter(is_active=True)

        serializer = InfrastructureObjectSerializer(
            objects_qs,
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
    badge_translated = serializers.SerializerMethodField()

    class Meta:
        model = Infrastructure
        fields = [
            "id",
            "name",
            "title",
            "description",
            "badge",
            "badge_translated",
            "created_at",
            "stats",
            "categories",
        ]

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
        include_inactive = False
        if request:
            q = request.query_params.get("include_inactive", "false").lower()
            include_inactive = q in ("1", "true", "yes")

        if include_inactive:
            stats_qs = obj.statistics.all().order_by("order")
        else:
            stats_qs = obj.statistics.filter(is_active=True).order_by("order")

        serializer = InfrastructureStatisticSerializer(
            stats_qs, many=True, context={"request": request, "language": language}
        )
        return serializer.data

    def get_badge_translated(self, obj):
        request = self.context.get("request")
        language = request.query_params.get("language", "ru") if request else "ru"
        return obj.get_badge(language)

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
