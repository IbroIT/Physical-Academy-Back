from django.db import models

# Create your models here.


class PhdPrograms(models.Model):
    emoji = models.CharField(max_length=10, verbose_name="Эмодзи")

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="Название (KG)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_kg = models.TextField(verbose_name="Описание (KG)")
    description_en = models.TextField(verbose_name="Описание (EN)")

    features_ru = models.JSONField(
        verbose_name="Особенности (RU)", default=list, null=True, blank=True
    )
    features_kg = models.JSONField(
        verbose_name="Особенности (KG)", default=list, null=True, blank=True
    )
    features_en = models.JSONField(
        verbose_name="Особенности (EN)", default=list, null=True, blank=True
    )

    duration_years = models.IntegerField(verbose_name="Продолжительность (годы)")
    offline = models.BooleanField(default=True, verbose_name="Очная форма")
    tuition_fee = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Стоимость обучения"
    )

    class Meta:
        verbose_name = "Программа докторантуры"
        verbose_name_plural = "Программы докторантуры"

    def str(self):
        return self.name_ru

    def get_name(self, language="ru"):
        return getattr(self, f"name_{language}", self.name_ru)

    def get_description(self, language="ru"):
        return getattr(self, f"description_{language}", self.description_ru)

    def get_features(self, language="ru"):
        return getattr(self, f"features_{language}", self.features_ru)


class CollegePrograms(models.Model):
    emoji = models.CharField(max_length=10, verbose_name="Эмодзи")

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="Название (KG)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_kg = models.TextField(verbose_name="Описание (KG)")
    description_en = models.TextField(verbose_name="Описание (EN)")

    features_ru = models.JSONField(
        verbose_name="Особенности (RU)", default=list, null=True, blank=True
    )
    features_kg = models.JSONField(
        verbose_name="Особенности (KG)", default=list, null=True, blank=True
    )
    features_en = models.JSONField(
        verbose_name="Особенности (EN)", default=list, null=True, blank=True
    )

    duration_years = models.IntegerField(verbose_name="Продолжительность (годы)")
    offline = models.BooleanField(default=True, verbose_name="Очная форма")
    tuition_fee = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Стоимость обучения"
    )

    class Meta:
        verbose_name = "Программа колледжа"
        verbose_name_plural = "Программы колледжа"

    def str(self):
        return self.name_ru

    def get_name(self, language="ru"):
        return getattr(self, f"name_{language}", self.name_ru)

    def get_description(self, language="ru"):
        return getattr(self, f"description_{language}", self.description_ru)

    def get_features(self, language="ru"):
        return getattr(self, f"features_{language}", self.features_ru)


class MasterPrograms(models.Model):
    emoji = models.CharField(max_length=10, verbose_name="Эмодзи")

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="Название (KG)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_kg = models.TextField(verbose_name="Описание (KG)")
    description_en = models.TextField(verbose_name="Описание (EN)")
    
    features_ru = models.JSONField(verbose_name="Особенности (RU)")
    features_kg = models.JSONField(verbose_name="Особенности (KG)")
    features_en = models.JSONField(verbose_name="Особенности (EN)")

    duration_years = models.IntegerField(verbose_name="Продолжительность (годы)")
    offline = models.BooleanField(default=True, verbose_name="Очная форма")
    tuition_fee = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Стоимость обучения"
    )

    class Meta:
        verbose_name = "Программа магистра"
        verbose_name_plural = "Программы магистра"

    def str(self):
        return self.name_ru

    def get_name(self, language="ru"):
        return getattr(self, f"name_{language}", self.name_ru)

    def get_description(self, language="ru"):
        return getattr(self, f"description_{language}", self.description_ru)

    def get_features(self, language="ru"):
        return getattr(self, f"features_{language}", self.features_ru)


class FacultyStatistics(models.Model):
    faculty = models.ForeignKey(
        "Faculty", on_delete=models.CASCADE, related_name="statistics"
    )

    titleInt = models.CharField(max_length=100, verbose_name="Заголовок (INT)")

    meaning_ru = models.CharField(max_length=100, verbose_name="Значение (RU)")
    meaning_kg = models.CharField(max_length=100, verbose_name="Значение (KG)")
    meaning_en = models.CharField(max_length=100, verbose_name="Значение (EN)")

    class Meta:
        verbose_name = "Статистика факультета"
        verbose_name_plural = "Статистика факультетов"

    def str(self):
        return f"{self.titleInt} - {self.meaning_ru}"

    def get_meaning(self, language="ru"):
        return getattr(self, f"meaning_{language}", self.meaning_ru)


