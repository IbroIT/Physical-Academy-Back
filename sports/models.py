from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class SportSection(models.Model):
    """
    Модель спортивной секции
    """

    SPORT_TYPE_CHOICES = [
        ("game", _("Игровые виды спорта")),
        ("combat", _("Единоборства")),
        ("winter", _("Зимние виды спорта")),
        ("water", _("Водные виды спорта")),
        ("athletics", _("Легкая атлетика")),
        ("gymnastics", _("Гимнастика")),
        ("team", _("Командные виды")),
        ("individual", _("Индивидуальные виды")),
    ]

    # Базовые поля
    sport_type = models.CharField(
        _("Тип спорта"),
        max_length=20,
        choices=SPORT_TYPE_CHOICES,
        default="individual",
        db_index=True,  # Индекс для быстрой фильтрации
    )
    image = models.ImageField(
        _("Изображение"), upload_to="sports/sections/", blank=True, null=True
    )

    # Информация о тренере
    coach_name = models.CharField(_("ФИО тренера"), max_length=200)
    coach_rank = models.CharField(
        _("Звание тренера"),
        max_length=200,
        blank=True,
        help_text=_("Например: Мастер спорта, Заслуженный тренер"),
    )
    coach_contacts = models.CharField(
        _("Контакты тренера"), max_length=200, blank=True, help_text=_("Телефон, email")
    )

    # Расписание
    schedule = models.CharField(
        _("Расписание"),
        max_length=200,
        help_text=_("Краткое расписание, например: Пн, Ср, Пт 18:00-20:00"),
    )

    # Мета
    is_active = models.BooleanField(
        _("Активна"), default=True, db_index=True
    )  # Индекс для фильтрации
    order = models.PositiveIntegerField(
        _("Порядок сортировки"), default=0, db_index=True
    )  # Индекс для сортировки
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Дата обновления"), auto_now=True)

    class Meta:
        verbose_name = _("Спортивная секция")
        verbose_name_plural = _("Спортивные секции")
        ordering = ["order", "coach_name"]
        indexes = [
            models.Index(fields=["is_active", "order"]),  # Композитный индекс
            models.Index(fields=["sport_type", "is_active"]),  # Для фильтрации по типу
        ]

    def __str__(self):
        # Попытка получить название на русском
        translation = self.translations.filter(language="ru").first()
        if translation:
            return f"{translation.name} ({self.coach_name})"
        return f"{self.coach_name} - {self.get_sport_type_display()}"

    def get_name(self, language="ru"):
        """Получить название секции на указанном языке"""
        translation = self.translations.filter(language=language).first()
        if translation:
            return translation.name
        # Fallback на русский
        translation = self.translations.filter(language="ru").first()
        if translation:
            return translation.name
        # Fallback на первый доступный
        translation = self.translations.first()
        return translation.name if translation else self.coach_name

    def get_description(self, language="ru"):
        """Получить описание секции на указанном языке"""
        translation = self.translations.filter(language=language).first()
        if translation:
            return translation.description
        # Fallback на русский
        translation = self.translations.filter(language="ru").first()
        if translation:
            return translation.description
        # Fallback на первый доступный
        translation = self.translations.first()
        return translation.description if translation else ""

    def get_contact_info(self, language="ru"):
        """Получить контактную информацию на указанном языке"""
        translation = self.translations.filter(language=language).first()
        if translation:
            return translation.contact_info
        # Fallback на русский
        translation = self.translations.filter(language="ru").first()
        if translation:
            return translation.contact_info
        # Fallback на первый доступный
        translation = self.translations.first()
        return translation.contact_info if translation else ""


class SportSectionTranslation(models.Model):
    """
    Переводы для спортивных секций
    """

    LANGUAGES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    section = models.ForeignKey(
        SportSection,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name=_("Секция"),
    )
    language = models.CharField(_("Язык"), max_length=2, choices=LANGUAGES)

    # Переводимые поля
    name = models.CharField(_("Название секции"), max_length=200)
    description = models.TextField(_("Описание"))
    contact_info = models.CharField(
        _("Контактная информация"), max_length=500, blank=True
    )

    class Meta:
        verbose_name = _("Перевод секции")
        verbose_name_plural = _("Переводы секций")
        unique_together = ["section", "language"]

    def __str__(self):
        return f"{self.section.id} - {self.name} ({self.get_language_display()})"


