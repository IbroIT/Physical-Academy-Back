from django.db import models


class InstructionCategory(models.Model):
    """Categories for instruction documents"""

    name_ru = models.CharField(max_length=100, verbose_name="Name (RU)")
    name_en = models.CharField(max_length=100, verbose_name="Name (EN)")
    name_kg = models.CharField(max_length=100, verbose_name="Name (KG)")
    code = models.CharField(max_length=50, unique=True, verbose_name="Category Code")
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = "Instruction Category"
        verbose_name_plural = "Instruction Categories"
        ordering = ["order"]


class InstructionDocument(models.Model):
    """Academic instruction documents"""

    # Basic info
    name_ru = models.CharField(max_length=255, verbose_name="Name (RU)")
    name_en = models.CharField(max_length=255, verbose_name="Name (EN)")
    name_kg = models.CharField(max_length=255, verbose_name="Name (KG)")

    description_ru = models.TextField(verbose_name="Description (RU)")
    description_en = models.TextField(verbose_name="Description (EN)")
    description_kg = models.TextField(verbose_name="Description (KG)")

    category = models.ForeignKey(
        InstructionCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="documents",
        verbose_name="Category",
    )

    # File details
    FORMAT_CHOICES = [
        ("PDF", "PDF"),
        ("DOC", "DOC"),
        ("DOCX", "DOCX"),
        ("XLS", "XLS"),
        ("XLSX", "XLSX"),
        ("PPT", "PPT"),
        ("PPTX", "PPTX"),
        ("ZIP", "ZIP"),
    ]
    format = models.CharField(
        max_length=10, choices=FORMAT_CHOICES, verbose_name="File Format"
    )
    file = models.FileField(upload_to="instructions/", verbose_name="Document File")
    size = models.CharField(
        max_length=20, help_text="File size (e.g., '2.5 MB')", verbose_name="File Size"
    )
    version = models.CharField(max_length=20, default="1.0", verbose_name="Version")
    pages = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Number of Pages"
    )

    # Stats
    downloads = models.PositiveIntegerField(default=0, verbose_name="Download Count")

    # Tags
    tags = models.JSONField(
        default=list, blank=True, help_text="List of tags", verbose_name="Tags"
    )

    # Metadata
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = "Instruction Document"
        verbose_name_plural = "Instruction Documents"
        ordering = ["order", "-updated_at"]


class ImportantUpdate(models.Model):
    """Important updates for instructions page"""

    title_ru = models.CharField(max_length=255, verbose_name="Title (RU)")
    title_en = models.CharField(max_length=255, verbose_name="Title (EN)")
    title_kg = models.CharField(max_length=255, verbose_name="Title (KG)")

    description_ru = models.TextField(verbose_name="Description (RU)")
    description_en = models.TextField(verbose_name="Description (EN)")
    description_kg = models.TextField(verbose_name="Description (KG)")

    date = models.CharField(
        max_length=100,
        help_text="Display date (e.g., 'Oct 15, 2023')",
        verbose_name="Display Date",
    )

    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")
    actual_date = models.DateTimeField(verbose_name="Actual Date")

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = "Important Update"
        verbose_name_plural = "Important Updates"
        ordering = ["order", "-actual_date"]
