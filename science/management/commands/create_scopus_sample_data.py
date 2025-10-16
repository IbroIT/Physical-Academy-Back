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
                "title_ru": "Novel approaches to sports medicine: rehabilitation technologies",
                "title_en": "Novel approaches to sports medicine: rehabilitation technologies",
                "title_kg": "Novel approaches to sports medicine: rehabilitation technologies",
                "authors_ru": "Petrova A.K., Sidorov M.V., Johnson R.T.",
                "authors_en": "Petrova A.K., Sidorov M.V., Johnson R.T.",
                "authors_kg": "Petrova A.K., Sidorov M.V., Johnson R.T.",
                "journal_ru": "Sports Science Journal",
                "journal_en": "Sports Science Journal",
                "journal_kg": "Sports Science Journal",
                "year": 2023,
                "citation_count": 8,
                "document_type": "Article",
                "subject_area": "Sports Science",
                "url": "https://example.com/publication1",
                "order": 1,
            },
            {
                "title_ru": "Physiological responses during high-intensity interval training in elite athletes",
                "title_en": "Physiological responses during high-intensity interval training in elite athletes",
                "title_kg": "Physiological responses during high-intensity interval training in elite athletes",
                "authors_ru": "Alimov D.S., Kozlov I.I., Williams T.J.",
                "authors_en": "Alimov D.S., Kozlov I.I., Williams T.J.",
                "authors_kg": "Alimov D.S., Kozlov I.I., Williams T.J.",
                "journal_ru": "Journal of Exercise Physiology",
                "journal_en": "Journal of Exercise Physiology",
                "journal_kg": "Journal of Exercise Physiology",
                "year": 2022,
                "citation_count": 12,
                "document_type": "Article",
                "subject_area": "Exercise Physiology",
                "url": "https://example.com/publication2",
                "order": 2,
            },
            {
                "title_ru": "Comparative analysis of training methodologies for Olympic weightlifters",
                "title_en": "Comparative analysis of training methodologies for Olympic weightlifters",
                "title_kg": "Comparative analysis of training methodologies for Olympic weightlifters",
                "authors_ru": "Borisov K.L., Zhang W., Miller P.S.",
                "authors_en": "Borisov K.L., Zhang W., Miller P.S.",
                "authors_kg": "Borisov K.L., Zhang W., Miller P.S.",
                "journal_ru": "International Journal of Strength Research",
                "journal_en": "International Journal of Strength Research",
                "journal_kg": "International Journal of Strength Research",
                "year": 2022,
                "citation_count": 12,
                "document_type": "Article",
                "subject_area": "Sports Training",
                "url": "https://example.com/publication3",
                "order": 3,
            },
            {
                "title_ru": "Mental health in professional athletes: a systematic review",
                "title_en": "Mental health in professional athletes: a systematic review",
                "title_kg": "Mental health in professional athletes: a systematic review",
                "authors_ru": "Smirnova E.V., Garcia F.T., Taylor M.L.",
                "authors_en": "Smirnova E.V., Garcia F.T., Taylor M.L.",
                "authors_kg": "Smirnova E.V., Garcia F.T., Taylor M.L.",
                "journal_ru": "Sports Psychology Review",
                "journal_en": "Sports Psychology Review",
                "journal_kg": "Sports Psychology Review",
                "year": 2021,
                "citation_count": 24,
                "document_type": "Review",
                "subject_area": "Sports Psychology",
                "url": "https://example.com/publication4",
                "order": 4,
            },
            {
                "title_ru": "Biomechanical analysis of modern swimming techniques",
                "title_en": "Biomechanical analysis of modern swimming techniques",
                "title_kg": "Biomechanical analysis of modern swimming techniques",
                "authors_ru": "Ivanov P.P., Anderson J.K.",
                "authors_en": "Ivanov P.P., Anderson J.K.",
                "authors_kg": "Ivanov P.P., Anderson J.K.",
                "journal_ru": "Biomechanics in Sport Conference",
                "journal_en": "Biomechanics in Sport Conference",
                "journal_kg": "Biomechanics in Sport Conference",
                "year": 2023,
                "citation_count": 6,
                "document_type": "Conference Paper",
                "subject_area": "Sports Biomechanics",
                "url": "https://example.com/publication5",
                "order": 5,
            },
            {
                "title_ru": "Nutritional interventions for recovery optimization in combat sports",
                "title_en": "Nutritional interventions for recovery optimization in combat sports",
                "title_kg": "Nutritional interventions for recovery optimization in combat sports",
                "authors_ru": "Romanov I.S., Lee H.J., Davis K.M.",
                "authors_en": "Romanov I.S., Lee H.J., Davis K.M.",
                "authors_kg": "Romanov I.S., Lee H.J., Davis K.M.",
                "journal_ru": "Journal of Combat Sports Nutrition",
                "journal_en": "Journal of Combat Sports Nutrition",
                "journal_kg": "Journal of Combat Sports Nutrition",
                "year": 2022,
                "citation_count": 11,
                "document_type": "Article",
                "subject_area": "Sports Nutrition",
                "url": "https://example.com/publication6",
                "order": 6,
            },
            {
                "title_ru": "Innovations in wearable technology for athletic performance monitoring",
                "title_en": "Innovations in wearable technology for athletic performance monitoring",
                "title_kg": "Innovations in wearable technology for athletic performance monitoring",
                "authors_ru": "Denisov R.A., Wilson T.R.",
                "authors_en": "Denisov R.A., Wilson T.R.",
                "authors_kg": "Denisov R.A., Wilson T.R.",
                "journal_ru": "Sports Technology Proceedings",
                "journal_en": "Sports Technology Proceedings",
                "journal_kg": "Sports Technology Proceedings",
                "year": 2023,
                "citation_count": 9,
                "document_type": "Conference Paper",
                "subject_area": "Sports Technology",
                "url": "https://example.com/publication7",
                "order": 7,
            },
            {
                "title_ru": "The effect of altitude training on endurance performance: meta-analysis",
                "title_en": "The effect of altitude training on endurance performance: meta-analysis",
                "title_kg": "The effect of altitude training on endurance performance: meta-analysis",
                "authors_ru": "Sokolov M.M., Brown L.K., Chen Y.",
                "authors_en": "Sokolov M.M., Brown L.K., Chen Y.",
                "authors_kg": "Sokolov M.M., Brown L.K., Chen Y.",
                "journal_ru": "Altitude Medicine & Physiology",
                "journal_en": "Altitude Medicine & Physiology",
                "journal_kg": "Altitude Medicine & Physiology",
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
