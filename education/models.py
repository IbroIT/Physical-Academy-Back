from django.db import models

# Create your models here.

class MasterPrograms(models.Model):
    emoji = models.CharField(max_length=10, verbose_name="Р­РјРѕРґР·Рё")

    name_ru = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="РќР°Р·РІР°РЅРёРµ (EN)")

    description_ru = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (RU)')
    description_kg = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (KY)')
    description_en = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (EN)')

    features_ru = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (RU)')
    features_kg = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (KY)')
    features_en = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (EN)')

    duration_years = models.IntegerField(verbose_name="РџСЂРѕРґРѕР»Р¶РёС‚РµР»СЊРЅРѕСЃС‚СЊ (РіРѕРґС‹)")
    offline = models.BooleanField(default=True, verbose_name="РћС‡РЅР°СЏ С„РѕСЂРјР°")
    tuition_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="РЎС‚РѕРёРјРѕСЃС‚СЊ РѕР±СѓС‡РµРЅРёСЏ")
    

    class Meta:
        verbose_name = 'РџСЂРѕРіСЂР°РјРјР° РјР°РіРёСЃС‚СЂР°'
        verbose_name_plural = 'РџСЂРѕРіСЂР°РјРјС‹ РјР°РіРёСЃС‚СЂР°'
    def __str__(self):
        return self.name_ru
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    def get_features(self, language='ru'):
        return getattr(self, f'features_{language}', self.features_ru)

class PhdPrograms(models.Model):
    emoji = models.CharField(max_length=10, verbose_name="Р­РјРѕРґР·Рё")

    name_ru = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="РќР°Р·РІР°РЅРёРµ (EN)")

    description_ru = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (RU)')
    description_kg = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (KY)')
    description_en = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (EN)')

    features_ru = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (RU)')
    features_kg = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (KY)')
    features_en = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (EN)')

    duration_years = models.IntegerField(verbose_name="РџСЂРѕРґРѕР»Р¶РёС‚РµР»СЊРЅРѕСЃС‚СЊ (РіРѕРґС‹)")
    offline = models.BooleanField(default=True, verbose_name="РћС‡РЅР°СЏ С„РѕСЂРјР°")
    tuition_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="РЎС‚РѕРёРјРѕСЃС‚СЊ РѕР±СѓС‡РµРЅРёСЏ")
    
    class Meta:
        verbose_name = 'РџСЂРѕРіСЂР°РјРјР° РґРѕРєС‚СѓСЂР°РЅС‚СѓСЂС‹'
        verbose_name_plural = 'РџСЂРѕРіСЂР°РјРјС‹ РґРѕРєС‚СѓСЂР°РЅС‚СѓСЂС‹'
    def __str__(self):
        return self.name_ru
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)
    def get_features(self, language='ru'):
        return getattr(self, f'features_{language}', self.features_ru)


class AboutPhoto(models.Model):
    photo = models.ImageField(upload_to='about_photos/')
    description = models.TextField()
    
class AboutStat(models.Model):
    value = models.IntegerField()
    label = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)
    suffix = models.CharField(max_length=10, blank=True)
    
class AboutFeature(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()

class CollegePrograms(models.Model):
    emoji = models.CharField(max_length=10, verbose_name="Р­РјРѕРґР·Рё")

    name_ru = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="РќР°Р·РІР°РЅРёРµ (EN)")

    description_ru = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (RU)')
    description_kg = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (KY)')
    description_en = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (EN)')

    features_ru = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (RU)')
    features_kg = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (KY)')
    features_en = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (EN)')

    duration_years = models.IntegerField(verbose_name="РџСЂРѕРґРѕР»Р¶РёС‚РµР»СЊРЅРѕСЃС‚СЊ (РіРѕРґС‹)")
    offline = models.BooleanField(default=True, verbose_name="РћС‡РЅР°СЏ С„РѕСЂРјР°")
    tuition_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="РЎС‚РѕРёРјРѕСЃС‚СЊ РѕР±СѓС‡РµРЅРёСЏ")
    
    class Meta:
        verbose_name = 'РџСЂРѕРіСЂР°РјРјР° РєРѕР»Р»РµРґР¶Р°'
        verbose_name_plural = 'РџСЂРѕРіСЂР°РјРјС‹ РєРѕР»Р»РµРґР¶Р°'
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
    
    titleInt = models.CharField(max_length=100, verbose_name="Р—Р°РіРѕР»РѕРІРѕРє (INT)")

    meaning_ru = models.CharField(max_length=100, verbose_name="Р—РЅР°С‡РµРЅРёРµ (RU)")
    meaning_kg = models.CharField(max_length=100, verbose_name="Р—РЅР°С‡РµРЅРёРµ (KY)")
    meaning_en = models.CharField(max_length=100 , verbose_name="Р—РЅР°С‡   РµРЅРёРµ (EN)")
    class Meta:
        verbose_name = 'РЎС‚Р°С‚РёСЃС‚РёРєР° С„Р°РєСѓР»СЊС‚РµС‚Р°'
        verbose_name_plural = 'РЎС‚Р°С‚РёСЃС‚РёРєР° С„Р°РєСѓР»СЊС‚РµС‚РѕРІ'
    def __str__(self):
        return f'{self.titleInt} - {self.meaning_ru}'
    def get_meaning(self, language='ru'):
        return getattr(self, f'meaning_{language}', self.meaning_ru)
    
