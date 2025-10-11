from django.db import models
from django.utils.translation import gettext_lazy as _


class QuotaType(models.Model):
    """Модель для типов квот с поддержкой трех языков"""
    
    QUOTA_TYPES = [
        ('sports', 'Sports'),
        ('health', 'Health'),
        ('target', 'Target'),
    ]
    
    COLORS = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('cyan', 'Cyan'),
        ('purple', 'Purple'),
        ('orange', 'Orange'),
    ]
    
    type = models.CharField(max_length=20, choices=QUOTA_TYPES, unique=True, verbose_name=_('Type'))
    
    # Многоязычные поля для названия
    title_ru = models.CharField(max_length=200, verbose_name=_('Title (Russian)'))
    title_ky = models.CharField(max_length=200, verbose_name=_('Title (Kyrgyz)'))
    title_en = models.CharField(max_length=200, verbose_name=_('Title (English)'))
    
    # Многоязычные поля для описания
    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))
    
    icon = models.CharField(max_length=10, verbose_name=_('Icon (emoji)'))
    spots = models.PositiveIntegerField(verbose_name=_('Available spots'))
    deadline = models.CharField(max_length=50, verbose_name=_('Application deadline'))
    color = models.CharField(max_length=20, choices=COLORS, default='blue', verbose_name=_('Color scheme'))
    
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'type']
        verbose_name = _('Quota Type')
        verbose_name_plural = _('Quota Types')
    
    def __str__(self):
        return self.title_ru
    
    def get_title(self, language='ru'):
        """Получить название на указанном языке"""
        return getattr(self, f'title_{language}', self.title_ru)
    
    def get_description(self, language='ru'):
        """Получить описание на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)


class QuotaRequirement(models.Model):
    """Модель для требований к квотам"""
    
    quota_type = models.ForeignKey(
        QuotaType, 
        on_delete=models.CASCADE, 
        related_name='requirements',
        verbose_name=_('Quota Type')
    )
    
    # Многоязычные поля для требований
    requirement_ru = models.TextField(verbose_name=_('Requirement (Russian)'))
    requirement_ky = models.TextField(verbose_name=_('Requirement (Kyrgyz)'))
    requirement_en = models.TextField(verbose_name=_('Requirement (English)'))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['quota_type', 'order']
        verbose_name = _('Quota Requirement')
        verbose_name_plural = _('Quota Requirements')
    
    def __str__(self):
        return f"{self.quota_type.title_ru} - {self.requirement_ru[:50]}"
    
    def get_requirement(self, language='ru'):
        """Получить требование на указанном языке"""
        return getattr(self, f'requirement_{language}', self.requirement_ru)


class QuotaBenefit(models.Model):
    """Модель для преимуществ квот"""
    
    quota_type = models.ForeignKey(
        QuotaType, 
        on_delete=models.CASCADE, 
        related_name='benefits',
        verbose_name=_('Quota Type')
    )
    
    # Многоязычные поля для преимуществ
    benefit_ru = models.TextField(verbose_name=_('Benefit (Russian)'))
    benefit_ky = models.TextField(verbose_name=_('Benefit (Kyrgyz)'))
    benefit_en = models.TextField(verbose_name=_('Benefit (English)'))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['quota_type', 'order']
        verbose_name = _('Quota Benefit')
        verbose_name_plural = _('Quota Benefits')
    
    def __str__(self):
        return f"{self.quota_type.title_ru} - {self.benefit_ru[:50]}"
    
    def get_benefit(self, language='ru'):
        """Получить преимущество на указанном языке"""
        return getattr(self, f'benefit_{language}', self.benefit_ru)


class QuotaStats(models.Model):
    """Модель для статистических данных о квотах"""
    
    STAT_TYPES = [
        ('total_spots', 'Total Spots'),
        ('success_rate', 'Success Rate'),
        ('organizations', 'Organizations'),
        ('quota_types', 'Quota Types'),
    ]
    
    stat_type = models.CharField(max_length=20, choices=STAT_TYPES, unique=True, verbose_name=_('Statistic Type'))
    
    number = models.CharField(max_length=20, verbose_name=_('Number/Value'))
    
    # Многоязычные поля для подписи
    label_ru = models.CharField(max_length=200, verbose_name=_('Label (Russian)'))
    label_ky = models.CharField(max_length=200, verbose_name=_('Label (Kyrgyz)'))
    label_en = models.CharField(max_length=200, verbose_name=_('Label (English)'))
    
    # Многоязычные поля для описания
    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'stat_type']
        verbose_name = _('Quota Statistics')
        verbose_name_plural = _('Quota Statistics')
    
    def __str__(self):
        return f"{self.number} - {self.label_ru}"
    
    def get_label(self, language='ru'):
        """Получить подпись на указанном языке"""
        return getattr(self, f'label_{language}', self.label_ru)
    
    def get_description(self, language='ru'):
        """Получить описание на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)


