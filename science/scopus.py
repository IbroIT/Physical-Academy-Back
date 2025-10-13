from django.db import models
from django.utils.translation import gettext_lazy as _


class ScopusSection(models.Model):
    """Model for Scopus page sections with translations"""

    section_key = models.CharField(_("Section Key"), max_length=100, unique=True)

    title_ru = models.CharField(_("Title (Russian)"), max_length=200)
    title_en = models.CharField(_("Title (English)"), max_length=200, blank=True)
    title_kg = models.CharField(_("Title (Kyrgyz)"), max_length=200, blank=True)

    description_ru = models.TextField(_("Description (Russian)"))
    description_en = models.TextField(_("Description (English)"), blank=True)
    description_kg = models.TextField(_("Description (Kyrgyz)"), blank=True)

    class Meta:
        verbose_name = _("Scopus Section")
        verbose_name_plural = _("Scopus Sections")

    def __str__(self):
        return f"{self.section_key}: {self.title_ru}"

    def get_title(self, language="ru"):
        """Return the title in the specified language"""
        return getattr(self, f"title_{language}", self.title_ru)

    def get_description(self, language="ru"):
        """Return the description in the specified language"""
        return getattr(self, f"description_{language}", self.description_ru)


class ScopusMetrics(models.Model):
    """Model for Scopus metrics and information"""

    value = models.CharField(_("Value"), max_length=50)
    label_ru = models.CharField(_("Label (Russian)"), max_length=100)
    label_en = models.CharField(_("Label (English)"), max_length=100, blank=True)
    label_kg = models.CharField(_("Label (Kyrgyz)"), max_length=100, blank=True)
    icon = models.CharField(_("Icon"), max_length=20, default="📊")
    description_ru = models.CharField(_("Description (Russian)"), max_length=255)
    description_en = models.CharField(
        _("Description (English)"), max_length=255, blank=True
    )
    description_kg = models.CharField(
        _("Description (Kyrgyz)"), max_length=255, blank=True
    )
    trend = models.CharField(_("Trend"), max_length=20, default="stable")
    order = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Scopus Metric")
        verbose_name_plural = _("Scopus Metrics")
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.value} - {self.label_ru}"

    def get_label(self, language="ru"):
        """Return the label in the specified language"""
        return getattr(self, f"label_{language}", self.label_ru)

    def get_description(self, language="ru"):
        """Return the description in the specified language"""
        return getattr(self, f"description_{language}", self.description_ru)


class ScopusDocumentType(models.Model):
    """Model for Scopus document types"""

    name_ru = models.CharField(_("Name (Russian)"), max_length=100)
    name_en = models.CharField(_("Name (English)"), max_length=100, blank=True)
    name_kg = models.CharField(_("Name (Kyrgyz)"), max_length=100, blank=True)
    count = models.PositiveIntegerField(_("Document Count"))
    percentage = models.FloatField(_("Percentage of Total"))
    color = models.CharField(_("Chart Color"), max_length=20, default="#4C9BE8")
    order = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Scopus Document Type")
        verbose_name_plural = _("Scopus Document Types")
        ordering = ["-count"]

    def __str__(self):
        return f"{self.name_ru} ({self.count})"

    def get_name(self, language="ru"):
        """Return the name in the specified language"""
        return getattr(self, f"name_{language}", self.name_ru)


