from django.db import models


class IPChainInfo(models.Model):
    """Основная информация об IPChain"""

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    subtitle = models.TextField(verbose_name="Подзаголовок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Информация IPChain"
        verbose_name_plural = "Информация IPChain"

    def __str__(self):
        return self.title


class IPChainInfoTranslation(models.Model):
    """Переводы для IPChainInfo"""

    LANGUAGE_CHOICES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    info = models.ForeignKey(
        IPChainInfo,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name="Информация",
    )
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, verbose_name="Язык"
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    subtitle = models.TextField(verbose_name="Подзаголовок")

    class Meta:
        unique_together = ["info", "language"]
        verbose_name = "Перевод информации"
        verbose_name_plural = "Переводы информации"

    def __str__(self):
        return f"{self.info.title} - {self.language}"


class IPChainStatistic(models.Model):
    """Статистика IPChain"""

    value = models.CharField(
        max_length=50, verbose_name="Значение", help_text="Например: 1000+, 500, 99.9%"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"

    def __str__(self):
        return self.value


class IPChainStatisticTranslation(models.Model):
    """Переводы для статистики"""

    LANGUAGE_CHOICES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    statistic = models.ForeignKey(
        IPChainStatistic,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name="Статистика",
    )
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, verbose_name="Язык"
    )
    label = models.CharField(
        max_length=200,
        verbose_name="Название",
        help_text="Например: Защищено патентов, Пользователей",
    )

    class Meta:
        unique_together = ["statistic", "language"]
        verbose_name = "Перевод статистики"
        verbose_name_plural = "Переводы статистики"

    def __str__(self):
        return f"{self.statistic.value} - {self.label}"


class Patent(models.Model):
    """Патенты в системе IPChain"""

    STATUS_CHOICES = [
        ("Granted", "Выдан"),
        ("Pending", "В процессе"),
        ("Active", "Активный"),
    ]

    number = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Номер патента",
        help_text="Например: PAT2024001",
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, verbose_name="Статус"
    )
    year = models.CharField(max_length=4, verbose_name="Год")
    date = models.DateField(verbose_name="Дата подачи")
    icon = models.CharField(max_length=10, default="📄", verbose_name="Иконка")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ["order", "-date"]
        verbose_name = "Патент"
        verbose_name_plural = "Патенты"

    def __str__(self):
        return f"{self.number} - {self.year}"


class PatentTranslation(models.Model):
    """Переводы для патентов"""

    LANGUAGE_CHOICES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    patent = models.ForeignKey(
        Patent,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name="Патент",
    )
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, verbose_name="Язык"
    )
    title = models.CharField(max_length=300, verbose_name="Название")
    description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(blank=True, verbose_name="Полное описание")
    technologies = models.JSONField(
        default=list,
        verbose_name="Технологии",
        help_text='Например: ["Blockchain", "AI"]',
    )
    applications = models.JSONField(
        default=list,
        verbose_name="Применение",
        help_text='Например: ["IP Protection", "Verification"]',
    )

    class Meta:
        unique_together = ["patent", "language"]
        verbose_name = "Перевод патента"
        verbose_name_plural = "Переводы патентов"

    def __str__(self):
        return f"{self.patent.number} - {self.title}"


class BlockchainFeature(models.Model):
    """Функции блокчейна"""

    icon = models.CharField(max_length=10, default="✓", verbose_name="Иконка")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Функция блокчейна"
        verbose_name_plural = "Функции блокчейна"

    def __str__(self):
        return f"Функция {self.id}"


class BlockchainFeatureTranslation(models.Model):
    """Переводы для функций блокчейна"""

    LANGUAGE_CHOICES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    feature = models.ForeignKey(
        BlockchainFeature,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name="Функция",
    )
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, verbose_name="Язык"
    )
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        unique_together = ["feature", "language"]
        verbose_name = "Перевод функции"
        verbose_name_plural = "Переводы функций"

    def __str__(self):
        return f"{self.title}"


class IPChainBenefit(models.Model):
    """Преимущества IPChain"""

    icon = models.CharField(max_length=10, default="✅", verbose_name="Иконка")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

    def __str__(self):
        return f"Преимущество {self.id}"


class IPChainBenefitTranslation(models.Model):
    """Переводы для преимуществ"""

    LANGUAGE_CHOICES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    benefit = models.ForeignKey(
        IPChainBenefit,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name="Преимущество",
    )
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, verbose_name="Язык"
    )
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        unique_together = ["benefit", "language"]
        verbose_name = "Перевод преимущества"
        verbose_name_plural = "Переводы преимуществ"

    def __str__(self):
        return f"{self.title}"


class BlockchainData(models.Model):
    """Данные блокчейна в реальном времени"""

    current_block = models.CharField(
        max_length=50, verbose_name="Текущий блок", help_text="Например: 15,842,367"
    )
    ip_registrations = models.CharField(
        max_length=50, verbose_name="Регистраций IP", help_text="Например: 2,847"
    )
    smart_contracts = models.CharField(
        max_length=50, verbose_name="Смарт-контрактов", help_text="Например: 1,563"
    )
    network_hash = models.CharField(
        max_length=100, verbose_name="Хэш сети", help_text="Например: 0x8f3a...c42b"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.IntegerField(default=0, verbose_name="Порядок сортировки")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Последнее обновление"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ["order", "-updated_at"]
        verbose_name = "Данные блокчейна"
        verbose_name_plural = "Данные блокчейна"

    def __str__(self):
        return f"Блокчейн данные (блок: {self.current_block})"


class BlockchainDataTranslation(models.Model):
    """Переводы для BlockchainData"""

    LANGUAGE_CHOICES = [
        ("ru", "Русский"),
        ("en", "English"),
        ("kg", "Кыргызча"),
    ]

    blockchain_data = models.ForeignKey(
        BlockchainData,
        on_delete=models.CASCADE,
        related_name="translations",
        verbose_name="Данные блокчейна",
    )
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, verbose_name="Язык"
    )
    current_block_label = models.CharField(
        max_length=100, verbose_name="Название 'Текущий блок'", default="Текущий блок"
    )
    ip_registrations_label = models.CharField(
        max_length=100,
        verbose_name="Название 'Регистраций IP'",
        default="Регистраций IP",
    )
    smart_contracts_label = models.CharField(
        max_length=100,
        verbose_name="Название 'Смарт-контрактов'",
        default="Смарт-контрактов",
    )
    network_hash_label = models.CharField(
        max_length=100, verbose_name="Название 'Хэш сети'", default="Хэш сети"
    )

    class Meta:
        unique_together = ["blockchain_data", "language"]
        verbose_name = "Перевод данных блокчейна"
        verbose_name_plural = "Переводы данных блокчейна"

    def __str__(self):
        return f"Блокчейн данные - {self.language}"
