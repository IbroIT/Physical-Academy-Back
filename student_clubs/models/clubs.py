from django.db import models
from django.core.validators import URLValidator


class ClubCategory(models.Model):
    """Категории клубов с поддержкой 3 языков"""

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")
    name_kg = models.CharField(max_length=100, verbose_name="Название (KG)")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Club Category"
        verbose_name_plural = "Club Categories"
        ordering = ["order", "name_ru"]

    def __str__(self):
        return self.name_ru

    def get_name(self, language="ru"):
        """Получить название на указанном языке"""
        return getattr(self, f"name_{language}", self.name_ru)


class Club(models.Model):
    """Студенческий клуб с поддержкой 3 языков"""

    STATUS_CHOICES = [
        ("active", "Активен"),
        ("recruiting", "Набор"),
        ("inactive", "Неактивен"),
    ]

    # Основная информация
    category = models.ForeignKey(
        ClubCategory,
        on_delete=models.CASCADE,
        related_name="clubs",
        verbose_name="Категория",
    )
    icon = models.CharField(max_length=10, default="🎯", verbose_name="Иконка (эмодзи)")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="active", verbose_name="Статус"
    )
    members_count = models.IntegerField(default=0, verbose_name="Количество участников")
    join_link = models.URLField(
        max_length=500,
        validators=[URLValidator()],
        verbose_name="Ссылка для присоединения",
        help_text="Ссылка на форму регистрации или Telegram группу",
    )

    # Название (3 языка)
    name_ru = models.CharField(max_length=200, verbose_name="Название (RU)")
    name_en = models.CharField(max_length=200, verbose_name="Название (EN)")
    name_kg = models.CharField(max_length=200, verbose_name="Название (KG)")

    # Краткое описание (3 языка)
    short_description_ru = models.CharField(
        max_length=300, verbose_name="Краткое описание (RU)"
    )
    short_description_en = models.CharField(
        max_length=300, verbose_name="Краткое описание (EN)"
    )
    short_description_kg = models.CharField(
        max_length=300, verbose_name="Краткое описание (KG)"
    )

    # Полное описание (3 языка)
    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_en = models.TextField(verbose_name="Описание (EN)")
    description_kg = models.TextField(verbose_name="Описание (KG)")

    # Цели (3 языка)
    goals_ru = models.TextField(
        verbose_name="Цели и задачи (RU)", help_text="Основные цели клуба"
    )
    goals_en = models.TextField(
        verbose_name="Цели и задачи (EN)", help_text="Основные цели клуба"
    )
    goals_kg = models.TextField(
        verbose_name="Цели и задачи (KG)", help_text="Основные цели клуба"
    )

    # Мотивация (3 языка)
    motivation_ru = models.TextField(
        verbose_name="Мотивация для вступления (RU)",
        help_text="Почему стоит вступить в клуб",
    )
    motivation_en = models.TextField(
        verbose_name="Мотивация для вступления (EN)",
        help_text="Почему стоит вступить в клуб",
    )
    motivation_kg = models.TextField(
        verbose_name="Мотивация для вступления (KG)",
        help_text="Почему стоит вступить в клуб",
    )

    # Расписание встреч (3 языка)
    meetings_ru = models.CharField(
        max_length=200,
        verbose_name="Расписание встреч (RU)",
        help_text="Например: Каждую среду 19:00",
    )
    meetings_en = models.CharField(
        max_length=200,
        verbose_name="Расписание встреч (EN)",
        help_text="Например: Every Wednesday 7 PM",
    )
    meetings_kg = models.CharField(
        max_length=200,
        verbose_name="Расписание встреч (KG)",
        help_text="Например: Ар шаршемби саат 19:00",
    )

    # Теги
    tags = models.JSONField(
        default=list,
        blank=True,
        verbose_name="Теги",
        help_text="Список тегов для поиска",
    )

    # Метаданные
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubs"
        ordering = ["order", "-members_count", "name_ru"]

    def __str__(self):
        return self.name_ru

    def get_field(self, field_name, language="ru"):
        """Получить значение поля на указанном языке"""
        field_with_lang = f"{field_name}_{language}"
        return getattr(self, field_with_lang, getattr(self, f"{field_name}_ru"))


class ClubLeader(models.Model):
    """Руководители клубов"""

    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name="leaders", verbose_name="Клуб"
    )

    # ФИО (3 языка)
    name_ru = models.CharField(max_length=200, verbose_name="ФИО (RU)")
    name_en = models.CharField(max_length=200, verbose_name="ФИО (EN)")
    name_kg = models.CharField(max_length=200, verbose_name="ФИО (KG)")

    # Роль/должность (3 языка)
    role_ru = models.CharField(max_length=200, verbose_name="Роль (RU)")
    role_en = models.CharField(max_length=200, verbose_name="Роль (EN)")
    role_kg = models.CharField(max_length=200, verbose_name="Роль (KG)")

    # Контакты
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    phone = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Телефон"
    )
    photo = models.ImageField(
        upload_to="club_leaders/", blank=True, null=True, verbose_name="Фото"
    )

    order = models.IntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Club Leader"
        verbose_name_plural = "Club Leaders"
        ordering = ["order", "name_ru"]

    def __str__(self):
        return f"{self.name_ru} ({self.club.name_ru})"

    def get_field(self, field_name, language="ru"):
        """Получить значение поля на указанном языке"""
        field_with_lang = f"{field_name}_{language}"
        return getattr(self, field_with_lang, getattr(self, f"{field_name}_ru"))


class ClubStats(models.Model):
    """Статистика для страницы клубов"""

    # Значение
    value = models.CharField(max_length=50, verbose_name="Значение")

    # Метка (3 языка)
    label_ru = models.CharField(max_length=200, verbose_name="Метка (RU)")
    label_en = models.CharField(max_length=200, verbose_name="Метка (EN)")
    label_kg = models.CharField(max_length=200, verbose_name="Метка (KG)")

    icon = models.CharField(max_length=10, default="📊", verbose_name="Иконка")
    order = models.IntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Club Statistics"
        verbose_name_plural = "Club Statistics"
        ordering = ["order"]

    def __str__(self):
        return f"{self.value} - {self.label_ru}"

    def get_label(self, language="ru"):
        """Получить метку на указанном языке"""
        return getattr(self, f"label_{language}", self.label_ru)
