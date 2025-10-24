from django.contrib import admin
from .models import Announcement, AnnouncementTranslation

class AnnouncementTranslationInline(admin.TabularInline):
    model = AnnouncementTranslation
    extra = 1
    max_num = 3  # ru, en, ky

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'urgency', 'is_active', 'order', 'created_at', 'get_translations')
    list_filter = ('urgency', 'is_active', 'created_at')
    list_editable = ('urgency', 'is_active', 'order')
    inlines = [AnnouncementTranslationInline]
    readonly_fields = ('created_at', 'updated_at')
    
    def get_translations(self, obj):
        return ", ".join([f"{trans.language.upper()}" for trans in obj.translations.all()])
    get_translations.short_description = "Доступные переводы"

@admin.register(AnnouncementTranslation)
class AnnouncementTranslationAdmin(admin.ModelAdmin):
    list_display = ('announcement', 'language', 'title', 'category', 'department')
    list_filter = ('language', 'category', 'department')
    search_fields = ('title', 'description', 'department')