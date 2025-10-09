"""
Management command to create comprehensive sample data for leadership_structure module
"""
from django.core.management.base import BaseCommand
from leadership_structure.models import (
    BoardOfTrustees, BoardOfTrusteesStats,
    AuditCommission, AuditCommissionStatistics,
    AcademicCouncil, TradeUnionBenefit, TradeUnionEvent, TradeUnionStats,
    Commission, AdministrativeDepartment, AdministrativeUnit
)


class Command(BaseCommand):
    help = 'Creates comprehensive sample data for leadership structure module'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Creating comprehensive sample data...\n'))

        # Board of Trustees - 5 members
        self.stdout.write('Creating Board of Trustees...')
        if BoardOfTrustees.objects.count() == 0:
            BoardOfTrustees.objects.create(
                name="Иванов Иван Иванович",
                name_kg="Иванов Иван Иванович",
                name_en="Ivan Ivanov",
                position="Председатель попечительского совета",
                position_kg="Камкорлук кеңешинин төрагасы",
                position_en="Chairman of the Board of Trustees",
                bio="Опытный руководитель с 20-летним стажем управления образовательными учреждениями.",
                bio_kg="20 жылдык тажрыйбасы бар тажрыйбалуу жетекчи.",
                bio_en="Experienced leader with 20 years of educational management experience.",
                achievements=["Создание 5 образовательных программ", "Привлечение инвестиций на 50 млн рублей"],
                achievements_kg=["5 билим берүү программаларын түзүү", "50 млн сом инвестицияларды тартуу"],
                achievements_en=["Created 5 educational programs", "Attracted 50 million rubles in investments"],
                email="ivanov@academy.edu.kg",
                phone="+996 312 123456",
                order=1
            )
            
            BoardOfTrustees.objects.create(
                name="Петрова Мария Сергеевна",
                name_kg="Петрова Мария Сергеевна",
                name_en="Maria Petrova",
                position="Заместитель председателя",
                position_kg="Төраганын орун басары",
                position_en="Vice Chairman",
                bio="Эксперт в области спортивной медицины и физической культуры.",
                bio_kg="Спорттук медицина жана дене тарбия боюнча эксперт.",
                bio_en="Expert in sports medicine and physical education.",
                achievements=["15 научных публикаций", "Разработка инновационных методик тренировок"],
                achievements_kg=["15 илимий жарыялоо", "Инновациялык машыктыруу ыкмаларын иштеп чыгуу"],
                achievements_en=["15 scientific publications", "Development of innovative training methods"],
                email="petrova@academy.edu.kg",
                phone="+996 312 123457",
                order=2
            )
            self.stdout.write(self.style.SUCCESS('✓ Created Board of Trustees members'))

        # Board Stats
        if BoardOfTrusteesStats.objects.count() == 0:
            BoardOfTrusteesStats.objects.create(
                label="Лет опыта",
                label_kg="Тажрыйба жылы",
                label_en="Years of Experience",
                target_value=15,
                icon="📅",
                order=1
            )
            BoardOfTrusteesStats.objects.create(
                label="Проектов",
                label_kg="Долбоорлор",
                label_en="Projects",
                target_value=24,
                icon="🚀",
                order=2
            )
            self.stdout.write(self.style.SUCCESS('✓ Created Board statistics'))

        # Audit Commission
        if AuditCommission.objects.count() == 0:
            AuditCommission.objects.create(
                name="Сидоров Петр Николаевич",
                name_kg="Сидоров Петр Николаевич",
                name_en="Petr Sidorov",
                position="Председатель ревизионной комиссии",
                position_kg="Ревизиялык комиссиянын төрагасы",
                position_en="Chairman of the Audit Commission",
                department="Финансовый отдел",
                department_kg="Финансы бөлүмү",
                department_en="Finance Department",
                achievements=["Проведено 50+ аудитов", "Экономия средств на 10 млн рублей"],
                achievements_kg=["50+ аудит өткөрүлдү", "10 млн сом экономия"],
                achievements_en=["Conducted 50+ audits", "Saved 10 million rubles"],
                order=1
            )
            self.stdout.write(self.style.SUCCESS('✓ Created Audit Commission members'))

        # Audit Commission Statistics
        if AuditCommissionStatistics.objects.count() == 0:
            AuditCommissionStatistics.objects.create(
                label="Аудитов проведено",
                label_kg="Аудиттер өткөрүлдү",
                label_en="Audits Conducted",
                value="56",
                value_kg="56",
                value_en="56",
                order=1
            )
            self.stdout.write(self.style.SUCCESS('✓ Created Audit Commission statistics'))

        # Academic Council
        if AcademicCouncil.objects.count() == 0:
            AcademicCouncil.objects.create(
                name="Профессор Алексеев Дмитрий Владимирович",
                name_kg="Профессор Алексеев Дмитрий Владимирович",
                name_en="Professor Dmitry Alekseev",
                position="Председатель ученого совета",
                position_kg="Илимий кеңештин төрагасы",
                position_en="Chairman of the Academic Council",
                department="Кафедра теории и методики физической культуры",
                department_kg="Дене тарбия теориясы жана методикасы кафедрасы",
                department_en="Department of Theory and Methods of Physical Education",
                achievements=["30+ научных работ", "Руководство 10 диссертаций", "Международные награды"],
                achievements_kg=["30+ илимий эмгектер", "10 диссертацияга жетекчилик", "Эл аралык сыйлыктар"],
                achievements_en=["30+ scientific works", "Supervised 10 dissertations", "International awards"],
                order=1
            )
            self.stdout.write(self.style.SUCCESS('✓ Created Academic Council members'))

        # Trade Union Benefits
        if TradeUnionBenefit.objects.count() == 0:
            TradeUnionBenefit.objects.create(
                title="Медицинское страхование",
                title_kg="Медициналык камсыздандыруу",
                title_en="Medical Insurance",
                description="Полный пакет медицинского страхования для всех членов профсоюза",
                description_kg="Профсоюздун бардык мүчөлөрү үчүн толук медициналык камсыздандыруу пакети",
                description_en="Full medical insurance package for all union members",
                icon="🏥",
                order=1
            )
            TradeUnionBenefit.objects.create(
                title="Материальная помощь",
                title_kg="Материалдык жардам",
                title_en="Financial Assistance",
                description="Финансовая поддержка в сложных жизненных ситуациях",
                description_kg="Татаал жашоо кырдаалдарында каржылык колдоо",
                description_en="Financial support in difficult life situations",
                icon="💰",
                order=2
            )
            self.stdout.write(self.style.SUCCESS('✓ Created Trade Union benefits'))

        # Trade Union Events
        if TradeUnionEvent.objects.count() == 0:
            TradeUnionEvent.objects.create(
                title="Спортивный день",
                title_kg="Спорттук күн",
                title_en="Sports Day",
                description="Ежегодное спортивное мероприятие для сотрудников",
                description_kg="Кызматкерлер үчүн жыл сайынкы спорттук иш-чара",
                description_en="Annual sports event for employees",
                date="15 июня 2025",
                date_kg="2025-жылдын 15-июнунда",
                date_en="June 15, 2025",
                order=1
            )
            self.stdout.write(self.style.SUCCESS('✓ Created Trade Union events'))

        # Trade Union Stats
        if TradeUnionStats.objects.count() == 0:
            TradeUnionStats.objects.create(
                label="Членов профсоюза",
                label_kg="Профсоюз мүчөлөрү",
                label_en="Union Members",
                value=150,
                icon="👥",
                order=1
            )
            self.stdout.write(self.style.SUCCESS('✓ Created Trade Union statistics'))

        # Commissions
        if Commission.objects.count() == 0:
            Commission.objects.create(
                name="Учебно-методическая комиссия",
                name_kg="Окуу-методикалык комиссия",
                name_en="Academic and Methodological Commission",
                category="methodical",
                description="Разработка и утверждение учебных программ",
                description_kg="Окуу программаларын иштеп чыгуу жана бекитүү",
                description_en="Development and approval of educational programs",
                chairman="Доцент Смирнова А.П.",
                chairman_kg="Доцент Смирнова А.П.",
                chairman_en="Associate Professor Smirnova A.P.",
                members=["Иванов И.И.", "Петров П.П.", "Сидорова С.С."],
                members_kg=["Иванов И.И.", "Петров П.П.", "Сидорова С.С."],
                members_en=["Ivanov I.I.", "Petrov P.P.", "Sidorova S.S."],
                responsibilities=["Разработка учебных планов", "Методическое обеспечение"],
                responsibilities_kg=["Окуу пландарын иштеп чыгуу", "Методикалык камсыздоо"],
                responsibilities_en=["Development of curricula", "Methodological support"],
                order=1
            )
            self.stdout.write(self.style.SUCCESS('✓ Created Commissions'))

        # Administrative Departments
        if AdministrativeDepartment.objects.count() == 0:
            AdministrativeDepartment.objects.create(
                name="Ректорат",
                name_kg="Ректорат",
                name_en="Rectorate",
                head="Ректор Иванов И.И.",
                head_kg="Ректор Иванов И.И.",
                head_en="Rector Ivanov I.I.",
                responsibilities=["Общее руководство", "Стратегическое планирование"],
                responsibilities_kg=["Жалпы жетекчилик", "Стратегиялык пландоо"],
                responsibilities_en=["General management", "Strategic planning"],
                email="rector@academy.edu.kg",
                phone="+996 312 111111",
                order=1
            )
            self.stdout.write(self.style.SUCCESS('✓ Created Administrative Departments'))

        # Administrative Units
        if AdministrativeUnit.objects.count() == 0:
            AdministrativeUnit.objects.create(
                name="Учебный отдел",
                name_kg="Окуу бөлүмү",
                name_en="Academic Department",
                description="Организация и координация учебного процесса",
                description_kg="Окуу процессин уюштуруу жана координациялоо",
                description_en="Organization and coordination of the educational process",
                head="Начальник Петров П.П.",
                head_kg="Башчы Петров П.П.",
                head_en="Head Petrov P.P.",
                responsibilities=["Составление расписания", "Контроль успеваемости"],
                responsibilities_kg=["Расписание түзүү", "Үлгүлүктү көзөмөлдөө"],
                responsibilities_en=["Schedule compilation", "Performance monitoring"],
                email="academic@academy.edu.kg",
                phone="+996 312 222222",
                location="Главный корпус, каб. 201",
                location_kg="Башкы корпус, каб. 201",
                location_en="Main building, room 201",
                staff="15 сотрудников",
                staff_kg="15 кызматкер",
                staff_en="15 employees",
                order=1
            )
            self.stdout.write(self.style.SUCCESS('✓ Created Administrative Units'))

        self.stdout.write(self.style.SUCCESS('\n✅ Sample data creation completed!'))
