from django.contrib import admin
from .models import Club, ClubCategory, ClubLeader, ClubStats


class ClubLeaderInline(admin.TabularInline):
    model = ClubLeader
    extra = 1
    fields = ['name_ru', 'role_ru', 'email', 'phone', 'order']


@admin.register(ClubCategory)
class ClubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'slug', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name_ru',)}
    search_fields = ['name_ru', 'name_en', 'name_kg']
    ordering = ['order', 'name_ru']


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'category', 'status', 'members_count', 'is_active', 'order']
    list_filter = ['category', 'status', 'is_active']
    list_editable = ['status', 'is_active', 'order']
    search_fields = ['name_ru', 'name_en', 'name_kg', 'description_ru']
    ordering = ['order', '-members_count']
    inlines = [ClubLeaderInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('category', 'icon', 'status', 'members_count', 'join_link', 'order', 'is_active')
        }),
        ('Название', {
            'fields': ('name_ru', 'name_en', 'name_kg')
        }),
        ('Краткое описание', {
            'fields': ('short_description_ru', 'short_description_en', 'short_description_kg')
        }),
        ('Полное описание', {
            'fields': ('description_ru', 'description_en', 'description_kg')
        }),
        ('Цели и задачи', {
            'fields': ('goals_ru', 'goals_en', 'goals_kg')
        }),
        ('Мотивация', {
            'fields': ('motivation_ru', 'motivation_en', 'motivation_kg')
        }),
        ('Расписание встреч', {
            'fields': ('meetings_ru', 'meetings_en', 'meetings_kg')
        }),
        ('Дополнительно', {
            'fields': ('tags',)
        }),
    )


@admin.register(ClubLeader)
class ClubLeaderAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'club', 'role_ru', 'email', 'order']
    list_filter = ['club']
    list_editable = ['order']
    search_fields = ['name_ru', 'name_en', 'name_kg', 'email']
    ordering = ['order', 'name_ru']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('club', 'photo', 'order')
        }),
        ('ФИО', {
            'fields': ('name_ru', 'name_en', 'name_kg')
        }),
        ('Роль/Должность', {
            'fields': ('role_ru', 'role_en', 'role_kg')
        }),
        ('Контакты', {
            'fields': ('email', 'phone')
        }),
    )


@admin.register(ClubStats)
class ClubStatsAdmin(admin.ModelAdmin):
    list_display = ['label_ru', 'value', 'icon', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('value', 'icon', 'order', 'is_active')
        }),
        ('Метка', {
            'fields': ('label_ru', 'label_en', 'label_kg')
        }),
    )
