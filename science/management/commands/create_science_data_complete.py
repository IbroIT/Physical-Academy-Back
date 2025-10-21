from django.core.management.base import BaseCommand
from django.utils import timezone
from science.models import (
    # Publication models
    Publication,
    PublicationStats,
    # Vestnik models
    VestnikIssue,
    VestnikArticle,
    VestnikStats,
    # Scopus models
    ScopusSection,
    ScopusMetrics,
    ScopusDocumentType,
    ScopusPublication,
    ScopusStats,
    # NTS Committee models
    NTSCommitteeRole,
    NTSResearchDirection,
    NTSCommitteeMember,
    NTSCommitteeSection,
)


class Command(BaseCommand):
    help = "Creates sample data for all science-related models"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating data for all science-related models...")

        # Create publications
        self.create_publications()

        # Create Vestnik data
        self.create_vestnik()

        # Create Scopus data
        self.create_scopus()

        # Create NTS Committee data
        self.create_nts_committee()

        self.stdout.write(self.style.SUCCESS("Science data created successfully!"))

    def create_publications(self):
        # Create publication stats
        stats = [
            {
                "label_ru": "Всего публикаций",
                "label_en": "Total publications",
                "value": "325+",
                "icon": "📚",
                "order": 1,
            },
            {
                "label_ru": "Цитирований",
                "label_en": "Citations",
                "value": "1240+",
                "icon": "📝",
                "order": 2,
            },
            {
                "label_ru": "H-индекс",
                "label_en": "H-index",
                "value": "14",
                "icon": "📊",
                "order": 3,
            },
        ]

        for stat in stats:
            PublicationStats.objects.get_or_create(**stat)

        # Create publications
        publications = [
            {
                "title_ru": "Методы машинного обучения в спортивной аналитике",
                "title_en": "Machine Learning Methods in Sports Analytics",
                "author_ru": "Иванов А.С., Петров В.П.",
                "author_en": "Ivanov A.S., Petrov V.P.",
                "abstract_ru": "Анализ применения методов машинного обучения для анализа спортивных данных.",
                "abstract_en": "Analysis of machine learning methods application for sports data analysis.",
                "publication_type": "article",
                "year": 2023,
                "journal": "Journal of Sports Analytics",
                "citation_count": 12,
                "impact_factor": 2.4,
                "is_featured": True,
                "order": 1,
            },
            {
                "title_ru": "Биомеханика движений в командных видах спорта",
                "title_en": "Biomechanics of Movements in Team Sports",
                "author_ru": "Смирнов К.Л., Алексеев Д.М.",
                "author_en": "Smirnov K.L., Alekseev D.M.",
                "abstract_ru": "Исследование биомеханики движений спортсменов в командных видах спорта.",
                "abstract_en": "Research on biomechanics of athletes' movements in team sports.",
                "publication_type": "article",
                "year": 2022,
                "journal": "Sports Biomechanics Journal",
                "citation_count": 8,
                "impact_factor": 1.8,
                "is_featured": True,
                "order": 2,
            },
            {
                "title_ru": "Влияние высокоинтенсивных интервальных тренировок на выносливость",
                "title_en": "Impact of High-Intensity Interval Training on Endurance",
                "author_ru": "Козлов М.М., Николаев С.В.",
                "author_en": "Kozlov M.M., Nikolaev S.V.",
                "abstract_ru": "Анализ влияния HIIT на выносливость профессиональных спортсменов.",
                "abstract_en": "Analysis of HIIT impact on endurance of professional athletes.",
                "publication_type": "article",
                "year": 2023,
                "journal": "Journal of Training Science",
                "citation_count": 5,
                "impact_factor": 2.1,
                "is_featured": False,
                "order": 3,
            },
        ]

        for pub in publications:
            Publication.objects.get_or_create(**pub)

        self.stdout.write(
            f"Created {len(stats)} publication stats and {len(publications)} publications"
        )

    def create_vestnik(self):
        # Create Vestnik stats
        stats = [
            {
                "label_ru": "Выпусков",
                "label_en": "Issues",
                "value": "16",
                "icon": "📘",
                "order": 1,
            },
            {
                "label_ru": "Статей",
                "label_en": "Articles",
                "value": "320+",
                "icon": "📄",
                "order": 2,
            },
            {
                "label_ru": "Лет издания",
                "label_en": "Years of publishing",
                "value": "4",
                "icon": "📅",
                "order": 3,
            },
        ]

        for stat in stats:
            VestnikStats.objects.get_or_create(**stat)

        # Create Vestnik issues
        issues = [
            {
                "title_ru": "Вестник физической академии",
                "title_en": "Physical Academy Bulletin",
                "description_ru": "Научный журнал, посвященный вопросам физической культуры и спорта",
                "description_en": "Scientific journal dedicated to physical education and sports",
                "volume_number": 4,
                "issue_number": 2,
                "year": 2023,
                "publication_date": timezone.now(),
                "is_featured": True,
                "is_published": True,
                "order": 1,
            },
            {
                "title_ru": "Вестник физической академии",
                "title_en": "Physical Academy Bulletin",
                "description_ru": "Научный журнал, посвященный вопросам физической культуры и спорта",
                "description_en": "Scientific journal dedicated to physical education and sports",
                "volume_number": 4,
                "issue_number": 1,
                "year": 2023,
                "publication_date": timezone.now() - timezone.timedelta(days=90),
                "is_featured": False,
                "is_published": True,
                "order": 2,
            },
        ]

        created_issues = []
        for issue_data in issues:
            issue, created = VestnikIssue.objects.get_or_create(
                volume_number=issue_data["volume_number"],
                issue_number=issue_data["issue_number"],
                defaults=issue_data,
            )
            created_issues.append(issue)

        # Create Vestnik articles
        articles = [
            {
                "title_ru": "Современные методики тренировки в легкой атлетике",
                "title_en": "Modern training methods in athletics",
                "author_ru": "Петров И.А., Сидоров В.М.",
                "author_en": "Petrov I.A., Sidorov V.M.",
                "abstract_ru": "Обзор современных методик тренировки в легкой атлетике",
                "abstract_en": "Review of modern training methods in athletics",
                "article_type": "research",
                "pages_from": 5,
                "pages_to": 15,
                "issue": created_issues[0],
                "order": 1,
            },
            {
                "title_ru": "Психологическая подготовка спортсменов к соревнованиям",
                "title_en": "Psychological preparation of athletes for competitions",
                "author_ru": "Иванова А.С., Козлова Е.П.",
                "author_en": "Ivanova A.S., Kozlova E.P.",
                "abstract_ru": "Исследование методов психологической подготовки спортсменов",
                "abstract_en": "Research on psychological preparation methods for athletes",
                "article_type": "research",
                "pages_from": 16,
                "pages_to": 28,
                "issue": created_issues[0],
                "order": 2,
            },
        ]

        for article_data in articles:
            VestnikArticle.objects.get_or_create(
                title_ru=article_data["title_ru"],
                issue=article_data["issue"],
                defaults=article_data,
            )

        self.stdout.write(
            f"Created {len(stats)} Vestnik stats, {len(issues)} issues, and {len(articles)} articles"
        )

    def create_scopus(self):
        # Create Scopus metrics
        metrics = [
            {
                "label_ru": "Публикаций в Scopus",
                "label_en": "Publications in Scopus",
                "description_ru": "Общее количество публикаций в базе данных Scopus",
                "description_en": "Total number of publications in Scopus database",
                "value": "185+",
                "icon": "📊",
                "trend": "increasing",
                "order": 1,
            },
            {
                "label_ru": "Цитирований",
                "label_en": "Citations",
                "description_ru": "Общее количество цитирований в Scopus",
                "description_en": "Total number of citations in Scopus",
                "value": "720+",
                "icon": "📈",
                "trend": "increasing",
                "order": 2,
            },
            {
                "label_ru": "H-индекс",
                "label_en": "H-index",
                "description_ru": "Индекс Хирша по данным Scopus",
                "description_en": "H-index according to Scopus data",
                "value": "12",
                "icon": "🔝",
                "trend": "stable",
                "order": 3,
            },
        ]

        for metric in metrics:
            ScopusMetrics.objects.get_or_create(**metric)

        # Create document types
        doc_types = [
            {
                "name_ru": "Научные статьи",
                "name_en": "Articles",
                "count": 105,
                "percentage": 56.8,
                "color": "#3366CC",
                "order": 1,
            },
            {
                "name_ru": "Материалы конференций",
                "name_en": "Conference Papers",
                "count": 45,
                "percentage": 24.3,
                "color": "#33AA33",
                "order": 2,
            },
            {
                "name_ru": "Обзоры",
                "name_en": "Reviews",
                "count": 28,
                "percentage": 15.1,
                "color": "#FF9900",
                "order": 3,
            },
            {
                "name_ru": "Другое",
                "name_en": "Other",
                "count": 7,
                "percentage": 3.8,
                "color": "#AAAAAA",
                "order": 4,
            },
        ]

        for doc_type in doc_types:
            ScopusDocumentType.objects.get_or_create(**doc_type)

        # Create publications
        publications = [
            {
                "title_ru": "Применение искусственного интеллекта в анализе спортивных результатов",
                "title_en": "Application of Artificial Intelligence in Sports Results Analysis",
                "authors_ru": "Петров А.В., Смирнов М.М.",
                "authors_en": "Petrov A.V., Smirnov M.M.",
                "journal_ru": "Международный журнал спортивной науки",
                "journal_en": "International Journal of Sports Science",
                "abstract_ru": "Исследование применения методов искусственного интеллекта для анализа спортивных результатов.",
                "abstract_en": "Research on the application of artificial intelligence methods for analyzing sports results.",
                "year": 2023,
                "citation_count": 8,
                "document_type": "Article",
                "subject_area": "Sports Science",
                "is_featured": True,
                "order": 1,
                "url": "https://example.com/scopus/1",
            },
            {
                "title_ru": "Биомеханический анализ техники выполнения силовых упражнений",
                "title_en": "Biomechanical Analysis of Power Exercise Techniques",
                "authors_ru": "Иванов К.С., Козлов Д.В.",
                "authors_en": "Ivanov K.S., Kozlov D.V.",
                "journal_ru": "Журнал биомеханики спорта",
                "journal_en": "Journal of Sports Biomechanics",
                "abstract_ru": "Анализ биомеханики выполнения основных силовых упражнений.",
                "abstract_en": "Analysis of biomechanics of basic power exercises.",
                "year": 2022,
                "citation_count": 12,
                "document_type": "Article",
                "subject_area": "Biomechanics",
                "is_featured": True,
                "order": 2,
                "url": "https://example.com/scopus/2",
            },
            {
                "title_ru": "Влияние периодизации тренировок на результативность в циклических видах спорта",
                "title_en": "Impact of Training Periodization on Performance in Cyclic Sports",
                "authors_ru": "Соколов А.А., Николаев В.В.",
                "authors_en": "Sokolov A.A., Nikolaev V.V.",
                "journal_ru": "Наука о спортивных тренировках",
                "journal_en": "Science of Sports Training",
                "abstract_ru": "Исследование влияния различных моделей периодизации тренировок на результаты в циклических видах спорта.",
                "abstract_en": "Research on the impact of various training periodization models on results in cyclic sports.",
                "year": 2023,
                "citation_count": 5,
                "document_type": "Review",
                "subject_area": "Training Science",
                "is_featured": False,
                "order": 3,
                "url": "https://example.com/scopus/3",
            },
        ]

        for pub_data in publications:
            ScopusPublication.objects.get_or_create(
                title_ru=pub_data["title_ru"], year=pub_data["year"], defaults=pub_data
            )

        # Create Scopus stats
        stats = [
            {
                "label_ru": "В топ-10% журналах",
                "label_en": "In top-10% journals",
                "value": "35%",
                "icon": "🏆",
                "order": 1,
            },
            {
                "label_ru": "Международное соавторство",
                "label_en": "International co-authorship",
                "value": "42%",
                "icon": "🌐",
                "order": 2,
            },
            {
                "label_ru": "Цитирования на публикацию",
                "label_en": "Citations per publication",
                "value": "3.9",
                "icon": "📝",
                "order": 3,
            },
        ]

        for stat in stats:
            ScopusStats.objects.get_or_create(**stat)

        self.stdout.write(
            f"Created {len(metrics)} Scopus metrics, {len(doc_types)} document types, {len(publications)} publications, {len(stats)} stats"
        )

    def create_nts_committee(self):
        # Create committee roles
        roles = [
            {
                "name_ru": "Председатель",
                "name_en": "Chairman",
                "description_ru": "Руководит работой Научно-технического совета",
                "description_en": "Leads the work of the Scientific and Technical Council",
            },
            {
                "name_ru": "Заместитель председателя",
                "name_en": "Vice Chairman",
                "description_ru": "Помогает председателю в управлении советом",
                "description_en": "Assists the chairman in managing the council",
            },
            {
                "name_ru": "Секретарь",
                "name_en": "Secretary",
                "description_ru": "Ведет документацию и протоколы заседаний",
                "description_en": "Maintains documentation and meeting minutes",
            },
            {
                "name_ru": "Член совета",
                "name_en": "Council Member",
                "description_ru": "Участвует в работе совета и принятии решений",
                "description_en": "Participates in council work and decision-making",
            },
        ]

        role_objects = {}
        for role_data in roles:
            role, created = NTSCommitteeRole.objects.get_or_create(
                name_ru=role_data["name_ru"], defaults=role_data
            )
            role_objects[role_data["name_ru"]] = role

        # Create research directions
        directions = [
            {
                "name_ru": "Спортивная медицина",
                "name_en": "Sports Medicine",
                "description_ru": "Исследования в области спортивной медицины и реабилитации",
                "description_en": "Research in sports medicine and rehabilitation",
            },
            {
                "name_ru": "Биомеханика спорта",
                "name_en": "Sports Biomechanics",
                "description_ru": "Изучение биомеханики движений спортсменов",
                "description_en": "Study of biomechanics of athletes' movements",
            },
            {
                "name_ru": "Спортивная психология",
                "name_en": "Sports Psychology",
                "description_ru": "Психологические аспекты спортивной деятельности",
                "description_en": "Psychological aspects of sports activities",
            },
            {
                "name_ru": "Теория и методика физического воспитания",
                "name_en": "Theory and Methods of Physical Education",
                "description_ru": "Разработка методик физического воспитания и тренировки",
                "description_en": "Development of physical education and training methods",
            },
        ]

        direction_objects = {}
        for dir_data in directions:
            direction, created = NTSResearchDirection.objects.get_or_create(
                name_ru=dir_data["name_ru"], defaults=dir_data
            )
            direction_objects[dir_data["name_ru"]] = direction

        # Create committee members
        members = [
            {
                "name_ru": "Иванов Александр Петрович",
                "name_en": "Ivanov Alexander Petrovich",
                "position_ru": "Доктор медицинских наук, профессор",
                "position_en": "Doctor of Medical Sciences, Professor",
                "bio_ru": "Специалист в области спортивной медицины с 20-летним опытом работы",
                "bio_en": "Specialist in sports medicine with 20 years of experience",
                "email": "ivanov@example.com",
                "phone": "+996700123456",
                "role": role_objects["Председатель"],
                "research_direction": direction_objects["Спортивная медицина"],
                "is_active": True,
                "order": 1,
            },
            {
                "name_ru": "Петрова Елена Сергеевна",
                "name_en": "Petrova Elena Sergeevna",
                "position_ru": "Кандидат психологических наук, доцент",
                "position_en": "PhD in Psychology, Associate Professor",
                "bio_ru": "Исследователь в области спортивной психологии",
                "bio_en": "Researcher in sports psychology",
                "email": "petrova@example.com",
                "phone": "+996700234567",
                "role": role_objects["Заместитель председателя"],
                "research_direction": direction_objects["Спортивная психология"],
                "is_active": True,
                "order": 2,
            },
            {
                "name_ru": "Смирнов Михаил Владимирович",
                "name_en": "Smirnov Mikhail Vladimirovich",
                "position_ru": "Доктор педагогических наук, профессор",
                "position_en": "Doctor of Pedagogical Sciences, Professor",
                "bio_ru": "Эксперт по теории и методике физического воспитания",
                "bio_en": "Expert in theory and methods of physical education",
                "email": "smirnov@example.com",
                "phone": "+996700345678",
                "role": role_objects["Член совета"],
                "research_direction": direction_objects[
                    "Теория и методика физического воспитания"
                ],
                "is_active": True,
                "order": 3,
            },
        ]

        for member_data in members:
            NTSCommitteeMember.objects.get_or_create(
                name_ru=member_data["name_ru"],
                email=member_data["email"],
                defaults=member_data,
            )

        # Create committee sections
        sections = [
            {
                "section_key": "about",
                "title_ru": "О совете",
                "title_en": "About the Council",
                "description_ru": "Научно-технический совет (НТС) является консультативным органом, созданным для координации научно-исследовательской деятельности в области физической культуры и спорта.",
                "description_en": "The Scientific and Technical Council (STC) is an advisory body established to coordinate research activities in the field of physical culture and sports.",
            },
            {
                "section_key": "mission",
                "title_ru": "Миссия",
                "title_en": "Mission",
                "description_ru": "Миссия НТС - содействовать развитию научных исследований, внедрению инноваций и повышению качества образования в области физической культуры и спорта.",
                "description_en": "The mission of the STC is to promote the development of scientific research, implementation of innovations, and improvement of education quality in the field of physical culture and sports.",
            },
            {
                "section_key": "tasks",
                "title_ru": "Задачи",
                "title_en": "Tasks",
                "description_ru": "Основные задачи НТС: координация научно-исследовательской работы, экспертиза научных проектов, организация научных мероприятий, содействие публикационной активности.",
                "description_en": "The main tasks of the STC: coordination of research work, expertise of scientific projects, organization of scientific events, promotion of publication activity.",
            },
        ]

        for section_data in sections:
            NTSCommitteeSection.objects.get_or_create(
                section_key=section_data["section_key"], defaults=section_data
            )

        self.stdout.write(
            f"Created {len(roles)} NTS Committee roles, {len(directions)} research directions, {len(members)} committee members, {len(sections)} sections"
        )