class AdditionalSupport(models.Model):
    """Модель для дополнительной поддержки"""
    
    # Многоязычные поля для поддержки
    support_ru = models.TextField(verbose_name=_('Support (Russian)'))
    support_ky = models.TextField(verbose_name=_('Support (Kyrgyz)'))
    support_en = models.TextField(verbose_name=_('Support (English)'))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = _('Additional Support')
        verbose_name_plural = _('Additional Support')
    
    def __str__(self):
        return self.support_ru[:50]
    
    def get_support(self, language='ru'):
        """Получить поддержку на указанном языке"""
        return getattr(self, f'support_{language}', self.support_ru)


class ProcessStep(models.Model):
    """Модель для шагов процесса подачи заявления"""
    
    step_number = models.PositiveIntegerField(verbose_name=_('Step number'))
    
    # Многоязычные поля для названия шага
    title_ru = models.CharField(max_length=200, verbose_name=_('Title (Russian)'))
    title_ky = models.CharField(max_length=200, verbose_name=_('Title (Kyrgyz)'))
    title_en = models.CharField(max_length=200, verbose_name=_('Title (English)'))
    
    # Многоязычные поля для описания шага
    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))
    
    color_scheme = models.CharField(max_length=50, default='from-blue-500 to-cyan-500', verbose_name=_('Color scheme'))
    
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['step_number']
        verbose_name = _('Process Step')
        verbose_name_plural = _('Process Steps')
    
    def __str__(self):
        return f"Шаг {self.step_number}: {self.title_ru}"
    
    def get_title(self, language='ru'):
        """Получить название на указанном языке"""
        return getattr(self, f'title_{language}', self.title_ru)
    
    def get_description(self, language='ru'):
        """Получить описание на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)


class MasterDocuments(models.Model):
    """Модель для документов магистратуры"""
    
    # Многоязычные поля для названия документа
    document_name_ru = models.CharField(max_length=200, verbose_name=_('Document Name (Russian)'))
    document_name_ky = models.CharField(max_length=200, verbose_name=_('Document Name (Kyrgyz)'))
    document_name_en = models.CharField(max_length=200, verbose_name=_('Document Name (English)'))
    
    file = models.FileField(upload_to='master_documents/', verbose_name=_('File'))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = _('Master Document')
        verbose_name_plural = _('Master Documents')
    
    def __str__(self):
        return self.document_name_ru
    
    def get_document_name(self, language='ru'):
        """Получить название документа на указанном языке"""
        return getattr(self, f'document_name_{language}', self.document_name_ru)


class MasterMainDate(models.Model):
    """Модель для основных дат магистратуры"""
    
    # Многоязычные поля для названия события
    event_name_ru = models.CharField(max_length=200, verbose_name=_('Event Name (Russian)'))
    event_name_ky = models.CharField(max_length=200, verbose_name=_('Event Name (Kyrgyz)'))
    event_name_en = models.CharField(max_length=200, verbose_name=_('Event Name (English)'))
    
    date = models.CharField(max_length=100, verbose_name=_('Date/Period'))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = _('Master Main Date')
        verbose_name_plural = _('Master Main Dates')
    
    def __str__(self):
        return self.event_name_ru
    
    def get_event_name(self, language='ru'):
        """Получить название события на указанном языке"""
        return getattr(self, f'event_name_{language}', self.event_name_ru)
    
class MasterPrograms(models.Model):
    """Модель для программ магистратуры"""
    
    program_name_ru = models.CharField(max_length=200, verbose_name=_('Program Name'))
    program_name_ky = models.CharField(max_length=200, verbose_name=_('Program Name'))
    program_name_en = models.CharField(max_length=200, verbose_name=_('Program Name'))

    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))

    features_ru = models.JSONField(verbose_name=_('Features (Russian)'))
    features_ky = models.JSONField(verbose_name=_('Features (Kyrgyz)'))
    features_en = models.JSONField(verbose_name=_('Features (English)'))

    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'program_name_ru']
        verbose_name = _('Master Program')
        verbose_name_plural = _('Master Programs')
    
    def __str__(self):
        return self.program_name_ru
    
    def get_program_name(self, language='ru'):
        """Получить название программы на указанном языке"""
        return getattr(self, f'program_name_{language}', self.program_name_ru)
    
    def get_description(self, language='ru'):
        """Получить описание программы на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)
    
    def get_features(self, language='ru'):
        """Получить особенности программы на указанном языке"""
        return getattr(self, f'features_{language}', self.features_ru)

