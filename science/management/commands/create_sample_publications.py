from django.core.management.base import BaseCommand
from science.models import Publication, PublicationStats
from datetime import date


class Command(BaseCommand):
    help = "Create sample publications and statistics for testing"

    def handle(self, *args, **options):
        # Create sample statistics
        stats_data = [
            {
                "label_ru": "Научных публикаций",
                "label_en": "Scientific Publications",
                "label_kg": "Илимий макалалар",
                "value": 245,
                "icon": "📚",
                "order": 1,
            },
            {
                "label_ru": "Цитирований",
                "label_en": "Citations",
                "label_kg": "Цитаталар",
                "value": 1280,
                "icon": "📈",
                "order": 2,
            },
            {
                "label_ru": "Индекс Хирша",
                "label_en": "H-Index",
                "label_kg": "H-индекс",
                "value": 18,
                "icon": "🎯",
                "order": 3,
            },
            {
                "label_ru": "Международных журналов",
                "label_en": "International Journals",
                "label_kg": "Эл аралык журналдар",
                "value": 89,
                "icon": "🌍",
                "order": 4,
            },
        ]

        for stat_data in stats_data:
            stat, created = PublicationStats.objects.get_or_create(
                label_ru=stat_data["label_ru"], defaults=stat_data
            )
            if created:
                self.stdout.write(f"Created statistic: {stat.label_ru}")

        # Create sample publications
        publications_data = [
            {
                "title_ru": "Исследование методов машинного обучения в медицинской диагностике",
                "title_en": "Research on Machine Learning Methods in Medical Diagnosis",
                "title_kg": "Медициналык диагностикада машиналык үйрөнүү ыкмаларын изилдөө",
                "author_ru": "А.К. Иванов, С.М. Петрова",
                "author_en": "A.K. Ivanov, S.M. Petrova",
                "author_kg": "А.К. Иванов, С.М. Петрова",
                "journal": "Journal of Medical AI",
                "year": 2024,
                "publication_date": date(2024, 3, 15),
                "citation_count": 23,
                "impact_factor": 2.84,
                "abstract_ru": "В данной статье представлены результаты исследования применения методов машинного обучения для улучшения точности медицинской диагностики. Проведен анализ различных алгоритмов и их эффективности.",
                "abstract_en": "This article presents the results of a study on the application of machine learning methods to improve the accuracy of medical diagnosis. An analysis of various algorithms and their effectiveness is conducted.",
                "abstract_kg": "Бул макалада медициналык диагностиканын тактыгын жакшыртуу үчүн машиналык үйрөнүү ыкмаларын колдонуунун изилдөө жыйынтыктары берилген.",
                "doi": "10.1234/jmai.2024.001",
                "publication_type": "article",
                "is_featured": True,
                "order": 1,
            },
            {
                "title_ru": "Квантовые алгоритмы в криптографии",
                "title_en": "Quantum Algorithms in Cryptography",
                "title_kg": "Криптографиядагы квант алгоритмдери",
                "author_ru": "М.Н. Сидоров",
                "author_en": "M.N. Sidorov",
                "author_kg": "М.Н. Сидоров",
                "journal": "Quantum Computing Reviews",
                "year": 2023,
                "publication_date": date(2023, 11, 8),
                "citation_count": 41,
                "impact_factor": 4.12,
                "abstract_ru": "Обзор современных квантовых алгоритмов и их применения в области криптографической защиты информации. Рассмотрены перспективы развития квантовой криптографии.",
                "abstract_en": "A review of modern quantum algorithms and their applications in the field of cryptographic information protection. Prospects for the development of quantum cryptography are considered.",
                "abstract_kg": "Заманбап квант алгоритмдеринин жана алардын криптографиялык маалымат коргоо тармагындагы колдонуусунун сереп.",
                "doi": "10.5678/qcr.2023.456",
                "publication_type": "article",
                "is_featured": True,
                "order": 2,
            },
            {
                "title_ru": "Экологический мониторинг урбанизированных территорий",
                "title_en": "Environmental Monitoring of Urbanized Areas",
                "title_kg": "Шаарлашкан аймактардын экологиялык мониторинги",
                "author_ru": "Е.В. Козлова, Д.А. Морозов",
                "author_en": "E.V. Kozlova, D.A. Morozov",
                "author_kg": "Е.В. Козлова, Д.А. Морозов",
                "journal": "Environmental Science International",
                "year": 2023,
                "publication_date": date(2023, 8, 22),
                "citation_count": 15,
                "impact_factor": 3.67,
                "abstract_ru": "Исследование методов экологического мониторинга в крупных городах с использованием современных сенсорных технологий и анализа данных.",
                "abstract_en": "Research on environmental monitoring methods in major cities using modern sensor technologies and data analysis.",
                "abstract_kg": "Заманбап сенсордук технологиялар жана маалыматтарды талдоону колдонуу менен ири шаарлардагы экологиялык мониторинг ыкмаларын изилдөө.",
                "doi": "10.9012/esi.2023.789",
                "publication_type": "article",
                "is_featured": False,
                "order": 3,
            },
        ]

        for pub_data in publications_data:
            publication, created = Publication.objects.get_or_create(
                title_ru=pub_data["title_ru"], defaults=pub_data
            )
            if created:
                self.stdout.write(f"Created publication: {publication.title_ru}")

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully created sample publications and statistics!"
            )
        )
