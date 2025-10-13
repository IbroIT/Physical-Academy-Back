from django.db import models
from django.utils.translation import gettext_lazy as _


class NTSCommitteeSection(models.Model):
    """Model for NTS Committee page sections with translations"""

    section_key = models.CharField(_("Section Key"), max_length=100, unique=True)

    title_ru = models.CharField(_("Title (Russian)"), max_length=200)
    title_en = models.CharField(_("Title (English)"), max_length=200, blank=True)
    title_kg = models.CharField(_("Title (Kyrgyz)"), max_length=200, blank=True)

    description_ru = models.TextField(_("Description (Russian)"))
    description_en = models.TextField(_("Description (English)"), blank=True)
    description_kg = models.TextField(_("Description (Kyrgyz)"), blank=True)

    class Meta:
        verbose_name = _("NTS Committee Section")
        verbose_name_plural = _("NTS Committee Sections")

    def __str__(self):
        return f"{self.section_key}: {self.title_ru}"

    def get_title(self, language="ru"):
        """Return the title in the specified language"""
        return getattr(self, f"title_{language}", self.title_ru)

    def get_description(self, language="ru"):
        """Return the description in the specified language"""
        return getattr(self, f"description_{language}", self.description_ru)


class NTSCommitteeRole(models.Model):
    """Model for NTS Committee roles"""

    name_ru = models.CharField(_("Name (Russian)"), max_length=100)
    name_en = models.CharField(_("Name (English)"), max_length=100, blank=True)
    name_kg = models.CharField(_("Name (Kyrgyz)"), max_length=100, blank=True)
    description_ru = models.TextField(_("Description (Russian)"), blank=True)
    description_en = models.TextField(_("Description (English)"), blank=True)
    description_kg = models.TextField(_("Description (Kyrgyz)"), blank=True)

    class Meta:
        verbose_name = _("NTS Committee Role")
        verbose_name_plural = _("NTS Committee Roles")

    def __str__(self):
        return self.name_ru

    def get_name(self, language="ru"):
        """Return the name in the specified language"""
        return getattr(self, f"name_{language}", self.name_ru)

    def get_description(self, language="ru"):
        """Return the description in the specified language"""
        return getattr(self, f"description_{language}", self.description_ru)


class NTSResearchDirection(models.Model):
    """Model for NTS Committee research directions"""

    name_ru = models.CharField(_("Name (Russian)"), max_length=200)
    name_en = models.CharField(_("Name (English)"), max_length=200, blank=True)
    name_kg = models.CharField(_("Name (Kyrgyz)"), max_length=200, blank=True)
    description_ru = models.TextField(_("Description (Russian)"), blank=True)
    description_en = models.TextField(_("Description (English)"), blank=True)
    description_kg = models.TextField(_("Description (Kyrgyz)"), blank=True)

    class Meta:
        verbose_name = _("NTS Research Direction")
        verbose_name_plural = _("NTS Research Directions")

    def __str__(self):
        return self.name_ru

    def get_name(self, language="ru"):
        """Return the name in the specified language"""
        return getattr(self, f"name_{language}", self.name_ru)

    def get_description(self, language="ru"):
        """Return the description in the specified language"""
        return getattr(self, f"description_{language}", self.description_ru)


class NTSCommitteeMember(models.Model):
    """Model for NTS Committee members"""

    name_ru = models.CharField(_("Name (Russian)"), max_length=100)
    name_en = models.CharField(_("Name (English)"), max_length=100, blank=True)
    name_kg = models.CharField(_("Name (Kyrgyz)"), max_length=100, blank=True)

    role = models.ForeignKey(
        NTSCommitteeRole, on_delete=models.CASCADE, related_name="members"
    )
    research_direction = models.ForeignKey(
        NTSResearchDirection, on_delete=models.CASCADE, related_name="members"
    )

    position_ru = models.CharField(_("Position (Russian)"), max_length=200)
    position_en = models.CharField(_("Position (English)"), max_length=200, blank=True)
    position_kg = models.CharField(_("Position (Kyrgyz)"), max_length=200, blank=True)

    bio_ru = models.TextField(_("Biography (Russian)"), blank=True)
    bio_en = models.TextField(_("Biography (English)"), blank=True)
    bio_kg = models.TextField(_("Biography (Kyrgyz)"), blank=True)

    email = models.EmailField(_("Email"), blank=True)
    phone = models.CharField(_("Phone"), max_length=50, blank=True)
    photo = models.ImageField(_("Photo"), upload_to="nts_committee/", blank=True)

    is_active = models.BooleanField(_("Is Active"), default=True)
    order = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("NTS Committee Member")
        verbose_name_plural = _("NTS Committee Members")
        ordering = ["order", "name_ru"]

    def __str__(self):
        return f"{self.name_ru} - {self.role}"

    def get_name(self, language="ru"):
        """Return the name in the specified language"""
        return getattr(self, f"name_{language}", self.name_ru)

    def get_position(self, language="ru"):
        """Return the position in the specified language"""
        return getattr(self, f"position_{language}", self.position_ru)

    def get_bio(self, language="ru"):
        """Return the bio in the specified language"""
        return getattr(self, f"bio_{language}", self.bio_ru)
