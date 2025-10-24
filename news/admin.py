from django.contrib import admin
from .models import News, NewsTranslation

class NewsTranslationInline(admin.TabularInline):
    model = NewsTranslation
    extra = 1
    max_num = 3  # ru, en, ky

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'order', 'created_at', 'get_translations')
    list_filter = ('is_active', 'created_at')
    list_editable = ('is_active', 'order')
    inlines = [NewsTranslationInline]
    readonly_fields = ('created_at', 'updated_at')
    
    def get_translations(self, obj):
        return ", ".join([f"{trans.language.upper()}" for trans in obj.translations.all()])
    get_translations.short_description = "Доступные переводы"

@admin.register(NewsTranslation)
class NewsTranslationAdmin(admin.ModelAdmin):
    list_display = ('news', 'language', 'title', 'category')
    list_filter = ('language', 'category')
    search_fields = ('title', 'description')