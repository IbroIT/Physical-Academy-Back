from django.contrib import admin
from .models import (
    SportSection,
    TrainingSchedule,
    Achievement,
    Infrastructure,
    InfrastructureCategory,
    InfrastructureObject,
)


# Inline для расписания тренировок
class TrainingScheduleInline(admin.TabularInline):
    model = TrainingSchedule
    extra = 1
    fields = ("day_of_week", "time_start", "time_end", "location")


# Регистрация моделей
@admin.register(SportSection)
class SportSectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name_ru", "coach_name", "sport_type", "is_active", "order")
    list_filter = ("is_active", "sport_type")
    list_editable = ("is_active", "order")
    search_fields = ("name_ru", "name_kg", "name_en", "coach_name")
    fieldsets = (
        (
            "Основная информация",
            {"fields": ("sport_type", "image", "is_active", "order")},
        ),
        (
            "Название (Переводы)",
            {"fields": ("name_ru", "name_kg", "name_en"), "classes": ("collapse",)},
        ),
        (
            "Описание (Переводы)",
            {
                "fields": ("description_ru", "description_kg", "description_en"),
                "classes": ("collapse",),
            },
        ),
        (
            "Контактная информация (Переводы)",
            {
                "fields": ("contact_info_ru", "contact_info_kg", "contact_info_en"),
                "classes": ("collapse",),
            },
        ),
        ("Тренер", {"fields": ("coach_name", "coach_rank", "coach_contacts")}),
        ("Расписание", {"fields": ("schedule",)}),
    )
    inlines = [TrainingScheduleInline]


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "athlete_name",
        "sport",
        "result",
        "date",
        "category",
        "is_active",
        "order",
    )
    list_filter = ("is_active", "category", "sport")
    list_editable = ("is_active", "order")
    search_fields = ("athlete_name", "sport", "competition")
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "athlete_name",
                    "sport",
                    "competition",
                    "result",
                    "date",
                    "category",
                    "image",
                )
            },
        ),
        (
            "Описание достижения (Переводы)",
            {
                "fields": ("description_ru", "description_kg", "description_en"),
                "classes": ("collapse",),
            },
        ),
        ("Дополнительно", {"fields": ("details", "is_active", "order")}),
    )


@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ("id", "name_ru", "badge", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name_ru", "name_kg", "name_en")
    fieldsets = (
        ("Основная информация", {"fields": ("badge", "is_active")}),
        (
            "Название (Переводы)",
            {"fields": ("name_ru", "name_kg", "name_en"), "classes": ("collapse",)},
        ),
        (
            "Описание (Переводы)",
            {
                "fields": ("description_ru", "description_kg", "description_en"),
                "classes": ("collapse",),
            },
        ),
        (
            "Статистика 1",
            {
                "fields": (
                    "stat_1_value",
                    "stat_1_icon",
                    "stat_1_label_ru",
                    "stat_1_label_kg",
                    "stat_1_label_en",
                )
            },
        ),
        (
            "Статистика 2",
            {
                "fields": (
                    "stat_2_value",
                    "stat_2_icon",
                    "stat_2_label_ru",
                    "stat_2_label_kg",
                    "stat_2_label_en",
                )
            },
        ),
        (
            "Статистика 3",
            {
                "fields": (
                    "stat_3_value",
                    "stat_3_icon",
                    "stat_3_label_ru",
                    "stat_3_label_kg",
                    "stat_3_label_en",
                )
            },
        ),
        (
            "Статистика 4",
            {
                "fields": (
                    "stat_4_value",
                    "stat_4_icon",
                    "stat_4_label_ru",
                    "stat_4_label_kg",
                    "stat_4_label_en",
                )
            },
        ),
    )


@admin.register(InfrastructureCategory)
class InfrastructureCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name_ru", "slug", "infrastructure", "icon", "order")
    list_filter = ("infrastructure",)
    list_editable = ("order",)
    search_fields = ("slug", "name_ru", "name_kg", "name_en")
    fieldsets = (
        (
            "Основная информация",
            {"fields": ("infrastructure", "slug", "icon", "color", "order")},
        ),
        (
            "Название категории (Переводы)",
            {"fields": ("name_ru", "name_kg", "name_en"), "classes": ("collapse",)},
        ),
    )


@admin.register(InfrastructureObject)
class InfrastructureObjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name_ru", "category", "is_active", "order")
    list_filter = ("is_active", "category")
    list_editable = ("is_active", "order")
    search_fields = ("name_ru", "name_kg", "name_en")
    fieldsets = (
        (
            "Основная информация",
            {"fields": ("category", "image", "is_active", "order")},
        ),
        (
            "Название (Переводы)",
            {"fields": ("name_ru", "name_kg", "name_en"), "classes": ("collapse",)},
        ),
        (
            "Описание (Переводы)",
            {
                "fields": ("description_ru", "description_kg", "description_en"),
                "classes": ("collapse",),
            },
        ),
        ("Характеристики", {"fields": ("features",)}),
    )


# Регистрируем TrainingSchedule для отдельного управления
admin.site.register(TrainingSchedule)
