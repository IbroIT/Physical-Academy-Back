from django.test import TestCase
from .models import Publication, PublicationStats


class PublicationTests(TestCase):
    def setUp(self):
        self.publication = Publication.objects.create(
            title_ru="Тестовая публикация",
            title_en="Test Publication",
            title_kg="Тест басылма",
            authors_ru="Иван Иванов",
            authors_en="Ivan Ivanov",
            authors_kg="Иван Иванов",
            year=2023,
            journal="Test Journal",
            citation_count=10,
            publication_type="article",
        )

    def test_publication_creation(self):
        self.assertEqual(self.publication.title_ru, "Тестовая публикация")
        self.assertEqual(self.publication.title_en, "Test Publication")
        self.assertEqual(self.publication.year, 2023)

    def test_publication_str(self):
        self.assertEqual(str(self.publication), "Тестовая публикация")


class PublicationStatsTests(TestCase):
    def setUp(self):
        self.stat = PublicationStats.objects.create(
            label_ru="Всего публикаций",
            label_en="Total publications",
            label_kg="Жалпы басылмалар",
            value=42,
            icon="📚",
            order=1,
        )

    def test_stats_creation(self):
        self.assertEqual(self.stat.value, 42)
        self.assertEqual(self.stat.icon, "📚")

    def test_stats_str(self):
        self.assertEqual(str(self.stat), "Всего публикаций: 42")
