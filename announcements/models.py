from django.db import models
from django.utils.translation import gettext_lazy as _


class Announcement(models.Model):
    URGENCY_LEVELS = [
        ("high", _("Высокая")),
        ("medium", _("Средняя")),
        ("low", _("Низкая")),
    ]

    # Базовые поля (не переводимые)
    image = models.ImageField(
        upload_to="announcements/", verbose_name=_("Главное изображение")
    )
    urgency = models.CharField(
        max_length=10,
        choices=URGENCY_LEVELS,
        default="low",
        verbose_name=_("Срочность"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        verbose_name = _("Объявление")
        verbose_name_plural = _("Объявления")
        ordering = ["order", "-created_at"]

    def __str__(self):
        return f"Announcement {self.id}"


class AnnouncementImage(models.Model):
    """Модель для галереи изображений объявления"""

    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.CASCADE,
        related_name="gallery_images",
        verbose_name=_("Объявление"),
    )
    image = models.ImageField(
        upload_to="announcements/gallery/", verbose_name=_("Изображение")
    )
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата загрузки")
    )

    class Meta:
        verbose_name = _("Изображение галереи")
        verbose_name_plural = _("Изображения галереи")
        ordering = ["order", "created_at"]

    def __str__(self):
        return f"Image for Announcement {self.announcement.id} (Order: {self.order})"


class AnnouncementTranslation(models.Model):
    LANGUAGES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    announcement = models.ForeignKey(
        Announcement, on_delete=models.CASCADE, related_name="translations"
    )
    language = models.CharField(max_length=2, choices=LANGUAGES, verbose_name=_("Язык"))

    # Переводимые поля
    title = models.CharField(max_length=200, verbose_name=_("Заголовок"))
    description = models.TextField(verbose_name=_("Описание"))
    category = models.CharField(max_length=100, verbose_name=_("Категория"))
    department = models.CharField(max_length=150, verbose_name=_("Отдел/Факультет"))
    content = models.TextField(blank=True, verbose_name=_("Полное содержание"))

    class Meta:
        verbose_name = _("Перевод объявления")
        verbose_name_plural = _("Переводы объявлений")
        unique_together = ["announcement", "language"]

    def __str__(self):
        return f"{self.announcement.id} - {self.get_language_display()}"
