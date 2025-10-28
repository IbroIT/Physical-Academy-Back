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

    # Переводы - Название
    name_ru = models.CharField(_("Название секции (RU)"), max_length=200)
    name_kg = models.CharField(_("Название секции (KG)"), max_length=200)
    name_en = models.CharField(_("Название секции (EN)"), max_length=200)

    # Переводы - Описание
    description_ru = models.TextField(_("Описание (RU)"))
    description_kg = models.TextField(_("Описание (KG)"))
    description_en = models.TextField(_("Описание (EN)"))

    # Переводы - Контактная информация
    contact_info_ru = models.CharField(
        _("Контактная информация (RU)"), max_length=500, blank=True
    )
    contact_info_kg = models.CharField(
        _("Контактная информация (KG)"), max_length=500, blank=True
    )
    contact_info_en = models.CharField(
        _("Контактная информация (EN)"), max_length=500, blank=True
    )

    # Информация о тренере
    coach_name = models.CharField(_("ФИО тренера"), max_length=200)
    # Переводы для имени тренера (опционально)
    coach_name_ru = models.CharField(_("ФИО тренера (RU)"), max_length=200, blank=True)
    coach_name_kg = models.CharField(_("ФИО тренера (KG)"), max_length=200, blank=True)
    coach_name_en = models.CharField(_("ФИО тренера (EN)"), max_length=200, blank=True)
    coach_rank = models.CharField(
        _("Звание тренера"),
        max_length=200,
        blank=True,
        help_text=_("Например: Мастер спорта, Заслуженный тренер"),
    )
    # Переводы для звания тренера (опционально)
    coach_rank_ru = models.CharField(
        _("Звание тренера (RU)"), max_length=200, blank=True
    )
    coach_rank_kg = models.CharField(
        _("Звание тренера (KG)"), max_length=200, blank=True
    )
    coach_rank_en = models.CharField(
        _("Звание тренера (EN)"), max_length=200, blank=True
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
    # Если расписание содержит локализуемый текст — храните переводы
    schedule_ru = models.CharField(_("Расписание (RU)"), max_length=200, blank=True)
    schedule_kg = models.CharField(_("Расписание (KG)"), max_length=200, blank=True)
    schedule_en = models.CharField(_("Расписание (EN)"), max_length=200, blank=True)

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
        return f"{self.name_ru} ({self.coach_name})"

    def get_name(self, language="ru"):
        """Получить название секции на указанном языке"""
        value = getattr(self, f"name_{language}", None)
        return value if value else self.name_ru

    def get_description(self, language="ru"):
        """Получить описание секции на указанном языке"""
        value = getattr(self, f"description_{language}", None)
        return value if value else self.description_ru

    def get_contact_info(self, language="ru"):
        """Получить контактную информацию на указанном языке"""
        value = getattr(self, f"contact_info_{language}", None)
        return value if value else self.contact_info_ru

    def get_schedule(self, language="ru"):
        """Получить текст расписания на нужном языке"""
        value = getattr(self, f"schedule_{language}", None)
        return value if value else self.schedule

    def get_coach_rank(self, language="ru"):
        """Получить звание тренера на нужном языке"""
        value = getattr(self, f"coach_rank_{language}", None)
        return value if value else self.coach_rank

    def get_coach_name(self, language="ru"):
        """Получить имя тренера на указанном языке"""
        value = getattr(self, f"coach_name_{language}", None)
        return value if value else self.coach_name


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
    # Переводы для мест проведения (опционально)
    location_ru = models.CharField(
        _("Место проведения (RU)"), max_length=200, blank=True
    )
    location_kg = models.CharField(
        _("Место проведения (KG)"), max_length=200, blank=True
    )
    location_en = models.CharField(
        _("Место проведения (EN)"), max_length=200, blank=True
    )

    class Meta:
        verbose_name = _("Расписание тренировки")
        verbose_name_plural = _("Расписание тренировок")
        ordering = ["section", "day_of_week", "time_start"]

    def __str__(self):
        return f"{self.section} - {self.get_day_of_week_display()} {self.time_start}-{self.time_end}"

    def get_location(self, language="ru"):
        value = getattr(self, f"location_{language}", None)
        return value if value else self.location

    def get_day_display_for_language(self, language="ru"):
        """Return localized day label using Django's choices display.

        Note: this uses the built-in get_day_of_week_display which relies on
        the active translation; callers may need to activate language.
        """
        return self.get_day_of_week_display()


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
    # Переводы для имени спортсмена / команды
    athlete_name_ru = models.CharField(
        _("Имя спортсмена/команды (RU)"), max_length=200, blank=True
    )
    athlete_name_kg = models.CharField(
        _("Имя спортсмена/команды (KG)"), max_length=200, blank=True
    )
    athlete_name_en = models.CharField(
        _("Имя спортсмена/команды (EN)"), max_length=200, blank=True
    )
    sport = models.CharField(_("Вид спорта"), max_length=100)
    competition = models.CharField(_("Соревнование"), max_length=200)
    result = models.CharField(
        _("Результат"),
        max_length=100,
        help_text=_("Например: 1 место, Золото, Участник"),
    )
    # Переводы для полей sport/competition/result (опционально)
    sport_ru = models.CharField(_("Вид спорта (RU)"), max_length=200, blank=True)
    sport_kg = models.CharField(_("Вид спорта (KG)"), max_length=200, blank=True)
    sport_en = models.CharField(_("Вид спорта (EN)"), max_length=200, blank=True)

    competition_ru = models.CharField(
        _("Соревнование (RU)"), max_length=200, blank=True
    )
    competition_kg = models.CharField(
        _("Соревнование (KG)"), max_length=200, blank=True
    )
    competition_en = models.CharField(
        _("Соревнование (EN)"), max_length=200, blank=True
    )

    result_ru = models.CharField(_("Результат (RU)"), max_length=100, blank=True)
    result_kg = models.CharField(_("Результат (KG)"), max_length=100, blank=True)
    result_en = models.CharField(_("Результат (EN)"), max_length=100, blank=True)
    date = models.DateField(_("Дата достижения"))
    image = models.ImageField(
        _("Изображение"), upload_to="sports/achievements/", blank=True, null=True
    )

    # Переводы - Описание
    description_ru = models.TextField(_("Описание достижения (RU)"))
    description_kg = models.TextField(_("Описание достижения (KG)"))
    description_en = models.TextField(_("Описание достижения (EN)"))

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
        value = getattr(self, f"description_{language}", None)
        return value if value else self.description_ru

    def get_name(self, language="ru"):
        value = getattr(self, f"athlete_name_{language}", None)
        return value if value else self.athlete_name

    def get_sport(self, language="ru"):
        value = getattr(self, f"sport_{language}", None)
        return value if value else self.sport

    def get_competition(self, language="ru"):
        value = getattr(self, f"competition_{language}", None)
        return value if value else self.competition

    def get_result(self, language="ru"):
        value = getattr(self, f"result_{language}", None)
        return value if value else self.result


class Infrastructure(models.Model):
    """
    Модель спортивной инфраструктуры с многоязычной поддержкой (обычно одна запись)
    """

    # Переводы - Название и описание
    name_ru = models.CharField(_("Название (RU)"), max_length=200)
    name_kg = models.CharField(_("Название (KG)"), max_length=200)
    name_en = models.CharField(_("Название (EN)"), max_length=200)

    description_ru = models.TextField(_("Описание (RU)"))
    description_kg = models.TextField(_("Описание (KG)"))
    description_en = models.TextField(_("Описание (EN)"))

    # Общая информация
    badge = models.CharField(
        _("Бейдж"), max_length=100, default="Спортивная инфраструктура"
    )
    # Переводы для бейджа/заголовка
    badge_ru = models.CharField(_("Бейдж/заголовка (RU)"), max_length=100, blank=True)
    badge_kg = models.CharField(_("Бейдж/заголовка (KG)"), max_length=100, blank=True)
    badge_en = models.CharField(_("Бейдж/заголовка (EN)"), max_length=100, blank=True)

    # Мета
    is_active = models.BooleanField(_("Активно"), default=True)
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Дата обновления"), auto_now=True)

    class Meta:
        verbose_name = _("Спортивная инфраструктура")
        verbose_name_plural = _("Спортивная инфраструктура")

    def __str__(self):
        return self.name_ru

    def get_name(self, language="ru"):
        """Получить название на указанном языке"""
        value = getattr(self, f"name_{language}", None)
        return value if value else self.name_ru

    def get_description(self, language="ru"):
        """Получить описание на указанном языке"""
        value = getattr(self, f"description_{language}", None)
        return value if value else self.description_ru

    def get_badge(self, language="ru"):
        value = getattr(self, f"badge_{language}", None)
        return value if value else self.badge


class InfrastructureStatistic(models.Model):
    """
    Статистика спортивной инфраструктуры (динамическая модель)
    """

    infrastructure = models.ForeignKey(
        Infrastructure,
        on_delete=models.CASCADE,
        related_name="statistics",
        verbose_name=_("Инфраструктура"),
    )

    # Переводы - Подписи статистики
    label_ru = models.CharField(_("Подпись (RU)"), max_length=100)
    label_kg = models.CharField(_("Подпись (KG)"), max_length=100)
    label_en = models.CharField(_("Подпись (EN)"), max_length=100)

    # Значение и иконка
    value = models.CharField(
        _("Значение"), max_length=50, help_text=_("Например: 25+, 5000+")
    )
    icon = models.CharField(_("Иконка"), max_length=10, default="📊")

    # Порядок отображения
    order = models.PositiveIntegerField(_("Порядок"), default=0, db_index=True)
    is_active = models.BooleanField(_("Активно"), default=True)

    class Meta:
        verbose_name = _("Статистика инфраструктуры")
        verbose_name_plural = _("Статистика инфраструктуры")
        ordering = ["infrastructure", "order"]
        indexes = [
            models.Index(fields=["infrastructure", "order"]),
        ]

    def __str__(self):
        return f"{self.label_ru}: {self.value}"

    def get_label(self, language="ru"):
        """Получить подпись на указанном языке"""
        value = getattr(self, f"label_{language}", None)
        return value if value else self.label_ru


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

    # Переводы - Название категории
    name_ru = models.CharField(_("Название категории (RU)"), max_length=100)
    name_kg = models.CharField(_("Название категории (KG)"), max_length=100)
    name_en = models.CharField(_("Название категории (EN)"), max_length=100)

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
        return self.name_ru

    def get_name(self, language="ru"):
        """Получить название категории на указанном языке"""
        value = getattr(self, f"name_{language}", None)
        return value if value else self.name_ru


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

    # Переводы - Название и описание
    name_ru = models.CharField(_("Название (RU)"), max_length=200)
    name_kg = models.CharField(_("Название (KG)"), max_length=200)
    name_en = models.CharField(_("Название (EN)"), max_length=200)

    description_ru = models.TextField(_("Описание (RU)"))
    description_kg = models.TextField(_("Описание (KG)"))
    description_en = models.TextField(_("Описание (EN)"))

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
        return self.name_ru

    def get_name(self, language="ru"):
        """Получить название объекта на указанном языке"""
        value = getattr(self, f"name_{language}", None)
        return value if value else self.name_ru

    def get_description(self, language="ru"):
        """Получить описание объекта на указанном языке"""
        value = getattr(self, f"description_{language}", None)
        return value if value else self.description_ru
