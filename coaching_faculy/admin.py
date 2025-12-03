from django.contrib import admin
from .models import TabCategory, Card, TimelineEvent


class CardInline(admin.TabularInline):
    model = Card
    extra = 1
    fields = (
        "title_ru",
        "title_kg",
        "title_en",
        "description_ru",
        "order",
        "is_active",
    )


@admin.register(TabCategory)
class TabCategoryAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "key", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title_ru", "title_kg", "title_en", "key")
    ordering = ("order",)
    inlines = [CardInline]
    fieldsets = (
        (None, {"fields": ("key", "order", "is_active")}),
        ("Заголовки", {"fields": ("title_ru", "title_kg", "title_en")}),
        ("Иконка", {"fields": ("icon",)}),
    )


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "tab", "order", "is_active", "created_at")
    list_filter = ("tab", "is_active", "created_at")
    search_fields = (
        "title_ru",
        "title_kg",
        "title_en",
        "description_ru",
        "description_kg",
        "description_en",
    )
    ordering = ("tab", "order")
    list_editable = ("order", "is_active")
    fieldsets = (
        (None, {"fields": ("tab", "order", "is_active")}),
        ("Заголовки", {"fields": ("title_ru", "title_kg", "title_en")}),
        (
            "Описания",
            {"fields": ("description_ru", "description_kg", "description_en")},
        ),
    )


@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ("year", "event_preview", "order", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("year", "event_ru", "event_kg", "event_en")
    ordering = ("order",)
    list_editable = ("order", "is_active")
    fieldsets = (
        (None, {"fields": ("year", "order", "is_active")}),
        ("События", {"fields": ("event_ru", "event_kg", "event_en")}),
    )

    def event_preview(self, obj):
        return obj.event_ru[:100] + "..." if len(obj.event_ru) > 100 else obj.event_ru

    event_preview.short_description = "Событие"
