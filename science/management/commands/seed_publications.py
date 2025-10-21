from django.core.management.base import BaseCommand
from science.models import Publication, PublicationStats


class Command(BaseCommand):
    help = "Seeds the publications database with initial data"

    def handle(self, *args, **kwargs):
        # Create sample stats
        stats_data = [
            {
                "label_ru": "Всего публикаций",
                "label_en": "Total publications",
                "label_kg": "Жалпы басылмалар",
                "value": "150+",
                "icon": "📚",
                "order": 1,
            },
            {
                "label_ru": "Цитирований",
                "label_en": "Citations",
                "label_kg": "Шилтемелер",
                "value": "500+",
                "icon": "📖",
                "order": 2,
            },
            {
                "label_ru": "Импакт-фактор",
                "label_en": "Impact factor",
                "label_kg": "Таасир фактору",
                "value": "3.5",
                "icon": "📊",
                "order": 3,
            },
        ]

        for stat_data in stats_data:
            PublicationStats.objects.get_or_create(**stat_data)

        # Create sample publications
        publications_data = [
            {
                "title_ru": "Исследование физической активности студентов",
                "title_en": "Study of Students Physical Activity",
                "title_kg": "Студенттердин физикалык активдүүлүгүн изилдөө",
                "authors_ru": "Иванов И.И., Петров П.П.",
                "authors_en": "Ivanov I.I., Petrov P.P.",
                "authors_kg": "Иванов И.И., Петров П.П.",
                "abstract_ru": "Описание исследования...",
                "abstract_en": "Research description...",
                "abstract_kg": "Изилдөө сүрөттөмөсү...",
                "journal": "Sports Science Journal",
                "year": 2023,
                "citation_count": 15,
                "impact_factor": 2.5,
                "doi": "10.1000/example123",
                "publication_type": "article",
                "is_featured": True,
                "order": 1,
            },
            {
                "title_ru": "Методология спортивной подготовки",
                "title_en": "Sports Training Methodology",
                "title_kg": "Спорттук машыгуу методологиясы",
                "authors_ru": "Сидоров С.С.",
                "authors_en": "Sidorov S.S.",
                "authors_kg": "Сидоров С.С.",
                "abstract_ru": "Методология...",
                "abstract_en": "Methodology...",
                "abstract_kg": "Методология...",
                "journal": "Physical Education Review",
                "year": 2023,
                "citation_count": 8,
                "impact_factor": 1.8,
                "doi": "10.1000/example456",
                "publication_type": "article",
                "is_featured": False,
                "order": 2,
            },
        ]

        for pub_data in publications_data:
            Publication.objects.get_or_create(**pub_data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded publications data"))
