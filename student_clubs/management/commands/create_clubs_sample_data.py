from django.core.management.base import BaseCommand
from student_clubs.models import Club, ClubCategory, ClubLeader, ClubStats


class Command(BaseCommand):
    help = 'Создает тестовые данные для студенческих клубов'

    def handle(self, *args, **kwargs):
        self.stdout.write('Создание тестовых данных для студенческих клубов...')
        
        # Очистка существующих данных
        Club.objects.all().delete()
        ClubCategory.objects.all().delete()
        ClubLeader.objects.all().delete()
        ClubStats.objects.all().delete()
        
        # Создание категорий
        categories = {
            'tech': ClubCategory.objects.create(
                name_ru='Технологии и IT',
                name_en='Technology & IT',
                name_kg='Технология жана IT',
                slug='tech',
                order=1
            ),
            'sports': ClubCategory.objects.create(
                name_ru='Спорт и здоровье',
                name_en='Sports & Health',
                name_kg='Спорт жанаден соолук',
                slug='sports',
                order=2
            ),
            'arts': ClubCategory.objects.create(
                name_ru='Искусство и творчество',
                name_en='Arts & Creativity',
                name_kg='Искусство жана чыгармачылык',
                slug='arts',
                order=3
            ),
            'science': ClubCategory.objects.create(
                name_ru='Наука и исследования',
                name_en='Science & Research',
                name_kg='Илим жана изилдөөлөр',
                slug='science',
                order=4
            ),
            'social': ClubCategory.objects.create(
                name_ru='Социальные проекты',
                name_en='Social Projects',
                name_kg='Социалдык долбоорлор',
                slug='social',
                order=5
            ),
            'business': ClubCategory.objects.create(
                name_ru='Бизнес и предпринимательство',
                name_en='Business & Entrepreneurship',
                name_kg='Бизнес жана ишкердик',
                slug='business',
                order=6
            ),
        }
        
        # Создание клубов
        clubs_data = [
            {
                'category': categories['tech'],
                'icon': '💻',
                'status': 'active',
                'members_count': 45,
                'name_ru': 'IT Club',
                'name_en': 'IT Club',
                'name_kg': 'IT клубу',
                'short_description_ru': 'Программирование и разработка',
                'short_description_en': 'Programming and development',
                'short_description_kg': 'Программалоо жана иштеп чыгуу',
                'description_ru': 'Клуб для студентов, интересующихся программированием, веб-разработкой и IT-технологиями. Проводим воркшопы, хакатоны и совместные проекты.',
                'description_en': 'Club for students interested in programming, web development and IT technologies. We conduct workshops, hackathons and joint projects.',
                'description_kg': 'Программалоого, веб-иштеп чыгууга жана IT технологияларына кызыккан студенттер үчүн клуб. Биз семинарларды, хакатондорду жана биргелешкен долбоорлорду өткөрөбүз.',
                'goals_ru': 'Развитие практических навыков программирования\nОбмен опытом между участниками\nУчастие в IT-конференциях и хакатонах\nСоздание реальных проектов',
                'goals_en': 'Developing practical programming skills\nSharing experience between participants\nParticipation in IT conferences and hackathons\nCreating real projects',
                'goals_kg': 'Практикалык программалоо көндүмдөрүн өнүктүрүү\nКатышуучулар ортосунда тажрыйба алмашуу\nIT конференцияларга жана хакатондорго катышуу\nРеалдуу долбоорлорду түзүү',
                'motivation_ru': 'Получите реальный опыт работы над проектами\nПодготовьтесь к карьере в IT\nНайдите единомышленников\nУлучшите свое портфолио',
                'motivation_en': 'Get real experience working on projects\nPrepare for a career in IT\nFind like-minded people\nImprove your portfolio',
                'motivation_kg': 'Долбоорлор боюнча иштөөдө реалдуу тажрыйба алыңыз\nIT тармагында карьераны даярдаңыз\nБир ой адамдарды табыңыз\nӨз портфолиоңузду жакшыртыңыз',
                'meetings_ru': 'Каждую среду 19:00',
                'meetings_en': 'Every Wednesday 7 PM',
                'meetings_kg': 'Ар шаршемби саат 19:00',
                'tags': ['python', 'javascript', 'web', 'programming'],
                'join_link': 'https://t.me/itclub_academy',
                'order': 1
            },
            {
                'category': categories['tech'],
                'icon': '🤖',
                'status': 'active',
                'members_count': 32,
                'name_ru': 'AI & Machine Learning',
                'name_en': 'AI & Machine Learning',
                'name_kg': 'AI жана Machine Learning',
                'short_description_ru': 'Искусственный интеллект и машинное обучение',
                'short_description_en': 'Artificial intelligence and machine learning',
                'short_description_kg': 'Жасалма интеллект жана машиналык окутуу',
                'description_ru': 'Изучаем искусственный интеллект, машинное обучение и нейронные сети. Работаем над проектами в области Data Science и AI.',
                'description_en': 'We study artificial intelligence, machine learning and neural networks. We work on projects in Data Science and AI.',
                'description_kg': 'Биз жасалма интеллектти, машиналык окутууну жана нейрондук тармактарды үйрөнөбүз. Data Science жана AI чөйрөсүндө долбоорлор боюнча иштейбиз.',
                'goals_ru': 'Освоение современных ML библиотек\nРазработка AI моделей\nУчастие в соревнованиях по Data Science\nПрименение AI в реальных задачах',
                'goals_en': 'Mastering modern ML libraries\nDeveloping AI models\nParticipation in Data Science competitions\nApplying AI to real problems',
                'goals_kg': 'Заманбап ML китепканаларды үйрөнүү\nAI моделдерин иштеп чыгуу\nData Science мелдештерине катышуу\nReалдуу маселелерде AI колдонуу',
                'motivation_ru': 'Работайте с передовыми технологиями\nСтаньте экспертом в AI\nУчаствуйте в Kaggle соревнованиях\nСоздавайте умные системы',
                'motivation_en': 'Work with cutting-edge technologies\nBecome an AI expert\nParticipate in Kaggle competitions\nCreate smart systems',
                'motivation_kg': 'Заманбап технологиялар менен иштеңиз\nAI адиси болуңуз\nKaggle мелдештерине катышыңыз\nАкылдуу системаларды түзүңүз',
                'meetings_ru': 'Каждый вторник 18:00',
                'meetings_en': 'Every Tuesday 6 PM',
                'meetings_kg': 'Ар шейшемби саат 18:00',
                'tags': ['ai', 'ml', 'datascience', 'neuralnetworks'],
                'join_link': 'https://t.me/aiml_academy',
                'order': 2
            },
            {
                'category': categories['sports'],
                'icon': '⚽',
                'status': 'active',
                'members_count': 67,
                'name_ru': 'Футбольный клуб',
                'name_en': 'Football Club',
                'name_kg': 'Футбол клубу',
                'short_description_ru': 'Футбол и командные игры',
                'short_description_en': 'Football and team games',
                'short_description_kg': 'Футбол жана командалык оюндар',
                'description_ru': 'Тренировки по футболу, участие в университетских лигах и турнирах. Приветствуются игроки любого уровня.',
                'description_en': 'Football training, participation in university leagues and tournaments. Players of all levels are welcome.',
                'description_kg': 'Футбол машыгуулары, университеттик лигаларга жана турнирлерге катышуу. Бардык деңгээлдеги оюнчулар кош келиңиз.',
                'goals_ru': 'Физическое развитие студентов\nУчастие в межвузовских соревнованиях\nРазвитие командного духа\nДостижение спортивных результатов',
                'goals_en': 'Physical development of students\nParticipation in interuniversity competitions\nDevelopment of team spirit\nAchieving sports results',
                'goals_kg': 'Студенттердин физикалык өнүгүшү\nЖогорку окуу жайлар аралык мелдештерге катышуу\nКомандалык руханы өнүктүрүү\nСпорттук жетишкендиктерге жетүү',
                'motivation_ru': 'Улучшите физическую форму\nНайдите друзей в команде\nУчаствуйте в турнирах\nПолучите здоровье и энергию',
                'motivation_en': 'Improve your fitness\nFind friends in the team\nParticipate in tournaments\nGet health and energy',
                'motivation_kg': 'Физикалык формаңызды жакшыртыңыз\nКомандада досторду табыңыз\nТурнирлерге катышыңыз\nДен соолукту жана энергияны алыңыз',
                'meetings_ru': 'Вторник, Четверг 17:00',
                'meetings_en': 'Tuesday, Thursday 5 PM',
                'meetings_kg': 'Шейшемби, Бейшемби 17:00',
                'tags': ['football', 'sport', 'team', 'fitness'],
                'join_link': 'https://t.me/football_academy',
                'order': 3
            },
            {
                'category': categories['arts'],
                'icon': '🎭',
                'status': 'active',
                'members_count': 28,
                'name_ru': 'Театральная студия',
                'name_en': 'Theater Studio',
                'name_kg': 'Театр студиясы',
                'short_description_ru': 'Актерское мастерство и театр',
                'short_description_en': 'Acting and theater',
                'short_description_kg': 'Актёрдук чеберчилик жана театр',
                'description_ru': 'Развиваем актерские навыки, ставим спектакли, изучаем сценическое искусство. Открыты для всех, кто любит театр.',
                'description_en': 'We develop acting skills, stage performances, study theatrical art. Open to everyone who loves theater.',
                'description_kg': 'Актёрдук көндүмдөрдү өнүктүрөбүз, спектакльдерди коёбуз, сахна искусствосун үйрөнөбүз. Театрды сүйгөн бардыгына ачык.',
                'goals_ru': 'Развитие актерского мастерства\nПостановка спектаклей\nУчастие в фестивалях\nРазвитие публичных выступлений',
                'goals_en': 'Development of acting skills\nStaging performances\nParticipation in festivals\nDevelopment of public speaking',
                'goals_kg': 'Актёрдук чеберчиликти өнүктүрүү\nСпектакльдерди коюу\nФестивалдарга катышуу\nКоомдук сүйлөөнү өнүктүрүү',
                'motivation_ru': 'Раскройте свой творческий потенциал\nПреодолейте страх публичных выступлений\nНайдите друзей-единомышленников\nУчаствуйте в постановках',
                'motivation_en': 'Unlock your creative potential\nOvercome fear of public speaking\nFind like-minded friends\nParticipate in productions',
                'motivation_kg': 'Чыгармачыл потенциалыңызды ачыңыз\nКоомдук сүйлөө коркунучун жеңиңиз\nБир ой досторду табыңыз\nКоюулуларга катышыңыз',
                'meetings_ru': 'Понедельник, Пятница 18:00',
                'meetings_en': 'Monday, Friday 6 PM',
                'meetings_kg': 'Дүйшөмбү, Жума 18:00',
                'tags': ['theater', 'acting', 'art', 'performance'],
                'join_link': 'https://t.me/theater_academy',
                'order': 4
            },
            {
                'category': categories['business'],
                'icon': '💼',
                'status': 'recruiting',
                'members_count': 25,
                'name_ru': 'Бизнес Клуб',
                'name_en': 'Business Club',
                'name_kg': 'Бизнес клубу',
                'short_description_ru': 'Предпринимательство и стартапы',
                'short_description_en': 'Entrepreneurship and startups',
                'short_description_kg': 'Ишкердик жана стартаптар',
                'description_ru': 'Изучаем основы бизнеса, создаем стартапы, встречаемся с предпринимателями. Развиваем деловое мышление.',
                'description_en': 'We study business basics, create startups, meet with entrepreneurs. We develop business thinking.',
                'description_kg': 'Бизнестин негиздерин үйрөнөбүз, стартаптарды түзөбүз, ишкерлер менен жолугабыз. Бизнес ой жүгүртүүнү өнүктүрөбүз.',
                'goals_ru': 'Обучение основам предпринимательства\nСоздание и развитие стартапов\nНетворкинг с бизнес-сообществом\nУчастие в питч-сессиях',
                'goals_en': 'Learning the basics of entrepreneurship\nCreating and developing startups\nNetworking with business community\nParticipation in pitch sessions',
                'goals_kg': 'Ишкердиктин негиздерин үйрөнүү\nСтартаптарды түзүү жана өнүктүрүү\nБизнес коомчулук менен байланыш\nПитч-сессияларга катышуу',
                'motivation_ru': 'Создайте свой бизнес\nОбучайтесь у успешных предпринимателей\nНайдите соучредителей\nПолучите инвестиции',
                'motivation_en': 'Create your business\nLearn from successful entrepreneurs\nFind co-founders\nGet investments',
                'motivation_kg': 'Өз бизнесиңизди түзүңүз\nУтулуктуу ишкерлерден үйрөнүңүз\nКо-негиздөөчүлөрдү табыңыз\nИнвестицияларды алыңыз',
                'meetings_ru': 'Каждую субботу 14:00',
                'meetings_en': 'Every Saturday 2 PM',
                'meetings_kg': 'Ар ишемби саат 14:00',
                'tags': ['business', 'startup', 'entrepreneurship', 'investment'],
                'join_link': 'https://t.me/business_academy',
                'order': 5
            },
            {
                'category': categories['science'],
                'icon': '🔬',
                'status': 'active',
                'members_count': 19,
                'name_ru': 'Клуб Физики',
                'name_en': 'Physics Club',
                'name_kg': 'Физика клубу',
                'short_description_ru': 'Исследования в области физики',
                'short_description_en': 'Research in physics',
                'short_description_kg': 'Физика чөйрөсүндө изилдөөлөр',
                'description_ru': 'Проводим эксперименты, изучаем современную физику, участвуем в научных конференциях и олимпиадах.',
                'description_en': 'We conduct experiments, study modern physics, participate in scientific conferences and olympiads.',
                'description_kg': 'Эксперименттерди жүргүзөбүз, заманбап физиканы үйрөнөбүз, илимий конференцияларга жана олимпиадаларга катышабыз.',
                'goals_ru': 'Проведение научных экспериментов\nИзучение передовых областей физики\nПубликация научных работ\nУчастие в олимпиадах',
                'goals_en': 'Conducting scientific experiments\nStudying advanced fields of physics\nPublishing scientific papers\nParticipation in olympiads',
                'goals_kg': 'Илимий эксперименттерди жүргүзүү\nФизиканын алдыңкы чөйрөлөрүн үйрөнүү\nИлимий эмгектерди жарыялоо\nОлимпиадаларга катышуу',
                'motivation_ru': 'Работайте с научным оборудованием\nПубликуйте статьи\nУчаствуйте в конференциях\nРазвивайте научное мышление',
                'motivation_en': 'Work with scientific equipment\nPublish articles\nParticipate in conferences\nDevelop scientific thinking',
                'motivation_kg': 'Илимий жабдуулар менен иштеңиз\nМакалаларды жарыялаңыз\nКонференцияларга катышыңыз\nИлимий ой жүгүртүүнү өнүктүрүңүз',
                'meetings_ru': 'Среда 16:00',
                'meetings_en': 'Wednesday 4 PM',
                'meetings_kg': 'Шаршемби 16:00',
                'tags': ['physics', 'science', 'research', 'experiments'],
                'join_link': 'https://t.me/physics_academy',
                'order': 6
            },
        ]
        
        # Создаем клубы
        for club_data in clubs_data:
            club = Club.objects.create(**club_data)
            self.stdout.write(self.style.SUCCESS(f'✓ Создан клуб: {club.name_ru}'))
            
            # Добавляем руководителей для каждого клуба
            leaders_data = [
                {
                    'club': club,
                    'name_ru': f'Иванов Иван Иванович',
                    'name_en': f'Ivan Ivanov',
                    'name_kg': f'Иван Иванов',
                    'role_ru': 'Президент клуба',
                    'role_en': 'Club President',
                    'role_kg': 'Клубдун президенти',
                    'email': f'president@{club.id}.club',
                    'order': 1
                },
                {
                    'club': club,
                    'name_ru': f'Петров Петр Петрович',
                    'name_en': f'Petr Petrov',
                    'name_kg': f'Петр Петров',
                    'role_ru': 'Вице-президент',
                    'role_en': 'Vice President',
                    'role_kg': 'Вице-президент',
                    'email': f'vicepresident@{club.id}.club',
                    'order': 2
                },
            ]
            
            for leader_data in leaders_data:
                ClubLeader.objects.create(**leader_data)
        
        # Создаем статистику
        stats_data = [
            {
                'value': '50+',
                'label_ru': 'Активных клубов',
                'label_en': 'Active clubs',
                'label_kg': 'Активдүү клубдар',
                'icon': '🎯',
                'order': 1
            },
            {
                'value': '1200+',
                'label_ru': 'Участников',
                'label_en': 'Members',
                'label_kg': 'Катышуучулар',
                'icon': '👥',
                'order': 2
            },
            {
                'value': '100+',
                'label_ru': 'Мероприятий в год',
                'label_en': 'Events per year',
                'label_kg': 'Жылына иш-чаралар',
                'icon': '📅',
                'order': 3
            },
            {
                'value': '15+',
                'label_ru': 'Категорий',
                'label_en': 'Categories',
                'label_kg': 'Категориялар',
                'icon': '🏷️',
                'order': 4
            },
        ]
        
        for stat_data in stats_data:
            ClubStats.objects.create(**stat_data)
        
        self.stdout.write(self.style.SUCCESS('\n✓ Тестовые данные успешно созданы!'))
        self.stdout.write(self.style.SUCCESS(f'Категорий: {ClubCategory.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Клубов: {Club.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Руководителей: {ClubLeader.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Статистики: {ClubStats.objects.count()}'))