class FacultyPrograms(models.Model):
    faculty = models.ForeignKey(
        "Faculty", on_delete=models.CASCADE, related_name="programs"
    )

    emoji = models.CharField(max_length=10, verbose_name="Эмодзи")

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="Название (KG)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")

    degree_ru = models.CharField(max_length=100, verbose_name="Степень на русском")
    degree_en = models.CharField(max_length=100, verbose_name="Степень на английском")
    degree_kg = models.CharField(max_length=100, verbose_name="Степень на киргизском")

    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_kg = models.TextField(verbose_name="Описание (KG)")
    description_en = models.TextField(verbose_name="Описание (EN)")

    duration_years = models.IntegerField(verbose_name="Продолжительность (годы)")
    offline = models.BooleanField(default=True, verbose_name="Очная форма")
    tuition_fee = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Стоимость обучения"
    )

    class Meta:
        verbose_name = "Программа факультета"
        verbose_name_plural = "Программы факультетов"

    def str(self):
        return self.name_ru

    def get_name(self, language="ru"):
        return getattr(self, f"name_{language}", self.name_ru)

    def get_description(self, language="ru"):
        return getattr(self, f"description_{language}", self.description_ru)

    def get_degree(self, language="ru"):
        return getattr(self, f"degree_{language}", self.degree_ru)


class FacultySpecialization(models.Model):
    faculty = models.ForeignKey(
        "Faculty", on_delete=models.CASCADE, related_name="specializations"
    )

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="Название (KG)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_kg = models.TextField(verbose_name="Описание (KG)")
    description_en = models.TextField(verbose_name="Описание (EN)")
    
    features_ru = models.JSONField(verbose_name="Особенности (RU)")
    features_kg = models.JSONField(verbose_name="Особенности (KG)")
    features_en = models.JSONField(verbose_name="Особенности (EN)")

    class Meta:
        verbose_name = "Специализация факультета"
        verbose_name_plural = "Специализации факультетов"

    def str(self):
        return self.name_ru

    def get_name(self, language="ru"):
        return getattr(self, f"name_{language}", self.name_ru)

    def get_description(self, language="ru"):
        return getattr(self, f"description_{language}", self.description_ru)

    def get_features(self, language="ru"):
        return getattr(self, f"features_{language}", self.features_ru)


class FacultySports(models.Model):
    faculty = models.ForeignKey(
        "Faculty", on_delete=models.CASCADE, related_name="sports"
    )

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="Название (KG)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_kg = models.TextField(verbose_name="Описание (KG)")
    description_en = models.TextField(verbose_name="Описание (EN)")

    emoji = models.CharField(max_length=10, verbose_name="Эмодзи")

    class Meta:
        verbose_name = "Спорт факультета"
        verbose_name_plural = "Спорт факультетов"

    def str(self):
        return self.name_ru

    def get_name(self, language="ru"):
        return getattr(self, f"name_{language}", self.name_ru)

    def get_description(self, language="ru"):
        return getattr(self, f"description_{language}", self.description_ru)


class FacultyTeachers(models.Model):
    faculty = models.ForeignKey(
        "Faculty", on_delete=models.CASCADE, related_name="teachers"
    )

    full_name_ru = models.CharField(max_length=100, verbose_name="Полное имя (RU)")
    full_name_kg = models.CharField(max_length=100, verbose_name="Полное имя (KG)")
    full_name_en = models.CharField(max_length=100, verbose_name="Полное имя (EN)")

    position_ru = models.CharField(max_length=100, verbose_name="Должность (RU)")
    position_kg = models.CharField(max_length=100, verbose_name="Должность (KG)")
    position_en = models.CharField(max_length=100, verbose_name="Должность (EN)")

    photo = models.ImageField(upload_to="faculty_teachers/", verbose_name="Фото")

    class Meta:
        verbose_name = "Преподаватель факультета"
        verbose_name_plural = "Преподаватели факультетов"

    def str(self):
        return self.full_name_ru

    def get_full_name(self, language="ru"):
        return getattr(self, f"full_name_{language}", self.full_name_ru)

    def get_position(self, language="ru"):
        return getattr(self, f"position_{language}", self.position_ru)


