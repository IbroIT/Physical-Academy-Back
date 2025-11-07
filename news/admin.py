from django.contrib import admin
from django import forms
from django.db import models
from .models import News, NewsTranslation, NewsImage


class NewsTranslationInline(admin.TabularInline):
    model = NewsTranslation
    extra = 1
    max_num = 3  # ru, en, ky


class MultipleImageInput(forms.ClearableFileInput):
    """Кастомный виджет для множественной загрузки файлов"""

    allow_multiple_selected = True


class MultipleImageField(forms.FileField):
    """Кастомное поле для множественной загрузки"""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleImageInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class NewsAdminForm(forms.ModelForm):
    """Форма с поддержкой множественной загрузки изображений"""

    gallery_images_upload = MultipleImageField(
        label="Загрузить изображения в галерею",
        required=False,
        help_text="Выберите несколько изображений для загрузки в галерею (можно выбрать сразу много)",
    )

    class Meta:
        model = News
        fields = "__all__"


class NewsImageInline(admin.TabularInline):
    """Inline для управления существующими изображениями галереи"""

    model = NewsImage
    extra = 0
    fields = ["image", "order", "image_preview"]
    readonly_fields = ["image_preview"]
    ordering = ["order"]

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 150px;" />'
        return "Нет изображения"

    image_preview.short_description = "Превью"
    image_preview.allow_tags = True


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = (
        "id",
        "is_active",
        "order",
        "created_at",
        "get_translations",
        "gallery_count",
    )
    list_filter = ("is_active", "created_at")
    list_editable = ("is_active", "order")
    inlines = [NewsTranslationInline, NewsImageInline]
    readonly_fields = ("created_at", "updated_at", "main_image_preview")

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("image", "main_image_preview", "is_active", "order")},
        ),
        (
            "Галерея",
            {
                "fields": ("gallery_images_upload",),
                "description": "Загрузите сразу несколько изображений для галереи. Используйте Ctrl/Cmd для выбора нескольких файлов.",
            },
        ),
        ("Даты", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    def main_image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 200px; max-width: 300px;" />'
        return "Нет изображения"

    main_image_preview.short_description = "Превью главного изображения"
    main_image_preview.allow_tags = True

    def get_translations(self, obj):
        return ", ".join(
            [f"{trans.language.upper()}" for trans in obj.translations.all()]
        )

    get_translations.short_description = "Доступные переводы"

    def gallery_count(self, obj):
        count = obj.gallery_images.count()
        return f"{count} фото"

    gallery_count.short_description = "Изображений в галерее"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Обработка множественной загрузки изображений
        images = request.FILES.getlist("gallery_images_upload")
        if images:
            # Получаем максимальный порядок существующих изображений
            max_order = (
                obj.gallery_images.aggregate(models.Max("order"))["order__max"] or 0
            )

            for index, image in enumerate(images):
                NewsImage.objects.create(
                    news=obj, image=image, order=max_order + index + 1
                )

            self.message_user(
                request, f"Успешно загружено {len(images)} изображений в галерею!"
            )


@admin.register(NewsTranslation)
class NewsTranslationAdmin(admin.ModelAdmin):
    list_display = ("news", "language", "title", "category")
    list_filter = ("language", "category")
    search_fields = ("title", "description")


@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    """Админка для прямого управления изображениями галереи"""

    list_display = ("id", "news", "image_preview", "order", "created_at")
    list_filter = ("news", "created_at")
    list_editable = ("order",)
    readonly_fields = ("created_at", "image_preview")
    ordering = ["news", "order"]

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 150px;" />'
        return "Нет изображения"

    image_preview.short_description = "Превью"
    image_preview.allow_tags = True
