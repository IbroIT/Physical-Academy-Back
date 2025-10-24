from django.contrib import admin
from django.utils.html import format_html
from .models import Fact, FactTranslation
from django.utils.translation import gettext_lazy as _

class FactTranslationInline(admin.TabularInline):
    model = FactTranslation
    extra = 1
    max_num = 3  # ru, en, ky

@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'icon_display', 'end_value', 'label_preview', 
        'color', 'is_active', 'order', 'get_translations'
    )
    list_filter = ('color', 'is_active', 'created_at')
    list_editable = ('end_value', 'color', 'is_active', 'order')
    inlines = [FactTranslationInline]
    readonly_fields = ('created_at', 'updated_at', 'preview_display')
    fieldsets = (
        (_("Основная информация"), {
            'fields': (
                'icon', 'end_value', 'duration', 'delay', 'color',
                'is_active', 'order'
            )
        }),
        (_("Предпросмотр"), {
            'fields': ('preview_display',),
            'classes': ('collapse',)
        }),
        (_("Даты"), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def icon_display(self, obj):
        return format_html(
            '<span style="font-size: 24px;">{}</span>',
            obj.icon
        )
    icon_display.short_description = _("Иконка")

    def label_preview(self, obj):
        ru_translation = obj.translations.filter(language='ru').first()
        return ru_translation.label if ru_translation else "No label"
    label_preview.short_description = _("Подпись")

    def get_translations(self, obj):
        return ", ".join([f"{trans.language.upper()}" for trans in obj.translations.all()])
    get_translations.short_description = _("Доступные переводы")

    def preview_display(self, obj):
        ru_translation = obj.translations.filter(language='ru').first()
        label = ru_translation.label if ru_translation else "No label"
        
        return format_html(
            '''
            <div style="border: 2px solid #e2e8f0; border-radius: 16px; padding: 32px; text-align: center; background: white; max-width: 300px;">
                <div style="font-size: 48px; margin-bottom: 16px;">{}</div>
                <div style="font-size: 48px; font-weight: bold; color: #2563eb; margin-bottom: 8px;">{}+</div>
                <div style="font-size: 18px; color: #374151; font-weight: 500; background: #dbeafe; padding: 8px 16px; border-radius: 9999px; border: 1px solid #dbeafe; display: inline-block;">
                    {}
                </div>
            </div>
            ''',
            obj.icon, obj.end_value, label
        )
    preview_display.short_description = _("Предпросмотр")

@admin.register(FactTranslation)
class FactTranslationAdmin(admin.ModelAdmin):
    list_display = ('fact', 'language', 'label')
    list_filter = ('language',)
    search_fields = ('label',)