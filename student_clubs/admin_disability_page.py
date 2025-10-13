from django.contrib import admin
from .models_disability_page import DisabilityPage


@admin.register(DisabilityPage)
class DisabilityPageAdmin(admin.ModelAdmin):
    """Admin interface for DisabilityPage model"""

    list_display = ["title_ru", "title_en", "order"]
    list_editable = ["order"]
    search_fields = [
        "title_ru",
        "title_en",
        "title_kg",
        "description_ru",
        "description_en",
        "description_kg",
    ]
    ordering = ["order", "id"]

    fieldsets = (
        (
            "Content in Russian",
            {
                "fields": ("title_ru", "description_ru"),
            },
        ),
        (
            "Content in English",
            {
                "fields": ("title_en", "description_en"),
            },
        ),
        (
            "Content in Kyrgyz",
            {
                "fields": ("title_kg", "description_kg"),
            },
        ),
        (
            "Ordering",
            {
                "fields": ("order",),
            },
        ),
    )
