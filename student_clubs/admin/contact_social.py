from django.contrib import admin
from ..models.contact_social import (
    StudentContactInfo,
    SocialNetworkAccount,
    SocialCommunity,
)


@admin.register(StudentContactInfo)
class StudentContactInfoAdmin(admin.ModelAdmin):
    list_display = [
        "title_ru",
        "contact_name_ru",
        "email",
        "is_featured",
        "order",
        "is_active",
    ]
    list_filter = ["is_active", "is_featured"]
    search_fields = [
        "title_ru",
        "title_en",
        "title_kg",
        "contact_name_ru",
        "email",
        "phone",
    ]
    list_editable = ["is_featured", "order", "is_active"]
    fieldsets = [
        (
            "Basic Information",
            {
                "fields": [
                    ("title_ru", "title_en", "title_kg"),
                    ("is_featured", "is_active", "order"),
                ]
            },
        ),
        (
            "Description",
            {
                "fields": [
                    "description_ru",
                    "description_en",
                    "description_kg",
                ]
            },
        ),
        (
            "Contact Person",
            {
                "fields": [
                    ("contact_name_ru", "contact_name_en", "contact_name_kg"),
                    ("email", "phone"),
                    "photo",
                ]
            },
        ),
        (
            "Office Information",
            {
                "fields": [
                    ("office_location_ru", "office_location_en", "office_location_kg"),
                    ("office_hours_ru", "office_hours_en", "office_hours_kg"),
                ]
            },
        ),
    ]


@admin.register(SocialNetworkAccount)
class SocialNetworkAccountAdmin(admin.ModelAdmin):
    list_display = [
        "name_ru",
        "network",
        "username",
        "is_official",
        "is_featured",
        "order",
        "is_active",
    ]
    list_filter = ["network", "is_official", "is_featured", "is_active"]
    search_fields = ["name_ru", "name_en", "name_kg", "username", "url"]
    list_editable = ["is_official", "is_featured", "order", "is_active"]
    fieldsets = [
        (
            "Basic Information",
            {
                "fields": [
                    ("name_ru", "name_en", "name_kg"),
                    ("network", "username"),
                    "url",
                ]
            },
        ),
        (
            "Description",
            {
                "fields": [
                    "description_ru",
                    "description_en",
                    "description_kg",
                ]
            },
        ),
        (
            "Display Settings",
            {
                "fields": [
                    ("icon", "color_hex"),
                    ("is_official", "is_featured"),
                    ("order", "is_active"),
                ]
            },
        ),
    ]


@admin.register(SocialCommunity)
class SocialCommunityAdmin(admin.ModelAdmin):
    list_display = [
        "title_ru",
        "network",
        "members_count",
        "is_verified",
        "is_featured",
        "order",
        "is_active",
    ]
    list_filter = ["network", "is_verified", "is_featured", "is_active"]
    search_fields = ["title_ru", "title_en", "title_kg", "url"]
    list_editable = ["is_verified", "is_featured", "order", "is_active"]
    fieldsets = [
        (
            "Basic Information",
            {
                "fields": [
                    ("title_ru", "title_en", "title_kg"),
                    "network",
                    "url",
                ]
            },
        ),
        (
            "Description",
            {
                "fields": [
                    "description_ru",
                    "description_en",
                    "description_kg",
                ]
            },
        ),
        (
            "Statistics",
            {
                "fields": [
                    ("members_count", "posts_count"),
                ]
            },
        ),
        (
            "Display Settings",
            {
                "fields": [
                    "banner_image",
                    ("is_verified", "is_featured"),
                    ("order", "is_active"),
                ]
            },
        ),
    ]
