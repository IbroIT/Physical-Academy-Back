from django.db import models

# Create your models here.
class aboutStatistics(models.Model):
    titleInt = models.CharField(max_length=200, verbose_name='цифры типа 15+')
    description_ru = models.CharField(max_length=500, verbose_name='Описание на русском')
    description_en = models.CharField(max_length=500, verbose_name='Описание на английском')
    description_ky = models.CharField(max_length=500, verbose_name='Описание на кыргызском')
    emoji = models.CharField(max_length=50, verbose_name='эмодзи')

    class Meta:
        verbose_name = 'Статистика на главной'
        verbose_name_plural = 'Статистики на главной'

    def __str__(self):
        return self.titleInt
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    
class AboutPhotos(models.Model):
    photo = models.ImageField(upload_to='about_photos/', verbose_name='Фото для секции о нас')
    description_ru = models.CharField(max_length=500, verbose_name='Описание на русском', blank=True)
    description_en = models.CharField(max_length=500, verbose_name='Описание на английском', blank=True)
    description_ky = models.CharField(max_length=500, verbose_name='Описание на кыргызском', blank=True)

    class Meta:
        verbose_name = 'Фото для секции о нас'
        verbose_name_plural = 'Фото для секции о нас'

    def __str__(self):
        return f'Фото {self.id} для секции о нас'

    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    

class HistoryStep(models.Model):
    year = models.PositiveBigIntegerField(verbose_name='Год')
    title_ru = models.CharField(max_length=200, verbose_name='Заголовок шага истории(русский)')
    title_en = models.CharField(max_length=200, verbose_name='Заголовок шага истории(английский)')
    title_ky = models.CharField(max_length=200, verbose_name='Заголовок шага истории(киргизский)')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_ky = models.TextField(verbose_name='Описание на кыргызском')

    buildings = models.PositiveBigIntegerField(verbose_name='количество корпусов')
    students = models.PositiveBigIntegerField(verbose_name='количество студентов')
    programs = models.PositiveBigIntegerField(verbose_name='количество программ')

    achievements_ru = models.JSONField(verbose_name='Достижения на русском', blank=True)
    achievements_en = models.JSONField(verbose_name='Достижения на английском', blank=True)
    achievements_ky = models.JSONField(verbose_name='Достижения на кыргызском', blank=True)

    class Meta:
        verbose_name = 'Шаг истории'
        verbose_name_plural = 'Шаги истории'

    def __str__(self):
        return self.title_ru

    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    def get_title(self, language='ru'):
        return getattr(self, f'title_{language}', self.title_ru)
    def get_achievements(self, language='ru'):
        return getattr(self, f'achievements_{language}', self.achievements_ru)
    

class ImportantDates(models.Model):
        
        year = models.PositiveBigIntegerField(verbose_name='Год')
        titleInt = models.CharField(max_length=200, verbose_name='Заголовок важной даты типа 15+')
        description_ru = models.TextField(verbose_name='Описание на русском')
        description_en = models.TextField(verbose_name='Описание на английском')
        description_ky = models.TextField(verbose_name='Описание на кыргызском')

        class Meta:
            verbose_name = 'Важная веха'
            verbose_name_plural = 'Важные вехи'

        def __str__(self):
            return f'Важная веха {self.year}'

        def get_description(self, language='ru'):
            return getattr(self, f'description_{language}', self.description_ru)


class MissionCategory(models.Model):
    name_ru = models.CharField(max_length=200, verbose_name='категории name(русский)')
    name_en = models.CharField(max_length=200, verbose_name='категории name(английский)')
    name_ky = models.CharField(max_length=200, verbose_name='категории name(киргизский)')

    class Meta:
        verbose_name = 'Категория миссии'
        verbose_name_plural = 'Категории миссии'

    def __str__(self):
        return self.name_ru
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)

class Mission(models.Model):
    category = models.ForeignKey(MissionCategory, on_delete=models.CASCADE, related_name='missions', verbose_name='Категория миссии')
    title_ru = models.CharField(max_length=200, verbose_name='Заголовок миссии(русский)')
    title_en = models.CharField(max_length=200, verbose_name='Заголовок миссии(английский)')
    title_ky = models.CharField(max_length=200, verbose_name='Заголовок миссии(киргизский)')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    description_ky = models.TextField(verbose_name='Описание на кыргызском')

    class Meta:
        verbose_name = 'Миссия'
        verbose_name_plural = 'Миссии'

    def __str__(self):
        return f'Миссия {self.id} в категории {self.category.name_ru}'

    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    def get_title(self, language='ru'):
        return getattr(self, f'title_{language}', self.title_ru)



