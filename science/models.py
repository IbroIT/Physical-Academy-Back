from django.db import models
from django.utils.translation import gettext_lazy as _

# Import models from separate files
from .scopus import (
    ScopusMetrics,
    ScopusDocumentType,
    ScopusPublication,
    ScopusStats,
    ScopusSection,
)

# Also import Scopus models added to scopus.py so they are available via science.models
from .scopus import (
    ScopusAuthor,
    ScopusPublicationAuthor,
    ScopusJournal,
    ScopusPublisher,
)


# Scientific Direction model
class ScientificDirection(models.Model):
    """Model for scientific research directions"""

    name_ru = models.CharField(_("Name (Russian)"), max_length=255)
    name_en = models.CharField(_("Name (English)"), max_length=255, blank=True)
    name_kg = models.CharField(_("Name (Kyrgyz)"), max_length=255, blank=True)

    description_ru = models.TextField(_("Description (Russian)"))
    description_en = models.TextField(_("Description (English)"), blank=True)
    description_kg = models.TextField(_("Description (Kyrgyz)"), blank=True)

    is_active = models.BooleanField(_("Active"), default=True)
    order = models.IntegerField(_("Order"), default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Scientific Direction")
        verbose_name_plural = _("Scientific Directions")
        ordering = ["order", "name_ru"]

    def __str__(self):
        return self.name_ru

    def get_name(self):
        return self.name_ru

    def get_description(self):
        return self.description_ru


# Dissertation models
class DissertationSpecialization(models.Model):
    """Model for dissertation specializations"""

    code = models.CharField(_("Specialization Code"), max_length=20)
    name_ru = models.CharField(_("Name (Russian)"), max_length=255)
    name_en = models.CharField(_("Name (English)"), max_length=255, blank=True)
    name_kg = models.CharField(_("Name (Kyrgyz)"), max_length=255, blank=True)

    degree_ru = models.CharField(_("Degree (Russian)"), max_length=100)
    degree_en = models.CharField(_("Degree (English)"), max_length=100, blank=True)
    degree_kg = models.CharField(_("Degree (Kyrgyz)"), max_length=100, blank=True)

    class Meta:
        verbose_name = _("Dissertation Specialization")
        verbose_name_plural = _("Dissertation Specializations")
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name_ru}"

    def get_name(self):
        return self.name_ru

    def get_degree(self):
        return self.degree_ru


class DissertationSecretary(models.Model):
    """Model for dissertation council secretary"""

    name_ru = models.CharField(_("Full Name (Russian)"), max_length=255)
    name_en = models.CharField(_("Full Name (English)"), max_length=255, blank=True)
    name_kg = models.CharField(_("Full Name (Kyrgyz)"), max_length=255, blank=True)

    position_ru = models.CharField(_("Position (Russian)"), max_length=255)
    position_en = models.CharField(_("Position (English)"), max_length=255, blank=True)
    position_kg = models.CharField(_("Position (Kyrgyz)"), max_length=255, blank=True)

    bio_ru = models.TextField(_("Bio (Russian)"))
    bio_en = models.TextField(_("Bio (English)"), blank=True)
    bio_kg = models.TextField(_("Bio (Kyrgyz)"), blank=True)

    email = models.EmailField(_("Email"), blank=True)
    phone = models.CharField(_("Phone"), max_length=20, blank=True)
    photo = models.ImageField(
        _("Photo"), upload_to="dissertation/secretary/", blank=True, null=True
    )

    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        verbose_name = _("Dissertation Secretary")
        verbose_name_plural = _("Dissertation Secretaries")

    def __str__(self):
        return self.name_ru

    def get_name(self):
        return self.name_ru

    def get_position(self):
        return self.position_ru

    def get_bio(self):
        return self.bio_ru


