from django.contrib import admin
from .models import TabCategory, Card, TimelineEvent


class CardInline(admin.TabularInline):
    model = Card
    extra = 1
    fields = ("title", "description", "order", "is_active")


@admin.register(TabCategory)
class TabCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "key", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "key")
    ordering = ("order",)
    inlines = [CardInline]
    fieldsets = (
        (None, {"fields": ("key", "title", "order", "is_active")}),
        ("Иконка", {"fields": ("icon_svg",), "classes": ("collapse",)}),
    )


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("title", "tab", "order", "is_active", "created_at")
    list_filter = ("tab", "is_active", "created_at")
    search_fields = ("title", "description")
    ordering = ("tab", "order")
    list_editable = ("order", "is_active")


@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ("year", "event_preview", "order", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("year", "event")
    ordering = ("order",)
    list_editable = ("order", "is_active")

    def event_preview(self, obj):
        return obj.event[:100] + "..." if len(obj.event) > 100 else obj.event

    event_preview.short_description = "Событие"
