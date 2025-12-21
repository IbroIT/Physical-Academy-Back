from django.contrib import admin
from .models import DepartmentInfo, TabCategory, Management


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    pass

class DepartmentInfoInline(admin.StackedInline):
    model = DepartmentInfo
    extra = 0
    max_num = 1
    fields = ("description_ru", "description_kg", "description_en", "is_active")


@admin.register(TabCategory)
class DepartmentCategoryAdmin(admin.ModelAdmin):
    inlines = [DepartmentInfoInline]

@admin.register(DepartmentInfo)
class DepartmentInfoAdmin(admin.ModelAdmin):
    pass

