from django.contrib import admin
from ..models_instructions import (
    InstructionCategory,
    InstructionDocument,
    ImportantUpdate,
)


@admin.register(InstructionCategory)
class InstructionCategoryAdmin(admin.ModelAdmin):
    list_display = ["name_en", "name_ru", "name_kg", "code", "order"]
    list_editable = ["order"]
    search_fields = ["name_en", "name_ru", "name_kg", "code"]
    ordering = ["order"]


@admin.register(InstructionDocument)
class InstructionDocumentAdmin(admin.ModelAdmin):
    list_display = [
        "name_en",
        "category",
        "format",
        "version",
        "downloads",
        "is_active",
        "updated_at",
    ]
    list_filter = ["category", "format", "is_active"]
    search_fields = ["name_en", "name_ru", "name_kg", "description_en"]
    ordering = ["order", "-updated_at"]
    readonly_fields = ["downloads", "created_at", "updated_at"]

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    ("name_ru", "name_en", "name_kg"),
                    ("description_ru", "description_en", "description_kg"),
                    "category",
                )
            },
        ),
        (
            "File Details",
            {
                "fields": (
                    "file",
                    ("format", "size", "version"),
                    "pages",
                )
            },
        ),
        (
            "Tags & Metadata",
            {
                "fields": (
                    "tags",
                    ("is_active", "order"),
                    ("downloads", "created_at", "updated_at"),
                )
            },
        ),
    )


@admin.register(ImportantUpdate)
class ImportantUpdateAdmin(admin.ModelAdmin):
    list_display = ["title_en", "date", "is_active", "order", "actual_date"]
    list_filter = ["is_active"]
    list_editable = ["order", "is_active"]
    search_fields = ["title_en", "title_ru", "title_kg", "description_en"]
    ordering = ["order", "-actual_date"]

    fieldsets = (
        (
            "Update Content",
            {
                "fields": (
                    ("title_ru", "title_en", "title_kg"),
                    ("description_ru", "description_en", "description_kg"),
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    ("date", "actual_date"),
                    ("is_active", "order"),
                )
            },
        ),
    )
