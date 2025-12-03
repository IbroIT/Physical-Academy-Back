from django.contrib import admin
from .models import DepartmentCategory, DepartmentInfo


class DepartmentInfoInline(admin.TabularInline):
    model = DepartmentInfo
    extra = 1
    fields = ("info_type", "content_ru", "order", "is_active")


@admin.register(DepartmentCategory)
class DepartmentCategoryAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "key", "color", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name_ru", "name_kg", "name_en", "key")
    ordering = ("order",)
    inlines = [DepartmentInfoInline]
    fieldsets = (
        (None, {"fields": ("key", "color", "order", "is_active")}),
        ("Названия", {"fields": ("name_ru", "name_kg", "name_en")}),
    )


@admin.register(DepartmentInfo)
class DepartmentInfoAdmin(admin.ModelAdmin):
    list_display = ("category", "info_type", "content_preview", "order", "is_active")
    list_filter = ("category", "info_type", "is_active")
    search_fields = ("content_ru", "content_kg", "content_en")
    ordering = ("category", "info_type", "order")
    list_editable = ("order", "is_active")
    fieldsets = (
        (None, {"fields": ("category", "info_type", "order", "is_active")}),
        ("Контент", {"fields": ("content_ru", "content_kg", "content_en")}),
    )

    def content_preview(self, obj):
        return (
            obj.content_ru[:100] + "..."
            if len(obj.content_ru) > 100
            else obj.content_ru
        )

    content_preview.short_description = "Контент"