class TrainingSchedule(models.Model):
    """
    Детальное расписание тренировок для секции
    """

    DAYS_OF_WEEK = [
        ("monday", _("Понедельник")),
        ("tuesday", _("Вторник")),
        ("wednesday", _("Среда")),
        ("thursday", _("Четверг")),
        ("friday", _("Пятница")),
        ("saturday", _("Суббота")),
        ("sunday", _("Воскресенье")),
    ]

    section = models.ForeignKey(
        SportSection,
        on_delete=models.CASCADE,
        related_name="training_schedules",
        verbose_name=_("Секция"),
    )
    day_of_week = models.CharField(
        _("День недели"), max_length=10, choices=DAYS_OF_WEEK
    )
    time_start = models.TimeField(_("Время начала"))
    time_end = models.TimeField(_("Время окончания"))
    location = models.CharField(_("Место проведения"), max_length=200, blank=True)

    class Meta:
        verbose_name = _("Расписание тренировки")
        verbose_name_plural = _("Расписание тренировок")
        ordering = ["section", "day_of_week", "time_start"]

    def __str__(self):
        return f"{self.section} - {self.get_day_of_week_display()} {self.time_start}-{self.time_end}"


class Achievement(models.Model):
    """
    Модель спортивных достижений
    """

    CATEGORY_CHOICES = [
        ("individual", _("Индивидуальные")),
        ("team", _("Командные")),
        ("international", _("Международные")),
        ("olympic", _("Олимпийские")),
        ("coaching", _("Тренерские")),
    ]

    # Базовая информация
    athlete_name = models.CharField(_("Имя спортсмена/команды"), max_length=200)
    sport = models.CharField(_("Вид спорта"), max_length=100)
    competition = models.CharField(_("Соревнование"), max_length=200)
    result = models.CharField(
        _("Результат"),
        max_length=100,
        help_text=_("Например: 1 место, Золото, Участник"),
    )
    date = models.DateField(_("Дата достижения"))
    image = models.ImageField(
        _("Изображение"), upload_to="sports/achievements/", blank=True, null=True
    )

    # Категория
    category = models.CharField(
        _("Категория"),
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="individual",
        db_index=True,  # Индекс для фильтрации по категориям
    )

    # Дополнительные детали - используем JSONField для гибкости
    details = models.JSONField(
        _("Дополнительные детали"),
        default=dict,
        blank=True,
        help_text=_(
            'JSON объект с дополнительной информацией: {"distance": "200м", "time": "1:54.32"}'
        ),
    )

    # Мета
    is_active = models.BooleanField(_("Активно"), default=True, db_index=True)
    order = models.PositiveIntegerField(_("Порядок сортировки"), default=0)
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Дата обновления"), auto_now=True)

    class Meta:
        verbose_name = _("Спортивное достижение")
        verbose_name_plural = _("Спортивные достижения")
        ordering = ["-date", "order"]
        indexes = [
            models.Index(fields=["-date", "is_active"]),  # Для сортировки по дате
            models.Index(
                fields=["category", "is_active"]
            ),  # Для фильтрации по категории
        ]

    def __str__(self):
        return f"{self.athlete_name} - {self.competition} ({self.result})"

    def get_description(self, language="ru"):
        """Получить описание достижения на указанном языке"""
        translation = self.translations.filter(language=language).first()
        if translation:
            return translation.description
        # Fallback на русский
        translation = self.translations.filter(language="ru").first()
        if translation:
            return translation.description
        # Fallback на первый доступный
        translation = self.translations.first()
        return translation.description if translation else ""


class AchievementTranslation(models.Model):
    """
    Переводы для достижений
    """

    LANGUAGES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name=_("Достижение"),
    )
    language = models.CharField(_("Язык"), max_length=2, choices=LANGUAGES)

    # Переводимые поля
    description = models.TextField(_("Описание достижения"))

    class Meta:
        verbose_name = _("Перевод достижения")
        verbose_name_plural = _("Переводы достижений")
        unique_together = ["achievement", "language"]

    def __str__(self):
        return f"{self.achievement.athlete_name} - {self.get_language_display()}"


