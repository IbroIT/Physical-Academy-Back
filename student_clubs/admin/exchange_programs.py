from django.contrib import admin
from ..models_exchange import (
    ExchangeRegion,
    ExchangeDurationType,
    ExchangeProgram,
    ExchangeProgramRequirement,
    ExchangeProgramBenefit,
    ExchangeProgramCourse,
    ExchangePageStat,
    ExchangeDeadline,
)


class ExchangeProgramRequirementInline(admin.TabularInline):
    model = ExchangeProgramRequirement
    extra = 1
    fields = ["text_ru", "text_en", "text_kg", "order"]


class ExchangeProgramBenefitInline(admin.TabularInline):
    model = ExchangeProgramBenefit
    extra = 1
    fields = ["text_ru", "text_en", "text_kg", "order"]


class ExchangeProgramCourseInline(admin.TabularInline):
    model = ExchangeProgramCourse
    extra = 1
    fields = ["name_ru", "name_en", "name_kg"]


@admin.register(ExchangeRegion)
class ExchangeRegionAdmin(admin.ModelAdmin):
    list_display = ["name_en", "name_ru", "name_kg", "code"]
    search_fields = ["name_en", "name_ru", "name_kg", "code"]


@admin.register(ExchangeDurationType)
class ExchangeDurationTypeAdmin(admin.ModelAdmin):
    list_display = ["name_en", "name_ru", "name_kg", "code"]
    search_fields = ["name_en", "name_ru", "name_kg", "code"]


@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = [
        "university_en",
        "country_en",
        "region",
        "duration_type",
        "is_active",
        "is_featured",
        "available_spots",
    ]
    list_filter = ["region", "duration_type", "is_active", "is_featured", "difficulty"]
    search_fields = [
        "university_en",
        "university_ru",
        "university_kg",
        "country_en",
        "country_ru",
        "country_kg",
        "description_en",
    ]
    inlines = [
        ExchangeProgramRequirementInline,
        ExchangeProgramBenefitInline,
        ExchangeProgramCourseInline,
    ]
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    ("university_ru", "university_en", "university_kg"),
                    ("country_ru", "country_en", "country_kg"),
                    ("region", "duration_type"),
                    ("duration_ru", "duration_en", "duration_kg"),
                    ("icon", "website"),
                )
            },
        ),
        (
            "Описание",
            {
                "fields": (
                    "description_ru",
                    "description_en",
                    "description_kg",
                )
            },
        ),
        (
            "Дополнительная информация",
            {
                "fields": (
                    "cost",
                    ("language_ru", "language_en", "language_kg"),
                    (
                        "grants_available_ru",
                        "grants_available_en",
                        "grants_available_kg",
                    ),
                    "deadline",
                    "available_spots",
                )
            },
        ),
        (
            "Сложность",
            {
                "fields": (
                    "difficulty",
                    (
                        "difficulty_label_ru",
                        "difficulty_label_en",
                        "difficulty_label_kg",
                    ),
                )
            },
        ),
        (
            "Настройки",
            {
                "fields": (
                    ("is_active", "is_featured"),
                    "order",
                )
            },
        ),
    )


@admin.register(ExchangePageStat)
class ExchangePageStatAdmin(admin.ModelAdmin):
    list_display = ["value_en", "label_en", "icon", "order"]
    list_editable = ["order", "icon"]
    fieldsets = (
        (
            "Информация",
            {
                "fields": (
                    "icon",
                    ("value_ru", "value_en", "value_kg"),
                    ("label_ru", "label_en", "label_kg"),
                    "order",
                )
            },
        ),
    )


@admin.register(ExchangeDeadline)
class ExchangeDeadlineAdmin(admin.ModelAdmin):
    list_display = ["date", "program_en", "days_left_en", "order"]
    list_editable = ["order"]
    fieldsets = (
        (
            "Информация",
            {
                "fields": (
                    "date",
                    ("program_ru", "program_en", "program_kg"),
                    ("days_left_ru", "days_left_en", "days_left_kg"),
                    "order",
                )
            },
        ),
    )
