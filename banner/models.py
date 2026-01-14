from django.db import models
from cloudinary.models import CloudinaryField

class BannerSlide(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    image = CloudinaryField(verbose_name="Изображение")
    alt_text = models.CharField(max_length=200, verbose_name="Альтернативный текст", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активный")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Слайд баннера"
        verbose_name_plural = "Слайды баннера"
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.title