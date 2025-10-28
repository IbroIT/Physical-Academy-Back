from django.contrib import admin
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


# Inline для переводов
class SportSectionTranslationInline(admin.TabularInline):
    model = SportSectionTranslation
    extra = 1


class TrainingScheduleInline(admin.TabularInline):
    model = TrainingSchedule
    extra = 1


class AchievementTranslationInline(admin.TabularInline):
    model = AchievementTranslation
    extra = 1


class InfrastructureTranslationInline(admin.TabularInline):
    model = InfrastructureTranslation
    extra = 1


class InfrastructureCategoryTranslationInline(admin.TabularInline):
    model = InfrastructureCategoryTranslation
    extra = 1


class InfrastructureObjectTranslationInline(admin.TabularInline):
    model = InfrastructureObjectTranslation
    extra = 1


# Регистрация моделей
@admin.register(SportSection)
class SportSectionAdmin(admin.ModelAdmin):
    list_display = ("id", "coach_name", "sport_type", "is_active", "order")
    list_filter = ("is_active", "sport_type")
    list_editable = ("is_active", "order")
    search_fields = ("coach_name",)
    inlines = [SportSectionTranslationInline, TrainingScheduleInline]


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "athlete_name",
        "sport",
        "result",
        "date",
        "is_active",
        "order",
    )
    list_filter = ("is_active", "category", "sport")
    list_editable = ("is_active", "order")
    search_fields = ("athlete_name", "sport")
    inlines = [AchievementTranslationInline]


@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ("id", "badge", "is_active")
    list_filter = ("is_active",)
    inlines = [InfrastructureTranslationInline]


@admin.register(InfrastructureCategory)
class InfrastructureCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "slug", "infrastructure", "order")
    list_filter = ("infrastructure",)
    list_editable = ("order",)
    inlines = [InfrastructureCategoryTranslationInline]


@admin.register(InfrastructureObject)
class InfrastructureObjectAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "is_active", "order")
    list_filter = ("is_active", "category")
    list_editable = ("is_active", "order")
    inlines = [InfrastructureObjectTranslationInline]


# Простая регистрация остальных моделей
admin.site.register(SportSectionTranslation)
admin.site.register(TrainingSchedule)
admin.site.register(AchievementTranslation)
admin.site.register(InfrastructureTranslation)
admin.site.register(InfrastructureCategoryTranslation)
admin.site.register(InfrastructureObjectTranslation)
