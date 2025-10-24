from django.contrib import admin
from django.utils.html import format_html
from .models import Quote, QuoteTranslation
from django.utils.translation import gettext_lazy as _

class QuoteTranslationInline(admin.TabularInline):
    model = QuoteTranslation
    extra = 1
    max_num = 3  # ru, en, ky

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'text_preview', 'author_preview', 
        'is_active', 'order', 'created_at', 'get_translations'
    )
    list_filter = ('is_active', 'created_at')
    list_editable = ('is_active', 'order')
    inlines = [QuoteTranslationInline]
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    fieldsets = (
        (_("Основная информация"), {
            'fields': ('image', 'image_preview', 'is_active', 'order')
        }),
        (_("Даты"), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def text_preview(self, obj):
        ru_translation = obj.translations.filter(language='ru').first()
        if ru_translation:
            text = ru_translation.text
            return text[:50] + "..." if len(text) > 50 else text
        return "No translation"
    text_preview.short_description = _("Текст цитаты")

    def author_preview(self, obj):
        ru_translation = obj.translations.filter(language='ru').first()
        return ru_translation.author if ru_translation else "No author"
    author_preview.short_description = _("Автор")

    def get_translations(self, obj):
        return ", ".join([f"{trans.language.upper()}" for trans in obj.translations.all()])
    get_translations.short_description = _("Доступные переводы")

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 50%;" />',
                obj.image.url
            )
        return _("Нет изображения")
    image_preview.short_description = _("Предпросмотр изображения")

@admin.register(QuoteTranslation)
class QuoteTranslationAdmin(admin.ModelAdmin):
    list_display = ('quote', 'language', 'author', 'text_preview')
    list_filter = ('language',)
    search_fields = ('text', 'author', 'author_title')

    def text_preview(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    text_preview.short_description = _("Текст цитаты")