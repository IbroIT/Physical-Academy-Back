from django.contrib import admin
from ..models_disabilities import (
    DisabilitySupportService,
    DisabilityContactPerson,
    DisabilityResource,
    DisabilityEmergencyContact,
)


@admin.register(DisabilitySupportService)
class DisabilitySupportServiceAdmin(admin.ModelAdmin):
    list_display = ["title_ru", "order", "icon"]
    list_editable = ["order", "icon"]
    search_fields = ["title_ru", "title_en", "title_kg", "description_ru"]
    ordering = ["order"]
    fieldsets = (
        (
            "Icon and Order",
            {
                "fields": ("icon", "order"),
            },
        ),
        (
            "Titles",
            {
                "fields": ("title_ru", "title_en", "title_kg"),
            },
        ),
        (
            "Descriptions",
            {
                "fields": ("description_ru", "description_en", "description_kg"),
            },
        ),
        (
            "Features",
            {
                "fields": ("features_ru", "features_en", "features_kg"),
                "description": "Enter features separated by new lines",
            },
        ),
    )


@admin.register(DisabilityContactPerson)
class DisabilityContactPersonAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "position_ru", "phone", "email", "order"]
    list_editable = ["order"]
    search_fields = ["name_ru", "name_en", "name_kg", "position_ru", "email", "phone"]
    ordering = ["order"]
    fieldsets = (
        (
            "Icon and Order",
            {
                "fields": ("icon", "order"),
            },
        ),
        (
            "Personal Information",
            {
                "fields": (("name_ru", "name_en", "name_kg"),),
            },
        ),
        (
            "Position",
            {
                "fields": (("position_ru", "position_en", "position_kg"),),
            },
        ),
        (
            "Contact Information",
            {
                "fields": ("phone", "email"),
            },
        ),
        (
            "Additional Information",
            {
                "fields": (
                    ("hours_ru", "hours_en", "hours_kg"),
                    ("location_ru", "location_en", "location_kg"),
                ),
            },
        ),
    )


@admin.register(DisabilityResource)
class DisabilityResourceAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "type_ru", "format_ru", "url", "order"]
    list_editable = ["order"]
    list_filter = ["type_ru", "format_ru"]
    search_fields = ["name_ru", "name_en", "name_kg", "description_ru"]
    ordering = ["order"]
    fieldsets = (
        (
            "Icon and Order",
            {
                "fields": ("icon", "order"),
            },
        ),
        (
            "Basic Information",
            {
                "fields": (
                    ("name_ru", "name_en", "name_kg"),
                    ("type_ru", "type_en", "type_kg"),
                    ("format_ru", "format_en", "format_kg"),
                ),
            },
        ),
        (
            "Description",
            {
                "fields": (("description_ru", "description_en", "description_kg"),),
            },
        ),
        (
            "Access",
            {
                "fields": ("url",),
            },
        ),
    )


@admin.register(DisabilityEmergencyContact)
class DisabilityEmergencyContactAdmin(admin.ModelAdmin):
    # Model uses title_* fields; update admin to reference existing fields
    list_display = ["title_ru", "phone", "order"]
    list_editable = ["order"]
    list_filter = ["order"]
    search_fields = ["title_ru", "title_en", "title_kg", "phone"]
    ordering = ["order"]
    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (("title_ru", "title_en", "title_kg"),),
            },
        ),
        (
            "Contents",
            {
                "fields": (("description_ru", "description_en", "description_kg"),),
            },
        ),
        (
            "Contact Information",
            {
                "fields": ("phone", "phone_link"),
            },
        ),
        (
            "Display",
            {
                "fields": (("order",),),
            },
        ),
    )