class MasterRequirements(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name=_('Title (Russian)'))
    title_ky = models.CharField(max_length=200, verbose_name=_('Title (Kyrgyz)'))
    title_en = models.CharField(max_length=200, verbose_name=_('Title (English)'))

    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))

    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title_ru']
        verbose_name = _('Master Requirement')
        verbose_name_plural = _('Master Requirements')
    
    def get_title(self, language='ru'):
        """Получить название на указанном языке"""
        return getattr(self, f'title_{language}', self.title_ru)

    def get_description(self, language='ru'):
        """Получить описание на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)


class AspirantMainDate(models.Model):
    """Модель для основных дат аспирантуры"""

    # Многоязычные поля для названия события
    event_name_ru = models.CharField(max_length=200, verbose_name=_('Event Name (Russian)'))
    event_name_ky = models.CharField(max_length=200, verbose_name=_('Event Name (Kyrgyz)'))
    event_name_en = models.CharField(max_length=200, verbose_name=_('Event Name (English)'))
    
    date = models.CharField(max_length=100, verbose_name=_('Date/Period'))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = _('Aspirant Main Date')
        verbose_name_plural = _('Aspirant Main Dates')

    def __str__(self):
        return self.event_name_ru
    
    def get_event_name(self, language='ru'):
        """Получить название события на указанном языке"""
        return getattr(self, f'event_name_{language}', self.event_name_ru)

class AspirantPrograms(models.Model):
    """Модель для программ аспирантуры"""

    program_name_ru = models.CharField(max_length=200, verbose_name=_('Program Name'))
    program_name_ky = models.CharField(max_length=200, verbose_name=_('Program Name'))
    program_name_en = models.CharField(max_length=200, verbose_name=_('Program Name'))

    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))

    features_ru = models.JSONField(verbose_name=_('Features (Russian)'))
    features_ky = models.JSONField(verbose_name=_('Features (Kyrgyz)'))
    features_en = models.JSONField(verbose_name=_('Features (English)'))

    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'program_name_ru']
        verbose_name = _('Aspirant Program')
        verbose_name_plural = _('Aspirant Programs')

    def __str__(self):
        return self.program_name_ru

    def get_program_name(self, language='ru'):
        """Получить название программы на указанном языке"""
        return getattr(self, f'program_name_{language}', self.program_name_ru)
    
    def get_description(self, language='ru'):
        """Получить описание программы на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)
    
    def get_features(self, language='ru'):
        """Получить особенности программы на указанном языке"""
        return getattr(self, f'features_{language}', self.features_ru)

class AspirantRequirements(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name=_('Title (Russian)'))
    title_ky = models.CharField(max_length=200, verbose_name=_('Title (Kyrgyz)'))
    title_en = models.CharField(max_length=200, verbose_name=_('Title (English)'))

    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))

    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title_ru']
        verbose_name = _('Aspirant Requirement')
        verbose_name_plural = _('Aspirant Requirements')

    def get_title(self, language='ru'):
        """Получить название на указанном языке"""
        return getattr(self, f'title_{language}', self.title_ru)

    def get_description(self, language='ru'):
        """Получить описание на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)

class AspirantDocuments(models.Model):
    """Модель для документов аспирантуры"""

    # Многоязычные поля для названия документа
    document_name_ru = models.CharField(max_length=200, verbose_name=_('Document Name (Russian)'))
    document_name_ky = models.CharField(max_length=200, verbose_name=_('Document Name (Kyrgyz)'))
    document_name_en = models.CharField(max_length=200, verbose_name=_('Document Name (English)'))
    
    file = models.FileField(upload_to='aspirant_documents/', verbose_name=_('File'))
    
    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = _('Aspirant  Document')
        verbose_name_plural = _('Aspirant Documents')

    def __str__(self):
        return self.document_name_ru
    
    def get_document_name(self, language='ru'):
        """Получить название документа на указанном языке"""
        return getattr(self, f'document_name_{language}', self.document_name_ru)



class DoctorAdmissionSteps(models.Model):
    """Модель для информации о приеме в докторантуру"""

    title_ru = models.TextField(verbose_name=_('Title (Russian)'))
    title_ky = models.TextField(verbose_name=_('Title (Kyrgyz)'))
    title_en = models.TextField(verbose_name=_('Title (English)'))

    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))   
    description_en = models.TextField(verbose_name=_('Description (English)'))

    deadline_ru = models.TextField(verbose_name=_('Deadline (Russian)'))
    deadline_ky = models.TextField(verbose_name=_('Deadline (Kyrgyz)'))
    deadline_en = models.TextField(verbose_name=_('Deadline (English)'))

    requirement_ru = models.TextField(verbose_name=_('Requirement (Russian)'))
    requirement_ky = models.TextField(verbose_name=_('Requirement (Kyrgyz)'))
    requirement_en = models.TextField(verbose_name=_('Requirement (English)'))

    order = models.PositiveIntegerField(verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = _('Doctor Admission Info')
        verbose_name_plural = _('Doctor Admission Info')
    
    def __str__(self):
        return self.title_en[:50]
    
    def get_title(self, language='ru'):
        """Получить название на указанном языке"""
        return getattr(self, f'title_{language}', self.title_ru)

    def get_description(self, language='ru'):
        """Получить описание на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)
    
    def get_deadline(self, language='ru'):
        """Получить дедлайн на указанном языке"""
        return getattr(self, f'deadline_{language}', self.deadline_ru)
    
    def get_requirement(self, language='ru'):
        """Получить требование на указанном языке"""
        return getattr(self, f'requirement_{language}', self.requirement_ru)



