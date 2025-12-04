from django.contrib import admin
from .models import DepartmentCategory, DepartmentInfo, DepartmentFeature


class DepartmentInfoInline(admin.StackedInline):
    model = DepartmentInfo
    extra = 0
    max_num = 1
    fields = ("description_ru", "description_kg", "description_en", "is_active")


class DepartmentFeatureInline(admin.TabularInline):
    model = DepartmentFeature
    extra = 1
    fields = ("feature_ru", "feature_kg", "feature_en", "order", "is_active")
    ordering = ["order"]


@admin.register(DepartmentCategory)
class DepartmentCategoryAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "key", "color", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name_ru", "name_kg", "name_en", "key")
    ordering = ("order",)
    inlines = [DepartmentInfoInline, DepartmentFeatureInline]
    fieldsets = (
        (None, {"fields": ("key", "color", "order", "is_active")}),
        ("Названия", {"fields": ("name_ru", "name_kg", "name_en")}),
    )


@admin.register(DepartmentInfo)
class DepartmentInfoAdmin(admin.ModelAdmin):
    list_display = ("category", "description_preview", "is_active")
    list_filter = ("is_active",)
    search_fields = (
        "category__name_ru",
        "description_ru",
        "description_kg",
        "description_en",
    )
    fieldsets = (
        (None, {"fields": ("category", "is_active")}),
        (
            "Описания",
            {"fields": ("description_ru", "description_kg", "description_en")},
        ),
    )

    def description_preview(self, obj):
        return (
            obj.description_ru[:100] + "..."
            if len(obj.description_ru) > 100
            else obj.description_ru
        )

    description_preview.short_description = "Описание"


@admin.register(DepartmentFeature)
class DepartmentFeatureAdmin(admin.ModelAdmin):
    list_display = ("category", "feature_preview", "order", "is_active")
    list_filter = ("is_active", "category")
    search_fields = ("category__name_ru", "feature_ru", "feature_kg", "feature_en")
    list_editable = ("order", "is_active")
    ordering = ["category", "order"]
    fieldsets = (
        (None, {"fields": ("category", "order", "is_active")}),
        ("Особенности", {"fields": ("feature_ru", "feature_kg", "feature_en")}),
    )

    def feature_preview(self, obj):
        return (
            obj.feature_ru[:50] + "..." if len(obj.feature_ru) > 50 else obj.feature_ru
        )

    feature_preview.short_description = "Особенность"
