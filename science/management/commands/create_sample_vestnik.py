from django.core.management.base import BaseCommand
from science.models import VestnikIssue, VestnikArticle, VestnikStats
from datetime import date


class Command(BaseCommand):
    help = "Create sample Vestnik issues, articles and statistics for testing"

    def handle(self, *args, **options):
        # Create sample statistics
        stats_data = [
            {
                "label_ru": "Выпущено номеров",
                "label_en": "Issues Published",
                "label_kg": "Чыгарылган саны",
                "value": 48,
                "icon": "📚",
                "order": 1,
            },
            {
                "label_ru": "Научных статей",
                "label_en": "Scientific Articles",
                "label_kg": "Илимий макалалар",
                "value": 324,
                "icon": "📄",
                "order": 2,
            },
            {
                "label_ru": "Лет издания",
                "label_en": "Years of Publication",
                "label_kg": "Басып чыгаруу жылы",
                "value": 12,
                "icon": "📅",
                "order": 3,
            },
            {
                "label_ru": "Средних цитирований",
                "label_en": "Average Citations",
                "label_kg": "Орточо цитаталар",
                "value": 7,
                "icon": "📈",
                "order": 4,
            },
        ]

        for stat_data in stats_data:
            stat, created = VestnikStats.objects.get_or_create(
                label_ru=stat_data["label_ru"], defaults=stat_data
            )
            if created:
                self.stdout.write(f"Created Vestnik statistic: {stat.label_ru}")

        # Create sample Vestnik issues
        issues_data = [
            {
                "title_ru": "Вестник Кыргызской физической академии - Том 4, №2",
                "title_en": "Bulletin of Kyrgyz Physical Academy - Vol. 4, No. 2",
                "title_kg": "Кыргыз физика академиясынын жарчысы - 4-том, №2",
                "description_ru": "Специальный выпуск, посвященный современным методам в физике и математике. Содержит передовые исследования в области квантовой механики, статистической физики и математического моделирования.",
                "description_en": "Special issue dedicated to modern methods in physics and mathematics. Contains cutting-edge research in quantum mechanics, statistical physics, and mathematical modeling.",
                "description_kg": "Физика жана математикадагы заманбап ыкмаларга арналган атайын чыгарылыш. Квант механикасы, статистикалык физика жана математикалык моделдештирүү тармагындагы алдыңкы изилдөөлөрдү камтыйт.",
                "volume_number": 4,
                "issue_number": 2,
                "year": 2024,
                "publication_date": date(2024, 6, 15),
                "issn_print": "1694-5220",
                "issn_online": "1694-5239",
                "doi_prefix": "10.52754/16945220",
                "is_featured": True,
                "order": 1,
            },
            {
                "title_ru": "Вестник Кыргызской физической академии - Том 4, №1",
                "title_en": "Bulletin of Kyrgyz Physical Academy - Vol. 4, No. 1",
                "title_kg": "Кыргыз физика академиясынын жарчысы - 4-том, №1",
                "description_ru": "Первый выпуск четвертого тома содержит исследования в области теоретической физики, астрофизики и нанотехнологий.",
                "description_en": "The first issue of the fourth volume contains research in theoretical physics, astrophysics, and nanotechnology.",
                "description_kg": "Төртүнчү томдун биринчи чыгарылышы теориялык физика, астрофизика жана нанотехнология тармагындагы изилдөөлөрдү камтыйт.",
                "volume_number": 4,
                "issue_number": 1,
                "year": 2024,
                "publication_date": date(2024, 3, 10),
                "issn_print": "1694-5220",
                "issn_online": "1694-5239",
                "doi_prefix": "10.52754/16945220",
                "is_featured": True,
                "order": 2,
            },
            {
                "title_ru": "Вестник Кыргызской физической академии - Том 3, №4",
                "title_en": "Bulletin of Kyrgyz Physical Academy - Vol. 3, No. 4",
                "title_kg": "Кыргыз физика академиясынын жарчысы - 3-том, №4",
                "description_ru": "Заключительный выпуск третьего тома с исследованиями в области физики твердого тела и материаловедения.",
                "description_en": "The final issue of the third volume featuring research in solid state physics and materials science.",
                "description_kg": "Катуу дене физикасы жана материалтануу тармагындагы изилдөөлөр менен үчүнчү томдун акыркы чыгарылышы.",
                "volume_number": 3,
                "issue_number": 4,
                "year": 2023,
                "publication_date": date(2023, 12, 20),
                "issn_print": "1694-5220",
                "issn_online": "1694-5239",
                "doi_prefix": "10.52754/16945220",
                "is_featured": False,
                "order": 3,
            },
        ]

        for issue_data in issues_data:
            issue, created = VestnikIssue.objects.get_or_create(
                volume_number=issue_data["volume_number"],
                issue_number=issue_data["issue_number"],
                year=issue_data["year"],
                defaults=issue_data,
            )
            if created:
                self.stdout.write(f"Created Vestnik issue: {issue}")

        # Create sample articles
        # Get the first issue to add articles to
        if VestnikIssue.objects.exists():
            first_issue = VestnikIssue.objects.first()

            articles_data = [
                {
                    "issue": first_issue,
                    "title_ru": "Квантовые эффекты в низкоразмерных системах",
                    "title_en": "Quantum Effects in Low-Dimensional Systems",
                    "title_kg": "Төмөнкү өлчөмдүү системалардагы квант эффекттери",
                    "author_ru": "А.К. Турдубеков, С.М. Осмонова",
                    "author_en": "A.K. Turdubekov, S.M. Osmonova",
                    "author_kg": "А.К. Турдубеков, С.М. Осмонова",
                    "abstract_ru": "В данной работе исследуются квантовые эффекты в низкоразмерных системах. Рассматриваются теоретические модели и экспериментальные методы изучения квантовых явлений в наноструктурах.",
                    "abstract_en": "This paper investigates quantum effects in low-dimensional systems. Theoretical models and experimental methods for studying quantum phenomena in nanostructures are considered.",
                    "abstract_kg": "Бул эмгекте төмөнкү өлчөмдүү системалардагы квант эффекттери изилденет. Наноструктуралардагы квант кубулуштарын изилдөөнүн теориялык моделдери жана эксперименталдык ыкмалары каралат.",
                    "keywords_ru": "квантовая механика, наноструктуры, низкоразмерные системы, квантовые эффекты",
                    "keywords_en": "quantum mechanics, nanostructures, low-dimensional systems, quantum effects",
                    "keywords_kg": "квант механикасы, наноструктуралар, төмөнкү өлчөмдүү системалар, квант эффекттери",
                    "pages_from": 5,
                    "pages_to": 18,
                    "doi": "10.52754/16945220.2024.2.001",
                    "article_type": "research",
                    "citation_count": 12,
                    "order": 1,
                },
                {
                    "issue": first_issue,
                    "title_ru": "Математическое моделирование физических процессов",
                    "title_en": "Mathematical Modeling of Physical Processes",
                    "title_kg": "Физикалык процесстерди математикалык моделдештирүү",
                    "author_ru": "М.Н. Касымов, Э.Б. Жумабекова",
                    "author_en": "M.N. Kasymov, E.B. Zhumabekova",
                    "author_kg": "М.Н. Касымов, Э.Б. Жумабекова",
                    "abstract_ru": "Представлены новые подходы к математическому моделированию сложных физических процессов с использованием современных вычислительных методов.",
                    "abstract_en": "New approaches to mathematical modeling of complex physical processes using modern computational methods are presented.",
                    "abstract_kg": "Заманбап эсептөө ыкмаларын колдонуу менен татаал физикалык процесстерди математикалык моделдештирүүнүн жаңы мамилелери берилген.",
                    "keywords_ru": "математическое моделирование, физические процессы, вычислительные методы",
                    "keywords_en": "mathematical modeling, physical processes, computational methods",
                    "keywords_kg": "математикалык моделдештирүү, физикалык процесстер, эсептөө ыкмалары",
                    "pages_from": 19,
                    "pages_to": 34,
                    "doi": "10.52754/16945220.2024.2.002",
                    "article_type": "research",
                    "citation_count": 8,
                    "order": 2,
                },
                {
                    "issue": first_issue,
                    "title_ru": "Современные тенденции в астрофизике",
                    "title_en": "Modern Trends in Astrophysics",
                    "title_kg": "Астрофизикадагы заманбап тенденциялар",
                    "author_ru": "К.Т. Алымкулов",
                    "author_en": "K.T. Alymkulov",
                    "author_kg": "К.Т. Алымкулов",
                    "abstract_ru": "Обзор современных направлений исследований в астрофизике, включая изучение темной материи, черных дыр и экзопланет.",
                    "abstract_en": "A review of current research directions in astrophysics, including studies of dark matter, black holes, and exoplanets.",
                    "abstract_kg": "Астрофизикадагы заманбап изилдөө багыттарынын сереп, анын ичинде кара материя, кара тешиктер жана экзопланеталарды изилдөө.",
                    "keywords_ru": "астрофизика, темная материя, черные дыры, экзопланеты",
                    "keywords_en": "astrophysics, dark matter, black holes, exoplanets",
                    "keywords_kg": "астрофизика, кара материя, кара тешиктер, экзопланеталар",
                    "pages_from": 35,
                    "pages_to": 48,
                    "doi": "10.52754/16945220.2024.2.003",
                    "article_type": "review",
                    "citation_count": 15,
                    "order": 3,
                },
            ]

            for article_data in articles_data:
                article, created = VestnikArticle.objects.get_or_create(
                    issue=article_data["issue"],
                    title_ru=article_data["title_ru"],
                    defaults=article_data,
                )
                if created:
                    self.stdout.write(f"Created Vestnik article: {article.title_ru}")

        self.stdout.write(
            self.style.SUCCESS("Successfully created sample Vestnik data!")
        )
