from django.contrib import admin
from .models import (
    IPChainInfo,
    IPChainInfoTranslation,
    IPChainStatistic,
    IPChainStatisticTranslation,
    Patent,
    PatentTranslation,
    BlockchainFeature,
    BlockchainFeatureTranslation,
    IPChainBenefit,
    IPChainBenefitTranslation,
    BlockchainData,
    BlockchainDataTranslation,
)


class IPChainInfoTranslationInline(admin.TabularInline):
    model = IPChainInfoTranslation
    extra = 3
    max_num = 3
    fields = ["language", "title", "subtitle"]


@admin.register(IPChainInfo)
class IPChainInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_active", "order", "created_at"]
    list_filter = ["is_active", "created_at"]
    list_editable = ["is_active", "order"]
    search_fields = ["title", "subtitle"]
    inlines = [IPChainInfoTranslationInline]

    fieldsets = (
        ("Основная информация", {"fields": ("title", "subtitle")}),
        ("Настройки", {"fields": ("is_active", "order")}),
    )


class IPChainStatisticTranslationInline(admin.TabularInline):
    model = IPChainStatisticTranslation
    extra = 3
    max_num = 3
    fields = ["language", "label"]


@admin.register(IPChainStatistic)
class IPChainStatisticAdmin(admin.ModelAdmin):
    list_display = ["id", "value", "is_active", "order", "created_at"]
    list_filter = ["is_active", "created_at"]
    list_editable = ["is_active", "order"]
    search_fields = ["value"]
    inlines = [IPChainStatisticTranslationInline]

    fieldsets = (
        ("Статистика", {"fields": ("value",)}),
        ("Настройки", {"fields": ("is_active", "order")}),
    )


class PatentTranslationInline(admin.StackedInline):
    model = PatentTranslation
    extra = 3
    max_num = 3
    fields = [
        "language",
        "title",
        "description",
        "full_description",
        "technologies",
        "applications",
    ]


@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    list_display = ["number", "status", "year", "date", "icon", "is_active", "order"]
    list_filter = ["status", "year", "is_active", "date"]
    list_editable = ["is_active", "order"]
    search_fields = ["number"]
    date_hierarchy = "date"
    inlines = [PatentTranslationInline]

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("number", "status", "year", "date", "icon")},
        ),
        ("Настройки", {"fields": ("is_active", "order")}),
    )


class BlockchainFeatureTranslationInline(admin.TabularInline):
    model = BlockchainFeatureTranslation
    extra = 3
    max_num = 3
    fields = ["language", "title", "description"]


@admin.register(BlockchainFeature)
class BlockchainFeatureAdmin(admin.ModelAdmin):
    list_display = ["id", "icon", "is_active", "order", "created_at"]
    list_filter = ["is_active", "created_at"]
    list_editable = ["is_active", "order"]
    inlines = [BlockchainFeatureTranslationInline]

    fieldsets = (
        ("Функция блокчейна", {"fields": ("icon",)}),
        ("Настройки", {"fields": ("is_active", "order")}),
    )


class IPChainBenefitTranslationInline(admin.TabularInline):
    model = IPChainBenefitTranslation
    extra = 3
    max_num = 3
    fields = ["language", "title", "description"]


@admin.register(IPChainBenefit)
class IPChainBenefitAdmin(admin.ModelAdmin):
    list_display = ["id", "icon", "is_active", "order", "created_at"]
    list_filter = ["is_active", "created_at"]
    list_editable = ["is_active", "order"]
    inlines = [IPChainBenefitTranslationInline]

    fieldsets = (
        ("Преимущество", {"fields": ("icon",)}),
        ("Настройки", {"fields": ("is_active", "order")}),
    )


class BlockchainDataTranslationInline(admin.TabularInline):
    model = BlockchainDataTranslation
    extra = 3
    max_num = 3
    fields = [
        "language",
        "current_block_label",
        "ip_registrations_label",
        "smart_contracts_label",
        "network_hash_label",
    ]


@admin.register(BlockchainData)
class BlockchainDataAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "current_block",
        "ip_registrations",
        "smart_contracts",
        "network_hash",
        "is_active",
        "order",
        "updated_at",
    ]
    list_filter = ["is_active", "updated_at", "created_at"]
    list_editable = ["is_active", "order"]
    search_fields = ["current_block", "network_hash"]
    readonly_fields = ["updated_at", "created_at"]
    inlines = [BlockchainDataTranslationInline]

    fieldsets = (
        (
            "Данные блокчейна",
            {
                "fields": (
                    "current_block",
                    "ip_registrations",
                    "smart_contracts",
                    "network_hash",
                )
            },
        ),
        ("Настройки", {"fields": ("is_active", "order")}),
        ("Даты", {"fields": ("updated_at", "created_at"), "classes": ("collapse",)}),
    )