class FacultyPrograms(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='programs')

    emoji= models.CharField(max_length=10, verbose_name="Р­РјРѕРґР·Рё")
    
    name_ru = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="РќР°Р·РІР°РЅРёРµ (EN)")

    degree_ru = models.CharField(max_length=100, verbose_name="РЎС‚РµРїРµРЅСЊ РЅР° СЂСѓСЃСЃРєРѕРј")
    degree_en = models.CharField(max_length=100, verbose_name="РЎС‚РµРїРµРЅСЊ РЅР° Р°РЅРіР»РёР№СЃРєРѕРј")
    degree_kg = models.CharField(max_length=100, verbose_name="РЎС‚РµРїРµРЅСЊ РЅР° РєРёСЂРіРёР·СЃРєРѕРј")

    description_ru = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (RU)')
    description_kg = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (KY)')
    description_en = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (EN)')
    
    duration_years = models.IntegerField(verbose_name="РџСЂРѕРґРѕР»Р¶РёС‚РµР»СЊРЅРѕСЃС‚СЊ (РіРѕРґС‹)")
    offline = models.BooleanField(default=True, verbose_name="РћС‡РЅР°СЏ С„РѕСЂРјР°")
    tuition_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="РЎС‚РѕРёРјРѕСЃС‚СЊ РѕР±СѓС‡РµРЅРёСЏ")
    
    class Meta:
        verbose_name = 'РџСЂРѕРіСЂР°РјРјР° С„Р°РєСѓР»СЊС‚РµС‚Р°'
        verbose_name_plural = 'РџСЂРѕРіСЂР°РјРјС‹ С„Р°РєСѓР»СЊС‚РµС‚РѕРІ'
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

    name_ru = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (KY)")
    name_en = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (EN)")

    description_ru = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (RU)')
    description_kg = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (KY)')
    description_en = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (EN)')
    
    features_ru = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (RU)')
    features_kg = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (KY)')
    features_en = models.JSONField(verbose_name='РћСЃРѕР±РµРЅРЅРѕСЃС‚Рё (EN)')
    
    class Meta:
        verbose_name = 'РЎРїРµС†РёР°Р»РёР·Р°С†РёСЏ С„Р°РєСѓР»СЊС‚РµС‚Р°'
        verbose_name_plural = 'РЎРїРµС†РёР°Р»РёР·Р°С†РёРё С„Р°РєСѓР»СЊС‚РµС‚РѕРІ'  

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

    name_ru = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="РќР°Р·РІР°РЅРёРµ (EN)")

    description_ru = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (RU)')
    description_kg = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (KY)')
    description_en = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (EN)')

    emoji = models.CharField(max_length=10, verbose_name="Р­РјРѕРґР·Рё")
    
    class Meta:
        verbose_name = 'РЎРїРѕСЂС‚ С„Р°РєСѓР»СЊС‚РµС‚Р°'
        verbose_name_plural = 'РЎРїРѕСЂС‚ С„Р°РєСѓР»СЊС‚РµС‚РѕРІ'  
    def __str__(self):
        return self.name_ru 
    def get_name(self, language='ru'):
        return getattr(self, f'name_{language}', self.name_ru)
    def get_description(self, language='ru'):
        return getattr(self, f'description_{language}', self.description_ru)

