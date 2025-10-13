from django.contrib import admin

# NTS Committee Admin Classes
from .models import (
    # NTS Committee models
    NTSCommitteeRole,
    NTSResearchDirection,
    NTSCommitteeMember,
    NTSCommitteeSection,
)


@admin.register(NTSCommitteeRole)
class NTSCommitteeRoleAdmin(admin.ModelAdmin):
    list_display = ["name_display", "description_preview"]

    fieldsets = (
        ("Names", {"fields": ("name_ru", "name_en", "name_kg")}),
        (
            "Descriptions",
            {"fields": ("description_ru", "description_en", "description_kg")},
        ),
    )

    def name_display(self, obj):
        return obj.name_ru or obj.name_en or obj.name_kg

    name_display.short_description = "Name"

    def description_preview(self, obj):
        desc = obj.description_ru or obj.description_en or obj.description_kg
        if desc:
            return desc[:100] + "..." if len(desc) > 100 else desc
        return "-"

    description_preview.short_description = "Description"


@admin.register(NTSResearchDirection)
class NTSResearchDirectionAdmin(admin.ModelAdmin):
    list_display = ["name_display", "description_preview"]

    fieldsets = (
        ("Names", {"fields": ("name_ru", "name_en", "name_kg")}),
        (
            "Descriptions",
            {"fields": ("description_ru", "description_en", "description_kg")},
        ),
    )

    def name_display(self, obj):
        return obj.name_ru or obj.name_en or obj.name_kg

    name_display.short_description = "Name"

    def description_preview(self, obj):
        desc = obj.description_ru or obj.description_en or obj.description_kg
        if desc:
            return desc[:100] + "..." if len(desc) > 100 else desc
        return "-"

    description_preview.short_description = "Description"


@admin.register(NTSCommitteeMember)
class NTSCommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ["name_display", "position_display", "role", "is_active", "order"]
    list_filter = ["role", "research_direction", "is_active"]
    search_fields = [
        "name_ru",
        "name_en",
        "name_kg",
        "position_ru",
        "position_en",
        "position_kg",
        "email",
    ]
    list_editable = ["is_active", "order"]

    fieldsets = (
        ("Names", {"fields": ("name_ru", "name_en", "name_kg")}),
        ("Positions", {"fields": ("position_ru", "position_en", "position_kg")}),
        ("Relations", {"fields": ("role", "research_direction")}),
        ("Biographies", {"fields": ("bio_ru", "bio_en", "bio_kg")}),
        ("Contact Information", {"fields": ("email", "phone", "photo")}),
        ("Display Settings", {"fields": ("is_active", "order")}),
    )

    def name_display(self, obj):
        return obj.name_ru or obj.name_en or obj.name_kg

    name_display.short_description = "Name"

    def position_display(self, obj):
        return obj.position_ru or obj.position_en or obj.position_kg

    position_display.short_description = "Position"


@admin.register(NTSCommitteeSection)
class NTSCommitteeSectionAdmin(admin.ModelAdmin):
    list_display = ["section_key", "title_display"]
    search_fields = ["section_key", "title_ru", "title_en", "title_kg"]

    fieldsets = (
        ("Section Info", {"fields": ("section_key",)}),
        ("Russian", {"fields": ("title_ru", "description_ru")}),
        ("English", {"fields": ("title_en", "description_en")}),
        ("Kyrgyz", {"fields": ("title_kg", "description_kg")}),
    )

    def title_display(self, obj):
        return obj.title_ru or obj.title_en or obj.title_kg

    title_display.short_description = "Title"
