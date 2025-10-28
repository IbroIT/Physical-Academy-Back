from django.contrib import admin
from .models import (
    SportSection,
    TrainingSchedule,
    Achievement,
    Infrastructure,
    InfrastructureStatistic,
    InfrastructureCategory,
    InfrastructureObject,
)


# ==================== Inlines ====================


class TrainingScheduleInline(admin.TabularInline):
    model = TrainingSchedule
    extra = 1
    fields = ("day_of_week", "time_start", "time_end", "location")


class InfrastructureStatisticInline(admin.TabularInline):
    model = InfrastructureStatistic
    extra = 1
    fields = ("label_ru", "label_kg", "label_en", "value", "icon", "order", "is_active")


class InfrastructureCategoryInline(admin.TabularInline):
    model = InfrastructureCategory
    extra = 0
    fields = ("slug", "name_ru", "name_kg", "name_en", "icon", "color", "order")
    readonly_fields = ("slug",)


class InfrastructureObjectInline(admin.TabularInline):
    model = InfrastructureObject
    extra = 0
    fields = ("name_ru", "image", "order", "is_active")
    readonly_fields = ("name_ru",)


# ==================== Admin Models ====================


@admin.register(SportSection)
class SportSectionAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "coach_name", "sport_type", "is_active", "order")
    list_filter = ("is_active", "sport_type")
    list_editable = ("is_active", "order")
    search_fields = ("name_ru", "name_en", "name_kg", "coach_name")
    inlines = [TrainingScheduleInline]

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("sport_type", "image", "is_active", "order")},
        ),
        ("Названия (многоязычность)", {"fields": ("name_ru", "name_kg", "name_en")}),
        (
            "Описания (многоязычность)",
            {"fields": ("description_ru", "description_kg", "description_en")},
        ),
        (
            "Контактная информация (многоязычность)",
            {"fields": ("contact_info_ru", "contact_info_kg", "contact_info_en")},
        ),
        (
            "Информация о тренере",
            {"fields": ("coach_name", "coach_rank", "coach_contacts", "schedule")},
        ),
    )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "athlete_name",
        "sport",
        "result",
        "date",
        "category",
        "is_active",
        "order",
    )
    list_filter = ("is_active", "category", "sport", "date")
    list_editable = ("is_active", "order")
    search_fields = ("athlete_name", "sport", "competition")
    date_hierarchy = "date"

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
                    "image",
                    "category",
                    "is_active",
                    "order",
                )
            },
        ),
        (
            "Описания (многоязычность)",
            {"fields": ("description_ru", "description_kg", "description_en")},
        ),
        ("Дополнительно", {"fields": ("details",), "classes": ("collapse",)}),
    )


@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "badge", "is_active")
    list_filter = ("is_active",)
    inlines = [InfrastructureStatisticInline, InfrastructureCategoryInline]

    fieldsets = (
        ("Основная информация", {"fields": ("badge", "is_active")}),
        ("Названия (многоязычность)", {"fields": ("name_ru", "name_kg", "name_en")}),
        (
            "Описания (многоязычность)",
            {"fields": ("description_ru", "description_kg", "description_en")},
        ),
    )


@admin.register(InfrastructureCategory)
class InfrastructureCategoryAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "slug", "infrastructure", "icon", "order")
    list_filter = ("infrastructure",)
    list_editable = ("order",)
    search_fields = ("name_ru", "name_en", "name_kg", "slug")
    inlines = [InfrastructureObjectInline]

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("infrastructure", "slug", "icon", "color", "order")},
        ),
        ("Названия (многоязычность)", {"fields": ("name_ru", "name_kg", "name_en")}),
    )


@admin.register(InfrastructureObject)
class InfrastructureObjectAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "category", "is_active", "order")
    list_filter = ("is_active", "category")
    list_editable = ("is_active", "order")
    search_fields = ("name_ru", "name_en", "name_kg")

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("category", "image", "features", "is_active", "order")},
        ),
        ("Названия (многоязычность)", {"fields": ("name_ru", "name_kg", "name_en")}),
        (
            "Описания (многоязычность)",
            {"fields": ("description_ru", "description_kg", "description_en")},
        ),
    )


# Простая регистрация остальных моделей
admin.site.register(TrainingSchedule)
admin.site.register(InfrastructureStatistic)
