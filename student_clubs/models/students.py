from django.db import models
from django.contrib.auth.models import User
from .clubs import Club


class StudentProfile(models.Model):
    """Профиль студента с расширенной информацией"""

    # Связь с пользователем Django (если авторизация через систему)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="student_profile",
        verbose_name="Пользователь",
    )

    # Основная информация
    full_name_ru = models.CharField(max_length=200, verbose_name="ФИО (RU)")
    full_name_en = models.CharField(max_length=200, verbose_name="ФИО (EN)")
    full_name_kg = models.CharField(max_length=200, verbose_name="ФИО (KG)")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Телефон"
    )

    # Учебная информация
    faculty_ru = models.CharField(
        max_length=200, verbose_name="Факультет (RU)", blank=True, null=True
    )
    faculty_en = models.CharField(
        max_length=200, verbose_name="Факультет (EN)", blank=True, null=True
    )
    faculty_kg = models.CharField(
        max_length=200, verbose_name="Факультет (KG)", blank=True, null=True
    )

    year_of_study = models.PositiveSmallIntegerField(
        verbose_name="Курс",
        blank=True,
        null=True,
        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6")],
    )

    major_ru = models.CharField(
        max_length=200, verbose_name="Специальность (RU)", blank=True, null=True
    )
    major_en = models.CharField(
        max_length=200, verbose_name="Специальность (EN)", blank=True, null=True
    )
    major_kg = models.CharField(
        max_length=200, verbose_name="Специальность (KG)", blank=True, null=True
    )

    # Дополнительная информация
    bio_ru = models.TextField(verbose_name="О себе (RU)", blank=True, null=True)
    bio_en = models.TextField(verbose_name="О себе (EN)", blank=True, null=True)
    bio_kg = models.TextField(verbose_name="О себе (KG)", blank=True, null=True)

    interests = models.JSONField(
        default=list,
        blank=True,
        verbose_name="Интересы",
        help_text="Список интересов для рекомендаций клубов",
    )

    photo = models.ImageField(
        upload_to="student_profiles/",
        blank=True,
        null=True,
        verbose_name="Фото профиля",
    )

    # Метаданные
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Student Profile"
        verbose_name_plural = "Student Profiles"
        ordering = ["full_name_ru"]

    def __str__(self):
        return self.full_name_ru

    def get_field(self, field_name, language="ru"):
        """Получить значение поля на указанном языке"""
        field_with_lang = f"{field_name}_{language}"
        return getattr(self, field_with_lang, getattr(self, f"{field_name}_ru"))


class ClubMembership(models.Model):
    """Участие студента в клубе"""

    STATUS_CHOICES = [
        ("pending", "На рассмотрении"),
        ("approved", "Участник"),
        ("leader", "Руководитель"),
        ("rejected", "Отклонено"),
        ("left", "Покинул клуб"),
    ]

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="memberships",
        verbose_name="Студент",
    )

    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name="memberships", verbose_name="Клуб"
    )

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="Статус"
    )

    joined_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата присоединения"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    # Дополнительная информация
    motivation_text = models.TextField(
        verbose_name="Мотивация для вступления",
        blank=True,
        null=True,
        help_text="Почему студент хочет вступить в клуб",
    )

    role_ru = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Роль в клубе (RU)"
    )
    role_en = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Роль в клубе (EN)"
    )
    role_kg = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Роль в клубе (KG)"
    )

    class Meta:
        verbose_name = "Club Membership"
        verbose_name_plural = "Club Memberships"
        unique_together = ("student", "club")
        ordering = ["-joined_at"]

    def __str__(self):
        return f"{self.student.full_name_ru} - {self.club.name_ru} ({self.get_status_display()})"

    def get_field(self, field_name, language="ru"):
        """Получить значение поля на указанном языке"""
        field_with_lang = f"{field_name}_{language}"
        return getattr(self, field_with_lang, getattr(self, f"{field_name}_ru"))