class Infrastructure(models.Model):
    """
    Модель спортивной инфраструктуры (обычно одна запись)
    """

    # Общая информация
    badge = models.CharField(
        _("Бейдж"), max_length=100, default="Спортивная инфраструктура"
    )

    # Статистика
    stat_1_value = models.CharField(
        _("Статистика 1 - Значение"), max_length=50, default="25+"
    )
    stat_1_icon = models.CharField(
        _("Статистика 1 - Иконка"), max_length=10, default="🏟️"
    )

    stat_2_value = models.CharField(
        _("Статистика 2 - Значение"), max_length=50, default="5000+"
    )
    stat_2_icon = models.CharField(
        _("Статистика 2 - Иконка"), max_length=10, default="👥"
    )

    stat_3_value = models.CharField(
        _("Статистика 3 - Значение"), max_length=50, default="100%"
    )
    stat_3_icon = models.CharField(
        _("Статистика 3 - Иконка"), max_length=10, default="⚡"
    )

    stat_4_value = models.CharField(
        _("Статистика 4 - Значение"), max_length=50, default="15+"
    )
    stat_4_icon = models.CharField(
        _("Статистика 4 - Иконка"), max_length=10, default="🎯"
    )

    # Мета
    is_active = models.BooleanField(_("Активно"), default=True)
    updated_at = models.DateTimeField(_("Дата обновления"), auto_now=True)

    class Meta:
        verbose_name = _("Спортивная инфраструктура")
        verbose_name_plural = _("Спортивная инфраструктура")

    def __str__(self):
        return "Спортивная инфраструктура КГАФКиС"

    def get_name(self, language="ru"):
        """Получить название инфраструктуры на указанном языке"""
        translation = self.translations.filter(language=language).first()
        if translation:
            return translation.name
        # Fallback на русский
        translation = self.translations.filter(language="ru").first()
        if translation:
            return translation.name
        # Fallback на первый доступный
        translation = self.translations.first()
        return translation.name if translation else "Спортивная инфраструктура"

    def get_description(self, language="ru"):
        """Получить описание инфраструктуры на указанном языке"""
        translation = self.translations.filter(language=language).first()
        if translation:
            return translation.description
        # Fallback на русский
        translation = self.translations.filter(language="ru").first()
        if translation:
            return translation.description
        # Fallback на первый доступный
        translation = self.translations.first()
        return translation.description if translation else ""


class InfrastructureTranslation(models.Model):
    """
    Переводы для инфраструктуры
    """

    LANGUAGES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    infrastructure = models.ForeignKey(
        Infrastructure,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name=_("Инфраструктура"),
    )
    language = models.CharField(_("Язык"), max_length=2, choices=LANGUAGES)

    # Переводимые поля
    name = models.CharField(_("Название"), max_length=200)
    description = models.TextField(_("Описание"))

    # Переводы для статистики
    stat_1_label = models.CharField(_("Статистика 1 - Подпись"), max_length=100)
    stat_2_label = models.CharField(_("Статистика 2 - Подпись"), max_length=100)
    stat_3_label = models.CharField(_("Статистика 3 - Подпись"), max_length=100)
    stat_4_label = models.CharField(_("Статистика 4 - Подпись"), max_length=100)

    class Meta:
        verbose_name = _("Перевод инфраструктуры")
        verbose_name_plural = _("Переводы инфраструктуры")
        unique_together = ["infrastructure", "language"]

    def __str__(self):
        return f"Инфраструктура - {self.get_language_display()}"


