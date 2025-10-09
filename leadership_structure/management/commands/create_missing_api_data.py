from django.core.management.base import BaseCommand
from leadership_structure.models import Leadership, OrganizationStructure, Document
from datetime import datetime, date


class Command(BaseCommand):
    help = 'Create sample data for missing API models: Leadership, OrganizationStructure, Document'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write("Clearing existing data...")
        Leadership.objects.all().delete()
        OrganizationStructure.objects.all().delete()
        Document.objects.all().delete()
        
        # Create Leadership data (для /leadership/)
        self.stdout.write("Creating Leadership data...")
        leadership_data = [
            {
                'name': 'Садыкова Айнура Омуркуловна',
                'name_kg': 'Садыкова Айнура Омуркуловна',
                'name_en': 'Sadykova Ainura Omurkulovna',
                'position': 'Ректор',
                'position_kg': 'Ректор',
                'position_en': 'Rector',
                'leadership_type': 'rector',
                'department': 'Ректорат',
                'department_kg': 'Ректорат',
                'department_en': 'Rectorate',
                'bio': 'Опытный руководитель с большим стажем в сфере образования.',
                'bio_kg': 'Билим берүү тармагында чоң тажрыйбасы бар көп жылдык жетекчи.',
                'bio_en': 'Experienced leader with extensive background in education.',
                'achievements': ['Почетный работник образования КР', 'Кандидат педагогических наук'],
                'achievements_kg': ['КРдин билим берүүнүн сыйлуу кызматкери', 'Педагогика илимдеринин кандидаты'],
                'achievements_en': ['Honorary Education Worker of KR', 'Candidate of Pedagogical Sciences'],
                'education': 'Высшее педагогическое образование, КГУ им. И. Арабаева',
                'education_kg': 'Жогорку педагогикалык билим, И. Арабаев атындагы КМУ',
                'education_en': 'Higher pedagogical education, KSU named after I. Arabaev',
                'email': 'rector@salymbekov.edu.kg',
                'phone': '+996 (312) 54-56-78',
                'experience_years': 25,
                'icon': '👩‍💼',
                'order': 1
            },
            {
                'name': 'Жумабеков Талант Асанович',
                'name_kg': 'Жумабеков Талант Асанович',
                'name_en': 'Zhumabekov Talant Asanovich',
                'position': 'Проректор по учебной работе',
                'position_kg': 'Окуу иши боюнча проректор',
                'position_en': 'Vice-Rector for Academic Affairs',
                'leadership_type': 'vice_rector',
                'department': 'Ректорат',
                'department_kg': 'Ректорат',
                'department_en': 'Rectorate',
                'bio': 'Специалист в области управления учебным процессом.',
                'bio_kg': 'Окуу процессин башкаруу тармагынын адиси.',
                'bio_en': 'Specialist in academic process management.',
                'achievements': ['Отличник образования КР', 'Доктор экономических наук'],
                'achievements_kg': ['КРдин билим берүүнүн мыкты кызматкери', 'Экономика илимдеринин доктору'],
                'achievements_en': ['Excellent Education Worker of KR', 'Doctor of Economic Sciences'],
                'education': 'Экономический факультет, КРСУ',
                'education_kg': 'Экономика факультети, КРСУ',
                'education_en': 'Faculty of Economics, KRSU',
                'email': 'vice.rector.academic@salymbekov.edu.kg',
                'phone': '+996 (312) 54-56-79',
                'experience_years': 20,
                'icon': '👨‍🏫',
                'order': 2
            },
            {
                'name': 'Алымкулова Жылдыз Бакытбековна',
                'name_kg': 'Алымкулова Жылдыз Бакытбековна',
                'name_en': 'Alymkulova Zhyldyz Bakytbekovna',
                'position': 'Проректор по научной работе',
                'position_kg': 'Илимий иш боюнча проректор',
                'position_en': 'Vice-Rector for Research',
                'leadership_type': 'vice_rector',
                'department': 'Ректорат',
                'department_kg': 'Ректорат',
                'department_en': 'Rectorate',
                'bio': 'Ведущий специалист в области научных исследований.',
                'bio_kg': 'Илимий изилдөөлөр тармагынын алдыңкы адиси.',
                'bio_en': 'Leading specialist in scientific research.',
                'achievements': ['Почетный деятель науки КР', 'Доктор философских наук'],
                'achievements_kg': ['КРдын илимдин сыйлуу ишмери', 'Философия илимдеринин доктору'],
                'achievements_en': ['Honorary Scientist of KR', 'Doctor of Philosophy'],
                'education': 'Философский факультет, МГУ им. М.В. Ломоносова',
                'education_kg': 'Философия факультети, М.В. Ломоносов атындагы МДУ',
                'education_en': 'Faculty of Philosophy, Moscow State University',
                'email': 'vice.rector.research@salymbekov.edu.kg',
                'phone': '+996 (312) 54-56-80',
                'experience_years': 18,
                'icon': '👩‍🔬',
                'order': 3
            },
            {
                'name': 'Бекназаров Азамат Султанович',
                'name_kg': 'Бекназаров Азамат Султанович',
                'name_en': 'Beknazarov Azamat Sultanovich',
                'position': 'Декан экономического факультета',
                'position_kg': 'Экономика факультетинин деканы',
                'position_en': 'Dean of Economics Faculty',
                'leadership_type': 'dean',
                'department': 'Экономический факультет',
                'department_kg': 'Экономика факультети',
                'department_en': 'Faculty of Economics',
                'bio': 'Опытный преподаватель и администратор.',
                'bio_kg': 'Тажрыйбалуу мугалим жана администратор.',
                'bio_en': 'Experienced teacher and administrator.',
                'achievements': ['Лучший преподаватель года', 'Кандидат экономических наук'],
                'achievements_kg': ['Жылдын эң мыкты мугалими', 'Экономика илимдеринин кандидаты'],
                'achievements_en': ['Best Teacher of the Year', 'Candidate of Economic Sciences'],
                'education': 'Экономический факультет, АУ им. Ж. Баласагына',
                'education_kg': 'Экономика факультети, Ж. Баласагын атындагы АУ',
                'education_en': 'Faculty of Economics, AU named after Zh. Balasagyn',
                'email': 'dean.economics@salymbekov.edu.kg',
                'phone': '+996 (312) 54-56-81',
                'experience_years': 15,
                'icon': '👨‍💼',
                'order': 4
            },
            {
                'name': 'Токтомушева Гүлзат Эркебековна',
                'name_kg': 'Токтомушева Гүлзат Эркебековна',
                'name_en': 'Toktomusheva Gulzat Erkebekovna',
                'position': 'Заведующая кафедрой менеджмента',
                'position_kg': 'Менеджмент кафедрасынын башчысы',
                'position_en': 'Head of Management Department',
                'leadership_type': 'department_head',
                'department': 'Кафедра менеджмента',
                'department_kg': 'Менеджмент кафедрасы',
                'department_en': 'Management Department',
                'bio': 'Специалист в области управления и менеджмента.',
                'bio_kg': 'Башкаруу жана менеджмент тармагынын адиси.',
                'bio_en': 'Specialist in management and administration.',
                'achievements': ['Лучший заведующий кафедрой', 'MBA'],
                'achievements_kg': ['Эң мыкты кафедра башчысы', 'MBA'],
                'achievements_en': ['Best Department Head', 'MBA'],
                'education': 'Факультет менеджмента, АУЦА',
                'education_kg': 'Менеджмент факультети, АУЦА',
                'education_en': 'Faculty of Management, AUCA',
                'email': 'head.management@salymbekov.edu.kg',
                'phone': '+996 (312) 54-56-82',
                'experience_years': 12,
                'icon': '👩‍💼',
                'order': 5
            }
        ]
        
        for data in leadership_data:
            Leadership.objects.create(**data)
        
        # Create Organization Structure data (для /organization-structure/)
        self.stdout.write("Creating Organization Structure data...")
        
        # Root structures (без parent)
        rectorate = OrganizationStructure.objects.create(
            name='Ректорат',
            name_kg='Ректорат',
            name_en='Rectorate',
            structure_type='unit',
            description='Высший орган управления академии',
            description_kg='Академиянын эң жогорку башкаруу органы',
            description_en='Highest governing body of the academy',
            head='Садыкова Айнура Омуркуловна',
            head_kg='Садыкова Айнура Омуркуловна',
            head_en='Sadykova Ainura Omurkulovna',
            responsibilities=['Стратегическое планирование', 'Управление академией', 'Принятие ключевых решений'],
            responsibilities_kg=['Стратегиялык пландоо', 'Академияны башкаруу', 'Негизги чечимдерди кабыл алуу'],
            responsibilities_en=['Strategic planning', 'Academy management', 'Key decision making'],
            email='rectorate@salymbekov.edu.kg',
            phone='+996 (312) 54-56-78',
            location='Главный корпус, 3 этаж',
            location_kg='Башкы корпус, 3-кат',
            location_en='Main building, 3rd floor',
            staff_count=5,
            icon='🏛️',
            order=1
        )
        
        economics_faculty = OrganizationStructure.objects.create(
            name='Экономический факультет',
            name_kg='Экономика факультети',
            name_en='Faculty of Economics',
            structure_type='faculty',
            description='Факультет экономических специальностей',
            description_kg='Экономикалык адистиктердин факультети',
            description_en='Faculty of economic specialties',
            head='Бекназаров Азамат Султанович',
            head_kg='Бекназаров Азамат Султанович',
            head_en='Beknazarov Azamat Sultanovich',
            responsibilities=['Организация учебного процесса', 'Контроль качества образования', 'Развитие факультета'],
            responsibilities_kg=['Окуу процессин уюштуруу', 'Билим берүү сапатын көзөмөлдөө', 'Факультетти өнүктүрүү'],
            responsibilities_en=['Educational process organization', 'Education quality control', 'Faculty development'],
            email='economics@salymbekov.edu.kg',
            phone='+996 (312) 54-56-81',
            location='Корпус А, 2 этаж',
            location_kg='А корпусу, 2-кат',
            location_en='Building A, 2nd floor',
            staff_count=25,
            icon='💼',
            order=2
        )
        
        # Departments under Economics Faculty
        OrganizationStructure.objects.create(
            name='Кафедра менеджмента',
            name_kg='Менеджмент кафедрасы',
            name_en='Management Department',
            structure_type='department',
            parent=economics_faculty,
            description='Кафедра менеджмента и управления',
            description_kg='Менеджмент жана башкаруу кафедрасы',
            description_en='Management and administration department',
            head='Токтомушева Гүлзат Эркебековна',
            head_kg='Токтомушева Гүлзат Эркебековна',
            head_en='Toktomusheva Gulzat Erkebekovna',
            responsibilities=['Преподавание дисциплин менеджмента', 'Научная работа', 'Методическая работа'],
            responsibilities_kg=['Менеджмент дисциплиналарын окутуу', 'Илимий иш', 'Методикалык иш'],
            responsibilities_en=['Teaching management disciplines', 'Research work', 'Methodological work'],
            email='management@salymbekov.edu.kg',
            phone='+996 (312) 54-56-85',
            location='Корпус А, каб. 205',
            location_kg='А корпусу, 205-бөлмө',
            location_en='Building A, room 205',
            staff_count=8,
            icon='📊',
            order=1
        )
        
        OrganizationStructure.objects.create(
            name='Кафедра экономики',
            name_kg='Экономика кафедрасы',
            name_en='Economics Department',
            structure_type='department',
            parent=economics_faculty,
            description='Кафедра экономических дисциплин',
            description_kg='Экономикалык дисциплиналардын кафедрасы',
            description_en='Economics disciplines department',
            head='Мамбетов Канат Асылбекович',
            head_kg='Мамбетов Канат Асылбекович',
            head_en='Mambetov Kanat Asylbekovich',
            responsibilities=['Преподавание экономических дисциплин', 'Исследования', 'Публикации'],
            responsibilities_kg=['Экономикалык дисциплиналарды окутуу', 'Изилдөөлөр', 'Басылмалар'],
            responsibilities_en=['Teaching economic disciplines', 'Research', 'Publications'],
            email='economics.dept@salymbekov.edu.kg',
            phone='+996 (312) 54-56-86',
            location='Корпус А, каб. 210',
            location_kg='А корпусу, 210-бөлмө',
            location_en='Building A, room 210',
            staff_count=10,
            icon='💰',
            order=2
        )
        
        # Services and centers
        OrganizationStructure.objects.create(
            name='Центр информационных технологий',
            name_kg='Маалыматтык технологиялар борбору',
            name_en='Information Technology Center',
            structure_type='center',
            description='Центр технической поддержки и развития ИТ',
            description_kg='Техникалык колдоо жана ИТ өнүктүрүү борбору',
            description_en='Technical support and IT development center',
            head='Исманов Бакыт Мурзакулович',
            head_kg='Исманов Бакыт Мурзакулович',
            head_en='Ismanov Bakyt Murzakulovich',
            responsibilities=['Техническая поддержка', 'Развитие ИТ-инфраструктуры', 'Обучение персонала'],
            responsibilities_kg=['Техникалык колдоо', 'ИТ инфраструктурасын өнүктүрүү', 'Кызматкерлерди үйрөтүү'],
            responsibilities_en=['Technical support', 'IT infrastructure development', 'Staff training'],
            email='it@salymbekov.edu.kg',
            phone='+996 (312) 54-56-90',
            location='Корпус Б, 1 этаж',
            location_kg='Б корпусу, 1-кат',
            location_en='Building B, 1st floor',
            staff_count=6,
            icon='💻',
            order=3
        )
        
        # Create Document data (для /documents/)
        self.stdout.write("Creating Document data...")
        documents_data = [
            {
                'title': 'Устав Международной академии управления, права, финансов и бизнеса',
                'title_kg': 'Эл аралык башкаруу, укук, каржы жана бизнес академиясынын жарыягы',
                'title_en': 'Charter of International Academy of Management, Law, Finance and Business',
                'document_type': 'charter',
                'description': 'Основополагающий документ академии, определяющий ее правовой статус и деятельность.',
                'description_kg': 'Академиянын укуктук статусун жана ишмердүүлүгүн аныктаган негизги документи.',
                'description_en': 'Founding document of the academy defining its legal status and activities.',
                'document_number': 'У-001',
                'document_date': date(2023, 1, 15),
                'file_size': 2048576,  # 2MB
                'file_format': 'PDF',
                'icon': '📜',
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'Положение об организации учебного процесса',
                'title_kg': 'Окуу процессин уюштуруу жөнүндө жобо',
                'title_en': 'Regulation on Educational Process Organization',
                'document_type': 'regulation',
                'description': 'Документ, регламентирующий организацию и проведение учебного процесса в академии.',
                'description_kg': 'Академияда окуу процессин уюштурууну жана өткөрүүнү регламенттөөчү документ.',
                'description_en': 'Document regulating the organization and conduct of educational process in the academy.',
                'document_number': 'П-002',
                'document_date': date(2023, 3, 10),
                'file_size': 1536000,  # 1.5MB
                'file_format': 'PDF',
                'icon': '📚',
                'is_featured': True,
                'order': 2
            },
            {
                'title': 'Приказ о назначении руководства академии',
                'title_kg': 'Академия жетекчилигин дайындоо жөнүндө буйрук',
                'title_en': 'Order on Academy Leadership Appointment',
                'document_type': 'order',
                'description': 'Приказ о назначении ректора и проректоров академии.',
                'description_kg': 'Академиянын ректорун жана проректорлорун дайындоо жөнүндө буйрук.',
                'description_en': 'Order on appointment of rector and vice-rectors of the academy.',
                'document_number': 'ПР-015',
                'document_date': date(2023, 9, 1),
                'file_size': 512000,  # 500KB
                'file_format': 'PDF',
                'icon': '📋',
                'order': 3
            },
            {
                'title': 'Стратегический план развития на 2024-2028 годы',
                'title_kg': '2024-2028-жылдарга өнүктүрүүнүн стратегиялык планы',
                'title_en': 'Strategic Development Plan for 2024-2028',
                'document_type': 'plan',
                'description': 'Долгосрочный план развития академии на пятилетний период.',
                'description_kg': 'Беш жылдык мөөнөткө академияны өнүктүрүүнүн узак мөөнөттүү планы.',
                'description_en': 'Long-term development plan of the academy for five-year period.',
                'document_number': 'СП-001',
                'document_date': date(2023, 12, 20),
                'file_size': 3072000,  # 3MB
                'file_format': 'PDF',
                'icon': '📈',
                'is_featured': True,
                'order': 4
            },
            {
                'title': 'Положение о студенческом самоуправлении',
                'title_kg': 'Студенттик өз алдынча башкаруу жөнүндө жобо',
                'title_en': 'Regulation on Student Self-Government',
                'document_type': 'regulation',
                'description': 'Документ, определяющий принципы и порядок работы органов студенческого самоуправления.',
                'description_kg': 'Студенттик өз алдынча башкаруу органдарынын иш принциптерин жана тартибин аныктаган документ.',
                'description_en': 'Document defining principles and procedures of student self-government bodies.',
                'document_number': 'П-025',
                'document_date': date(2023, 5, 15),
                'file_size': 1024000,  # 1MB
                'file_format': 'PDF',
                'icon': '🎓',
                'order': 5
            },
            {
                'title': 'Инструкция по технике безопасности в учебных аудиториях',
                'title_kg': 'Окуу залдарында коопсуздук техникасы боюнча көрсөтмө',
                'title_en': 'Safety Instructions for Classrooms',
                'document_type': 'instruction',
                'description': 'Инструкция по соблюдению техники безопасности в учебных помещениях.',
                'description_kg': 'Окуу бөлмөлөрүндө коопсуздук техникасын сактоо боюнча көрсөтмө.',
                'description_en': 'Instructions for safety compliance in educational facilities.',
                'document_number': 'И-003',
                'document_date': date(2023, 8, 30),
                'file_size': 768000,  # 750KB
                'file_format': 'PDF',
                'icon': '⚠️',
                'order': 6
            },
            {
                'title': 'Отчет о деятельности академии за 2023 год',
                'title_kg': '2023-жыл үчүн академиянын ишмердүүлүгү жөнүндө отчет',
                'title_en': 'Academy Activity Report for 2023',
                'document_type': 'report',
                'description': 'Годовой отчет о деятельности академии, достижениях и планах.',
                'description_kg': 'Академиянын ишмердүүлүгү, жетишкендиктери жана пландары жөнүндө жылдык отчет.',
                'description_en': 'Annual report on academy activities, achievements and plans.',
                'document_number': 'О-001',
                'document_date': date(2024, 1, 31),
                'file_size': 4096000,  # 4MB
                'file_format': 'PDF',
                'icon': '📊',
                'is_featured': True,
                'order': 7
            }
        ]
        
        for data in documents_data:
            Document.objects.create(**data)
        
        # Summary
        leadership_count = Leadership.objects.count()
        structure_count = OrganizationStructure.objects.count()
        document_count = Document.objects.count()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully created sample data:\n'
                f'  - Leadership: {leadership_count} records\n'
                f'  - Organization Structure: {structure_count} records\n'
                f'  - Documents: {document_count} records\n'
                f'\nNew API endpoints are now available:\n'
                f'  - /api/leadership-structure/leadership/\n'
                f'  - /api/leadership-structure/organization-structure/\n'
                f'  - /api/leadership-structure/documents/\n'
            )
        )