class DoctorStatistics(models.Model):
    titleInt = models.CharField(max_length=200, verbose_name=_('Title (Russian)'))

    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))

    class Meta:
        verbose_name = _('Doctor Statistics')
        verbose_name_plural = _('Doctor Statistics')

    def __str__(self):
        return self.titleInt
    
    def get_description(self, language='ru'):
        """Получить описание на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)
    
class DoctorPrograms(models.Model):
    """Модель для программ докторантуры"""

    program_name_ru = models.CharField(max_length=200, verbose_name=_('Program Name(russian)'))
    program_name_ky = models.CharField(max_length=200, verbose_name=_('Program Name(kyrgyz)'))
    program_name_en = models.CharField(max_length=200, verbose_name=_('Program Name(english)'))

    short_description_ru = models.CharField(max_length=300, verbose_name=_('Short Description (Russian)'))
    short_description_ky = models.CharField(max_length=300, verbose_name=_('Short   Description (Kyrgyz)'))
    short_description_en = models.CharField(max_length=300, verbose_name=_('Short Description (English)'))

    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))

    features_ru = models.JSONField(verbose_name=_('Features (Russian)'), default=list)
    features_ky = models.JSONField(verbose_name=_('Features (Kyrgyz)'), default=list)
    features_en = models.JSONField(verbose_name=_('Features (English)'), default=list)

    duration = models.PositiveBigIntegerField(verbose_name=_('Duration (years)'))

    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'program_name_ru']
        verbose_name = _('Doctor Program')
        verbose_name_plural = _('Doctor Programs')

    def __str__(self):
        return self.program_name_ru

    def get_program_name(self, language='ru'):
        """Получить название программы на указанном языке"""
        return getattr(self, f'program_name_{language}', self.program_name_ru)
    
    def get_description(self, language='ru'):
        """Получить описание программы на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)
    
    def get_features(self, language='ru'):
        """Получить особенности программы на указанном языке"""
        return getattr(self, f'features_{language}', self.features_ru)
    
    def get_short_description(self, language='ru'):
        """Получить краткое описание программы на указанном языке"""
        return getattr(self, f'short_description_{language}', self.short_description_ru)
    