class FacultyContacts(models.Model):
    faculty = models.ForeignKey(
        "Faculty", on_delete=models.CASCADE, related_name="contacts"
    )

    title_ru = models.CharField(max_length=100, verbose_name="Заголовок (RU)")
    title_kg = models.CharField(max_length=100, verbose_name="Заголовок (KG)")
    title_en = models.CharField(max_length=100, verbose_name="Заголовок (EN)")

    value = models.CharField(max_length=200, verbose_name="Значение")

    class Meta:
        verbose_name = "Контакт факультета"
        verbose_name_plural = "Контакты факультетов"

    def str(self):
        return self.title_ru

    def get_title(self, language="ru"):
        return getattr(self, f"title_{language}", self.title_ru)


class Faculty(models.Model):
    # Добавляем slug для URL-идентификации
    slug = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="URL Slug",
        help_text="URL identifier (e.g., coaching-faculty)",
        null=True,
        blank=True,
    )
    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="Название (KG)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name="Описание (RU)")
    description_kg = models.TextField(verbose_name="Описание (KG)")
    description_en = models.TextField(verbose_name="Описание (EN)")

    # Добавляем баннер
    banner_image = models.ImageField(
        upload_to="faculty_banners/", verbose_name="Баннер", null=True, blank=True
    )

    mission_ru = models.JSONField(verbose_name="Миссия (RU)")
    mission_kg = models.JSONField(verbose_name="Миссия (KG)")
    mission_en = models.JSONField(verbose_name="Миссия (EN)")

    achievements_ru = models.JSONField(verbose_name="Достижения (RU)")
    achievements_kg = models.JSONField(verbose_name="Достижения (KG)")
    achievements_en = models.JSONField(verbose_name="Достижения (EN)")

    is_active = models.BooleanField(default=True, verbose_name="Активен")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания", null=True, blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления", null=True, blank=True
    )

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"
        ordering = ["order", "name_ru"]

    def str(self):
        return self.name_ru

    def get_name(self, language="ru"):
        return getattr(self, f"name_{language}", self.name_ru)

    def get_description(self, language="ru"):
        return getattr(self, f"description_{language}", self.description_ru)

    def get_mission(self, language="ru"):
        return getattr(self, f"mission_{language}", self.mission_ru)

    def get_achievements(self, language="ru"):
        return getattr(self, f"achievements_{language}", self.achievements_ru)


# Разделы для факультетов (для публичных страниц)
class FacultySection(models.Model):
    """Sections for faculty public pages"""

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name="public_sections",
        verbose_name="Факультет",
    )

    title_ru = models.CharField(max_length=255, verbose_name="Заголовок раздела (RU)")
    title_en = models.CharField(max_length=255, verbose_name="Заголовок раздела (EN)")
    title_kg = models.CharField(max_length=255, verbose_name="Заголовок раздела (KG)")

    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = "Раздел факультета"
        verbose_name_plural = "Разделы факультетов"
        ordering = ["order"]

    def str(self):
        return f"{self.faculty.name_ru} - {self.title_ru}"

    def get_title(self, language="ru"):
        return getattr(self, f"title_{language}", self.title_ru)


class FacultySectionItem(models.Model):
    """Items within a faculty section"""

    section = models.ForeignKey(
        FacultySection,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Раздел",
    )

    text_ru = models.CharField(max_length=500, verbose_name="Текст элемента (RU)")
    text_en = models.CharField(max_length=500, verbose_name="Текст элемента (EN)")
    text_kg = models.CharField(max_length=500, verbose_name="Текст элемента (KG)")

    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")

    class Meta:
        verbose_name = "Элемент раздела"
        verbose_name_plural = "Элементы разделов"
        ordering = ["order"]

    def str(self):
        return f"{self.section.title_ru} - {self.text_ru[:50]}"

    def get_text(self, language="ru"):
        return getattr(self, f"text_{language}", self.text_ru)