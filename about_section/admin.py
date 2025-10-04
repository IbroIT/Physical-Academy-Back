from django.contrib import admin
from django.utils.html import format_html
from .models import Leadership, Accreditation, DownloadableDocument, OrganizationStructure

# Register your models here.

@admin.register(OrganizationStructure)
class OrganizationStructureAdmin(admin.ModelAdmin):
    """Admin interface for OrganizationStructure model"""
    
    list_display = [
        'name_ru', 'structure_type', 'head_name_ru', 'icon_display', 
        'children_count', 'is_active', 'order'
    ]
    list_filter = ['structure_type', 'is_active', 'parent']
    search_fields = ['name_ru', 'name_en', 'name_ky', 'head_name_ru', 'head_name_en', 'head_name_ky']
    ordering = ['structure_type', 'order', 'name_ru']
    list_editable = ['is_active', 'order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name_ru', 'structure_type', 'icon', 'parent', 'is_active', 'order')
        }),
        ('Переводы названия', {
            'fields': ('name_en', 'name_ky'),
            'classes': ('collapse',)
        }),
        ('Руководитель', {
            'fields': ('head_name_ru', 'phone', 'email'),
        }),
        ('Переводы имени руководителя', {
            'fields': ('head_name_en', 'head_name_ky'),
            'classes': ('collapse',)
        }),
    )
    
    def icon_display(self, obj):
        """Display icon in admin list"""
        if obj.icon:
            return format_html('<span style="font-size: 20px;">{}</span>', obj.icon)
        return '-'
    icon_display.short_description = 'Иконка'
    
    def children_count(self, obj):
        """Display count of child departments"""
        count = obj.children.count()
        if count > 0:
            return f'{count} подразделений'
        return '-'
    children_count.short_description = 'Подразделения'



@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'department', 'leadership_type', 'is_director', 'is_active', 'order']
    list_filter = ['leadership_type', 'department', 'is_director', 'is_active']
    search_fields = ['name', 'name_kg', 'name_en', 'position', 'email']
    list_editable = ['order', 'is_active']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'name_kg', 'name_en', 'image')
        }),
        ('Должность', {
            'fields': ('position', 'position_kg', 'position_en', 'leadership_type', 'is_director')
        }),
        ('Ученая степень', {
            'fields': ('degree', 'degree_kg', 'degree_en')
        }),
        ('Опыт работы', {
            'fields': ('experience', 'experience_kg', 'experience_en')
        }),
        ('Департамент/Кафедра', {
            'fields': ('department', 'department_kg', 'department_en')
        }),
        ('Специализация', {
            'fields': ('specialization', 'specialization_kg', 'specialization_en'),
            'classes': ('collapse',)
        }),
        ('Контакты', {
            'fields': ('email', 'phone')
        }),
        ('Биография', {
            'fields': ('bio', 'bio_kg', 'bio_en'),
            'classes': ('collapse',)
        }),
        ('Достижения', {
            'fields': ('achievements', 'achievements_kg', 'achievements_en'),
            'classes': ('collapse',)
        }),
        ('Системные поля', {
            'fields': ('is_active', 'order', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(Accreditation)
class AccreditationAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'accreditation_type', 'issue_date', 'expiry_date', 'is_valid', 'is_active']
    list_filter = ['accreditation_type', 'is_active', 'issue_date', 'expiry_date']
    search_fields = ['name', 'name_kg', 'name_en', 'organization', 'certificate_number']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at', 'is_valid']
    date_hierarchy = 'issue_date'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'name_kg', 'name_en', 'accreditation_type')
        }),
        ('Организация', {
            'fields': ('organization', 'organization_kg', 'organization_en', 'organization_logo')
        }),
        ('Описание', {
            'fields': ('description', 'description_kg', 'description_en'),
            'classes': ('collapse',)
        }),
        ('Сертификат', {
            'fields': ('certificate_image', 'certificate_number', 'issue_date', 'expiry_date')
        }),
        ('Настройки', {
            'fields': ('is_active', 'order')
        }),
        ('Метаданные', {
            'fields': ('created_at', 'updated_at', 'is_valid'),
            'classes': ('collapse',)
        })
    )


@admin.register(DownloadableDocument)
class DownloadableDocumentAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'file', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title_ru', 'title_kg', 'title_en']
    list_editable = ['is_active']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title_ru', 'title_kg', 'title_en', 'file')
        }),
        ('Описание', {
            'fields': ('description_ru', 'description_kg', 'description_en'),
            'classes': ('collapse',)
        }),
        ('Настройки', {
            'fields': ('is_active', 'file_size')
        }),
        ('Метаданные', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )