from django.db import models
from django.utils.translation import gettext_lazy as _


class TabCategory(models.Model):
    """Категории/табы (history, about, management, specializations, departments)"""

    key = models.CharField(max_length=50, unique=True, verbose_name=_("Ключ"))

    # Многоязычные поля для заголовка
    title_ru = models.CharField(max_length=200, verbose_name=_("Заголовок (Русский)"))
    title_kg = models.CharField(max_length=200, verbose_name=_("Заголовок (Кыргызча)"))
    title_en = models.CharField(max_length=200, verbose_name=_("Заголовок (English)"))

    icon = models.CharField(
        max_length=10, blank=True, verbose_name=_("Иконка (эмодзи)")
    )
    order = models.PositiveSmallIntegerField(default=0, verbose_name=_("Порядок"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активно"))

    class Meta:
        verbose_name = _("Категория/Таб")
        verbose_name_plural = _("Категории/Табы")
        ordering = ["order"]

    def __str__(self):
        return self.title_ru

    def get_title(self, language="ru"):
        """Получить заголовок на указанном языке"""
        value = getattr(self, f"title_{language}", None)
        return value if value else self.title_ru


class Card(models.Model):
    """Карточки для табов (кроме history)"""

    tab = models.ForeignKey(
        TabCategory,
        on_delete=models.CASCADE,
        related_name="cards",
        verbose_name=_("Таб"),
    )

    # Многоязычные поля для заголовка
    title_ru = models.CharField(max_length=200, verbose_name=_("Заголовок (Русский)"))
    title_kg = models.CharField(max_length=200, verbose_name=_("Заголовок (Кыргызча)"))
    title_en = models.CharField(max_length=200, verbose_name=_("Заголовок (English)"))

    # Многоязычные поля для описания
    description_ru = models.TextField(verbose_name=_("Описание (Русский)"))
    description_kg = models.TextField(verbose_name=_("Описание (Кыргызча)"))
    description_en = models.TextField(verbose_name=_("Описание (English)"))

    order = models.PositiveSmallIntegerField(default=0, verbose_name=_("Порядок"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активно"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Карточка")
        verbose_name_plural = _("Карточки")
        ordering = ["tab", "order"]

    def __str__(self):
        return self.title_ru

    def get_title(self, language="ru"):
        """Получить заголовок на указанном языке"""
        value = getattr(self, f"title_{language}", None)
        return value if value else self.title_ru

    def get_description(self, language="ru"):
        """Получить описание на указанном языке"""
        value = getattr(self, f"description_{language}", None)
        return value if value else self.description_ru


class TimelineEvent(models.Model):
    """События для категории History (timeline)"""

    tab = models.ForeignKey(
        TabCategory,
        on_delete=models.CASCADE,
        related_name="timeline_events",
        verbose_name=_("Таб"),
        limit_choices_to={"key": "history"},
    )
    year = models.CharField(max_length=20, verbose_name=_("Год"))

    # Многоязычные поля для события
    event_ru = models.TextField(verbose_name=_("Событие (Русский)"))
    event_kg = models.TextField(verbose_name=_("Событие (Кыргызча)"))
    event_en = models.TextField(verbose_name=_("Событие (English)"))

    order = models.PositiveSmallIntegerField(default=0, verbose_name=_("Порядок"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активно"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Событие истории")
        verbose_name_plural = _("События истории")
        ordering = ["order"]

    def __str__(self):
        return f"{self.year} - {self.event_ru[:50]}"

    def get_event(self, language="ru"):
        """Получить событие на указанном языке"""
        value = getattr(self, f"event_{language}", None)
        return value if value else self.event_ru
