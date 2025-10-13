from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Publication,
    PublicationStats,
    VestnikIssue,
    VestnikArticle,
    VestnikStats,
    # Scopus models
    ScopusMetrics,
    ScopusDocumentType,
    ScopusPublication,
    ScopusStats,
    ScopusSection,
)

# Import NTS committee admin from admin subpackage
from .admin import *

# Import NTS Committee admin classes
from . import admin_nts


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = [
        "title_display",
        "publication_type",
        "year",
        "citation_count",
        "is_featured",
        "order",
    ]
    list_filter = ["publication_type", "year", "is_featured"]
    search_fields = [
        "title_ru",
        "title_en",
        "title_kg",
        "author_ru",
        "author_en",
        "author_kg",
    ]
    list_editable = ["is_featured", "order"]

    fieldsets = (
        ("Russian", {"fields": ("title_ru", "author_ru", "abstract_ru")}),
        ("English", {"fields": ("title_en", "author_en", "abstract_en")}),
        ("Kyrgyz", {"fields": ("title_kg", "author_kg", "abstract_kg")}),
        (
            "Publication Details",
            {
                "fields": (
                    "publication_type",
                    "journal",
                    "year",
                    "citation_count",
                    "impact_factor",
                    "doi",
                    "url",
                    "pdf_file",
                )
            },
        ),
        ("Display Options", {"fields": ("is_featured", "order")}),
    )

    def title_display(self, obj):
        return obj.title_ru or obj.title_en or obj.title_kg

    title_display.short_description = "Title"


@admin.register(PublicationStats)
class PublicationStatsAdmin(admin.ModelAdmin):
    list_display = ["label_display", "value", "icon_preview", "order"]
    list_editable = ["value", "order"]

    fieldsets = (
        ("Labels", {"fields": ("label_ru", "label_en", "label_kg")}),
        ("Statistics", {"fields": ("value", "icon", "order")}),
    )

    def label_display(self, obj):
        return obj.label_ru or obj.label_en or obj.label_kg

    label_display.short_description = "Label"

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<span style="font-size: 20px;">{}</span>', obj.icon)
        return "-"

    icon_preview.short_description = "Icon"


# Vestnik Admin Classes
class VestnikArticleInline(admin.TabularInline):
    model = VestnikArticle
    extra = 0
    fields = [
        "title_ru",
        "author_ru",
        "pages_from",
        "pages_to",
        "article_type",
        "order",
    ]
    readonly_fields = ["created_at"]


@admin.register(VestnikIssue)
class VestnikIssueAdmin(admin.ModelAdmin):
    list_display = [
        "volume_issue_display",
        "year",
        "publication_date",
        "is_featured",
        "is_published",
        "articles_count",
    ]
    list_filter = ["year", "is_featured", "is_published", "publication_date"]
    search_fields = ["title_ru", "title_en", "title_kg", "description_ru"]
    list_editable = ["is_featured", "is_published"]
    inlines = [VestnikArticleInline]

    fieldsets = (
        ("Russian", {"fields": ("title_ru", "description_ru")}),
        ("English", {"fields": ("title_en", "description_en")}),
        ("Kyrgyz", {"fields": ("title_kg", "description_kg")}),
        (
            "Issue Details",
            {
                "fields": (
                    "volume_number",
                    "issue_number",
                    "year",
                    "publication_date",
                    "cover_image",
                    "pdf_file",
                )
            },
        ),
        (
            "Publication Info",
            {
                "fields": (
                    "issn_print",
                    "issn_online",
                    "doi_prefix",
                )
            },
        ),
        ("Display Options", {"fields": ("is_featured", "is_published", "order")}),
    )

    def volume_issue_display(self, obj):
        return f"Vol.{obj.volume_number} №{obj.issue_number}"

    volume_issue_display.short_description = "Volume/Issue"

    def articles_count(self, obj):
        return obj.articles.count()

    articles_count.short_description = "Articles"


@admin.register(VestnikArticle)
class VestnikArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title_display",
        "issue",
        "author_display",
        "page_range",
        "article_type",
        "citation_count",
    ]
    list_filter = ["issue__year", "article_type", "issue__volume_number"]
    search_fields = [
        "title_ru",
        "title_en",
        "title_kg",
        "author_ru",
        "author_en",
        "author_kg",
        "abstract_ru",
    ]
    list_select_related = ["issue"]

    fieldsets = (
        ("Issue", {"fields": ("issue",)}),
        (
            "Russian",
            {"fields": ("title_ru", "author_ru", "abstract_ru", "keywords_ru")},
        ),
        (
            "English",
            {"fields": ("title_en", "author_en", "abstract_en", "keywords_en")},
        ),
        ("Kyrgyz", {"fields": ("title_kg", "author_kg", "abstract_kg", "keywords_kg")}),
        (
            "Article Details",
            {
                "fields": (
                    "article_type",
                    "pages_from",
                    "pages_to",
                    "doi",
                    "pdf_file",
                    "citation_count",
                    "order",
                )
            },
        ),
    )

    def title_display(self, obj):
        return obj.title_ru or obj.title_en or obj.title_kg

    title_display.short_description = "Title"

    def author_display(self, obj):
        return obj.author_ru or obj.author_en or obj.author_kg

    author_display.short_description = "Author"


