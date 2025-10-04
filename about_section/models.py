from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator,FileExtensionValidator
import json
from django.utils.translation import gettext_lazy as _
from django.utils import timezone



class Leadership(models.Model):
    """Руководство"""
    LEADERSHIP_TYPES = [
        ('director', 'Директор'),
        ('deputy_director', 'Заместитель директора'),
        ('department_head', 'Заведующий кафедрой'),
        ('dean', 'Декан'),
        ('vice_dean', 'Заместитель декана'),
    ]
    
    
    # Имя
    name = models.CharField(max_length=200, verbose_name="ФИО")
    name_kg = models.CharField(max_length=200, verbose_name="ФИО (KG)", blank=True)
    name_en = models.CharField(max_length=200, verbose_name="ФИО (EN)", blank=True)
    
    # Должность
    position = models.CharField(max_length=200, verbose_name="Должность")
    position_kg = models.CharField(max_length=200, verbose_name="Должность (KG)", blank=True)
    position_en = models.CharField(max_length=200, verbose_name="Должность (EN)", blank=True)
    
    # Ученая степень
    degree = models.CharField(max_length=200, verbose_name="Ученая степень")
    degree_kg = models.CharField(max_length=200, verbose_name="Ученая степень (KG)", blank=True)
    degree_en = models.CharField(max_length=200, verbose_name="Ученая степень (EN)", blank=True)
    
    # Опыт работы
    experience = models.CharField(max_length=100, verbose_name="Опыт работы")
    experience_kg = models.CharField(max_length=100, verbose_name="Опыт работы (KG)", blank=True)
    experience_en = models.CharField(max_length=100, verbose_name="Опыт работы (EN)", blank=True)
    
    # Биография
    bio = models.TextField(verbose_name="Биография", blank=True)
    bio_kg = models.TextField(verbose_name="Биография (KG)", blank=True)
    bio_en = models.TextField(verbose_name="Биография (EN)", blank=True)
    
    # Достижения (JSON поле для списка достижений)
    achievements = models.JSONField(default=list, verbose_name="Достижения", blank=True)
    achievements_kg = models.JSONField(default=list, verbose_name="Достижения (KG)", blank=True)
    achievements_en = models.JSONField(default=list, verbose_name="Достижения (EN)", blank=True)
    
    # Департамент/кафедра
    department = models.CharField(max_length=50,  verbose_name="Департамент(RU)", blank=True)
    department_kg = models.CharField(max_length=200, verbose_name="Департамент (KG)", blank=True)
    department_en = models.CharField(max_length=200, verbose_name="Департамент (EN)", blank=True)
    
    # Специализация (для заведующих кафедрами)
    specialization = models.TextField(verbose_name="Специализация", blank=True)
    specialization_kg = models.TextField(verbose_name="Специализация (KG)", blank=True)
    specialization_en = models.TextField(verbose_name="Специализация (EN)", blank=True)
    

    # Контакты
    email = models.EmailField(verbose_name="Email", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    
    # Фото
    image = models.ImageField(upload_to='leadership/photos/', verbose_name="Фото", blank=True)
    
    # Тип руководства и статус директора
    leadership_type = models.CharField(max_length=20, choices=LEADERSHIP_TYPES, verbose_name="Тип руководства")
    is_director = models.BooleanField(default=False, verbose_name="Является директором")
    
    # Системные поля
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководство"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.position}"



class Accreditation(models.Model):
    """Аккредитации и сертификаты"""
    ACCREDITATION_TYPES = [
        ('national', 'Национальная'),
        ('international', 'Международная'),
        ('institutional', 'Институциональная'),
        ('programmatic', 'Программная'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Название")
    name_kg = models.CharField(max_length=200, verbose_name="Название (KG)", blank=True)
    name_en = models.CharField(max_length=200, verbose_name="Название (EN)", blank=True)
    
    organization = models.CharField(max_length=200, verbose_name="Аккредитующая организация")
    organization_kg = models.CharField(max_length=200, verbose_name="Аккредитующая организация (KG)", blank=True)
    organization_en = models.CharField(max_length=200, verbose_name="Аккредитующая организация (EN)", blank=True)
    
    accreditation_type = models.CharField(max_length=20, choices=ACCREDITATION_TYPES, verbose_name="Тип аккредитации")
    accreditation_type_kg = models.CharField(max_length=100, verbose_name="Тип аккредитации (KG)", blank=True)
    accreditation_type_en = models.CharField(max_length=100, verbose_name="Тип аккредитации (EN)", blank=True)
    
    description = models.TextField(verbose_name="Описание", blank=True)
    description_kg = models.TextField(verbose_name="Описание (KG)", blank=True)
    description_en = models.TextField(verbose_name="Описание (EN)", blank=True)
    
    certificate_image = models.ImageField(upload_to='accreditations/certificates/', verbose_name="Сертификат", blank=True)
    organization_logo = models.ImageField(upload_to='accreditations/logos/', verbose_name="Логотип организации", blank=True)
    
    issue_date = models.DateField(verbose_name="Дата выдачи")
    expiry_date = models.DateField(verbose_name="Дата окончания", blank=True, null=True)
    
    certificate_number = models.CharField(max_length=100, verbose_name="Номер сертификата", blank=True)
    
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    order = models.IntegerField(default=0, verbose_name="Порядок отображения")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Аккредитация"
        verbose_name_plural = "Аккредитации"
        ordering = ['order', '-issue_date']
    
    def __str__(self):
        return f"{self.name} - {self.organization}"
    
    @property
    def is_valid(self):
        """Проверяет, действительна ли аккредитация"""
        if self.expiry_date:
            return timezone.now().date() <= self.expiry_date
        return True





class OrganizationStructure(models.Model):
    """Model for university organizational structure"""
    
    STRUCTURE_TYPES = [
        ('leadership', 'Руководство'),
        ('faculties', 'Факультеты'),
        ('administrative', 'Административные подразделения'),
        ('support', 'Вспомогательные подразделения'),
    ]
    
    name_ru = models.CharField(
        max_length=200,
        verbose_name='Название (Русский)',
        help_text='Название подразделения на русском языке'
    )
    
    name_en = models.CharField(
        max_length=200,
        verbose_name='Name (English)',
        help_text='Department name in English',
        blank=True
    )
    
    name_ky = models.CharField(
        max_length=200,
        verbose_name='Аталышы (Кыргызча)',
        help_text='Department name in Kyrgyz',
        blank=True
    )
    
    head_name_ru = models.CharField(
        max_length=200,
        verbose_name='Руководитель (Русский)',
        help_text='ФИО руководителя на русском языке',
        blank=True
    )
    
    head_name_en = models.CharField(
        max_length=200,
        verbose_name='Head (English)',
        help_text='Head name in English',
        blank=True
    )
    
    head_name_ky = models.CharField(
        max_length=200,
        verbose_name='Башчы (Кыргызча)',
        help_text='Head name in Kyrgyz',
        blank=True
    )
    
    structure_type = models.CharField(
        max_length=20,
        choices=STRUCTURE_TYPES,
        verbose_name='Тип подразделения',
        help_text='Категория организационной структуры'
    )
    
    phone = models.CharField(
        max_length=50,
        verbose_name='Телефон',
        blank=True
    )
    
    email = models.EmailField(
        verbose_name='Email',
        blank=True
    )
    
    icon = models.CharField(
        max_length=10,
        verbose_name='Иконка',
        help_text='Emoji иконка для отображения',
        default='🏢'
    )
    
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительское подразделение'
    )
    
    order = models.PositiveIntegerField(
        default=1,
        verbose_name='Порядок сортировки'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно',
        help_text='Отображать подразделение на сайте'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    
    class Meta:
        verbose_name = 'Организационная структура'
        verbose_name_plural = 'Организационная структура'
        ordering = ['structure_type', 'order', 'name_ru']
        
    def __str__(self):
        return self.name_ru
    
    def get_display_name(self, language='ru'):
        """Get name in specified language"""
        if language == 'en' and self.name_en:
            return self.name_en
        elif language == 'ky' and self.name_ky:
            return self.name_ky
        return self.name_ru
    
    def get_display_head_name(self, language='ru'):
        """Get head name in specified language"""
        if language == 'en' and self.head_name_en:
            return self.head_name_en
        elif language == 'ky' and self.head_name_ky:
            return self.head_name_ky
        return self.head_name_ru



class DownloadableDocument(models.Model):
    """Документы для скачивания"""
    # Мультиязычные поля
    title_ru = models.CharField('Название документа (русский)', max_length=255)
    title_kg = models.CharField('Название документа (кыргызский)', max_length=255)
    title_en = models.CharField('Название документа (английский)', max_length=255)
    
    description_ru = models.TextField('Описание (русский)', blank=True)
    description_kg = models.TextField('Описание (кыргызский)', blank=True)
    description_en = models.TextField('Описание (английский)', blank=True)
    
    # Файл документа
    file = models.FileField(
        upload_to='documents/',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])],
        verbose_name=_('Файл документа')
    )
    
    # Немультиязычные поля
    file_size = models.PositiveIntegerField(_('Размер файла (байты)'), null=True, blank=True)
    is_active = models.BooleanField(_('Активен'), default=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        verbose_name = _('Документ для скачивания')
        verbose_name_plural = _('Документы для скачивания')
        ordering = ['title_ru']

    def __str__(self):
        return self.title_ru
    
    def get_display_title(self, language='ru'):
        """Get title in specified language"""
        if language == 'en' and self.title_en:
            return self.title_en
        elif language == 'ky' and self.title_kg:
            return self.title_kg
        return self.title_ru
    
    @property
    def upload_date(self):
        """Alias for created_at to match serializer"""
        return self.created_at