class AccreditationType(models.Model):
  
    name_ru = models.CharField(max_length=200, verbose_name='Название (русский)')
    name_en = models.CharField(max_length=200, verbose_name='Название (английский)')
    name_ky = models.CharField(max_length=200, verbose_name='Название (киргизский)')

    class Meta:
        verbose_name = 'Тип аккредитации'
        verbose_name_plural = 'Типы аккредитации'

    def __str__(self):
        return f"{self.name_ru}"

    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)


class Accreditation(models.Model):
    # Основная информация — три языка для текстов
    organization_ru = models.CharField(max_length=255)
    organization_en = models.CharField(max_length=255)
    organization_ky = models.CharField(max_length=255)

    logo = models.ImageField(upload_to='accreditation_logos/', blank=True, null=True)

    validity_ru = models.CharField(max_length=255)
    validity_en = models.CharField(max_length=255)
    validity_ky = models.CharField(max_length=255)

    description_ru = models.TextField()
    description_en = models.TextField()
    description_ky = models.TextField()

    # Ссылка на тип аккредитации (модель с переводами)
    accreditation_type = models.ForeignKey(
        AccreditationType,
        on_delete=models.PROTECT,
        related_name='accreditations'
    )
    photo = models.ImageField(upload_to='accreditation_photos/', blank=True, null=True)

    certificate_number = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    order = models.IntegerField(default=0)  # если нужен порядок вывода

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Аккредитация'
        verbose_name_plural = 'Аккредитации'
        ordering = ['order', '-created_at']  # сортировка по порядку, затем по дате создания

    def __str__(self):
        return self.organization_ru
    
    def get_organization(self, language='ru'):
        return getattr(self, f'organization_{language}', self.organization_ru)
    
    def get_validity(self, language='ru'):
        return getattr(self, f'validity_{language}', self.validity_ru)
    
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    
class AcademyStatistics(models.Model):
    titleInt = models.CharField(max_length=100, verbose_name='заголовок-цифры типа 15+')
    title_ru = models.CharField(max_length=250, verbose_name='заголовок на русском')
    title_en = models.CharField(max_length=250, verbose_name='заголовок на английском')
    title_ky = models.CharField(max_length=250, verbose_name='заголовок на киргизском')
    description_ru = models.TextField(verbose_name='описание на русском')
    description_en = models.TextField(verbose_name='описание на английском')
    description_ky = models.TextField(verbose_name='описание на киргизском')
    emoji = models.CharField(max_length=5, verbose_name='эмодзи', )

    class Meta:
        verbose_name = 'Статистика академии'
        verbose_name_plural = 'Статистики академии'

    def get_title(self, language='ru'):
        return getattr(self, f'title_{language}', self.title_ru)
    def get_description(self, language='ru'):
        return getattr(self, f'descripton_{language}', self.description_ru)

class AcademyAchievements(models.Model):
    year = models.PositiveBigIntegerField(verbose_name='год ')
    title_ru = models.CharField(max_length=500, verbose_name='заголовок на русском')
    title_en = models.CharField(max_length=500, verbose_name='заголовок на английском')
    title_ky = models.CharField(max_length=500, verbose_name='заголовок на киргизском')
    description_ru = models.TextField(verbose_name='описание на русском')
    description_en = models.TextField(verbose_name='описание на английском')
    description_ky = models.TextField(verbose_name='описание на киргизском')

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def get_title(self, language='ru'):
        return getattr(self, f'title_{language}', self.title_ru)

    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)


class AcademyInfrastructure(models.Model):
    emoji = models.CharField(max_length=5, verbose_name='эмодзи', )
    titleInt = models.CharField(max_length=20, verbose_name='заголовок-цифра типа 1000+')

    description_ru = models.CharField(max_length=250, verbose_name='описание на русском')
    description_en = models.CharField(max_length=250, verbose_name='описание на английском')
    description_ky = models.CharField(max_length=250, verbose_name='описание на киргизском')

    class Meta:
        verbose_name = 'Инфраструктура'
        verbose_name_plural = 'Инфраструктуры'

    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)

