from django.db import models
from django.core.validators import URLValidator


class DisabilitySupportService(models.Model):
    """Support services for students with disabilities with multilanguage support"""

    # Icons - stored as emoji or class names
    icon = models.CharField(
        max_length=30, default="🌟", verbose_name="Icon (emoji or class)"
    )

    # Order for sorting
    order = models.IntegerField(default=0, verbose_name="Sort Order")

    # Title in three languages
    title_ru = models.CharField(max_length=200, verbose_name="Title (RU)")
    title_en = models.CharField(max_length=200, verbose_name="Title (EN)")
    title_kg = models.CharField(max_length=200, verbose_name="Title (KG)")

    # Description in three languages
    description_ru = models.TextField(verbose_name="Description (RU)")
    description_en = models.TextField(verbose_name="Description (EN)")
    description_kg = models.TextField(verbose_name="Description (KG)")

    # Optional features list in three languages (stored as JSON)
    features_ru = models.TextField(
        blank=True,
        null=True,
        verbose_name="Features (RU)",
        help_text="Enter features separated by new lines",
    )
    features_en = models.TextField(
        blank=True,
        null=True,
        verbose_name="Features (EN)",
        help_text="Enter features separated by new lines",
    )
    features_kg = models.TextField(
        blank=True,
        null=True,
        verbose_name="Features (KG)",
        help_text="Enter features separated by new lines",
    )

    class Meta:
        verbose_name = "Disability Support Service"
        verbose_name_plural = "Disability Support Services"
        ordering = ["order"]

    def __str__(self):
        return self.title_ru

    def get_features_list(self, language="ru"):
        """Get features as a list for the specified language"""
        features_text = getattr(self, f"features_{language}", "") or ""
        if features_text:
            return [feat.strip() for feat in features_text.split("\n") if feat.strip()]
        return []


class DisabilityContactPerson(models.Model):
    """Contact persons for disabilities support with multilanguage support"""

    # Icon
    icon = models.CharField(
        max_length=30, default="👤", verbose_name="Icon (emoji or class)"
    )

    # Contact information
    name_ru = models.CharField(max_length=100, verbose_name="Name (RU)")
    name_en = models.CharField(max_length=100, verbose_name="Name (EN)")
    name_kg = models.CharField(max_length=100, verbose_name="Name (KG)")

    position_ru = models.CharField(max_length=200, verbose_name="Position (RU)")
    position_en = models.CharField(max_length=200, verbose_name="Position (EN)")
    position_kg = models.CharField(max_length=200, verbose_name="Position (KG)")

    phone = models.CharField(max_length=50, verbose_name="Phone Number")
    email = models.EmailField(verbose_name="Email")

    hours_ru = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Office Hours (RU)"
    )
    hours_en = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Office Hours (EN)"
    )
    hours_kg = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Office Hours (KG)"
    )

    location_ru = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Location (RU)"
    )
    location_en = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Location (EN)"
    )
    location_kg = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Location (KG)"
    )

    order = models.IntegerField(default=0, verbose_name="Sort Order")

    class Meta:
        verbose_name = "Disability Contact Person"
        verbose_name_plural = "Disability Contact People"
        ordering = ["order", "name_ru"]

    def __str__(self):
        return self.name_ru


class DisabilityResource(models.Model):
    """Resources for students with disabilities with multilanguage support"""

    RESOURCE_TYPE_CHOICES = [
        ("guide", "Guide"),
        ("tool", "Tool"),
        ("service", "Service"),
        ("document", "Document"),
        ("video", "Video"),
    ]

    FORMAT_CHOICES = [
        ("pdf", "PDF"),
        ("website", "Website"),
        ("app", "Application"),
        ("video", "Video"),
        ("text", "Text"),
    ]

    icon = models.CharField(
        max_length=30, default="📚", verbose_name="Icon (emoji or class)"
    )

    name_ru = models.CharField(max_length=200, verbose_name="Resource Name (RU)")
    name_en = models.CharField(max_length=200, verbose_name="Resource Name (EN)")
    name_kg = models.CharField(max_length=200, verbose_name="Resource Name (KG)")

    description_ru = models.TextField(verbose_name="Description (RU)")
    description_en = models.TextField(verbose_name="Description (EN)")
    description_kg = models.TextField(verbose_name="Description (KG)")

    url = models.URLField(
        max_length=500, validators=[URLValidator()], verbose_name="Resource URL"
    )

    type_ru = models.CharField(
        max_length=30,
        choices=RESOURCE_TYPE_CHOICES,
        default="guide",
        verbose_name="Resource Type (RU)",
    )
    type_en = models.CharField(
        max_length=30,
        choices=RESOURCE_TYPE_CHOICES,
        default="guide",
        verbose_name="Resource Type (EN)",
    )
    type_kg = models.CharField(
        max_length=30,
        choices=RESOURCE_TYPE_CHOICES,
        default="guide",
        verbose_name="Resource Type (KG)",
    )

    format_ru = models.CharField(
        max_length=30,
        choices=FORMAT_CHOICES,
        default="website",
        verbose_name="Format (RU)",
    )
    format_en = models.CharField(
        max_length=30,
        choices=FORMAT_CHOICES,
        default="website",
        verbose_name="Format (EN)",
    )
    format_kg = models.CharField(
        max_length=30,
        choices=FORMAT_CHOICES,
        default="website",
        verbose_name="Format (KG)",
    )

    order = models.IntegerField(default=0, verbose_name="Sort Order")

    class Meta:
        verbose_name = "Disability Resource"
        verbose_name_plural = "Disability Resources"
        ordering = ["order", "name_ru"]

    def __str__(self):
        return self.name_ru


class DisabilityEmergencyContact(models.Model):
    """Emergency contact information for students with disabilities"""

    order = models.PositiveIntegerField(default=0, verbose_name="Display order")
    
    title_ru = models.CharField(max_length=200, verbose_name="Title (RU)")
    title_en = models.CharField(max_length=200, verbose_name="Title (EN)")
    title_kg = models.CharField(max_length=200, verbose_name="Title (KG)")

    description_ru = models.TextField(verbose_name="Description (RU)")
    description_en = models.TextField(verbose_name="Description (EN)")
    description_kg = models.TextField(verbose_name="Description (KG)")

    phone = models.CharField(max_length=50, verbose_name="Emergency Phone")
    phone_link = models.CharField(
        max_length=50, verbose_name="Emergency Phone Link (tel:)"
    )

    class Meta:
        verbose_name = "Disability Emergency Contact"
        verbose_name_plural = "Disability Emergency Contacts"
        ordering = ["order", "title_ru"]

    def __str__(self):
        return self.title_ru