class ScopusPublication(models.Model):
    """Model for Scopus publications"""

    title_ru = models.CharField(_("Title (Russian)"), max_length=500, default="")
    title_en = models.CharField(
        _("Title (English)"), max_length=500, blank=True, default=""
    )
    title_kg = models.CharField(
        _("Title (Kyrgyz)"), max_length=500, blank=True, default=""
    )

    authors_ru = models.CharField(_("Authors (Russian)"), max_length=500, default="")
    authors_en = models.CharField(
        _("Authors (English)"), max_length=500, blank=True, default=""
    )
    authors_kg = models.CharField(
        _("Authors (Kyrgyz)"), max_length=500, blank=True, default=""
    )

    journal_ru = models.CharField(
        _("Journal/Conference (Russian)"), max_length=255, default=""
    )
    journal_en = models.CharField(
        _("Journal/Conference (English)"), max_length=255, blank=True, default=""
    )
    journal_kg = models.CharField(
        _("Journal/Conference (Kyrgyz)"), max_length=255, blank=True, default=""
    )

    abstract_ru = models.TextField(_("Abstract (Russian)"), blank=True, default="")
    abstract_en = models.TextField(_("Abstract (English)"), blank=True, default="")
    abstract_kg = models.TextField(_("Abstract (Kyrgyz)"), blank=True, default="")

    year = models.IntegerField(_("Publication Year"))
    citation_count = models.IntegerField(_("Citation Count"), default=0)
    document_type = models.CharField(_("Document Type"), max_length=100)
    subject_area = models.CharField(_("Subject Area"), max_length=100)
    url = models.URLField(_("URL"), blank=True)
    doi = models.CharField(_("DOI"), max_length=100, blank=True)
    is_featured = models.BooleanField(_("Is Featured"), default=False)
    order = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Scopus Publication")
        verbose_name_plural = _("Scopus Publications")
        ordering = ["-year", "order", "-citation_count"]

    def __str__(self):
        return f"{self.title_ru} ({self.year})"

    def get_title(self, language="ru"):
        """Return the title in the specified language"""
        return getattr(self, f"title_{language}", self.title_ru)

    def get_authors(self, language="ru"):
        """Return the authors in the specified language"""
        return getattr(self, f"authors_{language}", self.authors_ru)

    def get_journal(self, language="ru"):
        """Return the journal name in the specified language"""
        return getattr(self, f"journal_{language}", self.journal_ru)

    def get_abstract(self, language="ru"):
        """Return the abstract in the specified language"""
        return getattr(self, f"abstract_{language}", self.abstract_ru)


class ScopusAuthor(models.Model):
    """Model for Scopus authors"""

    scopus_id = models.CharField(_("Scopus ID"), max_length=50, blank=True)
    name = models.CharField(_("Name"), max_length=255)
    first_name = models.CharField(_("First Name"), max_length=100, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=100, blank=True)
    h_index = models.IntegerField(_("H-index"), default=0)

    class Meta:
        verbose_name = _("Scopus Author")
        verbose_name_plural = _("Scopus Authors")

    def __str__(self):
        return self.name


class ScopusJournal(models.Model):
    """Model for journals/conference sources"""

    scopus_id = models.CharField(_("Scopus ID"), max_length=50, blank=True)
    title = models.CharField(_("Title"), max_length=255)
    publisher = models.CharField(_("Publisher"), max_length=255, blank=True)
    issn = models.CharField(_("ISSN"), max_length=50, blank=True)
    eissn = models.CharField(_("E-ISSN"), max_length=50, blank=True)
    source_id = models.CharField(_("Source ID"), max_length=50, blank=True)
    cite_score = models.FloatField(_("CiteScore"), null=True, blank=True)
    sjr = models.FloatField(_("SJR"), null=True, blank=True)
    snip = models.FloatField(_("SNIP"), null=True, blank=True)

    class Meta:
        verbose_name = _("Scopus Journal")
        verbose_name_plural = _("Scopus Journals")

    def __str__(self):
        return self.title


class ScopusPublisher(models.Model):
    """Model for publishers in Scopus data"""

    scopus_id = models.CharField(_("Scopus ID"), max_length=50, blank=True)
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        verbose_name = _("Scopus Publisher")
        verbose_name_plural = _("Scopus Publishers")

    def __str__(self):
        return self.name


class ScopusPublicationAuthor(models.Model):
    """Through model linking publications and authors"""

    publication = models.ForeignKey(
        ScopusPublication, on_delete=models.CASCADE, related_name="publication_authors"
    )
    author = models.ForeignKey(ScopusAuthor, on_delete=models.CASCADE)
    seq = models.IntegerField(_("Sequence"), default=0)
    is_corresponding = models.BooleanField(_("Is Corresponding"), default=False)

    class Meta:
        verbose_name = _("Scopus Publication Author")
        verbose_name_plural = _("Scopus Publication Authors")
        ordering = ["seq"]

    def __str__(self):
        return f"{self.author} - {self.publication}"


class ScopusStats(models.Model):
    """Scopus Statistics"""

    value = models.CharField(_("Value"), max_length=50)
    label_ru = models.CharField(_("Label (Russian)"), max_length=100)
    label_en = models.CharField(_("Label (English)"), max_length=100, blank=True)
    label_kg = models.CharField(_("Label (Kyrgyz)"), max_length=100, blank=True)
    icon = models.CharField(_("Icon"), max_length=20, default="📊")
    order = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        verbose_name = _("Scopus Stats Item")
        verbose_name_plural = _("Scopus Stats")
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.value} - {self.label_ru}"

    def get_label(self, language="ru"):
        """Return the label in the specified language"""
        return getattr(self, f"label_{language}", self.label_ru)
