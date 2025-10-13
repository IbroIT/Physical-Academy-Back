from django.db import models


class ScholarshipProgram(models.Model):
    """Стипендиальная программа для студентов"""

    name_ru = models.CharField(max_length=200, verbose_name="Название программы (RU)")
    name_en = models.CharField(max_length=200, verbose_name="Название программы (EN)")
    name_kg = models.CharField(max_length=200, verbose_name="Название программы (KG)")

    description_ru = models.TextField(verbose_name="Описание программы (RU)")
    description_en = models.TextField(verbose_name="Описание программы (EN)")
    description_kg = models.TextField(verbose_name="Описание программы (KG)")

    eligibility_criteria_ru = models.TextField(verbose_name="Критерии отбора (RU)")
    eligibility_criteria_en = models.TextField(verbose_name="Критерии отбора (EN)")
    eligibility_criteria_kg = models.TextField(verbose_name="Критерии отбора (KG)")

    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Сумма стипендии"
    )
    currency = models.CharField(max_length=10, default="KGS", verbose_name="Валюта")

    application_deadline = models.DateField(verbose_name="Дедлайн подачи заявок")
    application_link = models.URLField(
        blank=True, null=True, verbose_name="Ссылка для подачи заявки"
    )

    contact_email = models.EmailField(
        blank=True, null=True, verbose_name="Контактный email"
    )
    contact_phone = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Контактный телефон"
    )

    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Scholarship Program"
        verbose_name_plural = "Scholarship Programs"
        ordering = ["name_ru"]

    def __str__(self):
        return self.name_ru

    def get_field(self, field_name, language="ru"):
        """Получить значение поля на указанном языке"""
        field_with_lang = f"{field_name}_{language}"
        return getattr(self, field_with_lang, getattr(self, f"{field_name}_ru"))


class ScholarshipRequiredDocument(models.Model):
    """Документы, необходимые для подачи заявки на стипендию"""

    scholarship = models.ForeignKey(
        ScholarshipProgram,
        on_delete=models.CASCADE,
        related_name="required_documents",
        verbose_name="Стипендиальная программа",
    )

    name_ru = models.CharField(max_length=200, verbose_name="Название документа (RU)")
    name_en = models.CharField(max_length=200, verbose_name="Название документа (EN)")
    name_kg = models.CharField(max_length=200, verbose_name="Название документа (KG)")

    description_ru = models.TextField(
        verbose_name="Описание документа (RU)", blank=True, null=True
    )
    description_en = models.TextField(
        verbose_name="Описание документа (EN)", blank=True, null=True
    )
    description_kg = models.TextField(
        verbose_name="Описание документа (KG)", blank=True, null=True
    )

    is_required = models.BooleanField(default=True, verbose_name="Обязательный")
    order = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок")

    class Meta:
        verbose_name = "Required Document"
        verbose_name_plural = "Required Documents"
        ordering = ["scholarship", "order"]

    def __str__(self):
        return f"{self.scholarship.name_ru} - {self.name_ru}"

    def get_field(self, field_name, language="ru"):
        """Получить значение поля на указанном языке"""
        field_with_lang = f"{field_name}_{language}"
        return getattr(self, field_with_lang, getattr(self, f"{field_name}_ru"))


class VisaSupportService(models.Model):
    """Сервис поддержки по визовым вопросам"""

    title_ru = models.CharField(max_length=200, verbose_name="Заголовок (RU)")
    title_en = models.CharField(max_length=200, verbose_name="Заголовок (EN)")
    title_kg = models.CharField(max_length=200, verbose_name="Заголовок (KG)")

    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_en = models.TextField(verbose_name="Описание (EN)")
    description_kg = models.TextField(verbose_name="Описание (KG)")

    is_featured = models.BooleanField(default=False, verbose_name="Выделенный сервис")
    icon = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Иконка (класс)"
    )

    order = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Visa Support Service"
        verbose_name_plural = "Visa Support Services"
        ordering = ["order"]

    def __str__(self):
        return self.title_ru

    def get_field(self, field_name, language="ru"):
        """Получить значение поля на указанном языке"""
        field_with_lang = f"{field_name}_{language}"
        return getattr(self, field_with_lang, getattr(self, f"{field_name}_ru"))


class VisaSupportContact(models.Model):
    """Контактное лицо по визовым вопросам"""

    full_name_ru = models.CharField(max_length=200, verbose_name="ФИО (RU)")
    full_name_en = models.CharField(max_length=200, verbose_name="ФИО (EN)")
    full_name_kg = models.CharField(max_length=200, verbose_name="ФИО (KG)")

    position_ru = models.CharField(max_length=200, verbose_name="Должность (RU)")
    position_en = models.CharField(max_length=200, verbose_name="Должность (EN)")
    position_kg = models.CharField(max_length=200, verbose_name="Должность (KG)")

    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Телефон"
    )

    photo = models.ImageField(
        upload_to="visa_support/", blank=True, null=True, verbose_name="Фото"
    )

    office_location_ru = models.CharField(
        max_length=200, verbose_name="Расположение офиса (RU)"
    )
    office_location_en = models.CharField(
        max_length=200, verbose_name="Расположение офиса (EN)"
    )
    office_location_kg = models.CharField(
        max_length=200, verbose_name="Расположение офиса (KG)"
    )

    office_hours_ru = models.CharField(max_length=200, verbose_name="Часы приема (RU)")
    office_hours_en = models.CharField(max_length=200, verbose_name="Часы приема (EN)")
    office_hours_kg = models.CharField(max_length=200, verbose_name="Часы приема (KG)")

    order = models.PositiveSmallIntegerField(default=1, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Visa Support Contact"
        verbose_name_plural = "Visa Support Contacts"
        ordering = ["order"]

    def __str__(self):
        return self.full_name_ru

    def get_field(self, field_name, language="ru"):
        """Получить значение поля на указанном языке"""
        field_with_lang = f"{field_name}_{language}"
        return getattr(self, field_with_lang, getattr(self, f"{field_name}_ru"))
