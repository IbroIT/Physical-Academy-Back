from django.db import models
from django.utils.translation import gettext_lazy as _

class News(models.Model):
    # Базовые поля (не переводимые)
    image = models.ImageField(upload_to='news/', verbose_name=_("Изображение"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"News {self.id}"

class NewsTranslation(models.Model):
    LANGUAGES = [
        ('ru', 'Русский'),
        ('en', 'English'),
        ('kg', 'Кыргызча'),
    ]

    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=2, choices=LANGUAGES, verbose_name=_("Язык"))
    
    # Переводимые поля
    title = models.CharField(max_length=200, verbose_name=_("Заголовок"))
    description = models.TextField(verbose_name=_("Описание"))
    category = models.CharField(max_length=100, verbose_name=_("Категория"))
    content = models.TextField(blank=True, verbose_name=_("Полное содержание"))

    class Meta:
        verbose_name = _("Перевод новости")
        verbose_name_plural = _("Переводы новостей")
        unique_together = ['news', 'language']

    def __str__(self):
        return f"{self.news.id} - {self.get_language_display()}"