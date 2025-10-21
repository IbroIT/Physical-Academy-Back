from django.db import models


class ExchangeRegion(models.Model):
    """Regions for exchange programs (e.g., Europe, Asia, America)"""

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")
    name_kg = models.CharField(max_length=100, verbose_name="Название (KG)")
    code = models.CharField(max_length=50, unique=True, verbose_name="Код региона")

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = "Exchange Region"
        verbose_name_plural = "Exchange Regions"


class ExchangeDurationType(models.Model):
    """Duration types for exchange programs (e.g., semester, year, summer)"""

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")
    name_kg = models.CharField(max_length=100, verbose_name="Название (KG)")
    code = models.CharField(
        max_length=50, unique=True, verbose_name="Код типа длительности"
    )

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = "Exchange Duration Type"
        verbose_name_plural = "Exchange Duration Types"


class ExchangeProgram(models.Model):
    """Exchange program with universities around the world"""

    # Basic info
    university_ru = models.CharField(max_length=255, verbose_name="Университет (RU)")
    university_en = models.CharField(max_length=255, verbose_name="Университет (EN)")
    university_kg = models.CharField(max_length=255, verbose_name="Университет (KG)")
    country_ru = models.CharField(max_length=100, verbose_name="Страна (RU)")
    country_en = models.CharField(max_length=100, verbose_name="Страна (EN)")
    country_kg = models.CharField(max_length=100, verbose_name="Страна (KG)")

    # Region and Duration
    region = models.ForeignKey(
        ExchangeRegion,
        on_delete=models.CASCADE,
        related_name="programs",
        verbose_name="Регион",
    )
    duration_type = models.ForeignKey(
        ExchangeDurationType,
        on_delete=models.CASCADE,
        related_name="programs",
        verbose_name="Тип длительности",
    )
    duration_ru = models.CharField(max_length=100, verbose_name="Длительность (RU)")
    duration_en = models.CharField(max_length=100, verbose_name="Длительность (EN)")
    duration_kg = models.CharField(max_length=100, verbose_name="Длительность (KG)")

    # Description
    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_en = models.TextField(verbose_name="Описание (EN)")
    description_kg = models.TextField(verbose_name="Описание (KG)")

    # Additional info
    cost = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Стоимость"
    )
    language_ru = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Язык обучения (RU)"
    )
    language_en = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Язык обучения (EN)"
    )
    language_kg = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Язык обучения (KG)"
    )
    grants_available_ru = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Доступные гранты (RU)"
    )
    grants_available_en = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Доступные гранты (EN)"
    )
    grants_available_kg = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Доступные гранты (KG)"
    )
    deadline = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Срок подачи"
    )
    available_spots = models.PositiveIntegerField(
        default=0, verbose_name="Доступные места"
    )
    icon = models.CharField(max_length=20, default="🎓", verbose_name="Иконка (emoji)")
    website = models.URLField(blank=True, null=True, verbose_name="Веб-сайт")

    # Difficulty level
    DIFFICULTY_CHOICES = [
        ("low", "Низкая"),
        ("medium", "Средняя"),
        ("high", "Высокая"),
    ]
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default="medium",
        verbose_name="Сложность поступления",
    )
    difficulty_label_ru = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Метка сложности (RU)"
    )
    difficulty_label_en = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Метка сложности (EN)"
    )
    difficulty_label_kg = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Метка сложности (KG)"
    )

    # Featured
    is_featured = models.BooleanField(default=False, verbose_name="Избранная программа")

    # Status
    is_active = models.BooleanField(default=True, verbose_name="Активная программа")

    # Ordering
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    def __str__(self):
        return f"{self.university_en} ({self.country_en})"

    class Meta:
        verbose_name = "Exchange Program"
        verbose_name_plural = "Exchange Programs"
        ordering = ["order", "university_en"]


class ExchangeProgramRequirement(models.Model):
    """Requirements for exchange programs"""

    program = models.ForeignKey(
        ExchangeProgram,
        on_delete=models.CASCADE,
        related_name="requirements",
        verbose_name="Программа обмена",
    )
    text_ru = models.CharField(max_length=255, verbose_name="Требование (RU)")
    text_en = models.CharField(max_length=255, verbose_name="Требование (EN)")
    text_kg = models.CharField(max_length=255, verbose_name="Требование (KG)")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    def __str__(self):
        return self.text_en[:50]

    class Meta:
        verbose_name = "Exchange Program Requirement"
        verbose_name_plural = "Exchange Program Requirements"
        ordering = ["order"]


class ExchangeProgramBenefit(models.Model):
    """Benefits of exchange programs"""

    program = models.ForeignKey(
        ExchangeProgram,
        on_delete=models.CASCADE,
        related_name="benefits",
        verbose_name="Программа обмена",
    )
    text_ru = models.CharField(max_length=255, verbose_name="Преимущество (RU)")
    text_en = models.CharField(max_length=255, verbose_name="Преимущество (EN)")
    text_kg = models.CharField(max_length=255, verbose_name="Преимущество (KG)")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    def __str__(self):
        return self.text_en[:50]

    class Meta:
        verbose_name = "Exchange Program Benefit"
        verbose_name_plural = "Exchange Program Benefits"
        ordering = ["order"]


class ExchangeProgramCourse(models.Model):
    """Available courses in exchange programs"""

    program = models.ForeignKey(
        ExchangeProgram,
        on_delete=models.CASCADE,
        related_name="available_courses",
        verbose_name="Программа обмена",
    )
    name_ru = models.CharField(max_length=255, verbose_name="Название курса (RU)")
    name_en = models.CharField(max_length=255, verbose_name="Название курса (EN)")
    name_kg = models.CharField(max_length=255, verbose_name="Название курса (KG)")

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = "Exchange Program Course"
        verbose_name_plural = "Exchange Program Courses"


class ExchangePageStat(models.Model):
    """Statistics for exchange programs page"""

    icon = models.CharField(max_length=20, verbose_name="Иконка (emoji)", default="🌍")
    value_ru = models.CharField(max_length=50, verbose_name="Значение (RU)")
    value_en = models.CharField(max_length=50, verbose_name="Значение (EN)")
    value_kg = models.CharField(max_length=50, verbose_name="Значение (KG)")
    label_ru = models.CharField(max_length=100, verbose_name="Подпись (RU)")
    label_en = models.CharField(max_length=100, verbose_name="Подпись (EN)")
    label_kg = models.CharField(max_length=100, verbose_name="Подпись (KG)")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    def __str__(self):
        return f"{self.value_en} - {self.label_en}"

    class Meta:
        verbose_name = "Exchange Page Stat"
        verbose_name_plural = "Exchange Page Stats"
        ordering = ["order"]


class ExchangeDeadline(models.Model):
    """Deadlines for exchange programs"""

    date = models.CharField(max_length=100, verbose_name="Дата дедлайна")
    program_ru = models.CharField(max_length=255, verbose_name="Программа (RU)")
    program_en = models.CharField(max_length=255, verbose_name="Программа (EN)")
    program_kg = models.CharField(max_length=255, verbose_name="Программа (KG)")
    days_left_ru = models.CharField(max_length=100, verbose_name="Осталось дней (RU)")
    days_left_en = models.CharField(max_length=100, verbose_name="Осталось дней (EN)")
    days_left_kg = models.CharField(max_length=100, verbose_name="Осталось дней (KG)")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    def __str__(self):
        return f"{self.date} - {self.program_en}"

    class Meta:
        verbose_name = "Exchange Deadline"
        verbose_name_plural = "Exchange Deadlines"
        ordering = ["order"]