class FacultyTeachers(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='teachers')

    full_name_ru = models.CharField(max_length=100, verbose_name="РџРѕР»РЅРѕРµ РёРјСЏ (RU)")
    full_name_kg = models.CharField(max_length=100, verbose_name="РџРѕР»РЅРѕРµ РёРјСЏ (KY)")
    full_name_en = models.CharField(max_length=100 , verbose_name="РџРѕР»РЅРѕРµ РёРјСЏ (EN)")

    position_ru = models.CharField(max_length=100, verbose_name="Р”РѕР»Р¶РЅРѕСЃС‚СЊ (RU)")
    position_kg = models.CharField(max_length=100, verbose_name="Р”РѕР»Р¶РЅРѕСЃС‚СЊ (KY)")
    position_en = models.CharField(max_length=100 , verbose_name="Р”РѕР»Р¶РЅРѕСЃС‚СЊ (EN)")

    photo = models.ImageField(upload_to='faculty_teachers/', verbose_name="Р¤РѕС‚Рѕ")
    
    class Meta:
        verbose_name = 'РџСЂРµРїРѕРґР°РІР°С‚РµР»СЊ С„Р°РєСѓР»СЊС‚РµС‚Р°'
        verbose_name_plural = 'РџСЂРµРїРѕРґР°РІР°С‚РµР»Рё С„Р°РєСѓР»СЊС‚РµС‚РѕРІ'  
    def __str__(self):
        return self.full_name_ru 
    def get_full_name(self, language='ru'):
        return getattr(self, f'full_name_{language}', self.full_name_ru)
    def get_position(self, language='ru'):
        return getattr(self, f'position_{language}', self.position_ru)

class FacultyContacts(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, related_name='contacts')

    title_ru = models.CharField(max_length=100, verbose_name="Р—Р°РіРѕР»РѕРІРѕРє (RU)")
    title_kg = models.CharField(max_length=100, verbose_name="Р—Р°РіРѕР»РѕРІРѕРє (KY)")
    title_en = models.CharField(max_length=100 , verbose_name="Р—Р°РіРѕР»РѕРІРѕРє (EN)")

    value = models.CharField(max_length=200, verbose_name="Р—РЅР°С‡РµРЅРёРµ")
    
    class Meta:
        verbose_name = 'РљРѕРЅС‚Р°РєС‚ С„Р°РєСѓР»СЊС‚РµС‚Р°'
        verbose_name_plural = 'РљРѕРЅС‚Р°РєС‚С‹ С„Р°РєСѓР»СЊС‚РµС‚РѕРІ'  
    def __str__(self):
        return self.title_ru 
    def get_title(self, language='ru'):
        return getattr(self, f'title_{language}', self.title_ru)
    
class Faculty(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (RU)")
    name_kg = models.CharField(max_length=100, verbose_name="РќР°Р·РІР°РЅРёРµ (KY)")
    name_en = models.CharField(max_length=100 , verbose_name="РќР°Р·РІР°РЅРёРµ (EN)")

    description_ru = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (RU)')
    description_kg = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (KY)')
    description_en = models.TextField(verbose_name='РћРїРёСЃР°РЅРёРµ (EN)')

    mission_ru = models.JSONField(verbose_name='РњРёСЃСЃРёСЏ (RU)')
    mission_kg = models.JSONField(verbose_name='РњРёСЃСЃРёСЏ (KY)')
    mission_en = models.JSONField(verbose_name='РњРёСЃСЃРёСЏ (EN)')

    achievements_ru = models.JSONField(verbose_name='Р”РѕСЃС‚РёР¶РµРЅРёСЏ (RU)')
    achievements_kg = models.JSONField(verbose_name='Р”РѕСЃС‚РёР¶РµРЅРёСЏ (KY)')
    achievements_en = models.JSONField(verbose_name='Р”РѕСЃС‚РёР¶РµРЅРёСЏ (EN)')

    class Meta:
        verbose_name = 'Р¤Р°РєСѓР»СЊС‚РµС‚'
        verbose_name_plural = 'Р¤Р°РєСѓР»СЊС‚РµС‚С‹'
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
    


