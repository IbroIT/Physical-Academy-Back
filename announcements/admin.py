from django.contrib import admin
from django import forms
from django.db import models
from .models import Announcement, AnnouncementTranslation, AnnouncementImage


class AnnouncementTranslationInline(admin.TabularInline):
    model = AnnouncementTranslation
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


class AnnouncementAdminForm(forms.ModelForm):
    """Форма с поддержкой множественной загрузки изображений"""

    gallery_images_upload = MultipleImageField(
        label="Загрузить изображения в галерею",
        required=False,
        help_text="Выберите несколько изображений для загрузки в галерею (можно выбрать сразу много)",
    )

    class Meta:
        model = Announcement
        fields = "__all__"


class AnnouncementImageInline(admin.TabularInline):
    """Inline для управления существующими изображениями галереи"""

    model = AnnouncementImage
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


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    form = AnnouncementAdminForm
    list_display = (
        "id",
        "urgency",
        "is_active",
        "order",
        "created_at",
        "get_translations",
        "gallery_count",
    )
    list_filter = ("urgency", "is_active", "created_at")
    list_editable = ("urgency", "is_active", "order")
    inlines = [AnnouncementTranslationInline, AnnouncementImageInline]
    readonly_fields = ("created_at", "updated_at", "main_image_preview")

    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "image",
                    "main_image_preview",
                    "urgency",
                    "is_active",
                    "order",
                )
            },
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
                AnnouncementImage.objects.create(
                    announcement=obj, image=image, order=max_order + index + 1
                )

            self.message_user(
                request, f"Успешно загружено {len(images)} изображений в галерею!"
            )


@admin.register(AnnouncementTranslation)
class AnnouncementTranslationAdmin(admin.ModelAdmin):
    list_display = ("announcement", "language", "title", "category", "department")
    list_filter = ("language", "category", "department")
    search_fields = ("title", "description", "department")


@admin.register(AnnouncementImage)
class AnnouncementImageAdmin(admin.ModelAdmin):
    """Админка для прямого управления изображениями галереи"""

    list_display = ("id", "announcement", "image_preview", "order", "created_at")
    list_filter = ("announcement", "created_at")
    list_editable = ("order",)
    readonly_fields = ("created_at", "image_preview")
    ordering = ["announcement", "order"]

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 150px;" />'
        return "Нет изображения"

    image_preview.short_description = "Превью"
    image_preview.allow_tags = True
