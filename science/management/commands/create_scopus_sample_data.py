from django.core.management.base import BaseCommand
from django.db import transaction
from science.models import (
    ScopusMetrics,
    ScopusDocumentType,
    ScopusPublication,
    ScopusStats,
)


class Command(BaseCommand):
    help = "Creates sample data for Scopus models"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating Scopus sample data...")

        with transaction.atomic():
            # Create Scopus metrics
            self.create_scopus_metrics()

            # Create document types
            self.create_document_types()

            # Create publications
            self.create_publications()

            # Create stats
            self.create_stats()

        self.stdout.write(
            self.style.SUCCESS("Scopus sample data created successfully!")
        )

    def create_scopus_metrics(self):
        metrics = [
            {
                "value": "520+",
                "label_ru": "Всего документов в Scopus",
                "label_en": "Total documents in Scopus",
                "icon": "📄",
                "description_ru": "Все публикации наших авторов, индексируемые в Scopus",
                "description_en": "All publications by our authors indexed in Scopus",
                "trend": "increasing",
                "order": 1,
            },
            {
                "value": "215",
                "label_ru": "Публикации в журналах Q1/Q2",
                "label_en": "Publications in Q1/Q2 journals",
                "icon": "⭐",
                "description_ru": "Высококачественные исследования в топовых журналах",
                "description_en": "High-quality research in top-tier journals",
                "trend": "increasing",
                "order": 2,
            },
            {
                "value": "3800+",
                "label_ru": "Всего цитирований",
                "label_en": "Total citations",
                "icon": "📚",
                "description_ru": "Цитирования наших исследований другими учеными",
                "description_en": "Citations of our research by other scholars",
                "trend": "increasing",
                "order": 3,
            },
            {
                "value": "18.5",
                "label_ru": "Средний h-индекс",
                "label_en": "Average h-index",
                "icon": "📊",
                "description_ru": "Метрика влияния наших ведущих исследователей",
                "description_en": "Impact metric of our leading researchers",
                "trend": "stable",
                "order": 4,
            },
            {
                "value": "42",
                "label_ru": "Международные коллаборации",
                "label_en": "International collaborations",
                "icon": "🌐",
                "description_ru": "Совместные исследовательские проекты с зарубежными учреждениями",
                "description_en": "Joint research projects with foreign institutions",
                "trend": "increasing",
                "order": 5,
            },
        ]

        for metric in metrics:
            ScopusMetrics.objects.create(**metric)

        self.stdout.write(f"Created {len(metrics)} Scopus metrics")

    def create_document_types(self):
        document_types = [
            {
                "name_ru": "Статьи",
                "name_en": "Articles",
                "count": 320,
                "percentage": 61.5,
                "color": "#4C9BE8",
                "order": 1,
            },
            {
                "name_ru": "Доклады на конференциях",
                "name_en": "Conference Papers",
                "count": 112,
                "percentage": 21.5,
                "color": "#45C4B0",
                "order": 2,
            },
            {
                "name_ru": "Обзоры",
                "name_en": "Reviews",
                "count": 58,
                "percentage": 11.2,
                "color": "#6665DD",
                "order": 3,
            },
            {
                "name_ru": "Другое",
                "name_en": "Other",
                "count": 30,
                "percentage": 5.8,
                "color": "#BFBFBF",
                "order": 4,
            },
        ]

        for doc_type in document_types:
            ScopusDocumentType.objects.create(**doc_type)

        self.stdout.write(f"Created {len(document_types)} document types")

    def create_publications(self):
        publications = [
            {
                "title": "Novel approaches to sports medicine: rehabilitation technologies",
                "authors": "Petrova A.K., Sidorov M.V., Johnson R.T.",
                "journal": "Sports Science Journal",
                "year": 2023,
                "citation_count": 8,
                "document_type": "Article",
                "subject_area": "Sports Science",
                "url": "https://example.com/publication1",
                "order": 1,
            },
            {
                "title": "Physiological responses during high-intensity interval training in elite athletes",
                "authors": "Alimov D.S., Kozlov I.I., Williams T.J.",
                "journal": "Journal of Exercise Physiology",
                "year": 2022,
                "citation_count": 15,
                "document_type": "Article",
                "subject_area": "Exercise Physiology",
                "url": "https://example.com/publication2",
                "order": 2,
            },
            {
                "title": "Comparative analysis of training methodologies for Olympic weightlifters",
                "authors": "Borisov K.L., Zhang W., Miller P.S.",
                "journal": "International Journal of Strength Research",
                "year": 2022,
                "citation_count": 12,
                "document_type": "Article",
                "subject_area": "Sports Training",
                "url": "https://example.com/publication3",
                "order": 3,
            },
            {
                "title": "Mental health in professional athletes: a systematic review",
                "authors": "Smirnova E.V., Garcia F.T., Taylor M.L.",
                "journal": "Sports Psychology Review",
                "year": 2021,
                "citation_count": 24,
                "document_type": "Review",
                "subject_area": "Sports Psychology",
                "url": "https://example.com/publication4",
                "order": 4,
            },
            {
                "title": "Biomechanical analysis of modern swimming techniques",
                "authors": "Ivanov P.P., Anderson J.K.",
                "journal": "Biomechanics in Sport Conference",
                "year": 2023,
                "citation_count": 6,
                "document_type": "Conference Paper",
                "subject_area": "Sports Biomechanics",
                "url": "https://example.com/publication5",
                "order": 5,
            },
            {
                "title": "Nutritional interventions for recovery optimization in combat sports",
                "authors": "Romanov I.S., Lee H.J., Davis K.M.",
                "journal": "Journal of Combat Sports Nutrition",
                "year": 2022,
                "citation_count": 11,
                "document_type": "Article",
                "subject_area": "Sports Nutrition",
                "url": "https://example.com/publication6",
                "order": 6,
            },
            {
                "title": "Innovations in wearable technology for athletic performance monitoring",
                "authors": "Denisov R.A., Wilson T.R.",
                "journal": "Sports Technology Proceedings",
                "year": 2023,
                "citation_count": 9,
                "document_type": "Conference Paper",
                "subject_area": "Sports Technology",
                "url": "https://example.com/publication7",
                "order": 7,
            },
            {
                "title": "The effect of altitude training on endurance performance: meta-analysis",
                "authors": "Sokolov M.M., Brown L.K., Chen Y.",
                "journal": "Altitude Medicine & Physiology",
                "year": 2021,
                "citation_count": 18,
                "document_type": "Review",
                "subject_area": "Exercise Physiology",
                "url": "https://example.com/publication8",
                "order": 8,
            },
        ]

        for pub in publications:
            ScopusPublication.objects.create(**pub)

        self.stdout.write(f"Created {len(publications)} Scopus publications")

    def create_stats(self):
        stats = [
            {
                "value": "42%",
                "label_ru": "Публикации в топ-10% журналах",
                "label_en": "Publications in top 10% journals",
                "icon": "📈",
                "order": 1,
            },
            {
                "value": "65%",
                "label_ru": "Международное соавторство",
                "label_en": "International co-authorship",
                "icon": "🌍",
                "order": 2,
            },
            {
                "value": "28",
                "label_ru": "Охваченные предметные области",
                "label_en": "Subject areas covered",
                "icon": "🔬",
                "order": 3,
            },
            {
                "value": "13.2",
                "label_ru": "Цитирований на документ",
                "label_en": "Citations per document",
                "icon": "📣",
                "order": 4,
            },
        ]

        for stat in stats:
            ScopusStats.objects.create(**stat)

        self.stdout.write(f"Created {len(stats)} Scopus stats")
