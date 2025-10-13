from django.db import models

# Create your models here.

class MasterPrograms(models.Model):
    emoji = models.CharField(max_length=10, verbose_name="Эмодзи")

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_ky = models.CharField(max_length=100, verbose_name="Название (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name='Описание (RU)')
    description_ky = models.TextField(verbose_name='Описание (KY)')
    description_en = models.TextField(verbose_name='Описание (EN)')

    features_ru = models.JSONField(verbose_name='Особенности (RU)')
    features_ky = models.JSONField(verbose_name='Особенности (KY)')
    features_en = models.JSONField(verbose_name='Особенности (EN)')

    duration_years = models.IntegerField(verbose_name="Продолжительность (годы)")
    offline = models.BooleanField(default=True, verbose_name="Очная форма")
    tuition_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Стоимость обучения")
    

    class Meta:
        verbose_name = 'Программа магистра'
        verbose_name_plural = 'Программы магистра'
    def __str__(self):
        return self.name_ru
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    def get_features(self, language='ru'):
        return getattr(self, f'features_{language}', self.features_ru)

class PhdPrograms(models.Model):
    emoji = models.CharField(max_length=10, verbose_name="Эмодзи")

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_ky = models.CharField(max_length=100, verbose_name="Название (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name='Описание (RU)')
    description_ky = models.TextField(verbose_name='Описание (KY)')
    description_en = models.TextField(verbose_name='Описание (EN)')

    features_ru = models.JSONField(verbose_name='Особенности (RU)')
    features_ky = models.JSONField(verbose_name='Особенности (KY)')
    features_en = models.JSONField(verbose_name='Особенности (EN)')

    duration_years = models.IntegerField(verbose_name="Продолжительность (годы)")
    offline = models.BooleanField(default=True, verbose_name="Очная форма")
    tuition_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Стоимость обучения")
    
    class Meta:
        verbose_name = 'Программа доктурантуры'
        verbose_name_plural = 'Программы доктурантуры'
    def __str__(self):
        return self.name_ru
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    def get_features(self, language='ru'):
        return getattr(self, f'features_{language}', self.features_ru)

class CollegePrograms(models.Model):
    emoji = models.CharField(max_length=10, verbose_name="Эмодзи")

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_ky = models.CharField(max_length=100, verbose_name="Название (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name='Описание (RU)')
    description_ky = models.TextField(verbose_name='Описание (KY)')
    description_en = models.TextField(verbose_name='Описание (EN)')

    features_ru = models.JSONField(verbose_name='Особенности (RU)')
    features_ky = models.JSONField(verbose_name='Особенности (KY)')
    features_en = models.JSONField(verbose_name='Особенности (EN)')

    duration_years = models.IntegerField(verbose_name="Продолжительность (годы)")
    offline = models.BooleanField(default=True, verbose_name="Очная форма")
    tuition_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Стоимость обучения")
    
    class Meta:
        verbose_name = 'Программа колледжа'
        verbose_name_plural = 'Программы колледжа'
    def __str__(self):
        return self.name_ru
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    def get_features(self, language='ru'):
        return getattr(self, f'features_{language}', self.features_ru)


class FacultyStatistics(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='statistics')
    
    titleInt = models.CharField(max_length=100, verbose_name="Заголовок (INT)")

    meaning_ru = models.CharField(max_length=100, verbose_name="Значение (RU)")
    meaning_ky = models.CharField(max_length=100, verbose_name="Значение (KY)")
    meaning_en = models.CharField(max_length=100 , verbose_name="Знач   ение (EN)")
    class Meta:
        verbose_name = 'Статистика факультета'
        verbose_name_plural = 'Статистика факультетов'
    def __str__(self):
        return f'{self.titleInt} - {self.meaning_ru}'
    def get_meaning(self, language='ru'):
        return getattr(self, f'meaning_{language}', self.meaning_ru)
    
class FacultyPrograms(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='programs')

    emoji= models.CharField(max_length=10, verbose_name="Эмодзи")
    
    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_ky = models.CharField(max_length=100, verbose_name="Название (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="Название (EN)")

    degree_ru = models.CharField(max_length=100, verbose_name="Степень на русском")
    degree_en = models.CharField(max_length=100, verbose_name="Степень на английском")
    degree_ky = models.CharField(max_length=100, verbose_name="Степень на киргизском")

    description_ru = models.TextField(verbose_name='Описание (RU)')
    description_ky = models.TextField(verbose_name='Описание (KY)')
    description_en = models.TextField(verbose_name='Описание (EN)')
    
    duration_years = models.IntegerField(verbose_name="Продолжительность (годы)")
    offline = models.BooleanField(default=True, verbose_name="Очная форма")
    tuition_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Стоимость обучения")
    
    class Meta:
        verbose_name = 'Программа факультета'
        verbose_name_plural = 'Программы факультетов'
    def __str__(self):
        return self.name_ru
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    def get_degree(self, language='ru'):
        return getattr(self, f'degree_{language}', self.degree_ru)

class FacultySpecialization(models.Model):    
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='specializations')

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_ky = models.CharField(max_length=100, verbose_name="Название (KY)")
    name_en = models.CharField(max_length=100, verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name='Описание (RU)')
    description_ky = models.TextField(verbose_name='Описание (KY)')
    description_en = models.TextField(verbose_name='Описание (EN)')
    
    features_ru = models.JSONField(verbose_name='Особенности (RU)')
    features_ky = models.JSONField(verbose_name='Особенности (KY)')
    features_en = models.JSONField(verbose_name='Особенности (EN)')
    
    class Meta:
        verbose_name = 'Специализация факультета'
        verbose_name_plural = 'Специализации факультетов'  

    def __str__(self):
        return self.name_ru 
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    def get_features(self, language='ru'):
        return getattr(self, f'features_{language}', self.features_ru)

class FacultySports(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='sports')

    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_ky = models.CharField(max_length=100, verbose_name="Название (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name='Описание (RU)')
    description_ky = models.TextField(verbose_name='Описание (KY)')
    description_en = models.TextField(verbose_name='Описание (EN)')

    emoji = models.CharField(max_length=10, verbose_name="Эмодзи")
    
    class Meta:
        verbose_name = 'Спорт факультета'
        verbose_name_plural = 'Спорт факультетов'  
    def __str__(self):
        return self.name_ru 
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)

class FacultyTeachers(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='teachers')

    full_name_ru = models.CharField(max_length=100, verbose_name="Полное имя (RU)")
    full_name_ky = models.CharField(max_length=100, verbose_name="Полное имя (KY)")
    full_name_en = models.CharField(max_length=100 , verbose_name="Полное имя (EN)")

    position_ru = models.CharField(max_length=100, verbose_name="Должность (RU)")
    position_ky = models.CharField(max_length=100, verbose_name="Должность (KY)")
    position_en = models.CharField(max_length=100 , verbose_name="Должность (EN)")

    photo = models.ImageField(upload_to='faculty_teachers/', verbose_name="Фото")
    
    class Meta:
        verbose_name = 'Преподаватель факультета'
        verbose_name_plural = 'Преподаватели факультетов'  
    def __str__(self):
        return self.full_name_ru 
    def get_full_name(self, language='ru'):
        return getattr(self, f'full_name_{language}', self.full_name_ru)
    def get_position(self, language='ru'):
        return getattr(self, f'position_{language}', self.position_ru)

class FacultyContacts(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='contacts')

    title_ru = models.CharField(max_length=100, verbose_name="Заголовок (RU)")
    title_ky = models.CharField(max_length=100, verbose_name="Заголовок (KY)")
    title_en = models.CharField(max_length=100 , verbose_name="Заголовок (EN)")

    value = models.CharField(max_length=200, verbose_name="Значение")
    
    class Meta:
        verbose_name = 'Контакт факультета'
        verbose_name_plural = 'Контакты факультетов'  
    def __str__(self):
        return self.title_ru 
    def get_title(self, language='ru'):
        return getattr(self, f'title_{language}', self.title_ru)
    
class Faculty(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name="Название (RU)")
    name_ky = models.CharField(max_length=100, verbose_name="Название (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="Название (EN)")

    description_ru = models.TextField(verbose_name='Описание (RU)')
    description_ky = models.TextField(verbose_name='Описание (KY)')
    description_en = models.TextField(verbose_name='Описание (EN)')

    mission_ru = models.JSONField(verbose_name='Миссия (RU)')
    mission_ky = models.JSONField(verbose_name='Миссия (KY)')
    mission_en = models.JSONField(verbose_name='Миссия (EN)')

    achievements_ru = models.JSONField(verbose_name='Достижения (RU)')
    achievements_ky = models.JSONField(verbose_name='Достижения (KY)')
    achievements_en = models.JSONField(verbose_name='Достижения (EN)')

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'
    def __str__(self):
        return self.name_ru
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    def get_mission(self, language='ru'):
        return getattr(self, f'mission_{language}', self.mission_ru)
    def get_achievements(self, language='ru'):
        return getattr(self, f'achievements_{language}', self.achievements_ru)
    