class DoctorSoonEvents(models.Model):
    event_ru = models.CharField(max_length=200, verbose_name=_('Event (Russian)'))
    event_ky = models.CharField(max_length=200, verbose_name=_('Event (Kyrgyz)'))
    event_en = models.CharField(max_length=200, verbose_name=_('Event (English)'))
    date = models.CharField(max_length=100, verbose_name=_('Date/Period'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    class Meta:
        ordering = ['date']
        verbose_name = _('Doctor Soon Event')
        verbose_name_plural = _('Doctor Soon Events')

    def __str__(self):
        return self.event_ru
    
    def get_event(self, language='ru'):
        """Получить событие на указанном языке"""
        return getattr(self, f'event_{language}', self.event_ru)


class CollegeSoonEvents(models.Model):
    event_ru = models.CharField(max_length=200, verbose_name=_('Event (Russian)'))
    event_ky = models.CharField(max_length=200, verbose_name=_('Event (Kyrgyz)'))
    event_en = models.CharField(max_length=200, verbose_name=_('Event (English)'))
    date = models.CharField(max_length=100, verbose_name=_('Date/Period'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    class Meta:
        ordering = ['date']
        verbose_name = _('College Soon Event')
        verbose_name_plural = _('College Soon Events')

    def __str__(self):
        return self.event_ru
    
    def get_event(self, language='ru'):
        """Получить событие на указанном языке"""
        return getattr(self, f'event_{language}', self.event_ru)
    

class CollegePrograms(models.Model):
    """Модель для программ докторантуры"""

    program_name_ru = models.CharField(max_length=200, verbose_name=_('Program Name(russian)'))
    program_name_ky = models.CharField(max_length=200, verbose_name=_('Program Name(kyrgyz)'))
    program_name_en = models.CharField(max_length=200, verbose_name=_('Program Name(english)'))

    short_description_ru = models.CharField(max_length=300, verbose_name=_('Short Description (Russian)'))
    short_description_ky = models.CharField(max_length=300, verbose_name=_('Short   Description (Kyrgyz)'))
    short_description_en = models.CharField(max_length=300, verbose_name=_('Short Description (English)'))

    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))

    features_ru = models.JSONField(verbose_name=_('Features (Russian)'), default=list)
    features_ky = models.JSONField(verbose_name=_('Features (Kyrgyz)'), default=list)
    features_en = models.JSONField(verbose_name=_('Features (English)'), default=list)

    duration = models.PositiveBigIntegerField(verbose_name=_('Duration (years)'))

    order = models.PositiveIntegerField(default=0, verbose_name=_('Display order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'program_name_ru']
        verbose_name = _('College Program')
        verbose_name_plural = _('College Programs')

    def __str__(self):
        return self.program_name_ru

    def get_program_name(self, language='ru'):
        """Получить название программы на указанном языке"""
        return getattr(self, f'program_name_{language}', self.program_name_ru)
    
    def get_description(self, language='ru'):
        """Получить описание программы на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)
    
    def get_features(self, language='ru'):
        """Получить особенности программы на указанном языке"""
        return getattr(self, f'features_{language}', self.features_ru)
    
    def get_short_description(self, language='ru'):
        """Получить краткое описание программы на указанном языке"""
        return getattr(self, f'short_description_{language}', self.short_description_ru)
    

class CollegeAdmissionSteps(models.Model):
    title_ru = models.TextField(verbose_name=_('Title (Russian)')) 
    title_ky = models.TextField(verbose_name=_('Title (Kyrgyz)'))
    title_en = models.TextField(verbose_name=_('Title (English)'))

    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))

    duration_ru = models.TextField(verbose_name=_('Duration (Russian) date and month'))
    duration_ky = models.TextField(verbose_name=_('Duration (Kyrgyz) date and month'))
    duration_en = models.TextField(verbose_name=_('Duration (English) date and month'))

    order = models.PositiveIntegerField(verbose_name=_('Display order'))

    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('College Admission Step')
        verbose_name_plural = _('College Admission Steps')

    def __str__(self):
        return self.title_ru[:50]
    
    def get_title(self, language='ru'):
        """Получить название на указанном языке"""
        return getattr(self, f'title_{language}', self.title_ru)
    
    def get_description(self, language='ru'):
        """Получить описание на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)
    
    def get_duration(self, language='ru'):
        """Получить продолжительность на указанном языке"""
        return getattr(self, f'duration_{language}', self.duration_ru)


class CollegeAdmissionRequirements(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name=_('Title (Russian)'))
    title_ky = models.CharField(max_length=200, verbose_name=_('Title (Kyrgyz)'))
    title_en = models.CharField(max_length=200, verbose_name=_('Title (English)'))

    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))

    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [ 'title_ru']
        verbose_name = _('College Admission Requirement')
        verbose_name_plural = _('College Admission Requirements')
    
    def get_title(self, language='ru'):
        """Получить название на указанном языке"""
        return getattr(self, f'title_{language}', self.title_ru)

    def get_description(self, language='ru'):
        """Получить описание на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)

class CollegeStatistics(models.Model):
    titleInt = models.CharField(max_length=200, verbose_name=_('Title (Russian)'))

    description_ru = models.TextField(verbose_name=_('Description (Russian)'))
    description_ky = models.TextField(verbose_name=_('Description (Kyrgyz)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))

    class Meta:
        verbose_name = _('College Statistics')
        verbose_name_plural = _('College Statistics')

    def __str__(self):
        return self.titleInt
    
    def get_description(self, language='ru'):
        """Получить описание на указанном языке"""
        return getattr(self, f'description_{language}', self.description_ru)