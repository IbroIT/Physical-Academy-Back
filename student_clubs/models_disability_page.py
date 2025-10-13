from django.db import models


class DisabilityPage(models.Model):
    """Disability page content with multilanguage support"""

    # Title in three languages
    title_ru = models.CharField(max_length=200, verbose_name="Title (RU)")
    title_en = models.CharField(max_length=200, verbose_name="Title (EN)")
    title_kg = models.CharField(max_length=200, verbose_name="Title (KG)")

    # Description in three languages
    description_ru = models.TextField(verbose_name="Description (RU)")
    description_en = models.TextField(verbose_name="Description (EN)")
    description_kg = models.TextField(verbose_name="Description (KG)")

    # Order for sorting
    order = models.IntegerField(default=0, verbose_name="Sort Order")

    class Meta:
        verbose_name = "Disability Page Content"
        verbose_name_plural = "Disability Page Content"
        ordering = ["order", "id"]

    def __str__(self):
        return self.title_ru
