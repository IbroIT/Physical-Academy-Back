from rest_framework import serializers
from .models_exchange import (
    ExchangeRegion,
    ExchangeDurationType,
    ExchangeProgram,
    ExchangeProgramRequirement,
    ExchangeProgramBenefit,
    ExchangeProgramCourse,
    ExchangePageStat,
    ExchangeDeadline,
)


class ExchangeRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRegion
        fields = ["id", "name_ru", "name_en", "name_kg", "code"]


class ExchangeDurationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeDurationType
        fields = ["id", "name_ru", "name_en", "name_kg", "code"]


class ExchangeProgramRequirementSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    class Meta:
        model = ExchangeProgramRequirement
        fields = ["id", "text", "text_ru", "text_en", "text_kg", "order"]

    def get_text(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.text_ru
        elif language == "kg":
            return obj.text_kg
        return obj.text_en


class ExchangeProgramBenefitSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    class Meta:
        model = ExchangeProgramBenefit
        fields = ["id", "text", "text_ru", "text_en", "text_kg", "order"]

    def get_text(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.text_ru
        elif language == "kg":
            return obj.text_kg
        return obj.text_en


class ExchangeProgramCourseSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = ExchangeProgramCourse
        fields = ["id", "name", "name_ru", "name_en", "name_kg"]

    def get_name(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.name_ru
        elif language == "kg":
            return obj.name_kg
        return obj.name_en


class ExchangeProgramSerializer(serializers.ModelSerializer):
    requirements = serializers.SerializerMethodField()
    benefits = serializers.SerializerMethodField()
    available_courses = serializers.SerializerMethodField()
    region_name = serializers.SerializerMethodField()
    duration_type_name = serializers.SerializerMethodField()

    # Add localized fields
    university = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    grants_available = serializers.SerializerMethodField()
    difficulty_label = serializers.SerializerMethodField()

    class Meta:
        model = ExchangeProgram
        fields = [
            "id",
            "university",
            "university_ru",
            "university_en",
            "university_kg",
            "country",
            "country_ru",
            "country_en",
            "country_kg",
            "region",
            "region_name",
            "duration_type",
            "duration_type_name",
            "duration",
            "duration_ru",
            "duration_en",
            "duration_kg",
            "description",
            "description_ru",
            "description_en",
            "description_kg",
            "cost",
            "language",
            "language_ru",
            "language_en",
            "language_kg",
            "grants_available",
            "grants_available_ru",
            "grants_available_en",
            "grants_available_kg",
            "deadline",
            "available_spots",
            "icon",
            "website",
            "difficulty",
            "difficulty_label",
            "difficulty_label_ru",
            "difficulty_label_en",
            "difficulty_label_kg",
            "is_featured",
            "is_active",
            "order",
            "requirements",
            "benefits",
            "available_courses",
        ]

    def get_requirements(self, obj):
        return ExchangeProgramRequirementSerializer(
            obj.requirements.all(), many=True, context=self.context
        ).data

    def get_benefits(self, obj):
        return ExchangeProgramBenefitSerializer(
            obj.benefits.all(), many=True, context=self.context
        ).data

    def get_available_courses(self, obj):
        return ExchangeProgramCourseSerializer(
            obj.available_courses.all(), many=True, context=self.context
        ).data

    def get_university(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.university_ru
        elif language == "kg":
            return obj.university_kg
        return obj.university_en

    def get_country(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.country_ru
        elif language == "kg":
            return obj.country_kg
        return obj.country_en

    def get_duration(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.duration_ru
        elif language == "kg":
            return obj.duration_kg
        return obj.duration_en

    def get_description(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.description_ru
        elif language == "kg":
            return obj.description_kg
        return obj.description_en

    def get_language(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.language_ru
        elif language == "kg":
            return obj.language_kg
        return obj.language_en

    def get_grants_available(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.grants_available_ru
        elif language == "kg":
            return obj.grants_available_kg
        return obj.grants_available_en

    def get_difficulty_label(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.difficulty_label_ru
        elif language == "kg":
            return obj.difficulty_label_kg
        return obj.difficulty_label_en

    def get_region_name(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.region.name_ru
        elif language == "kg":
            return obj.region.name_kg
        return obj.region.name_en

    def get_duration_type_name(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.duration_type.name_ru
        elif language == "kg":
            return obj.duration_type.name_kg
        return obj.duration_type.name_en


class ExchangePageStatSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()

    class Meta:
        model = ExchangePageStat
        fields = [
            "id",
            "icon",
            "value",
            "label",
            "value_ru",
            "value_en",
            "value_kg",
            "label_ru",
            "label_en",
            "label_kg",
            "order",
        ]

    def get_value(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.value_ru
        elif language == "kg":
            return obj.value_kg
        return obj.value_en

    def get_label(self, obj):
        language = self.context.get("language", "en")
        if language == "ru":
            return obj.label_ru
        elif language == "kg":
            return obj.label_kg
        return obj.label_en


class ExchangeDeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeDeadline
        fields = [
            "id",
            "date",
            "program_ru",
            "program_en",
            "program_kg",
            "days_left_ru",
            "days_left_en",
            "days_left_kg",
            "order",
        ]


class ExchangePageDataSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()
    subtitle = serializers.SerializerMethodField()
    stats = serializers.SerializerMethodField()
    programs = serializers.SerializerMethodField()
    filters = serializers.SerializerMethodField()
    deadlines = serializers.SerializerMethodField()

    def get_title(self, obj):
        language = self.context.get("language", "en")
        titles = {
            "en": "International Exchange Programs",
            "ru": "Международные программы обмена",
            "kg": "Эл аралык алмашуу программалары",
        }
        return titles.get(language, titles["en"])

    def get_subtitle(self, obj):
        language = self.context.get("language", "en")
        subtitles = {
            "en": "Expand your horizons with our partner universities worldwide and gain invaluable international experience",
            "ru": "Расширьте свои горизонты с нашими университетами-партнерами по всему миру и получите бесценный международный опыт",
            "kg": "Дүйнө жүзү боюнча өнөктөш университеттер менен өз горизонтторуңузду кеңейтип, баа жеткис эл аралык тажрыйбага ээ болуңуз",
        }
        return subtitles.get(language, subtitles["en"])

    def get_stats(self, obj):
        language = self.context.get("language", "en")
        return ExchangePageStatSerializer(
            ExchangePageStat.objects.all().order_by("order"),
            many=True,
            context={"language": language},
        ).data

    def get_programs(self, obj):
        language = self.context.get("language", "en")
        return ExchangeProgramSerializer(
            ExchangeProgram.objects.filter(is_active=True),
            many=True,
            context={"language": language},
        ).data

    def get_filters(self, obj):
        language = self.context.get("language", "en")
        regions = ExchangeRegionSerializer(ExchangeRegion.objects.all(), many=True).data
        durations = ExchangeDurationTypeSerializer(
            ExchangeDurationType.objects.all(), many=True
        ).data

        # Format regions for frontend
        formatted_regions = []
        for region in regions:
            if language == "ru":
                name = region["name_ru"]
            elif language == "kg":
                name = region["name_kg"]
            else:
                name = region["name_en"]

            formatted_regions.append(
                {
                    "id": region["id"],
                    "name": name,
                    "code": region["code"],
                }
            )

        # Format durations for frontend
        formatted_durations = []
        for duration in durations:
            if language == "ru":
                name = duration["name_ru"]
            elif language == "kg":
                name = duration["name_kg"]
            else:
                name = duration["name_en"]

            formatted_durations.append(
                {
                    "id": duration["id"],
                    "name": name,
                    "code": duration["code"],
                }
            )

        return {
            "regions": formatted_regions,
            "durations": formatted_durations,
        }

    def get_deadlines(self, obj):
        language = self.context.get("language", "en")
        return {
            "title": {
                "en": "Upcoming Deadlines",
                "ru": "Предстоящие дедлайны",
                "kg": "Алдыдагы дедлайндар",
            }.get(language, "Upcoming Deadlines"),
            "list": ExchangeDeadlineSerializer(
                ExchangeDeadline.objects.all().order_by("order"), many=True
            ).data,
        }
