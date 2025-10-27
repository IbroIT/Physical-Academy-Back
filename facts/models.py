from django.db import models
from django.utils.translation import gettext_lazy as _

class Fact(models.Model):
    # Базовые поля (не переводимые)
    end_value = models.PositiveIntegerField(verbose_name=_("Конечное значение"))
    icon = models.CharField(
        max_length=50, 
        verbose_name=_("Иконка"),
        help_text=_("Эмодзи или код иконки, например: 🎓, 🏆, ⚽")
    )
    duration = models.PositiveIntegerField(
        default=2000,
        verbose_name=_("Длительность анимации (мс)"),
        help_text=_("Время анимации счетчика в миллисекундах")
    )
    delay = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Задержка анимации (мс)"),
        help_text=_("Задержка перед началом анимации в миллисекундах")
    )
    color = models.CharField(
        max_length=50,
        default='blue',
        choices=[
            ('blue', _('Синий')),
            ('green', _('Зеленый')),
            ('red', _('Красный')),
            ('purple', _('Фиолетовый')),
            ('orange', _('Оранжевый')),
            ('cyan', _('Голубой')),
        ],
        verbose_name=_("Цветовая схема")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        verbose_name = _("Факт")
        verbose_name_plural = _("Факты")
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"Fact {self.id} - {self.end_value}"

class FactTranslation(models.Model):
    LANGUAGES = [
        ('ru', 'Русский'),
        ('en', 'English'),
        ('kg', 'Кыргызча'),
    ]

    fact = models.ForeignKey(Fact, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=2, choices=LANGUAGES, verbose_name=_("Язык"))
    
    # Переводимые поля
    label = models.CharField(max_length=200, verbose_name=_("Подпись"))

    class Meta:
        verbose_name = _("Перевод факта")
        verbose_name_plural = _("Переводы фактов")
        unique_together = ['fact', 'language']

    def __str__(self):
        return f"{self.fact.id} - {self.get_language_display()}"