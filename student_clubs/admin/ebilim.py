# COMMENTED OUT: Ebilim admin not needed - using i18n translations on frontend

"""
from django.contrib import admin
from ..models_ebilim import EbilimStat, EbilimQuickLink, EbilimSystemStatus


@admin.register(EbilimStat)
class EbilimStatAdmin(admin.ModelAdmin):
    list_display = ["key", "value", "label_en", "order"]
    list_editable = ["order"]
    search_fields = ["key", "value", "label_en", "label_ru", "label_kg"]
    ordering = ["order"]


@admin.register(EbilimQuickLink)
class EbilimQuickLinkAdmin(admin.ModelAdmin):
    list_display = ["name_en", "url", "icon", "order", "is_active"]
    list_editable = ["order", "is_active"]
    search_fields = ["name_en", "name_ru", "name_kg", "url"]
    list_filter = ["is_active"]
    ordering = ["order"]


@admin.register(EbilimSystemStatus)
class EbilimSystemStatusAdmin(admin.ModelAdmin):
    list_display = ["status", "last_update", "message_en"]
    list_filter = ["status"]
    search_fields = ["message_en", "message_ru", "message_kg"]
    readonly_fields = ["last_update"]
"""
