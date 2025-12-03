from django.db import models
from django.utils.translation import gettext_lazy as _


class DepartmentCategory(models.Model):
    """Категория кафедры (languages, philosophy, fundamental, theory, pedagogy)"""

    key = models.CharField(max_length=50, unique=True, verbose_name=_("Ключ категории"))

    # Многоязычные поля для названия
    name_ru = models.CharField(max_length=200, verbose_name=_("Название (Русский)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Название (Кыргызча)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Название (English)"))

    # Цвета для UI (опционально)
    color = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Цвет"),
        help_text="Например: blue-500, green-600",
    )

    order = models.PositiveSmallIntegerField(default=0, verbose_name=_("Порядок"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активно"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Категория кафедры")
        verbose_name_plural = _("Категории кафедр")
        ordering = ["order"]

    def __str__(self):
        return self.name_ru

    def get_name(self, language="ru"):
        """Получить название на указанном языке"""
        value = getattr(self, f"name_{language}", None)
        return value if value else self.name_ru


class DepartmentInfo(models.Model):
    """Информация о кафедре (описание, особенности)"""

    category = models.ForeignKey(
        DepartmentCategory,
        on_delete=models.CASCADE,
        related_name="info_items",
        verbose_name=_("Категория"),
    )

    info_type = models.CharField(
        max_length=50,
        choices=[
            ("description", _("Описание")),
            ("feature", _("Особенность")),
        ],
        verbose_name=_("Тип информации"),
    )

    # Многоязычные поля для контента
    content_ru = models.TextField(verbose_name=_("Контент (Русский)"))
    content_kg = models.TextField(verbose_name=_("Контент (Кыргызча)"))
    content_en = models.TextField(verbose_name=_("Контент (English)"))

    order = models.PositiveSmallIntegerField(default=0, verbose_name=_("Порядок"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активно"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Информация о кафедре")
        verbose_name_plural = _("Информация о кафедрах")
        ordering = ["category", "info_type", "order"]

    def __str__(self):
        return f"{self.category.name_ru} - {self.get_info_type_display()}"

    def get_content(self, language="ru"):
        """Получить контент на указанном языке"""
        value = getattr(self, f"content_{language}", None)
        return value if value else self.content_ru
