from django.contrib import admin
from .models import (
    FacultyTeachers,
    MasterPrograms,
    Faculty,
    FacultyContacts,
    FacultyStatistics,
    FacultySports,
    FacultyPrograms,
    FacultySpecialization,
    CollegePrograms,
    PhdPrograms,
    FacultySection,
    FacultySectionItem,
)

# Register existing models
admin.site.register(MasterPrograms)
admin.site.register(FacultyTeachers)
admin.site.register(FacultySpecialization)
admin.site.register(FacultyPrograms)
admin.site.register(FacultySports)
admin.site.register(FacultyContacts)
admin.site.register(FacultyStatistics)
admin.site.register(CollegePrograms)
admin.site.register(PhdPrograms)


# Faculty Public Pages Admin
class FacultySectionItemInline(admin.TabularInline):
    """Inline for faculty section items"""

    model = FacultySectionItem
    extra = 1
    fields = ["text_ru", "text_en", "text_kg", "order"]
    ordering = ["order"]


class FacultySectionInline(admin.StackedInline):
    """Inline for faculty sections"""

    model = FacultySection
    extra = 1
    fields = ["title_ru", "title_en", "title_kg", "order"]
    ordering = ["order"]
    show_change_link = True  # Allow editing items in section


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    """Admin for faculties with inline public sections"""

    list_display = ["name_ru", "slug", "is_active", "order", "updated_at"]
    list_filter = ["is_active", "created_at"]
    search_fields = ["name_ru", "name_en", "name_kg", "slug"]
    prepopulated_fields = {"slug": ("name_en",)}

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("slug", "is_active", "order")},
        ),
        (
            "Название (локализация)",
            {"fields": ("name_ru", "name_en", "name_kg"), "classes": ("wide",)},
        ),
        (
            "Описание (локализация)",
            {
                "fields": ("description_ru", "description_en", "description_kg"),
                "classes": ("wide",),
            },
        ),
        ("Баннер", {"fields": ("banner_image",)}),
        (
            "Миссия (JSON)",
            {
                "fields": ("mission_ru", "mission_en", "mission_kg"),
                "classes": ("collapse",),
            },
        ),
        (
            "Достижения (JSON)",
            {
                "fields": ("achievements_ru", "achievements_en", "achievements_kg"),
                "classes": ("collapse",),
            },
        ),
    )

    inlines = [FacultySectionInline]

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"


@admin.register(FacultySection)
class FacultySectionAdmin(admin.ModelAdmin):
    """Admin for faculty sections with inline items"""

    list_display = ["title_ru", "faculty", "order"]
    list_filter = ["faculty"]
    search_fields = ["title_ru", "title_en", "title_kg"]

    fieldsets = (
        ("Информация о разделе", {"fields": ("faculty", "order")}),
        (
            "Заголовок (локализация)",
            {"fields": ("title_ru", "title_en", "title_kg"), "classes": ("wide",)},
        ),
    )

    inlines = [FacultySectionItemInline]

    class Meta:
        verbose_name = "Раздел факультета"
        verbose_name_plural = "Разделы факультетов"


@admin.register(FacultySectionItem)
class FacultySectionItemAdmin(admin.ModelAdmin):
    """Admin for individual faculty section items"""

    list_display = ["text_ru", "section", "order"]
    list_filter = ["section__faculty"]
    search_fields = ["text_ru", "text_en", "text_kg"]

    fieldsets = (
        ("Информация об элементе", {"fields": ("section", "order")}),
        (
            "Текст (локализация)",
            {"fields": ("text_ru", "text_en", "text_kg"), "classes": ("wide",)},
        ),
    )

    class Meta:
        verbose_name = "Элемент раздела"
        verbose_name_plural = "Элементы разделов"