@admin.register(VestnikStats)
class VestnikStatsAdmin(admin.ModelAdmin):
    list_display = ["label_display", "value", "icon_preview", "order"]
    list_editable = ["value", "order"]

    fieldsets = (
        ("Labels", {"fields": ("label_ru", "label_en", "label_kg")}),
        ("Statistics", {"fields": ("value", "icon", "order")}),
    )

    def label_display(self, obj):
        return obj.label_ru or obj.label_en or obj.label_kg

    label_display.short_description = "Label"

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<span style="font-size: 20px;">{}</span>', obj.icon)
        return "-"

    icon_preview.short_description = "Icon"


# Scopus Admin Classes
@admin.register(ScopusMetrics)
class ScopusMetricsAdmin(admin.ModelAdmin):
    list_display = ["label_display", "value", "trend", "order"]
    list_editable = ["value", "order"]

    fieldsets = (
        ("Labels", {"fields": ("label_ru", "label_en", "label_kg")}),
        (
            "Descriptions",
            {"fields": ("description_ru", "description_en", "description_kg")},
        ),
        ("Values", {"fields": ("value", "icon", "trend", "order")}),
    )

    def label_display(self, obj):
        return obj.label_ru or obj.label_en or obj.label_kg

    label_display.short_description = "Label"


@admin.register(ScopusDocumentType)
class ScopusDocumentTypeAdmin(admin.ModelAdmin):
    list_display = ["name_display", "count", "order"]
    list_editable = ["count", "order"]

    fieldsets = (
        ("Names", {"fields": ("name_ru", "name_en", "name_kg")}),
        ("Values", {"fields": ("count", "color", "order")}),
    )

    def name_display(self, obj):
        return obj.name_ru or obj.name_en or obj.name_kg

    name_display.short_description = "Type"


@admin.register(ScopusPublication)
class ScopusPublicationAdmin(admin.ModelAdmin):
    list_display = [
        "title_display",
        "year",
        "authors_display",
        "citation_count",
        "is_featured",
        "order",
    ]
    list_filter = ["year", "document_type", "subject_area", "is_featured"]
    search_fields = [
        "title_ru",
        "title_en",
        "title_kg",
        "authors_ru",
        "authors_en",
        "authors_kg",
        "journal_ru",
        "journal_en",
        "journal_kg",
    ]
    list_editable = ["is_featured", "order"]

    fieldsets = (
        (
            "Russian",
            {"fields": ("title_ru", "authors_ru", "journal_ru", "abstract_ru")},
        ),
        (
            "English",
            {"fields": ("title_en", "authors_en", "journal_en", "abstract_en")},
        ),
        ("Kyrgyz", {"fields": ("title_kg", "authors_kg", "journal_kg", "abstract_kg")}),
        ("Classification", {"fields": ("document_type", "subject_area")}),
        ("Metrics", {"fields": ("year", "citation_count", "doi", "url")}),
        ("Display Options", {"fields": ("is_featured", "order")}),
    )

    def title_display(self, obj):
        return obj.title_ru or obj.title_en or obj.title_kg

    title_display.short_description = "Title"

    def authors_display(self, obj):
        return obj.authors_ru or obj.authors_en or obj.authors_kg

    authors_display.short_description = "Authors"


@admin.register(ScopusSection)
class ScopusSectionAdmin(admin.ModelAdmin):
    list_display = ["section_key", "title_display"]
    search_fields = ["section_key", "title_ru", "title_en", "title_kg"]

    fieldsets = (
        ("Section Info", {"fields": ("section_key",)}),
        ("Russian", {"fields": ("title_ru", "description_ru")}),
        ("English", {"fields": ("title_en", "description_en")}),
        ("Kyrgyz", {"fields": ("title_kg", "description_kg")}),
    )

    def title_display(self, obj):
        return obj.title_ru or obj.title_en or obj.title_kg

    title_display.short_description = "Title"


@admin.register(ScopusStats)
class ScopusStatsAdmin(admin.ModelAdmin):
    list_display = ["label_display", "value", "icon_preview", "order"]
    list_editable = ["value", "order"]

    fieldsets = (
        ("Labels", {"fields": ("label_ru", "label_en", "label_kg")}),
        ("Statistics", {"fields": ("value", "icon", "order")}),
    )

    def label_display(self, obj):
        return obj.label_ru or obj.label_en or obj.label_kg

    label_display.short_description = "Label"

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<span style="font-size: 20px;">{}</span>', obj.icon)
        return "-"

    icon_preview.short_description = "Icon"