class DissertationCouncil(models.Model):
    """Model for dissertation councils"""

    name_ru = models.CharField(_("Name (Russian)"), max_length=255)
    name_en = models.CharField(_("Name (English)"), max_length=255, blank=True)
    name_kg = models.CharField(_("Name (Kyrgyz)"), max_length=255, blank=True)

    description_ru = models.TextField(_("Description (Russian)"))
    description_en = models.TextField(_("Description (English)"), blank=True)
    description_kg = models.TextField(_("Description (Kyrgyz)"), blank=True)

    secretary = models.ForeignKey(
        DissertationSecretary, on_delete=models.PROTECT, related_name="councils"
    )
    specializations = models.ManyToManyField(
        DissertationSpecialization, related_name="councils"
    )

    order_number = models.CharField(_("Order Number"), max_length=50)
    from_date = models.DateField(_("Active From"))
    to_date = models.DateField(_("Active To"))

    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        verbose_name = _("Dissertation Council")
        verbose_name_plural = _("Dissertation Councils")

    def __str__(self):
        return self.name_ru

    def get_name(self):
        return self.name_ru

    def get_description(self):
        return self.description_ru


class DissertationCouncilDocuments(models.Model):
    """Model for dissertation council documents"""

    name_ru = models.CharField(_("Document Name (Russian)"), max_length=255)
    name_en = models.CharField(_("Document Name (English)"), max_length=255, blank=True)
    name_kg = models.CharField(_("Document Name (Kyrgyz)"), max_length=255, blank=True)

    description_ru = models.TextField(_("Description (Russian)"), blank=True)
    description_en = models.TextField(_("Description (English)"), blank=True)
    description_kg = models.TextField(_("Description (Kyrgyz)"), blank=True)

    file = models.FileField(_("Document File"), upload_to="dissertation/documents/")
    is_active = models.BooleanField(_("Active"), default=True)

    council = models.ForeignKey(
        DissertationCouncil,
        on_delete=models.CASCADE,
        related_name="documents",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Dissertation Council Document")
        verbose_name_plural = _("Dissertation Council Documents")

    def __str__(self):
        return self.name_ru

    def get_name(self):
        return self.name_ru

    def get_description(self):
        return self.description_ru


class DissertationCouncilAdminStaff(models.Model):
    """Model for dissertation council administrative staff members"""

    name_ru = models.CharField(_("Full Name (Russian)"), max_length=255)
    name_en = models.CharField(_("Full Name (English)"), max_length=255, blank=True)
    name_kg = models.CharField(_("Full Name (Kyrgyz)"), max_length=255, blank=True)

    position_ru = models.CharField(_("Position (Russian)"), max_length=255)
    position_en = models.CharField(_("Position (English)"), max_length=255, blank=True)
    position_kg = models.CharField(_("Position (Kyrgyz)"), max_length=255, blank=True)

    bio_ru = models.TextField(_("Bio (Russian)"), blank=True)
    bio_en = models.TextField(_("Bio (English)"), blank=True)
    bio_kg = models.TextField(_("Bio (Kyrgyz)"), blank=True)

    email = models.EmailField(_("Email"), blank=True)
    phone = models.CharField(_("Phone"), max_length=20, blank=True)
    photo = models.ImageField(
        _("Photo"), upload_to="dissertation/staff/", blank=True, null=True
    )

    council = models.ForeignKey(
        DissertationCouncil, on_delete=models.CASCADE, related_name="admin_staff"
    )
    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        verbose_name = _("Council Admin Staff")
        verbose_name_plural = _("Council Admin Staff")

    def __str__(self):
        return self.name_ru

    def get_name(self):
        return self.name_ru

    def get_position(self):
        return self.position_ru

    def get_bio(self):
        return self.bio_ru

    def get_bio(self):
        return self.bio_ru


from .nts_committee import (
    NTSCommitteeRole,
    NTSResearchDirection,
    NTSCommitteeMember,
    NTSCommitteeSection,
)


class Publication(models.Model):
    """Model for scientific publications"""

    title_ru = models.CharField(_("Title (Russian)"), max_length=500)
    title_en = models.CharField(_("Title (English)"), max_length=500, blank=True)
    title_kg = models.CharField(_("Title (Kyrgyz)"), max_length=500, blank=True)

    author_ru = models.CharField(_("Author (Russian)"), max_length=500, default="")
    author_en = models.CharField(
        _("Author (English)"), max_length=500, blank=True, default=""
    )
    author_kg = models.CharField(
        _("Author (Kyrgyz)"), max_length=500, blank=True, default=""
    )

    journal = models.CharField(_("Journal/Conference"), max_length=255)
    year = models.IntegerField(_("Publication Year"))
    publication_date = models.DateField(_("Publication Date"), null=True, blank=True)
    citation_count = models.IntegerField(_("Citation Count"), default=0)
    impact_factor = models.FloatField(_("Impact Factor"), null=True, blank=True)

    abstract_ru = models.TextField(_("Abstract (Russian)"))
    abstract_en = models.TextField(_("Abstract (English)"), blank=True)
    abstract_kg = models.TextField(_("Abstract (Kyrgyz)"), blank=True)

    doi = models.CharField(_("DOI"), max_length=100, blank=True)
    url = models.URLField(_("External URL"), blank=True)
    pdf_file = models.FileField(_("PDF File"), upload_to="publications/", blank=True)
    image = models.ImageField(
        _("Publication Cover Image"),
        upload_to="publications/images/",
        blank=True,
        null=True,
    )

    publication_type = models.CharField(
        _("Publication Type"),
        max_length=50,
        choices=[
            ("article", _("Journal Article")),
            ("conference", _("Conference Paper")),
            ("book", _("Book/Chapter")),
            ("patent", _("Patent")),
        ],
        default="article",
    )
    is_featured = models.BooleanField(_("Featured"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)
    order = models.IntegerField(_("Order"), default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-year", "-order", "title_ru"]
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")

    def __str__(self):
        return f"{self.title_ru} ({self.year})"


class PublicationTypeOptions:
    """Helper to map publication_type keys to human-readable labels.

    Used by serializers as PublicationTypeOptions(obj.pub_type).label
    """

    _choices = {
        "article": _("Journal Article"),
        "conference": _("Conference Paper"),
        "book": _("Book/Chapter"),
        "patent": _("Patent"),
    }

    def __init__(self, key):
        self.key = key
        self.label = self._choices.get(key, str(key))


class PublicationStats(models.Model):
    """Statistics for publications page"""

    label_ru = models.CharField(_("Label (Russian)"), max_length=255)
    label_en = models.CharField(_("Label (English)"), max_length=255, blank=True)
    label_kg = models.CharField(_("Label (Kyrgyz)"), max_length=255, blank=True)

    value = models.IntegerField(_("Value"))
    icon = models.CharField(_("Icon Class"), max_length=50, blank=True)
    order = models.IntegerField(_("Order"), default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = _("Publication Statistic")
        verbose_name_plural = _("Publication Statistics")

    def __str__(self):
        return f"{self.label_ru}: {self.value}"


class VestnikIssue(models.Model):
    """Model for Vestnik journal issues"""

    title_ru = models.CharField(_("Title (Russian)"), max_length=500)
    title_en = models.CharField(_("Title (English)"), max_length=500, blank=True)
    title_kg = models.CharField(_("Title (Kyrgyz)"), max_length=500, blank=True)

    description_ru = models.TextField(_("Description (Russian)"))
    description_en = models.TextField(_("Description (English)"), blank=True)
    description_kg = models.TextField(_("Description (Kyrgyz)"), blank=True)

    volume_number = models.IntegerField(_("Volume Number"))
    issue_number = models.IntegerField(_("Issue Number"))
    year = models.IntegerField(_("Year"))
    publication_date = models.DateField(_("Publication Date"))

    cover_image = models.ImageField(
        _("Cover Image"), upload_to="vestnik/covers/", blank=True, null=True
    )
    pdf_file = models.FileField(_("PDF File"), upload_to="vestnik/issues/", blank=True)

    issn_print = models.CharField(_("ISSN (Print)"), max_length=20, blank=True)
    issn_online = models.CharField(_("ISSN (Online)"), max_length=20, blank=True)
    doi_prefix = models.CharField(_("DOI Prefix"), max_length=100, blank=True)

    is_featured = models.BooleanField(_("Featured"), default=False)
    is_published = models.BooleanField(_("Published"), default=True)
    order = models.IntegerField(_("Order"), default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-year", "-volume_number", "-issue_number", "order"]
        verbose_name = _("Vestnik Issue")
        verbose_name_plural = _("Vestnik Issues")
        unique_together = ["volume_number", "issue_number", "year"]

    def __str__(self):
        return f"Vestnik Vol.{self.volume_number} №{self.issue_number} ({self.year})"


class VestnikArticle(models.Model):
    """Model for articles within Vestnik issues"""

    issue = models.ForeignKey(
        VestnikIssue, on_delete=models.CASCADE, related_name="articles"
    )

    title_ru = models.CharField(_("Title (Russian)"), max_length=500)
    title_en = models.CharField(_("Title (English)"), max_length=500, blank=True)
    title_kg = models.CharField(_("Title (Kyrgyz)"), max_length=500, blank=True)

    author_ru = models.CharField(_("Authors (Russian)"), max_length=500)
    author_en = models.CharField(_("Authors (English)"), max_length=500, blank=True)
    author_kg = models.CharField(_("Authors (Kyrgyz)"), max_length=500, blank=True)

    abstract_ru = models.TextField(_("Abstract (Russian)"))
    abstract_en = models.TextField(_("Abstract (English)"), blank=True)
    abstract_kg = models.TextField(_("Abstract (Kyrgyz)"), blank=True)

    keywords_ru = models.TextField(
        _("Keywords (Russian)"), help_text="Comma-separated keywords", blank=True
    )
    keywords_en = models.TextField(
        _("Keywords (English)"), help_text="Comma-separated keywords", blank=True
    )
    keywords_kg = models.TextField(
        _("Keywords (Kyrgyz)"), help_text="Comma-separated keywords", blank=True
    )

    pages_from = models.IntegerField(_("Page From"))
    pages_to = models.IntegerField(_("Page To"))

    doi = models.CharField(_("DOI"), max_length=100, blank=True)
    pdf_file = models.FileField(
        _("Article PDF"), upload_to="vestnik/articles/", blank=True
    )

    article_type = models.CharField(
        _("Article Type"),
        max_length=50,
        choices=[
            ("research", _("Research Article")),
            ("review", _("Review Article")),
            ("case_study", _("Case Study")),
            ("editorial", _("Editorial")),
            ("letter", _("Letter to Editor")),
        ],
        default="research",
    )

    citation_count = models.IntegerField(_("Citation Count"), default=0)
    order = models.IntegerField(_("Order in Issue"), default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["issue", "order", "pages_from"]
        verbose_name = _("Vestnik Article")
        verbose_name_plural = _("Vestnik Articles")

    def __str__(self):
        return f"{self.title_ru} - {self.issue}"

    @property
    def page_range(self):
        return f"{self.pages_from}-{self.pages_to}"


class VestnikStats(models.Model):
    """Statistics for Vestnik page"""

    label_ru = models.CharField(_("Label (Russian)"), max_length=255)
    label_en = models.CharField(_("Label (English)"), max_length=255, blank=True)
    label_kg = models.CharField(_("Label (Kyrgyz)"), max_length=255, blank=True)

    value = models.IntegerField(_("Value"))
    icon = models.CharField(_("Icon Class"), max_length=50, blank=True)
    order = models.IntegerField(_("Order"), default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = _("Vestnik Statistic")
        verbose_name_plural = _("Vestnik Statistics")

    def __str__(self):
        return f"{self.label_ru}: {self.value}"


class DissertationDefense(models.Model):
    """Model for dissertation defense information"""

    title_ru = models.CharField(_("Dissertation Title (Russian)"), max_length=500)
    title_en = models.CharField(
        _("Dissertation Title (English)"), max_length=500, blank=True
    )
    title_kg = models.CharField(
        _("Dissertation Title (Kyrgyz)"), max_length=500, blank=True
    )

    applicant_ru = models.CharField(_("Applicant Name (Russian)"), max_length=255)
    applicant_en = models.CharField(
        _("Applicant Name (English)"), max_length=255, blank=True
    )
    applicant_kg = models.CharField(
        _("Applicant Name (Kyrgyz)"), max_length=255, blank=True
    )

    abstract_ru = models.TextField(_("Abstract (Russian)"))
    abstract_en = models.TextField(_("Abstract (English)"), blank=True)
    abstract_kg = models.TextField(_("Abstract (Kyrgyz)"), blank=True)

    specializations = models.ManyToManyField(
        DissertationSpecialization, related_name="defenses"
    )
    defense_date = models.DateTimeField(_("Defense Date and Time"))

    council = models.ForeignKey(
        DissertationCouncil, on_delete=models.PROTECT, related_name="defenses"
    )

    dissertation_file = models.FileField(
        _("Dissertation File"), upload_to="dissertation/files/", blank=True
    )
    abstract_file = models.FileField(
        _("Abstract File"), upload_to="dissertation/abstracts/", blank=True
    )

    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        verbose_name = _("Dissertation Defense")
        verbose_name_plural = _("Dissertation Defenses")
        ordering = ["-defense_date"]

    def __str__(self):
        return self.title_ru

    def get_title(self):
        return self.title_ru

    def get_applicant(self):
        return self.applicant_ru

    def get_abstract(self):
        return self.abstract_ru


class ConferenceNotice(models.Model):
    """Model for scientific conference announcements"""

    title_ru = models.CharField(_("Conference Title (Russian)"), max_length=500)
    title_en = models.CharField(
        _("Conference Title (English)"), max_length=500, blank=True
    )
    title_kg = models.CharField(
        _("Conference Title (Kyrgyz)"), max_length=500, blank=True
    )

    description_ru = models.TextField(_("Description (Russian)"))
    description_en = models.TextField(_("Description (English)"), blank=True)
    description_kg = models.TextField(_("Description (Kyrgyz)"), blank=True)

    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"))
    registration_deadline = models.DateField(_("Registration Deadline"))

    location = models.CharField(_("Location"), max_length=255)
    organizer = models.CharField(_("Organizer"), max_length=255)

    website = models.URLField(_("Conference Website"), blank=True)
    file = models.FileField(_("Information File"), upload_to="conferences/", blank=True)

    contact_email = models.EmailField(_("Contact Email"), blank=True)
    contact_phone = models.CharField(_("Contact Phone"), max_length=20, blank=True)

    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        verbose_name = _("Conference Notice")
        verbose_name_plural = _("Conference Notices")
        ordering = ["start_date"]

    def __str__(self):
        return self.title_ru

    def get_title(self):
        return self.title_ru

    def get_description(self):
        return self.description_ru


class Vestnik(models.Model):
    """Model for scientific journal Vestnik"""

    title_ru = models.CharField(_("Journal Title (Russian)"), max_length=255)
    title_en = models.CharField(
        _("Journal Title (English)"), max_length=255, blank=True
    )
    title_kg = models.CharField(_("Journal Title (Kyrgyz)"), max_length=255, blank=True)

    description_ru = models.TextField(_("Description (Russian)"))
    description_en = models.TextField(_("Description (English)"), blank=True)
    description_kg = models.TextField(_("Description (Kyrgyz)"), blank=True)

    issn = models.CharField(_("ISSN"), max_length=20)
    image = models.ImageField(_("Journal Logo"), upload_to="vestnik/", blank=True)

    is_active = models.BooleanField(_("Active"), default=True)

    class Meta:
        verbose_name = _("Vestnik Journal")
        verbose_name_plural = _("Vestnik Journals")

    def __str__(self):
        return self.title_ru

    def get_title(self):
        return self.title_ru

    def get_description(self):
        return self.description_ru
