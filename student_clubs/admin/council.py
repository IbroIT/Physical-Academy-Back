from django.contrib import admin
from ..models_council import (
    CouncilMember,
    CouncilInitiative,
    CouncilEvent,
    CouncilStats,
)


class CouncilEventsInline(admin.TabularInline):
    model = CouncilEvent
    extra = 1
    fields = ["title_ru", "date", "location_ru", "status"]


@admin.register(CouncilMember)
class CouncilMemberAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "role", "position_ru", "department_ru", "order"]
    list_editable = ["order", "role"]
    list_filter = ["role"]
    search_fields = ["name_ru", "name_en", "name_kg", "position_ru", "department_ru"]
    ordering = ["order", "role"]
    fieldsets = (
        (
            "Order and Role",
            {
                "fields": (("order", "role"),),
            },
        ),
        (
            "Personal Information",
            {
                "fields": (
                    "avatar",
                    ("name_ru", "name_en", "name_kg"),
                ),
            },
        ),
        (
            "Position and Department",
            {
                "fields": (
                    ("position_ru", "position_en", "position_kg"),
                    ("department_ru", "department_en", "department_kg"),
                ),
            },
        ),
        (
            "Contact Information",
            {
                "fields": ("email", "phone"),
            },
        ),
        (
            "Social Media",
            {
                "fields": ("instagram", "linkedin"),
            },
        ),
        (
            "Biography",
            {
                "fields": (("bio_ru", "bio_en", "bio_kg"),),
            },
        ),
        (
            "Achievements",
            {
                "fields": (("achievements_ru", "achievements_en", "achievements_kg"),),
            },
        ),
    )


@admin.register(CouncilInitiative)
class CouncilInitiativeAdmin(admin.ModelAdmin):
    list_display = ["title_ru", "status", "start_date", "end_date", "order"]
    list_editable = ["status", "order"]
    list_filter = ["status"]
    search_fields = ["title_ru", "title_en", "title_kg", "description_ru"]
    ordering = ["order", "status", "start_date"]
    filter_horizontal = ["lead_members"]
    inlines = [CouncilEventsInline]

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (("icon", "order", "status"),),
            },
        ),
        (
            "Title",
            {
                "fields": (("title_ru", "title_en", "title_kg"),),
            },
        ),
        (
            "Description",
            {
                "fields": (("description_ru", "description_en", "description_kg"),),
            },
        ),
        (
            "Goals",
            {
                "fields": (("goals_ru", "goals_en", "goals_kg"),),
            },
        ),
        (
            "Timeline",
            {
                "fields": (("start_date", "end_date"),),
            },
        ),
        (
            "Leadership",
            {
                "fields": ("lead_members",),
            },
        ),
    )


@admin.register(CouncilEvent)
class CouncilEventAdmin(admin.ModelAdmin):
    list_display = ["title_ru", "initiative", "date", "location_ru", "status"]
    list_editable = ["status"]
    list_filter = ["status", "initiative"]
    search_fields = ["title_ru", "title_en", "title_kg", "description_ru"]
    ordering = ["date", "status"]

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (("initiative", "status", "icon", "order"),),
            },
        ),
        (
            "Title",
            {
                "fields": (("title_ru", "title_en", "title_kg"),),
            },
        ),
        (
            "Description",
            {
                "fields": (("description_ru", "description_en", "description_kg"),),
            },
        ),
        (
            "Details",
            {
                "fields": (
                    "date",
                    ("location_ru", "location_en", "location_kg"),
                ),
            },
        ),
        (
            "Additional Information",
            {
                "fields": ("registration_link", "image"),
            },
        ),
    )


@admin.register(CouncilStats)
class CouncilStatsAdmin(admin.ModelAdmin):
    list_display = ["key", "value", "label_ru", "order"]
    list_editable = ["value", "order"]
    search_fields = ["key", "value", "label_ru", "label_en", "label_kg"]
    ordering = ["order"]

    fieldsets = (
        (
            "Statistic Information",
            {
                "fields": (("key", "value", "order"),),
            },
        ),
        (
            "Labels",
            {
                "fields": (("label_ru", "label_en", "label_kg"),),
            },
        ),
    )
