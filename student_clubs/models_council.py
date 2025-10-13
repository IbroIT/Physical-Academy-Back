from django.db import models
from django.core.validators import URLValidator


class CouncilMember(models.Model):
    """Student council member with multilanguage support"""

    ROLE_CHOICES = [
        ("president", "President"),
        ("vice_president", "Vice President"),
        ("secretary", "Secretary"),
        ("treasurer", "Treasurer"),
        ("member", "Member"),
    ]

    # Basic information
    avatar = models.ImageField(
        upload_to="student_council/members/",
        blank=True,
        null=True,
        verbose_name="Avatar",
    )
    order = models.IntegerField(default=0, verbose_name="Sort Order")
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default="member", verbose_name="Role"
    )

    # Name and position in three languages
    name_ru = models.CharField(max_length=100, verbose_name="Name (RU)")
    name_en = models.CharField(max_length=100, verbose_name="Name (EN)")
    name_kg = models.CharField(max_length=100, verbose_name="Name (KG)")

    position_ru = models.CharField(max_length=200, verbose_name="Position (RU)")
    position_en = models.CharField(max_length=200, verbose_name="Position (EN)")
    position_kg = models.CharField(max_length=200, verbose_name="Position (KG)")

    department_ru = models.CharField(max_length=200, verbose_name="Department (RU)")
    department_en = models.CharField(max_length=200, verbose_name="Department (EN)")
    department_kg = models.CharField(max_length=200, verbose_name="Department (KG)")

    # Contact information
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name="Phone")

    # Social media links
    instagram = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="Instagram",
    )
    linkedin = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="LinkedIn",
    )

    # Bio in three languages
    bio_ru = models.TextField(blank=True, null=True, verbose_name="Biography (RU)")
    bio_en = models.TextField(blank=True, null=True, verbose_name="Biography (EN)")
    bio_kg = models.TextField(blank=True, null=True, verbose_name="Biography (KG)")

    # Accomplishments in three languages
    achievements_ru = models.TextField(
        blank=True, null=True, verbose_name="Achievements (RU)"
    )
    achievements_en = models.TextField(
        blank=True, null=True, verbose_name="Achievements (EN)"
    )
    achievements_kg = models.TextField(
        blank=True, null=True, verbose_name="Achievements (KG)"
    )

    class Meta:
        verbose_name = "Student Council Member"
        verbose_name_plural = "Student Council Members"
        ordering = ["order", "role", "name_ru"]

    def __str__(self):
        return f"{self.name_ru} ({self.get_role_display()})"


class CouncilInitiative(models.Model):
    """Student council initiatives with multilanguage support"""

    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    # Basic information
    icon = models.CharField(
        max_length=30, default="🚀", verbose_name="Icon (emoji or class)"
    )
    order = models.IntegerField(default=0, verbose_name="Sort Order")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="in_progress",
        verbose_name="Status",
    )

    # Title and description in three languages
    title_ru = models.CharField(max_length=200, verbose_name="Title (RU)")
    title_en = models.CharField(max_length=200, verbose_name="Title (EN)")
    title_kg = models.CharField(max_length=200, verbose_name="Title (KG)")

    description_ru = models.TextField(verbose_name="Description (RU)")
    description_en = models.TextField(verbose_name="Description (EN)")
    description_kg = models.TextField(verbose_name="Description (KG)")

    # Goals in three languages
    goals_ru = models.TextField(blank=True, null=True, verbose_name="Goals (RU)")
    goals_en = models.TextField(blank=True, null=True, verbose_name="Goals (EN)")
    goals_kg = models.TextField(blank=True, null=True, verbose_name="Goals (KG)")

    # Dates
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")

    # Lead members (optional)
    lead_members = models.ManyToManyField(
        CouncilMember,
        blank=True,
        related_name="led_initiatives",
        verbose_name="Lead Members",
    )

    class Meta:
        verbose_name = "Student Council Initiative"
        verbose_name_plural = "Student Council Initiatives"
        ordering = ["order", "status", "start_date"]

    def __str__(self):
        return self.title_ru


class CouncilEvent(models.Model):
    """Student council events with multilanguage support"""

    STATUS_CHOICES = [
        ("upcoming", "Upcoming"),
        ("ongoing", "Ongoing"),
        ("past", "Past"),
    ]

    # Basic information
    icon = models.CharField(
        max_length=30, default="📅", verbose_name="Icon (emoji or class)"
    )
    order = models.IntegerField(default=0, verbose_name="Sort Order")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="upcoming", verbose_name="Status"
    )

    # Title and description in three languages
    title_ru = models.CharField(max_length=200, verbose_name="Title (RU)")
    title_en = models.CharField(max_length=200, verbose_name="Title (EN)")
    title_kg = models.CharField(max_length=200, verbose_name="Title (KG)")

    description_ru = models.TextField(verbose_name="Description (RU)")
    description_en = models.TextField(verbose_name="Description (EN)")
    description_kg = models.TextField(verbose_name="Description (KG)")

    # Date and location
    date = models.DateTimeField(verbose_name="Event Date and Time")

    location_ru = models.CharField(max_length=200, verbose_name="Location (RU)")
    location_en = models.CharField(max_length=200, verbose_name="Location (EN)")
    location_kg = models.CharField(max_length=200, verbose_name="Location (KG)")

    # Optional registration link
    registration_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="Registration Link",
    )

    # Optional image
    image = models.ImageField(
        upload_to="student_council/events/",
        blank=True,
        null=True,
        verbose_name="Event Image",
    )

    # Related initiative (optional)
    initiative = models.ForeignKey(
        CouncilInitiative,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="events",
        verbose_name="Related Initiative",
    )

    class Meta:
        verbose_name = "Student Council Event"
        verbose_name_plural = "Student Council Events"
        ordering = ["order", "status", "date"]

    def __str__(self):
        return self.title_ru


class CouncilStats(models.Model):
    """Statistics for student council with multilanguage support"""

    # Statistics key
    key = models.CharField(max_length=50, unique=True, verbose_name="Statistic Key")

    # Value
    value = models.CharField(max_length=50, verbose_name="Statistic Value")

    # Labels in three languages
    label_ru = models.CharField(max_length=100, verbose_name="Label (RU)")
    label_en = models.CharField(max_length=100, verbose_name="Label (EN)")
    label_kg = models.CharField(max_length=100, verbose_name="Label (KG)")

    order = models.IntegerField(default=0, verbose_name="Sort Order")

    class Meta:
        verbose_name = "Student Council Statistic"
        verbose_name_plural = "Student Council Statistics"
        ordering = ["order"]

    def __str__(self):
        return f"{self.key}: {self.value}"
