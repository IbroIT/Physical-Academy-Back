from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('conference', _('Конференция')),
        ('seminar', _('Семинар')),
        ('workshop', _('Воркшоп')),
        ('lecture', _('Лекция')),
        ('exhibition', _('Выставка')),
        ('competition', _('Соревнование')),
        ('festival', _('Фестиваль')),
        ('sports', _('Спорт')),
        ('cultural', _('Культурное мероприятие')),
        ('other', _('Другое')),
    ]

    DEPARTMENT_CHOICES = [
        ('computer_science', _('Факультет компьютерных наук')),
        ('engineering', _('Инженерный факультет')),
        ('business', _('Бизнес факультет')),
        ('medicine', _('Медицинский факультет')),
        ('arts', _('Факультет искусств')),
        ('science', _('Естественнонаучный факультет')),
        ('law', _('Юридический факультет')),
        ('international', _('Международный отдел')),
        ('student_union', _('Студенческий союз')),
    ]

    # Мультиязычные поля
    title_ru = models.CharField(_('Заголовок (русский)'), max_length=200, default='')
    title_en = models.CharField(_('Заголовок (английский)'), max_length=200, default='')
    title_ky = models.CharField(_('Заголовок (кыргызский)'), max_length=200, default='')
    
    description_ru = models.TextField(_('Описание (русский)'), default='')
    description_en = models.TextField(_('Описание (английский)'), default='')
    description_ky = models.TextField(_('Описание (кыргызский)'), default='')
    
    full_description_ru = models.TextField(_('Полное описание (русский)'), blank=True, default='')
    full_description_en = models.TextField(_('Полное описание (английский)'), blank=True, default='')
    full_description_ky = models.TextField(_('Полное описание (кыргызский)'), blank=True, default='')

    # Общие поля
    category = models.CharField(
        _('Категория'),
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other'
    )
    
    department = models.CharField(
        _('Факультет/Отдел'),
        max_length=20,
        choices=DEPARTMENT_CHOICES,
        default='computer_science'
    )
    
    image = models.ImageField(
        _('Изображение'),
        upload_to='events/',
        blank=True,
        null=True
    )
    
    date = models.DateField(
        _('Дата мероприятия'),
        default=timezone.now
    )
    
    time = models.TimeField(
        _('Время мероприятия'),
        default=timezone.now
    )
    
    location_ru = models.CharField(_('Место проведения (русский)'), max_length=300, default='')
    location_en = models.CharField(_('Место проведения (английский)'), max_length=300, default='')
    location_ky = models.CharField(_('Место проведения (кыргызский)'), max_length=300, default='')

    # Дополнительные поля
    audience_ru = models.CharField(_('Аудитория (русский)'), max_length=200, blank=True, default='')
    audience_en = models.CharField(_('Аудитория (английский)'), max_length=200, blank=True, default='')
    audience_ky = models.CharField(_('Аудитория (кыргызский)'), max_length=200, blank=True, default='')
    
    format_ru = models.CharField(_('Формат (русский)'), max_length=100, blank=True, default='')
    format_en = models.CharField(_('Формат (английский)'), max_length=100, blank=True, default='')
    format_ky = models.CharField(_('Формат (кыргызский)'), max_length=100, blank=True, default='')
    
    duration_ru = models.CharField(_('Продолжительность (русский)'), max_length=50, blank=True, default='')
    duration_en = models.CharField(_('Продолжительность (английский)'), max_length=50, blank=True, default='')
    duration_ky = models.CharField(_('Продолжительность (кыргызский)'), max_length=50, blank=True, default='')

    # Организатор
    organizer_name_ru = models.CharField(_('Имя организатора (русский)'), max_length=100, blank=True, default='')
    organizer_name_en = models.CharField(_('Имя организатора (английский)'), max_length=100, blank=True, default='')
    organizer_name_ky = models.CharField(_('Имя организатора (кыргызский)'), max_length=100, blank=True, default='')
    
    organizer_contact_ru = models.CharField(_('Контакты организатора (русский)'), max_length=200, blank=True, default='')
    organizer_contact_en = models.CharField(_('Контакты организатора (английский)'), max_length=200, blank=True, default='')
    organizer_contact_ky = models.CharField(_('Контакты организатора (кыргызский)'), max_length=200, blank=True, default='')

    # Статус и даты
    is_active = models.BooleanField(_('Активно'), default=True)
    is_featured = models.BooleanField(_('Рекомендуемое'), default=False)
    order = models.PositiveIntegerField(_('Порядок отображения'), default=0)
    
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Дата обновления'), auto_now=True)

    class Meta:
        verbose_name = _('Мероприятие')
        verbose_name_plural = _('Мероприятия')
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.title_ru} ({self.date})"

    def clean(self):
        if self.date and self.date < timezone.now().date():
            raise ValidationError(_('Дата мероприятия не может быть в прошлом'))

    def get_title(self, language):
        return getattr(self, f'title_{language}', self.title_ru)

    def get_description(self, language):
        return getattr(self, f'description_{language}', self.description_ru)

    def get_full_description(self, language):
        return getattr(self, f'full_description_{language}', self.full_description_ru)

    def get_location(self, language):
        return getattr(self, f'location_{language}', self.location_ru)

    def get_audience(self, language):
        return getattr(self, f'audience_{language}', self.audience_ru)

    def get_format(self, language):
        return getattr(self, f'format_{language}', self.format_ru)

    def get_duration(self, language):
        return getattr(self, f'duration_{language}', self.duration_ru)

    def get_organizer_name(self, language):
        return getattr(self, f'organizer_name_{language}', self.organizer_name_ru)

    def get_organizer_contact(self, language):
        return getattr(self, f'organizer_contact_{language}', self.organizer_contact_ru)