class InfrastructureCategory(models.Model):
    """
    Категории инфраструктуры (стадионы, бассейны, залы и т.д.)
    """

    infrastructure = models.ForeignKey(
        Infrastructure,
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name=_("Инфраструктура"),
    )
    slug = models.SlugField(
        _("Идентификатор"),
        max_length=50,
        help_text=_("Уникальный идентификатор категории: stadiums, pools, gyms"),
    )
    icon = models.CharField(_("Иконка"), max_length=10, default="🏟️")
    color = models.CharField(
        _("Цвет градиента"),
        max_length=50,
        default="from-blue-500 to-cyan-500",
        help_text=_("Tailwind классы градиента"),
    )
    order = models.PositiveIntegerField(_("Порядок"), default=0, db_index=True)

    class Meta:
        verbose_name = _("Категория инфраструктуры")
        verbose_name_plural = _("Категории инфраструктуры")
        ordering = ["order"]
        # Уникальность slug только в рамках одной инфраструктуры
        unique_together = ["infrastructure", "slug"]
        indexes = [
            models.Index(fields=["infrastructure", "order"]),
        ]

    def __str__(self):
        translation = self.translations.filter(language="ru").first()
        if translation:
            return translation.name
        return self.slug

    def get_name(self, language="ru"):
        """Получить название категории на указанном языке"""
        translation = self.translations.filter(language=language).first()
        if translation:
            return translation.name
        # Fallback на русский
        translation = self.translations.filter(language="ru").first()
        if translation:
            return translation.name
        # Fallback на первый доступный
        translation = self.translations.first()
        return translation.name if translation else self.slug


class InfrastructureCategoryTranslation(models.Model):
    """
    Переводы для категорий инфраструктуры
    """

    LANGUAGES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    category = models.ForeignKey(
        InfrastructureCategory,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name=_("Категория"),
    )
    language = models.CharField(_("Язык"), max_length=2, choices=LANGUAGES)
    name = models.CharField(_("Название категории"), max_length=100)

    class Meta:
        verbose_name = _("Перевод категории")
        verbose_name_plural = _("Переводы категорий")
        unique_together = ["category", "language"]

    def __str__(self):
        return f"{self.category.slug} - {self.get_language_display()}"


class InfrastructureObject(models.Model):
    """
    Объекты инфраструктуры (конкретные стадионы, залы и т.д.)
    """

    category = models.ForeignKey(
        InfrastructureCategory,
        on_delete=models.CASCADE,
        related_name="objects",
        verbose_name=_("Категория"),
    )
    image = models.ImageField(
        _("Изображение"), upload_to="sports/infrastructure/", blank=True, null=True
    )

    # Характеристики - используем JSONField для неограниченного количества
    features = models.JSONField(
        _("Характеристики"),
        default=list,
        blank=True,
        help_text=_(
            'Список характеристик: ["Вместимость: 1500", "Синтетическое покрытие"]'
        ),
    )

    order = models.PositiveIntegerField(_("Порядок"), default=0, db_index=True)
    is_active = models.BooleanField(_("Активно"), default=True, db_index=True)

    class Meta:
        verbose_name = _("Объект инфраструктуры")
        verbose_name_plural = _("Объекты инфраструктуры")
        ordering = ["order"]
        indexes = [
            models.Index(fields=["category", "is_active", "order"]),
        ]

    def __str__(self):
        translation = self.translations.filter(language="ru").first()
        if translation:
            return translation.name
        return f"Объект {self.id}"

    def get_name(self, language="ru"):
        """Получить название объекта на указанном языке"""
        translation = self.translations.filter(language=language).first()
        if translation:
            return translation.name
        # Fallback на русский
        translation = self.translations.filter(language="ru").first()
        if translation:
            return translation.name
        # Fallback на первый доступный
        translation = self.translations.first()
        return translation.name if translation else f"Объект {self.id}"

    def get_description(self, language="ru"):
        """Получить описание объекта на указанном языке"""
        translation = self.translations.filter(language=language).first()
        if translation:
            return translation.description
        # Fallback на русский
        translation = self.translations.filter(language="ru").first()
        if translation:
            return translation.description
        # Fallback на первый доступный
        translation = self.translations.first()
        return translation.description if translation else ""


class InfrastructureObjectTranslation(models.Model):
    """
    Переводы для объектов инфраструктуры
    """

    LANGUAGES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    infrastructure_object = models.ForeignKey(
        InfrastructureObject,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name=_("Объект"),
    )
    language = models.CharField(_("Язык"), max_length=2, choices=LANGUAGES)

    # Переводимые поля
    name = models.CharField(_("Название"), max_length=200)
    description = models.TextField(_("Описание"))

    class Meta:
        verbose_name = _("Перевод объекта")
        verbose_name_plural = _("Переводы объектов")
        unique_together = ["infrastructure_object", "language"]

    def __str__(self):
        return f"{self.name} - {self.get_language_display()}"
