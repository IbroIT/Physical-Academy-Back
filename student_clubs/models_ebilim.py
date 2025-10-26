# COMMENTED OUT: Ebilim backend not needed - using i18n translations on frontend instead

"""
from django.db import models
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _


class EbilimStat(models.Model):
    key = models.CharField(_("Key"), max_length=100)
    value = models.CharField(_("Value"), max_length=100)
    label_ru = models.CharField(_("Label (Russian)"), max_length=200)
    label_en = models.CharField(_("Label (English)"), max_length=200)
    label_kg = models.CharField(_("Label (Kyrgyz)"), max_length=200)
    order = models.IntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = "E-learning Statistic"
        verbose_name_plural = "E-learning Statistics"
        ordering = ["order"]

    def __str__(self):
        return f"{self.key}: {self.value}"


class EbilimQuickLink(models.Model):
    name_ru = models.CharField(_("Name (Russian)"), max_length=200)
    name_en = models.CharField(_("Name (English)"), max_length=200)
    name_kg = models.CharField(_("Name (Kyrgyz)"), max_length=200)
    url = models.URLField(_("URL"), validators=[URLValidator()])
    icon = models.CharField(_("Icon"), max_length=50, help_text="Emoji or icon code")
    order = models.IntegerField(_("Order"), default=0)
    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        verbose_name = "E-learning Quick Link"
        verbose_name_plural = "E-learning Quick Links"
        ordering = ["order"]

    def __str__(self):
        return self.name_en


class EbilimSystemStatus(models.Model):
    STATUS_CHOICES = [
        ("online", "Online"),
        ("maintenance", "Maintenance"),
        ("issues", "Issues"),
    ]

    status = models.CharField(
        _("Status"), max_length=20, choices=STATUS_CHOICES, default="online"
    )
    last_update = models.DateTimeField(_("Last Update"), auto_now=True)
    message_ru = models.CharField(_("Status Message (Russian)"), max_length=200)
    message_en = models.CharField(_("Status Message (English)"), max_length=200)
    message_kg = models.CharField(_("Status Message (Kyrgyz)"), max_length=200)
    support_email = models.EmailField(_("Support Email"), blank=True)
    support_phone = models.CharField(_("Support Phone"), max_length=50, blank=True)

    class Meta:
        verbose_name = "E-learning System Status"
        verbose_name_plural = "E-learning System Statuses"

    def __str__(self):
        return f"System Status: {self.get_status_display()}"
"""
