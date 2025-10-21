from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from science.models import PublicationStats, VestnikStats, VestnikIssue, VestnikArticle


class Command(BaseCommand):
    help = "Create sample publication and vestnik statistics"

    def handle(self, *args, **options):
        self.stdout.write("Creating sample publication statistics...")

        # Create Publication Stats
        pub_stats = [
            {
                "label_ru": "Всего публикаций",
                "label_en": "Total Publications",
                "label_kg": "Бардык басылмалар",
                "value": 125,
                "icon": "📚",
                "order": 1,
            },
            {
                "label_ru": "Научные статьи",
                "label_en": "Research Articles",
                "label_kg": "Изилдөө макалалары",
                "value": 85,
                "icon": "📄",
                "order": 2,
            },
            {
                "label_ru": "Цитирования",
                "label_en": "Citations",
                "label_kg": "Шилтемелер",
                "value": 450,
                "icon": "📊",
                "order": 3,
            },
            {
                "label_ru": "H-индекс",
                "label_en": "H-Index",
                "label_kg": "H-индекс",
                "value": 15,
                "icon": "📈",
                "order": 4,
            },
        ]

        for stat_data in pub_stats:
            stat, created = PublicationStats.objects.get_or_create(
                order=stat_data["order"], defaults=stat_data
            )
            if created:
                self.stdout.write(f"Created: {stat.label_ru}")
            else:
                # Update existing
                for key, value in stat_data.items():
                    setattr(stat, key, value)
                stat.save()
                self.stdout.write(f"Updated: {stat.label_ru}")

        self.stdout.write("Creating sample Vestnik statistics...")

        # Create Vestnik Stats
        vestnik_stats = [
            {
                "label_ru": "Выпущено номеров",
                "label_en": "Issues Published",
                "label_kg": "Чыгарылган сандар",
                "value": 24,
                "icon": "📰",
                "order": 1,
            },
            {
                "label_ru": "Статей опубликовано",
                "label_en": "Articles Published",
                "label_kg": "Басылган макалалар",
                "value": 180,
                "icon": "📝",
                "order": 2,
            },
            {
                "label_ru": "Авторов",
                "label_en": "Authors",
                "label_kg": "Авторлор",
                "value": 95,
                "icon": "👥",
                "order": 3,
            },
            {
                "label_ru": "Стран",
                "label_en": "Countries",
                "label_kg": "Өлкөлөр",
                "value": 12,
                "icon": "🌍",
                "order": 4,
            },
        ]

        for stat_data in vestnik_stats:
            stat, created = VestnikStats.objects.get_or_create(
                order=stat_data["order"], defaults=stat_data
            )
            if created:
                self.stdout.write(f"Created: {stat.label_ru}")
            else:
                # Update existing
                for key, value in stat_data.items():
                    setattr(stat, key, value)
                stat.save()
                self.stdout.write(f"Updated: {stat.label_ru}")

        self.stdout.write("Creating sample Vestnik issues...")

        # Create sample Vestnik Issues
        sample_issues = [
            {
                "title_ru": "Вестник Физической Академии",
                "title_en": "Bulletin of Physical Academy",
                "title_kg": "Физикалык академиянын жарчысы",
                "description_ru": "Научный журнал по физике и техническим наукам",
                "description_en": "Scientific journal on physics and technical sciences",
                "description_kg": "Физика жана техникалык илимдер боюнча илимий журнал",
                "volume_number": 1,
                "issue_number": 1,
                "year": 2024,
                "publication_date": date(2024, 3, 15),
                "issn_print": "1234-5678",
                "issn_online": "8765-4321",
                "is_featured": True,
                "is_published": True,
                "order": 1,
            },
            {
                "title_ru": "Вестник Физической Академии",
                "title_en": "Bulletin of Physical Academy",
                "title_kg": "Физикалык академиянын жарчысы",
                "description_ru": "Научный журнал по физике и техническим наукам",
                "description_en": "Scientific journal on physics and technical sciences",
                "description_kg": "Физика жана техникалык илимдер боюнча илимий журнал",
                "volume_number": 1,
                "issue_number": 2,
                "year": 2024,
                "publication_date": date(2024, 6, 15),
                "issn_print": "1234-5678",
                "issn_online": "8765-4321",
                "is_featured": False,
                "is_published": True,
                "order": 2,
            },
            {
                "title_ru": "Вестник Физической Академии",
                "title_en": "Bulletin of Physical Academy",
                "title_kg": "Физикалык академиянын жарчысы",
                "description_ru": "Научный журнал по физике и техническим наукам",
                "description_en": "Scientific journal on physics and technical sciences",
                "description_kg": "Физика жана техникалык илимдер боюнча илимий журнал",
                "volume_number": 1,
                "issue_number": 3,
                "year": 2024,
                "publication_date": date(2024, 9, 15),
                "issn_print": "1234-5678",
                "issn_online": "8765-4321",
                "is_featured": False,
                "is_published": True,
                "order": 3,
            },
        ]

        for issue_data in sample_issues:
            issue, created = VestnikIssue.objects.get_or_create(
                volume_number=issue_data["volume_number"],
                issue_number=issue_data["issue_number"],
                year=issue_data["year"],
                defaults=issue_data,
            )
            if created:
                self.stdout.write(
                    f"Created issue: Vol.{issue.volume_number} №{issue.issue_number} ({issue.year})"
                )

                # Create sample articles for this issue
                sample_articles = [
                    {
                        "title_ru": "Квантовые эффекты в наноматериалах",
                        "title_en": "Quantum effects in nanomaterials",
                        "author_ru": "А.И. Петров, Б.С. Сидоров",
                        "author_en": "A.I. Petrov, B.S. Sidorov",
                        "abstract_ru": "Исследование квантовых эффектов в наноструктурах",
                        "abstract_en": "Study of quantum effects in nanostructures",
                        "keywords_ru": "квантовая физика, наноматериалы, наноструктуры",
                        "keywords_en": "quantum physics, nanomaterials, nanostructures",
                        "pages_from": 1,
                        "pages_to": 15,
                        "article_type": "research",
                        "order": 1,
                    },
                    {
                        "title_ru": "Теплопроводность композитных материалов",
                        "title_en": "Thermal conductivity of composite materials",
                        "author_ru": "В.Н. Кузнецов",
                        "author_en": "V.N. Kuznetsov",
                        "abstract_ru": "Анализ теплопроводности новых композитных материалов",
                        "abstract_en": "Analysis of thermal conductivity of new composite materials",
                        "keywords_ru": "теплопроводность, композиты, материаловедение",
                        "keywords_en": "thermal conductivity, composites, materials science",
                        "pages_from": 16,
                        "pages_to": 28,
                        "article_type": "research",
                        "order": 2,
                    },
                ]

                for article_data in sample_articles:
                    article_data["issue"] = issue
                    VestnikArticle.objects.get_or_create(
                        issue=issue, order=article_data["order"], defaults=article_data
                    )
                    self.stdout.write(f'  Created article: {article_data["title_ru"]}')
            else:
                self.stdout.write(
                    f"Issue already exists: Vol.{issue.volume_number} №{issue.issue_number} ({issue.year})"
                )

        self.stdout.write(
            self.style.SUCCESS("Successfully created/updated sample data!")
        )
