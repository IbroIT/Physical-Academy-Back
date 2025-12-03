from django.db import models
from django.utils.translation import gettext_lazy as _


class TabCategory(models.Model):
    """Категории/табы (history, about, management, specializations, departments)"""

    key = models.CharField(max_length=50, unique=True, verbose_name=_("Ключ"))
    title = models.CharField(max_length=200, verbose_name=_("Заголовок"))
    icon_svg = models.TextField(blank=True, verbose_name=_("SVG иконка"))
    order = models.PositiveSmallIntegerField(default=0, verbose_name=_("Порядок"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активно"))

    class Meta:
        verbose_name = _("Категория/Таб")
        verbose_name_plural = _("Категории/Табы")
        ordering = ["order"]

    def __str__(self):
        return self.title


class Card(models.Model):
    """Карточки для табов (кроме history)"""

    tab = models.ForeignKey(
        TabCategory,
        on_delete=models.CASCADE,
        related_name="cards",
        verbose_name=_("Таб"),
    )
    title = models.CharField(max_length=200, verbose_name=_("Заголовок"))
    description = models.TextField(verbose_name=_("Описание"))
    order = models.PositiveSmallIntegerField(default=0, verbose_name=_("Порядок"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активно"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Карточка")
        verbose_name_plural = _("Карточки")
        ordering = ["tab", "order"]

    def __str__(self):
        return self.title


class TimelineEvent(models.Model):
    """События для категории History (timeline)"""

    year = models.CharField(max_length=20, verbose_name=_("Год"))
    event = models.TextField(verbose_name=_("Событие"))
    order = models.PositiveSmallIntegerField(default=0, verbose_name=_("Порядок"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активно"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Событие истории")
        verbose_name_plural = _("События истории")
        ordering = ["order"]

    def __str__(self):
        return f"{self.year} - {self.event[:50]}"
