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
        self.stdout.write(self.style.WARNING('🚀 Creating comprehensive sample data...\n'))

        # Clear existing data first
        self.stdout.write('🗑️ Clearing existing data...')
        BoardOfTrustees.objects.all().delete()
        BoardOfTrusteesStats.objects.all().delete()
        AuditCommission.objects.all().delete()
        AuditCommissionStatistics.objects.all().delete()
        AcademicCouncil.objects.all().delete()
        TradeUnionBenefit.objects.all().delete()
        TradeUnionEvent.objects.all().delete()
        TradeUnionStats.objects.all().delete()
        Commission.objects.all().delete()
        AdministrativeDepartment.objects.all().delete()
        AdministrativeUnit.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✓ Cleared existing data\n'))

        # Board of Trustees - 5 members
        self.stdout.write('👔 Creating Board of Trustees...')
        BoardOfTrustees.objects.create(
            name="Асанов Темирбек Абдиевич",
            name_kg="Асанов Темирбек Абдиевич",
            name_en="Temirbek Asanov",
            position="Председатель попечительского совета",
            position_kg="Камкорлук кеңешинин төрагасы",
            position_en="Chairman of the Board of Trustees",
            bio="Заслуженный тренер Кыргызской Республики, мастер спорта международного класса по вольной борьбе. Более 25 лет опыта в развитии физической культуры и спорта.",
            bio_kg="Кыргыз Республикасынын атактуу машыктыруучусу, эркин күрөш боюнча эл аралык класстагы спорт чебери. Дене тарбия жана спортту өнүктүрүү боюнча 25 жылдан ашык тажрыйба.",
            bio_en="Honored Coach of the Kyrgyz Republic, International Master of Sports in freestyle wrestling. Over 25 years of experience in physical education and sports development.",
            achievements=[
                "Подготовил 15 мастеров спорта",
                "Организовал 50+ международных соревнований",
                "Привлек инвестиции более 100 млн сомов"
            ],
            achievements_kg=[
                "15 спорт чеберин даярдаган",
                "50+ эл аралык мелдештерди уюштурган",
                "100 млн сомдон ашык инвестиция тартты"
            ],
            achievements_en=[
                "Trained 15 masters of sports",
                "Organized 50+ international competitions",
                "Attracted investments over 100 million soms"
            ],
            email="asanov@academy.edu.kg",
            phone="+996 555 123 456",
            icon="👔",
            order=1
        )
        
        BoardOfTrustees.objects.create(
            name="Курманова Айгуль Бакытовна",
            name_kg="Курманова Айгүл Бакытовна",
            name_en="Aigul Kurmanova",
            position="Заместитель председателя",
            position_kg="Төраганын орун басары",
            position_en="Vice Chairman",
            bio="Доктор педагогических наук, профессор. Специалист в области теории и методики физического воспитания. Автор более 80 научных публикаций.",
            bio_kg="Педагогика илимдеринин доктору, профессор. Дене тарбиясынын теориясы жана методикасы боюнча адис. 80дөн ашык илимий макаланын автору.",
            bio_en="Doctor of Pedagogical Sciences, Professor. Specialist in theory and methods of physical education. Author of over 80 scientific publications.",
            achievements=[
                "80+ научных публикаций",
                "Руководство 12 кандидатскими диссертациями",
                "Разработка инновационных учебных программ"
            ],
            achievements_kg=[
                "80+ илимий макала",
                "12 кандидаттык диссертацияга жетекчилик",
                "Инновациялык окуу программаларын иштеп чыгуу"
            ],
            achievements_en=[
                "80+ scientific publications",
                "Supervised 12 PhD dissertations",
                "Development of innovative curricula"
            ],
            email="kurmanova@academy.edu.kg",
            phone="+996 555 234 567",
            icon="👩‍🏫",
            order=2
        )
        
        BoardOfTrustees.objects.create(
            name="Исаков Нурлан Токтогулович",
            name_kg="Исаков Нурлан Токтогулович",
            name_en="Nurlan Isakov",
            position="Член попечительского совета",
            position_kg="Камкорлук кеңешинин мүчөсү",
            position_en="Member of the Board of Trustees",
            bio="Президент Федерации легкой атлетики КР. Олимпийский чемпион по бегу на средние дистанции. Заслуженный спортсмен Кыргызстана.",
            bio_kg="КРнын жеңил атлетика федерациясынын президенти. Орто аралыкка чуркоо боюнча олимпиада чемпиону. Кыргызстандын атактуу спортчусу.",
            bio_en="President of the Athletics Federation of the KR. Olympic champion in middle-distance running. Honored athlete of Kyrgyzstan.",
            achievements=[
                "Олимпийский чемпион",
                "3 золотые медали на Азиатских играх",
                "Основатель спортивных школ в 5 регионах"
            ],
            achievements_kg=[
                "Олимпиада чемпиону",
                "Азия оюндарында 3 алтын медаль",
                "5 аймакта спорт мектептеринин негиздөөчүсү"
            ],
            achievements_en=[
                "Olympic champion",
                "3 gold medals at Asian Games",
                "Founder of sports schools in 5 regions"
            ],
            email="isakov@academy.edu.kg",
            phone="+996 555 345 678",
            icon="🏃",
            order=3
        )
        
        BoardOfTrustees.objects.create(
            name="Абдыкеримова Жылдыз Касымовна",
            name_kg="Абдыкеримова Жылдыз Касымовна",
            name_en="Zhyldyz Abdykerimova",
            position="Член попечительского совета",
            position_kg="Камкорлук кеңешинин мүчөсү",
            position_en="Member of the Board of Trustees",
            bio="Директор Института физической культуры и спорта. Кандидат биологических наук. Специалист по спортивной медицине и физиологии.",
            bio_kg="Дене тарбия жана спорт институтунун директору. Биология илимдеринин кандидаты. Спорттук медицина жана физиология боюнча адис.",
            bio_en="Director of the Institute of Physical Culture and Sports. Candidate of Biological Sciences. Specialist in sports medicine and physiology.",
            achievements=[
                "25 научных работ по спортивной физиологии",
                "Внедрение современных методов диагностики",
                "Международное сотрудничество с 10 странами"
            ],
            achievements_kg=[
                "Спорттук физиология боюнча 25 илимий эмгек",
                "Заманбап диагностика ыкмаларын киргизүү",
                "10 өлкө менен эл аралык кызматташуу"
            ],
            achievements_en=[
                "25 scientific works on sports physiology",
                "Implementation of modern diagnostic methods",
                "International cooperation with 10 countries"
            ],
            email="abdykerimova@academy.edu.kg",
            phone="+996 555 456 789",
            icon="⚕️",
            order=4
        )
        
        BoardOfTrustees.objects.create(
            name="Бекмуратов Азамат Жолдошбекович",
            name_kg="Бекмуратов Азамат Жолдошбекович",
            name_en="Azamat Bekmuratov",
            position="Член попечительского совета",
            position_kg="Камкорлук кеңешинин мүчөсү",
            position_en="Member of the Board of Trustees",
            bio="Генеральный директор крупнейшей спортивной компании в регионе. Меценат и спонсор спортивных проектов. Выпускник академии 2005 года.",
            bio_kg="Аймактагы эң ири спорт компаниясынын башкы директору. Спорттук долбоорлордун меценаты жана спонсору. 2005-жылы академияны бүтүргөн.",
            bio_en="General Director of the largest sports company in the region. Patron and sponsor of sports projects. Academy graduate of 2005.",
            achievements=[
                "Спонсорство 30+ спортивных проектов",
                "Создание спортивных стипендий для студентов",
                "Строительство 2 спортивных комплексов"
            ],
            achievements_kg=[
                "30+ спорттук долбоорду спонсорлоо",
                "Студенттер үчүн спорттук стипендияларды түзүү",
                "2 спорт комплексин курууу"
            ],
            achievements_en=[
                "Sponsorship of 30+ sports projects",
                "Creation of sports scholarships for students",
                "Construction of 2 sports complexes"
            ],
            email="bekmuratov@academy.edu.kg",
            phone="+996 555 567 890",
            icon="💼",
            order=5
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Created 5 Board of Trustees members'))

        # Board Stats - 4 statistics
        BoardOfTrusteesStats.objects.create(
            label="Лет опыта",
            label_kg="Тажрыйба жылы",
            label_en="Years of Experience",
            target_value=25,
            icon="📅",
            order=1
        )
        BoardOfTrusteesStats.objects.create(
            label="Проектов реализовано",
            label_kg="Ишке ашырылган долбоорлор",
            label_en="Projects Completed",
            target_value=150,
            icon="🚀",
            order=2
        )
        BoardOfTrusteesStats.objects.create(
            label="Международных партнеров",
            label_kg="Эл аралык өнөктөштөр",
            label_en="International Partners",
            target_value=35,
            icon="🌍",
            order=3
        )
        BoardOfTrusteesStats.objects.create(
            label="Млн сомов инвестиций",
            label_kg="Млн сом инвестиция",
            label_en="Million Soms Invested",
            target_value=500,
            icon="💰",
            order=4
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Created 4 Board statistics'))

        # Audit Commission - 3 members
        self.stdout.write('🔍 Creating Audit Commission...')
        AuditCommission.objects.create(
            name="Джолдошев Марат Асанбекович",
            name_kg="Жолдошев Марат Асанбекович",
            name_en="Marat Zholdoshev",
            position="Председатель ревизионной комиссии",
            position_kg="Ревизиялык комиссиянын төрагасы",
            position_en="Chairman of the Audit Commission",
            department="Финансово-экономический отдел",
            department_kg="Финансы-экономика бөлүмү",
            department_en="Finance and Economics Department",
            achievements=[
                "Провел 100+ аудиторских проверок",
                "Сэкономил 20 млн сомов бюджетных средств",
                "Внедрил автоматизированную систему контроля"
            ],
            achievements_kg=[
                "100+ аудиттик текшерүүлөрдү өткөрдү",
                "20 млн сом бюджет каражатын үнөмдөдү",
                "Автоматташтырылган көзөмөл системасын киргизди"
            ],
            achievements_en=[
                "Conducted 100+ auditing inspections",
                "Saved 20 million soms of budget funds",
                "Implemented automated control system"
            ],
            order=1
        )
        
        AuditCommission.objects.create(
            name="Токтосунова Гульнара Эркиновна",
            name_kg="Токтосунова Гүлнара Эркиновна",
            name_en="Gulnara Toktosunova",
            position="Заместитель председателя",
            position_kg="Төраганын орун басары",
            position_en="Vice Chairman",
            department="Юридический отдел",
            department_kg="Юридикалык бөлүм",
            department_en="Legal Department",
            achievements=[
                "Юрист с 15-летним стажем",
                "Специалист по финансовому праву",
                "Разработка внутренних нормативных актов"
            ],
            achievements_kg=[
                "15 жылдык тажрыйбалуу юрист",
                "Финансы укугу боюнча адис",
                "Ички нормативдик актыларды иштеп чыгуу"
            ],
            achievements_en=[
                "Lawyer with 15 years of experience",
                "Financial law specialist",
                "Development of internal regulations"
            ],
            order=2
        )
        
        AuditCommission.objects.create(
            name="Кожобеков Алмаз Турдубекович",
            name_kg="Кожобеков Алмаз Турдубекович",
            name_en="Almaz Kozhobekov",
            position="Член ревизионной комиссии",
            position_kg="Ревизиялык комиссиянын мүчөсү",
            position_en="Member of the Audit Commission",
            department="Отдел внутреннего контроля",
            department_kg="Ички көзөмөл бөлүмү",
            department_en="Internal Control Department",
            achievements=[
                "Сертифицированный внутренний аудитор",
                "Опыт работы в международных организациях",
                "Эксперт по рискам и комплаенсу"
            ],
            achievements_kg=[
                "Сертификатталган ички аудитор",
                "Эл аралык уюмдарда иштөө тажрыйбасы",
                "Тобокелдиктер жана комплаенс боюнча эксперт"
            ],
            achievements_en=[
                "Certified internal auditor",
                "Experience in international organizations",
                "Risk and compliance expert"
            ],
            order=3
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Created 3 Audit Commission members'))

        # Audit Commission Statistics - 3 stats
        AuditCommissionStatistics.objects.create(
            label="Аудитов проведено",
            label_kg="Аудиттер өткөрүлдү",
            label_en="Audits Conducted",
            value="127",
            value_kg="127",
            value_en="127",
            order=1
        )
        AuditCommissionStatistics.objects.create(
            label="Нарушений выявлено",
            label_kg="Бузууларды аныкталды",
            label_en="Violations Identified",
            value="23",
            value_kg="23",
            value_en="23",
            order=2
        )
        AuditCommissionStatistics.objects.create(
            label="Млн сомов сэкономлено",
            label_kg="Млн сом үнөмдөлдү",
            label_en="Million Soms Saved",
            value="45",
            value_kg="45",
            value_en="45",
            order=3
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Created 3 Audit Commission statistics'))

        # Academic Council - 7 members
        self.stdout.write('🎓 Creating Academic Council...')
        AcademicCouncil.objects.create(
            name="Профессор Мамбетов Кубатбек Абдылдаевич",
            name_kg="Профессор Мамбетов Кубатбек Абдылдаевич",
            name_en="Professor Kubatbek Mambetov",
            position="Председатель ученого совета",
            position_kg="Илимий кеңештин төрагасы",
            position_en="Chairman of the Academic Council",
            department="Кафедра теории и методики физической культуры",
            department_kg="Дене тарбия теориясы жана методикасы кафедрасы",
            department_en="Department of Theory and Methods of Physical Education",
            achievements=[
                "Доктор педагогических наук",
                "50+ научных публикаций",
                "Руководство 15 диссертациями",
                "Член 3 международных научных обществ"
            ],
            achievements_kg=[
                "Педагогика илимдеринин доктору",
                "50+ илимий макала",
                "15 диссертацияга жетекчилик",
                "3 эл аралык илимий коомдун мүчөсү"
            ],
            achievements_en=[
                "Doctor of Pedagogical Sciences",
                "50+ scientific publications",
                "Supervised 15 dissertations",
                "Member of 3 international scientific societies"
            ],
            order=1
        )
        
        AcademicCouncil.objects.create(
            name="Доцент Эсенбекова Айнура Жолдошбековна",
            name_kg="Доцент Эсенбекова Айнура Жолдошбековна",
            name_en="Associate Professor Ainura Esenbekova",
            position="Заместитель председателя",
            position_kg="Төраганын орун басары",
            position_en="Vice Chairman",
            department="Кафедра спортивных игр",
            department_kg="Спорттук оюндар кафедрасы",
            department_en="Department of Sports Games",
            achievements=[
                "Кандидат педагогических наук",
                "Мастер спорта по волейболу",
                "30+ научных работ",
                "Тренер национальной сборной"
            ],
            achievements_kg=[
                "Педагогика илимдеринин кандидаты",
                "Волейбол боюнча спорт чебери",
                "30+ илимий эмгек",
                "Улуттук курама командасынын машыктыруучусу"
            ],
            achievements_en=[
                "Candidate of Pedagogical Sciences",
                "Master of Sports in volleyball",
                "30+ scientific works",
                "National team coach"
            ],
            order=2
        )
        
        # Создаем еще 5 членов ученого совета
        for i, (name_data) in enumerate([
            ("Профессор Турдубеков Бакыт Исаевич", "Профессор Турдубеков Бакыт Исаевич", "Professor Bakyt Turdubekov", "Декан факультета"),
            ("Доцент Касымова Венера Мамбетовна", "Доцент Касымова Венера Мамбетовна", "Associate Professor Venera Kasymova", "Заведующий кафедрой"),
            ("Профессор Сыдыков Нуркан Абдыразакович", "Профессор Сыдыков Нуркан Абдыразакович", "Professor Nurkan Sydykov", "Научный руководитель"),
            ("Доцент Абдраимова Жыпаргуль Токтосуновна", "Доцент Абдраимова Жыпаргүл Токтосуновна", "Associate Professor Zhypargul Abdraimova", "Член совета"),
            ("Кандидат наук Токтомушев Элмурат Асылбекович", "Кандидат наук Токтомушев Элмурат Асылбекович", "PhD Elmurat Toktomushev", "Член совета")
        ], 3):
            AcademicCouncil.objects.create(
                name=name_data[0],
                name_kg=name_data[1], 
                name_en=name_data[2],
                position=name_data[3],
                position_kg=name_data[3],
                position_en=name_data[3],
                department="Кафедра физической культуры",
                department_kg="Дене тарбия кафедрасы",
                department_en="Department of Physical Education",
                achievements=["Научная деятельность", "Педагогический опыт"],
                achievements_kg=["Илимий ишмердүүлүк", "Педагогикалык тажрыйба"],
                achievements_en=["Scientific activity", "Pedagogical experience"],
                order=i+3
            )
        self.stdout.write(self.style.SUCCESS('  ✓ Created 7 Academic Council members'))

        # Trade Union Benefits - 6 benefits
        self.stdout.write('🤝 Creating Trade Union Benefits...')
        benefits_data = [
            ("Медицинское страхование", "Медициналык камсыздандыруу", "Medical Insurance", "🏥", "Полный пакет медицинского страхования"),
            ("Материальная помощь", "Материалдык жардам", "Financial Assistance", "💰", "Финансовая поддержка в сложных ситуациях"),
            ("Санаторно-курортное лечение", "Санаторий-курорт дарылоо", "Spa Treatment", "🏖️", "Бесплатные путевки в санатории"),
            ("Спортивные секции", "Спорттук секциялар", "Sports Sections", "⚽", "Бесплатные занятия спортом для сотрудников"),
            ("Корпоративные мероприятия", "Корпоративдик иш-чаралар", "Corporate Events", "🎉", "Организация праздников и мероприятий"),
            ("Льготное питание", "Арзандатылган тамак", "Subsidized Meals", "🍽️", "Скидки в столовой академии")
        ]
        
        for i, (title_ru, title_kg, title_en, icon, desc_ru) in enumerate(benefits_data, 1):
            TradeUnionBenefit.objects.create(
                title=title_ru,
                title_kg=title_kg,
                title_en=title_en,
                description=desc_ru,
                description_kg=desc_ru,  # Упрощенно используем русский
                description_en=desc_ru,
                icon=icon,
                order=i
            )
        self.stdout.write(self.style.SUCCESS('  ✓ Created 6 Trade Union benefits'))

        # Trade Union Events - 4 events
        events_data = [
            ("Спартакиада профсоюза", "Профсоюздун спартакиадасы", "Union Sports Festival", "15-20 мая 2025"),
            ("День здоровья", "Ден соолук күнү", "Health Day", "10 июня 2025"),
            ("Новогодний корпоратив", "Жаңы жыл корпоративи", "New Year Corporate Party", "25 декабря 2025"),
            ("Семейный пикник", "Үй-бүлөлүк пикник", "Family Picnic", "15 августа 2025")
        ]
        
        for i, (title_ru, title_kg, title_en, date_ru) in enumerate(events_data, 1):
            TradeUnionEvent.objects.create(
                title=title_ru,
                title_kg=title_kg,
                title_en=title_en,
                description=f"Ежегодное мероприятие профсоюза - {title_ru}",
                description_kg=f"Профсоюздун жыл сайынкы иш-чарасы - {title_kg}",
                description_en=f"Annual union event - {title_en}",
                date=date_ru,
                date_kg=date_ru,
                date_en=date_ru,
                order=i
            )
        self.stdout.write(self.style.SUCCESS('  ✓ Created 4 Trade Union events'))

        # Trade Union Stats - 3 stats
        TradeUnionStats.objects.create(
            label="Членов профсоюза",
            label_kg="Профсоюз мүчөлөрү",
            label_en="Union Members",
            value=285,
            icon="👥",
            order=1
        )
        TradeUnionStats.objects.create(
            label="Проведено мероприятий",
            label_kg="Өткөрүлгөн иш-чаралар",
            label_en="Events Held",
            value=24,
            icon="🎯",
            order=2
        )
        TradeUnionStats.objects.create(
            label="Выделено льгот (млн сом)",
            label_kg="Берилген жеңилдиктер (млн сом)",
            label_en="Benefits Provided (mln som)",
            value=12,
            icon="💝",
            order=3
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Created 3 Trade Union statistics'))

        # Commissions - 5 commissions
        self.stdout.write('📋 Creating Commissions...')
        commissions_data = [
            ("Учебно-методическая комиссия", "methodical", "Разработка и утверждение учебных программ", "Доцент Смирнова А.П."),
            ("Научно-техническая комиссия", "scientific", "Координация научно-исследовательской деятельности", "Профессор Иванов И.И."),
            ("Комиссия по качеству образования", "quality", "Контроль качества образовательного процесса", "Доцент Петрова М.С."),
            ("Этическая комиссия", "ethics", "Рассмотрение этических вопросов и конфликтов", "Профессор Сидоров П.Н."),
            ("Стипендиальная комиссия", "scholarship", "Распределение стипендий и премий", "Доцент Козлова Е.В.")
        ]
        
        for i, (name, category, description, chairman) in enumerate(commissions_data, 1):
            Commission.objects.create(
                name=name,
                name_kg=name,  # Упрощенно
                name_en=name,
                category=category,
                description=description,
                description_kg=description,
                description_en=description,
                chairman=chairman,
                chairman_kg=chairman,
                chairman_en=chairman,
                members=["Иванов И.И.", "Петров П.П.", "Сидорова С.С.", "Козлов К.К."],
                members_kg=["Иванов И.И.", "Петров П.П.", "Сидорова С.С.", "Козлов К.К."],
                members_en=["Ivanov I.I.", "Petrov P.P.", "Sidorova S.S.", "Kozlov K.K."],
                responsibilities=["Планирование", "Контроль", "Отчетность"],
                responsibilities_kg=["Пландоо", "Көзөмөл", "Отчет"],
                responsibilities_en=["Planning", "Control", "Reporting"],
                order=i
            )
        self.stdout.write(self.style.SUCCESS('  ✓ Created 5 Commissions'))

        # Administrative Departments - 4 departments
        self.stdout.write('🏢 Creating Administrative Departments...')
        
        AdministrativeDepartment.objects.create(
            name="Ректорат",
            name_kg="Ректорат",
            name_en="Rectorate",
            head="Ректор Асанов Т.А.",
            head_kg="Ректор Асанов Т.А.",
            head_en="Rector Asanov T.A.",
            responsibilities=["Общее руководство академией", "Планирование деятельности", "Контроль исполнения"],
            responsibilities_kg=["Академиянын жалпы жетекчилиги", "Ишмердүүлүктү пландоо", "Аткарууну көзөмөлдөө"],
            responsibilities_en=["General management of academy", "Activity planning", "Execution control"],
            email="rector@academy.edu.kg",
            phone="+996 312 111111",
            order=1
        )
        
        AdministrativeDepartment.objects.create(
            name="Проректорат по учебной работе",
            name_kg="Окуу иши боюнча проректорат",
            name_en="Vice-Rectorate for Academic Affairs",
            head="Проректор Курманова А.Б.",
            head_kg="Проректор Курманова А.Б.",
            head_en="Vice-Rector Kurmanova A.B.",
            responsibilities=["Координация учебного процесса", "Планирование деятельности", "Контроль исполнения"],
            responsibilities_kg=["Окуу процессин координациялоо", "Ишмердүүлүктү пландоо", "Аткарууну көзөмөлдөө"],
            responsibilities_en=["Coordination of educational process", "Activity planning", "Execution control"],
            email="study@academy.edu.kg",
            phone="+996 312 222222",
            order=2
        )
        
        AdministrativeDepartment.objects.create(
            name="Проректорат по научной работе",
            name_kg="Илимий иш боюнча проректорат",
            name_en="Vice-Rectorate for Scientific Affairs",
            head="Проректор Исаков Н.Т.",
            head_kg="Проректор Исаков Н.Т.",
            head_en="Vice-Rector Isakov N.T.",
            responsibilities=["Руководство научной деятельностью", "Планирование деятельности", "Контроль исполнения"],
            responsibilities_kg=["Илимий ишмердүүлүккө жетекчилик", "Ишмердүүлүктү пландоо", "Аткарууну көзөмөлдөө"],
            responsibilities_en=["Management of scientific activities", "Activity planning", "Execution control"],
            email="science@academy.edu.kg",
            phone="+996 312 333333",
            order=3
        )
        
        AdministrativeDepartment.objects.create(
            name="Административно-хозяйственная часть",
            name_kg="Административдик-чарба бөлүмү",
            name_en="Administrative and Economic Department",
            head="Начальник Петров П.П.",
            head_kg="Башчы Петров П.П.",
            head_en="Head Petrov P.P.",
            responsibilities=["Хозяйственное обеспечение", "Планирование деятельности", "Контроль исполнения"],
            responsibilities_kg=["Чарба камсыздоо", "Ишмердүүлүктү пландоо", "Аткарууну көзөмөлдөө"],
            responsibilities_en=["Economic support", "Activity planning", "Execution control"],
            email="admin@academy.edu.kg",
            phone="+996 312 444444",
            order=4
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Created 4 Administrative Departments'))

        # Administrative Units - 6 units
        self.stdout.write('🏛️ Creating Administrative Units...')
        
        AdministrativeUnit.objects.create(
            name="Учебный отдел",
            name_kg="Окуу бөлүмү",
            name_en="Academic Department",
            description="Организация учебного процесса",
            description_kg="Окуу процессин уюштуруу",
            description_en="Organization of educational process",
            head="Начальник Иванова И.И.",
            head_kg="Башчы Иванова И.И.",
            head_en="Head Ivanova I.I.",
            responsibilities=["Планирование работы", "Исполнение задач", "Отчетность"],
            responsibilities_kg=["Жумушту пландоо", "Милдеттерди аткаруу", "Отчет"],
            responsibilities_en=["Work planning", "Task execution", "Reporting"],
            email="academic@academy.edu.kg",
            phone="+996 312 555111",
            location="Главный корпус, каб. 201",
            location_kg="Башкы корпус, каб. 201",
            location_en="Main building, room 201",
            staff="12 сотрудников",
            staff_kg="12 кызматкер",
            staff_en="12 employees",
            order=1
        )
        
        AdministrativeUnit.objects.create(
            name="Отдел кадров",
            name_kg="Кадр бөлүмү",
            name_en="HR Department",
            description="Управление персоналом",
            description_kg="Персоналды башкаруу",
            description_en="Personnel management",
            head="Начальник Петрова П.П.",
            head_kg="Башчы Петрова П.П.",
            head_en="Head Petrova P.P.",
            responsibilities=["Планирование работы", "Исполнение задач", "Отчетность"],
            responsibilities_kg=["Жумушту пландоо", "Милдеттерди аткаруу", "Отчет"],
            responsibilities_en=["Work planning", "Task execution", "Reporting"],
            email="hr@academy.edu.kg",
            phone="+996 312 555222",
            location="Главный корпус, каб. 105",
            location_kg="Башкы корпус, каб. 105",
            location_en="Main building, room 105",
            staff="8 сотрудников",
            staff_kg="8 кызматкер",
            staff_en="8 employees",
            order=2
        )
        
        AdministrativeUnit.objects.create(
            name="Финансовый отдел",
            name_kg="Финансы бөлүмү",
            name_en="Finance Department",
            description="Финансовое планирование",
            description_kg="Финансылык пландоо",
            description_en="Financial planning",
            head="Начальник Сидоров С.С.",
            head_kg="Башчы Сидоров С.С.",
            head_en="Head Sidorov S.S.",
            responsibilities=["Планирование работы", "Исполнение задач", "Отчетность"],
            responsibilities_kg=["Жумушту пландоо", "Милдеттерди аткаруу", "Отчет"],
            responsibilities_en=["Work planning", "Task execution", "Reporting"],
            email="finance@academy.edu.kg",
            phone="+996 312 555333",
            location="Главный корпус, каб. 301",
            location_kg="Башкы корпус, каб. 301",
            location_en="Main building, room 301",
            staff="15 сотрудников",
            staff_kg="15 кызматкер",
            staff_en="15 employees",
            order=3
        )
        
        AdministrativeUnit.objects.create(
            name="IT-отдел",
            name_kg="IT-бөлүмү",
            name_en="IT Department",
            description="Информационная поддержка",
            description_kg="Маалыматтык колдоо",
            description_en="Information support",
            head="Начальник Козлов К.К.",
            head_kg="Башчы Козлов К.К.",
            head_en="Head Kozlov K.K.",
            responsibilities=["Планирование работы", "Исполнение задач", "Отчетность"],
            responsibilities_kg=["Жумушту пландоо", "Милдеттерди аткаруу", "Отчет"],
            responsibilities_en=["Work planning", "Task execution", "Reporting"],
            email="it@academy.edu.kg",
            phone="+996 312 555444",
            location="Корпус Б, каб. 101",
            location_kg="Корпус Б, каб. 101",
            location_en="Building B, room 101",
            staff="10 сотрудников",
            staff_kg="10 кызматкер",
            staff_en="10 employees",
            order=4
        )
        
        AdministrativeUnit.objects.create(
            name="Библиотека",
            name_kg="Китепкана",
            name_en="Library",
            description="Информационно-библиотечные услуги",
            description_kg="Маалыматтык-китепкана кызматтары",
            description_en="Information and library services",
            head="Заведующий Орлова О.О.",
            head_kg="Башкы Орлова О.О.",
            head_en="Head Orlova O.O.",
            responsibilities=["Планирование работы", "Исполнение задач", "Отчетность"],
            responsibilities_kg=["Жумушту пландоо", "Милдеттерди аткаруу", "Отчет"],
            responsibilities_en=["Work planning", "Task execution", "Reporting"],
            email="library@academy.edu.kg",
            phone="+996 312 555555",
            location="Главный корпус, 1 этаж",
            location_kg="Башкы корпус, 1 кабат",
            location_en="Main building, 1st floor",
            staff="6 сотрудников",
            staff_kg="6 кызматкер",
            staff_en="6 employees",
            order=5
        )
        
        AdministrativeUnit.objects.create(
            name="Медицинский пункт",
            name_kg="Медициналык пункт",
            name_en="Medical Point",
            description="Медицинское обслуживание",
            description_kg="Медициналык тейлөө",
            description_en="Medical services",
            head="Заведующий Морозов М.М.",
            head_kg="Башкы Морозов М.М.",
            head_en="Head Morozov M.M.",
            responsibilities=["Планирование работы", "Исполнение задач", "Отчетность"],
            responsibilities_kg=["Жумушту пландоо", "Милдеттерди аткаруу", "Отчет"],
            responsibilities_en=["Work planning", "Task execution", "Reporting"],
            email="medical@academy.edu.kg",
            phone="+996 312 555666",
            location="Спортивный корпус",
            location_kg="Спорттук корпус",
            location_en="Sports building",
            staff="4 сотрудника",
            staff_kg="4 кызматкер",
            staff_en="4 employees",
            order=6
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Created 6 Administrative Units'))

        # Summary
        self.stdout.write(self.style.SUCCESS('\n🎉 COMPREHENSIVE DATA CREATION COMPLETED!'))
        self.stdout.write(self.style.SUCCESS('📊 Created:'))
        self.stdout.write(self.style.SUCCESS(f'  • {BoardOfTrustees.objects.count()} Board of Trustees members'))
        self.stdout.write(self.style.SUCCESS(f'  • {BoardOfTrusteesStats.objects.count()} Board statistics'))
        self.stdout.write(self.style.SUCCESS(f'  • {AuditCommission.objects.count()} Audit Commission members'))
        self.stdout.write(self.style.SUCCESS(f'  • {AuditCommissionStatistics.objects.count()} Audit statistics'))
        self.stdout.write(self.style.SUCCESS(f'  • {AcademicCouncil.objects.count()} Academic Council members'))
        self.stdout.write(self.style.SUCCESS(f'  • {TradeUnionBenefit.objects.count()} Trade Union benefits'))
        self.stdout.write(self.style.SUCCESS(f'  • {TradeUnionEvent.objects.count()} Trade Union events'))
        self.stdout.write(self.style.SUCCESS(f'  • {TradeUnionStats.objects.count()} Trade Union statistics'))
        self.stdout.write(self.style.SUCCESS(f'  • {Commission.objects.count()} Commissions'))
        self.stdout.write(self.style.SUCCESS(f'  • {AdministrativeDepartment.objects.count()} Administrative Departments'))
        self.stdout.write(self.style.SUCCESS(f'  • {AdministrativeUnit.objects.count()} Administrative Units'))
        self.stdout.write(self.style.SUCCESS('\n✅ All leadership components now have comprehensive data!'))