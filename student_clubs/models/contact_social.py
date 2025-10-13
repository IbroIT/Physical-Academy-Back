from django.db import models


class StudentContactInfo(models.Model):
    """Student contact information with multilanguage support"""

    title_ru = models.CharField(max_length=200, verbose_name="Title (RU)")
    title_en = models.CharField(max_length=200, verbose_name="Title (EN)")
    title_kg = models.CharField(max_length=200, verbose_name="Title (KG)")

    description_ru = models.TextField(verbose_name="Description (RU)")
    description_en = models.TextField(verbose_name="Description (EN)")
    description_kg = models.TextField(verbose_name="Description (KG)")

    contact_name_ru = models.CharField(max_length=200, verbose_name="Contact Name (RU)")
    contact_name_en = models.CharField(max_length=200, verbose_name="Contact Name (EN)")
    contact_name_kg = models.CharField(max_length=200, verbose_name="Contact Name (KG)")

    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=50, verbose_name="Phone")

    office_location_ru = models.CharField(
        max_length=200, verbose_name="Office Location (RU)"
    )
    office_location_en = models.CharField(
        max_length=200, verbose_name="Office Location (EN)"
    )
    office_location_kg = models.CharField(
        max_length=200, verbose_name="Office Location (KG)"
    )

    office_hours_ru = models.CharField(max_length=200, verbose_name="Office Hours (RU)")
    office_hours_en = models.CharField(max_length=200, verbose_name="Office Hours (EN)")
    office_hours_kg = models.CharField(max_length=200, verbose_name="Office Hours (KG)")

    is_featured = models.BooleanField(default=False, verbose_name="Featured Contact")
    photo = models.ImageField(
        upload_to="contact_info/", blank=True, null=True, verbose_name="Photo"
    )

    order = models.PositiveSmallIntegerField(default=1, verbose_name="Order")
    is_active = models.BooleanField(default=True, verbose_name="Active")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Student Contact Info"
        verbose_name_plural = "Student Contact Info"
        ordering = ["order"]

    def __str__(self):
        return self.title_ru

    def get_field(self, field_name, language="ru"):
        """Get field value for the specified language"""
        field_with_lang = f"{field_name}_{language}"
        return getattr(self, field_with_lang, getattr(self, f"{field_name}_ru"))


class SocialNetworkAccount(models.Model):
    """Social network accounts for students"""

    NETWORK_CHOICES = [
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("twitter", "Twitter/X"),
        ("telegram", "Telegram"),
        ("whatsapp", "WhatsApp"),
        ("vk", "VKontakte"),
        ("youtube", "YouTube"),
        ("tiktok", "TikTok"),
        ("linkedin", "LinkedIn"),
        ("other", "Other"),
    ]

    network = models.CharField(
        max_length=20,
        choices=NETWORK_CHOICES,
        default="other",
        verbose_name="Social Network",
    )

    name_ru = models.CharField(max_length=200, verbose_name="Account Name (RU)")
    name_en = models.CharField(max_length=200, verbose_name="Account Name (EN)")
    name_kg = models.CharField(max_length=200, verbose_name="Account Name (KG)")

    description_ru = models.TextField(
        blank=True, null=True, verbose_name="Description (RU)"
    )
    description_en = models.TextField(
        blank=True, null=True, verbose_name="Description (EN)"
    )
    description_kg = models.TextField(
        blank=True, null=True, verbose_name="Description (KG)"
    )

    url = models.URLField(verbose_name="Profile URL")
    username = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Username"
    )

    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Icon Class (FontAwesome)",
        help_text="E.g. 'fa-facebook', 'fa-instagram'",
    )

    color_hex = models.CharField(
        max_length=7,
        default="#000000",
        verbose_name="Brand Color (Hex)",
        help_text="E.g. #3b5998 for Facebook",
    )

    is_featured = models.BooleanField(default=False, verbose_name="Featured Account")
    is_official = models.BooleanField(default=True, verbose_name="Official Account")

    order = models.PositiveSmallIntegerField(default=1, verbose_name="Order")
    is_active = models.BooleanField(default=True, verbose_name="Active")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Social Network Account"
        verbose_name_plural = "Social Network Accounts"
        ordering = ["order", "network"]

    def __str__(self):
        return f"{self.get_network_display()}: {self.name_ru}"

    def get_field(self, field_name, language="ru"):
        """Get field value for the specified language"""
        field_with_lang = f"{field_name}_{language}"
        return getattr(self, field_with_lang, getattr(self, f"{field_name}_ru"))


class SocialCommunity(models.Model):
    """Student communities on social networks"""

    title_ru = models.CharField(max_length=200, verbose_name="Community Title (RU)")
    title_en = models.CharField(max_length=200, verbose_name="Community Title (EN)")
    title_kg = models.CharField(max_length=200, verbose_name="Community Title (KG)")

    description_ru = models.TextField(verbose_name="Description (RU)")
    description_en = models.TextField(verbose_name="Description (EN)")
    description_kg = models.TextField(verbose_name="Description (KG)")

    members_count = models.PositiveIntegerField(default=0, verbose_name="Members Count")
    posts_count = models.PositiveIntegerField(default=0, verbose_name="Posts Count")

    network = models.CharField(
        max_length=20,
        choices=SocialNetworkAccount.NETWORK_CHOICES,
        default="other",
        verbose_name="Social Network",
    )

    url = models.URLField(verbose_name="Community URL")

    banner_image = models.ImageField(
        upload_to="social_communities/",
        blank=True,
        null=True,
        verbose_name="Banner Image",
    )

    is_featured = models.BooleanField(default=False, verbose_name="Featured Community")
    is_verified = models.BooleanField(default=False, verbose_name="Verified Community")

    order = models.PositiveSmallIntegerField(default=1, verbose_name="Order")
    is_active = models.BooleanField(default=True, verbose_name="Active")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Social Community"
        verbose_name_plural = "Social Communities"
        ordering = ["order", "-members_count"]

    def __str__(self):
        return self.title_ru

    def get_field(self, field_name, language="ru"):
        """Get field value for the specified language"""
        field_with_lang = f"{field_name}_{language}"
        return getattr(self, field_with_lang, getattr(self, f"{field_name}_ru"))
