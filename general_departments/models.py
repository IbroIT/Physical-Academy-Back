from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from cloudinary.models import CloudinaryField
from ckeditor_uploader.fields import RichTextUploadingField



class TabCategory(models.Model):
    """Категории/табы (history, about, management, specializations, departments)"""

    # Многоязычные поля для заголовка
    name_ru = models.CharField(max_length=200, verbose_name=_("Заголовок (Русский)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Заголовок (Кыргызча)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Заголовок (English)"))

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
    """Описание кафедры"""

    category = models.OneToOneField(
        TabCategory,
        on_delete=models.CASCADE,
        related_name="info",
        verbose_name=_("Категория"),
    )

    # Многоязычные поля для описания
    description_ru = RichTextUploadingField(verbose_name=_("Описание(Русский)"), blank=True, null=True)
    description_kg = RichTextUploadingField(verbose_name=_("Описание(Кыргызча)"), blank=True, null=True)
    description_en = RichTextUploadingField(verbose_name=_("Описание(English)"), blank=True, null=True)

    is_active = models.BooleanField(default=True, verbose_name=_("Активно"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Описание кафедры")
        verbose_name_plural = _("Описания кафедр")

    def __str__(self):
        return f"{self.category.name_ru} - Описание"

    def get_description(self, language="ru"):
        """Получить описание на указанном языке"""
        value = getattr(self, f"description_{language}", None)
        return value if value else self.description_ru

class Management(models.Model):
    """Руководство факультета (Management)"""

    department = models.ForeignKey(
        TabCategory,
        on_delete=models.CASCADE,
        related_name="management",
        verbose_name=_("Кафедра"),
        blank=True,
        null=True,
    )

    photo = CloudinaryField(verbose_name=_("Фото"))

    # Многоязычные поля для имени
    name_ru = models.CharField(max_length=200, verbose_name=_("Имя (Русский)"))
    name_kg = models.CharField(max_length=200, verbose_name=_("Имя (Кыргызча)"))
    name_en = models.CharField(max_length=200, verbose_name=_("Имя (English)"))

    # Многоязычные поля для роли
    role_ru = models.CharField(max_length=200, verbose_name=_("Роль (Русский)"))
    role_kg = models.CharField(max_length=200, verbose_name=_("Роль (Кыргызча)"))
    role_en = models.CharField(max_length=200, verbose_name=_("Роль (English)"))

    phone = models.CharField(
        max_length=50, blank=True, verbose_name=_("Номер телефона")
    )
    email = models.EmailField(blank=True, verbose_name=_("Email"))


    order = models.PositiveSmallIntegerField(default=0, verbose_name=_("Порядок"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активно"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Руководство")
        verbose_name_plural = _("Руководство")
        ordering = ["order"]

    def __str__(self):
        return f"{self.name_ru} - {self.role_ru}"

    def get_name(self, language="ru"):
        """Получить имя на указанном языке"""
        value = getattr(self, f"name_{language}", None)
        return value if value else self.name_ru

    def get_role(self, language="ru"):
        """Получить роль на указанном языке"""
        value = getattr(self, f"role_{language}", None)
        return value if value else self.role_ru

