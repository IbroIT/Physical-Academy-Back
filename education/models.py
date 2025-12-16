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
