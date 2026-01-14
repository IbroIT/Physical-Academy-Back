from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField

class Quote(models.Model):
    # Базовые поля (не переводимые)
    image = CloudinaryField(
        blank=True, 
        null=True, 
        verbose_name=_("Изображение автора")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        verbose_name = _("Цитата")
        verbose_name_plural = _("Цитаты")
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"Quote {self.id}"

class QuoteTranslation(models.Model):
    LANGUAGES = [
        ('ru', 'Русский'),
        ('en', 'English'),
        ('kg', 'Кыргызча'),
    ]

    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=2, choices=LANGUAGES, verbose_name=_("Язык"))
    
    # Переводимые поля
    text = models.TextField(verbose_name=_("Текст цитаты"))
    author = models.CharField(max_length=200, verbose_name=_("Автор"))
    author_title = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name=_("Должность/титул автора")
    )

    class Meta:
        verbose_name = _("Перевод цитаты")
        verbose_name_plural = _("Переводы цитат")
        unique_together = ['quote', 'language']

    def __str__(self):
        return f"{self.quote.id} - {self.get_language_display()}"