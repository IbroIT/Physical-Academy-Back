from django.core.management.base import BaseCommand
from main_page.models import MissionCategory, Mission


class Command(BaseCommand):
    help = "Добавляет тестовые данные для миссии, видения, ценностей и стратегии"

    def handle(self, *args, **options):
        self.stdout.write("Добавление тестовых данных для миссии...")

        # Создание категорий
        mission_cat, _ = MissionCategory.objects.get_or_create(
            name_ru="Миссия", defaults={"name_en": "Mission", "name_kg": "Миссия"}
        )

        vision_cat, _ = MissionCategory.objects.get_or_create(
            name_ru="Видение", defaults={"name_en": "Vision", "name_kg": "Көрүнүш"}
        )

        values_cat, _ = MissionCategory.objects.get_or_create(
            name_ru="Ценности",
            defaults={"name_en": "Values", "name_kg": "Баалуулуктар"},
        )

        strategy_cat, _ = MissionCategory.objects.get_or_create(
            name_ru="Стратегия",
            defaults={"name_en": "Strategy", "name_kg": "Стратегия"},
        )

        # Создание миссии
        Mission.objects.get_or_create(
            category=mission_cat,
            defaults={
                "title_ru": "Наша Миссия",
                "title_en": "Our Mission",
                "title_kg": "Биздин миссия",
                "description_ru": "Развивать физическую культуру и спортивную науку через качественное образование, инновационные исследования и подготовку лидеров, способных изменить мир спорта и здорового образа жизни.",
                "description_en": "To develop physical culture and sports science through quality education, innovative research and training leaders capable of changing the world of sports and healthy lifestyles.",
                "description_kg": "Сапаттуу билим берүү, инновациялык изилдөөлөр жана спорттун жана ден-соолук жашоо образынын дүйнөсүн өзгөртүүгө жөндөмдүү лидерлерди даярдоо аркылуу дене тарбия жана спорт илимин өнүктүрүү.",
            },
        )

        # Создание видения
        Mission.objects.get_or_create(
            category=vision_cat,
            defaults={
                "title_ru": "Наше Видение",
                "title_en": "Our Vision",
                "title_kg": "Биздин көрүнүш",
                "description_ru": "Стать мировым лидером в области спортивного образования, где каждый студент раскрывает свой потенциал, а научные открытия формируют будущее физической культуры и здоровья человечества.",
                "description_en": "To become a world leader in sports education, where every student realizes their potential, and scientific discoveries shape the future of physical culture and human health.",
                "description_kg": "Спорттук билим берүү тармагында дүйнөлүк лидер болуу, мында ар бир студент өзүнүн потенциалын ачат, ал эми илимий ачылыштар адамзаттын дене тарбиясынын жана ден-соолугунун келечегин калыптандырат.",
            },
        )

        # Создание ценностей
        values_data = [
            {
                "title_ru": "Академическое превосходство",
                "title_en": "Academic Excellence",
                "title_kg": "Академиялык артыкчылык",
                "description_ru": "Стремимся к высочайшим стандартам образования и научных исследований в области физической культуры",
                "description_en": "We strive for the highest standards of education and research in physical culture",
                "description_kg": "Биз дене тарбия тармагында билим берүү жана илимий изилдөөлөрдүн эң жогорку стандарттарына умтулабыз",
            },
            {
                "title_ru": "Инновации и прогресс",
                "title_en": "Innovation and Progress",
                "title_kg": "Инновация жана прогресс",
                "description_ru": "Внедряем передовые технологии и методики для развития спортивной науки и практики",
                "description_en": "We implement advanced technologies and methods for the development of sports science and practice",
                "description_kg": "Биз спорттук илим жана практиканы өнүктүрүү үчүн алдыңкы технологияларды жана ыкмаларды киргизебиз",
            },
            {
                "title_ru": "Сообщество и сотрудничество",
                "title_en": "Community and Collaboration",
                "title_kg": "Жамаат жана кызматташтык",
                "description_ru": "Создаем поддерживающую среду, где студенты, преподаватели и спортсмены растут вместе",
                "description_en": "We create a supportive environment where students, teachers and athletes grow together",
                "description_kg": "Биз студенттер, мугалимдер жана спортчулар чогуу өсүп-өнүгүү чөйрөсүн түзөбүз",
            },
            {
                "title_ru": "Научный подход",
                "title_en": "Scientific Approach",
                "title_kg": "Илимий мамиле",
                "description_ru": "Основываем все решения на доказательных исследованиях и данных современной науки",
                "description_en": "We base all decisions on evidence-based research and modern science data",
                "description_kg": "Биз бардык чечимдерди далилденген изилдөөлөргө жана заманбап илимдин маалыматтарына негиздейбиз",
            },
        ]

        for value_data in values_data:
            Mission.objects.get_or_create(
                category=values_cat,
                title_ru=value_data["title_ru"],
                defaults=value_data,
            )

        # Создание стратегических целей
        strategy_data = [
            {
                "title_ru": "Цифровая трансформация образования",
                "title_en": "Digital Transformation of Education",
                "title_kg": "Билим берүүнүн санариптик трансформациясы",
                "description_ru": "Внедрение VR-технологий в тренировочный процесс, создание цифровой образовательной платформы, разработка мобильных приложений для студентов",
                "description_en": "Implementation of VR technologies in the training process, creation of a digital educational platform, development of mobile applications for students",
                "description_kg": "Машыгуу процессине VR технологияларын киргизүү, санариптик билим берүү платформасын түзүү, студенттер үчүн мобилдик тиркемелерди иштеп чыгуу",
            },
            {
                "title_ru": "Международное признание",
                "title_en": "International Recognition",
                "title_kg": "Эл аралык таануу",
                "description_ru": "Аккредитация в международных спортивных ассоциациях, увеличение иностранных студентов на 200%, партнерства с ведущими мировыми вузами",
                "description_en": "Accreditation in international sports associations, increase in foreign students by 200%, partnerships with leading world universities",
                "description_kg": "Эл аралык спорт ассоциацияларында аккредитация, чет өлкөлүк студенттердин 200%га көбөйүшү, дүйнөнүн алдыңкы университеттери менен өнөктөштүк",
            },
            {
                "title_ru": "Инновационный кампус",
                "title_en": "Innovative Campus",
                "title_kg": "Инновациялык кампус",
                "description_ru": "Строительство умных спортивных объектов, создание исследовательских центров мирового уровня, внедрение устойчивых экологических решений",
                "description_en": "Construction of smart sports facilities, creation of world-class research centers, implementation of sustainable environmental solutions",
                "description_kg": "Акылдуу спорттук объекттерди куруу, дүйнөлүк деңгээлдеги изилдөө борборлорун түзүү, туруктуу экологиялык чечимдерди киргизүү",
            },
        ]

        for strat_data in strategy_data:
            Mission.objects.get_or_create(
                category=strategy_cat,
                title_ru=strat_data["title_ru"],
                defaults=strat_data,
            )

        self.stdout.write(self.style.SUCCESS("✅ Тестовые данные успешно добавлены!"))
        self.stdout.write(f"Создано категорий: {MissionCategory.objects.count()}")
        self.stdout.write(f"Создано записей миссий: {Mission.objects.count()}")
