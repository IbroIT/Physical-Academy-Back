from django.contrib import admin
from ..models_scholarship_visa import (
    ScholarshipProgram,
    ScholarshipRequiredDocument,
    VisaSupportService,
    VisaSupportContact,
)


class ScholarshipRequiredDocumentInline(admin.TabularInline):
    model = ScholarshipRequiredDocument
    extra = 1
    fields = [
        "name_ru",
        "name_en",
        "name_kg",
        "description_ru",
        "description_en",
        "description_kg",
        "is_required",
        "order",
    ]


@admin.register(ScholarshipProgram)
class ScholarshipProgramAdmin(admin.ModelAdmin):
    list_display = [
        "name_ru",
        "amount",
        "currency",
        "application_deadline",
        "is_active",
    ]
    list_filter = ["is_active", "currency"]
    search_fields = ["name_ru", "name_en", "name_kg", "description_ru"]
    date_hierarchy = "application_deadline"
    fieldsets = [
        (
            "Basic Information",
            {
                "fields": [
                    ("name_ru", "name_en", "name_kg"),
                    ("amount", "currency"),
                    "application_deadline",
                    "application_link",
                    "is_active",
                ]
            },
        ),
        (
            "Program Description",
            {
                "fields": [
                    "description_ru",
                    "description_en",
                    "description_kg",
                ]
            },
        ),
        (
            "Eligibility Criteria",
            {
                "fields": [
                    "eligibility_criteria_ru",
                    "eligibility_criteria_en",
                    "eligibility_criteria_kg",
                ]
            },
        ),
        (
            "Contact Information",
            {
                "fields": [
                    "contact_email",
                    "contact_phone",
                ]
            },
        ),
    ]
    inlines = [ScholarshipRequiredDocumentInline]


@admin.register(VisaSupportService)
class VisaSupportServiceAdmin(admin.ModelAdmin):
    list_display = ["title_ru", "is_featured", "order", "is_active"]
    list_filter = ["is_active", "is_featured"]
    search_fields = ["title_ru", "title_en", "title_kg", "description_ru"]
    list_editable = ["is_featured", "order", "is_active"]
    fieldsets = [
        (
            "Basic Information",
            {
                "fields": [
                    ("title_ru", "title_en", "title_kg"),
                    ("is_featured", "icon", "order"),
                    "is_active",
                ]
            },
        ),
        (
            "Service Description",
            {
                "fields": [
                    "description_ru",
                    "description_en",
                    "description_kg",
                ]
            },
        ),
    ]


@admin.register(VisaSupportContact)
class VisaSupportContactAdmin(admin.ModelAdmin):
    # VisaSupportContact model defines full_name_* and office_location_* fields
    list_display = ["full_name_ru", "position_ru", "email", "phone", "order"]
    list_filter = ["is_active"]
    search_fields = [
        "full_name_ru",
        "full_name_en",
        "full_name_kg",
        "position_ru",
        "email",
        "phone",
    ]
    list_editable = ["order"]
    fieldsets = [
        (
            "Basic Information",
            {
                "fields": [
                    ("full_name_ru", "full_name_en", "full_name_kg"),
                    ("position_ru", "position_en", "position_kg"),
                    ("email", "phone"),
                    "photo",
                    ("order", "is_active"),
                ]
            },
        ),
        (
            "Office Information",
            {
                "fields": [
                    ("office_hours_ru", "office_hours_en", "office_hours_kg"),
                    ("office_location_ru", "office_location_en", "office_location_kg"),
                ]
            },
        ),
    ]


@admin.register(ScholarshipRequiredDocument)
class ScholarshipRequiredDocumentAdmin(admin.ModelAdmin):
    """Standalone admin for ScholarshipRequiredDocument so it appears in admin list."""

    list_display = ("scholarship", "name_ru", "is_required", "order")
    list_filter = ("scholarship", "is_required")
    search_fields = ("name_ru", "name_en", "name_kg", "scholarship__name_ru")
    list_editable = ("is_required", "order")
    raw_id_fields = ("scholarship",)
    fieldsets = (
        ("Relation", {"fields": ("scholarship",)}),
        ("Names", {"fields": ("name_ru", "name_en", "name_kg")}),
        (
            "Descriptions",
            {"fields": ("description_ru", "description_en", "description_kg")},
        ),
        ("Settings", {"fields": ("is_required", "order")}),
    )
