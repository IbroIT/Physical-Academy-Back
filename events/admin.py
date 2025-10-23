from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title_preview', 
        'category', 
        'department', 
        'date', 
        'is_active', 
        'is_featured',
        'order'
    )
    list_filter = (
        'category', 
        'department', 
        'is_active', 
        'is_featured', 
        'date',
        'created_at'
    )
    list_editable = ('is_active', 'is_featured', 'order')
    search_fields = (
        'title_ru', 'title_en', 'title_ky',
        'description_ru', 'description_en', 'description_ky'
    )
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'date'
    
    fieldsets = (
        (_('Основная информация'), {
            'fields': (
                ('title_ru', 'title_en', 'title_ky'),
                ('description_ru', 'description_en', 'description_ky'),
                ('full_description_ru', 'full_description_en', 'full_description_ky'),
                'image',
            )
        }),
        (_('Детали мероприятия'), {
            'fields': (
                'category',
                'department',
                'date',
                'time',
                ('location_ru', 'location_en', 'location_ky'),
            )
        }),
        (_('Дополнительная информация'), {
            'fields': (
                ('audience_ru', 'audience_en', 'audience_ky'),
                ('format_ru', 'format_en', 'format_ky'),
                ('duration_ru', 'duration_en', 'duration_ky'),
            ),
            'classes': ('collapse',)
        }),
        (_('Организатор'), {
            'fields': (
                ('organizer_name_ru', 'organizer_name_en', 'organizer_name_ky'),
                ('organizer_contact_ru', 'organizer_contact_en', 'organizer_contact_ky'),
            ),
            'classes': ('collapse',)
        }),
        (_('Настройки'), {
            'fields': (
                'is_active',
                'is_featured',
                'order'
            )
        }),
        (_('Даты'), {
            'fields': (
                'created_at',
                'updated_at'
            ),
            'classes': ('collapse',)
        })
    )

    def title_preview(self, obj):
        return obj.title_ru[:50] + '...' if len(obj.title_ru) > 50 else obj.title_ru
    title_preview.short_description = _('Заголовок')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Добавляем CSS классы для лучшего отображения полей
        for field_name in form.base_fields:
            if field_name.endswith(('_ru', '_en', '_ky')):
                form.base_fields[field_name].widget.attrs['style'] = 'width: 95%;'
        return form