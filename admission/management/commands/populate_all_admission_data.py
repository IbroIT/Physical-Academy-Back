from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from admission.models import (
    QuotaType, QuotaRequirement, QuotaBenefit, 
    QuotaStats, AdditionalSupport, ProcessStep,
    MasterDocuments, MasterMainDate, MasterPrograms, MasterRequirements,
    AspirantMainDate, AspirantPrograms, AspirantRequirements, AspirantDocuments
)
import os


class Command(BaseCommand):
    help = 'Загружает полные данные для всех моделей приложения admission'

    def handle(self, *args, **options):
        self.stdout.write('Начинаем загрузку всех данных для admission...')
        
        # Очищаем существующие данные
        self.clear_existing_data()
        
        # Загружаем данные по категориям
        self.create_quota_data()
        self.create_master_data()
        self.create_aspirant_data()
        
        self.stdout.write(
            self.style.SUCCESS('Все данные успешно загружены!')
        )

    def clear_existing_data(self):
        """Очистка существующих данных"""
        self.stdout.write('Очищаем существующие данные...')
        
        # Удаляем все записи
        models_to_clear = [
            QuotaType, QuotaStats, AdditionalSupport, ProcessStep,
            MasterDocuments, MasterMainDate, MasterPrograms, MasterRequirements,
            AspirantMainDate, AspirantPrograms, AspirantRequirements, AspirantDocuments
        ]
        
        for model in models_to_clear:
            model.objects.all().delete()

    def create_quota_data(self):
        """Создание данных по квотам"""
        self.stdout.write('Создаем данные по квотам...')
        
        # Создаем типы квот
        self.create_quota_types()
        
        # Создаем статистику
        self.create_quota_stats()
        
        # Создаем дополнительную поддержку
        self.create_additional_support()
        
        # Создаем шаги процесса
        self.create_process_steps()

    def create_master_data(self):
        """Создание данных для магистратуры"""
        self.stdout.write('Создаем данные для магистратуры...')
        
        # Создаем программы магистратуры
        self.create_master_programs()
        
        # Создаем требования для магистратуры
        self.create_master_requirements()
        
        # Создаем основные даты для магистратуры
        self.create_master_main_dates()
        
        # Создаем документы для магистратуры
        self.create_master_documents()

    def create_aspirant_data(self):
        """Создание данных для аспирантуры"""
        self.stdout.write('Создаем данные для аспирантуры...')
        
        # Создаем программы аспирантуры
        self.create_aspirant_programs()
        
        # Создаем требования для аспирантуры
        self.create_aspirant_requirements()
        
        # Создаем основные даты для аспирантуры
        self.create_aspirant_main_dates()
        
        # Создаем документы для аспирантуры
        self.create_aspirant_documents()

    def create_quota_types(self):
        """Создание типов квот с требованиями и преимуществами"""
        
        # Спортивная квота
        sports_quota = QuotaType.objects.create(
            type='sports',
            title_ru='Спортивная квота',
            title_kg='Спорттук квота',
            title_en='Sports Quota',
            description_ru='Для спортсменов с выдающимися достижениями',
            description_kg='Мыкты жетишкендиктери бар спортчулар үчүн',
            description_en='For athletes with outstanding achievements',
            icon='🏆',
            spots=15,
            deadline='20 августа',
            color='blue',
            order=1
        )
        
        # Требования для спортивной квоты
        sports_requirements = [
            {
                'ru': 'Документы, подтверждающие спортивные достижения',
                'kg': 'Спорттук жетишкендиктерди ырастаган документтер',
                'en': 'Documents confirming sports achievements'
            },
            {
                'ru': 'Рекомендация от спортивной федерации',
                'kg': 'Спорт федерациясынан сунуш',
                'en': 'Recommendation from sports federation'
            },
            {
                'ru': 'Медицинская справка о допуске к занятиям',
                'kg': 'Машыгууларга уруксат берүү тууралуу медициналык справка',
                'en': 'Medical certificate for training admission'
            },
            {
                'ru': 'Аттестат о среднем образовании',
                'kg': 'Орто билим тууралуу аттестат',
                'en': 'Secondary education certificate'
            }
        ]
        
        for idx, req in enumerate(sports_requirements):
            QuotaRequirement.objects.create(
                quota_type=sports_quota,
                requirement_ru=req['ru'],
                requirement_kg=req['ky'],
                requirement_en=req['en'],
                order=idx + 1
            )
        
        # Преимущества для спортивной квоты
        sports_benefits = [
            {
                'ru': 'Индивидуальный учебный план',
                'kg': 'Жеке окуу планы',
                'en': 'Individual study plan'
            },
            {
                'ru': 'Совмещение тренировок и учебы',
                'kg': 'Машыгуулар менен окууну айкалыштыруу',
                'en': 'Combining training and studies'
            },
            {
                'ru': 'Спортивная стипендия',
                'kg': 'Спорттук стипендия',
                'en': 'Sports scholarship'
            },
            {
                'ru': 'Проживание в спортивном общежитии',
                'kg': 'Спорттук жатаканада жашоо',
                'en': 'Accommodation in sports dormitory'
            }
        ]
        
        for idx, benefit in enumerate(sports_benefits):
            QuotaBenefit.objects.create(
                quota_type=sports_quota,
                benefit_ru=benefit['ru'],
                benefit_kg=benefit['ky'],
                benefit_en=benefit['en'],
                order=idx + 1
            )
        
        # Квота по состоянию здоровья
        health_quota = QuotaType.objects.create(
            type='health',
            title_ru='Квота по состоянию здоровья',
            title_kg='Ден соолук абалы боюнча квота',
            title_en='Health Status Quota',
            description_ru='Для лиц с ограниченными возможностями здоровья',
            description_kg='Ден соолук мүмкүнчүлүктөрү чектелген адамдар үчүн',
            description_en='For people with limited health opportunities',
            icon='❤️',
            spots=10,
            deadline='25 августа',
            color='green',
            order=2
        )
        
        # Требования для квоты по здоровью
        health_requirements = [
            {
                'ru': 'Медико-социальная экспертиза',
                'kg': 'Медициналык-социалдык экспертиза',
                'en': 'Medical-social examination'
            },
            {
                'ru': 'Индивидуальная программа реабилитации',
                'kg': 'Жеке реабилитация программасы',
                'en': 'Individual rehabilitation program'
            },
            {
                'ru': 'Заключение врачебной комиссии академии',
                'kg': 'Академиянын дарыгер комиссиясынын корутундусу',
                'en': 'Conclusion of academy medical commission'
            }
        ]
        
        for idx, req in enumerate(health_requirements):
            QuotaRequirement.objects.create(
                quota_type=health_quota,
                requirement_ru=req['ru'],
                requirement_kg=req['ky'],
                requirement_en=req['en'],
                order=idx + 1
            )
        
        # Преимущества для квоты по здоровью
        health_benefits = [
            {
                'ru': 'Адаптированная программа обучения',
                'kg': 'Адаптацияланган окуу программасы',
                'en': 'Adapted learning program'
            },
            {
                'ru': 'Доступная среда',
                'kg': 'Жеткиликтүү чөйрө',
                'en': 'Accessible environment'
            },
            {
                'ru': 'Персональный тьютор',
                'kg': 'Жеке тьютор',
                'en': 'Personal tutor'
            },
            {
                'ru': 'Социальная поддержка',
                'kg': 'Социалдык колдоо',
                'en': 'Social support'
            }
        ]
        
        for idx, benefit in enumerate(health_benefits):
            QuotaBenefit.objects.create(
                quota_type=health_quota,
                benefit_ru=benefit['ru'],
                benefit_kg=benefit['ky'],
                benefit_en=benefit['en'],
                order=idx + 1
            )
        
        # Целевая квота
        target_quota = QuotaType.objects.create(
            type='target',
            title_ru='Целевая квота',
            title_kg='Максаттуу квота',
            title_en='Target Quota',
            description_ru='Для будущих сотрудников спортивных организаций',
            description_kg='Спорттук уюмдардын келечектеги кызматкерлери үчүн',
            description_en='For future employees of sports organizations',
            icon='🎯',
            spots=20,
            deadline='15 августа',
            color='cyan',
            order=3
        )
        
        # Требования для целевой квоты
        target_requirements = [
            {
                'ru': 'Направление от спортивной организации',
                'kg': 'Спорттук уюмдан багыт',
                'en': 'Referral from sports organization'
            },
            {
                'ru': 'Трехсторонний договор',
                'kg': 'Үч тараптуу келишим',
                'en': 'Tripartite agreement'
            },
            {
                'ru': 'Обязательство отработать 3 года',
                'kg': '3 жыл иштөө милдеттенмеси',
                'en': 'Commitment to work for 3 years'
            }
        ]
        
        for idx, req in enumerate(target_requirements):
            QuotaRequirement.objects.create(
                quota_type=target_quota,
                requirement_ru=req['ru'],
                requirement_kg=req['ky'],
                requirement_en=req['en'],
                order=idx + 1
            )
        
        # Преимущества для целевой квоты
        target_benefits = [
            {
                'ru': 'Гарантированное трудоустройство',
                'kg': 'Кепилдик берилген жумуш орду',
                'en': 'Guaranteed employment'
            },
            {
                'ru': 'Стажировка в профильных организациях',
                'kg': 'Профилдик уюмдарда стажировка',
                'en': 'Internship in specialized organizations'
            },
            {
                'ru': 'Дополнительная стипендия',
                'kg': 'Кошумча стипендия',
                'en': 'Additional scholarship'
            }
        ]
        
        for idx, benefit in enumerate(target_benefits):
            QuotaBenefit.objects.create(
                quota_type=target_quota,
                benefit_ru=benefit['ru'],
                benefit_kg=benefit['ky'],
                benefit_en=benefit['en'],
                order=idx + 1
            )

    def create_quota_stats(self):
        """Создание статистических данных"""
        stats_data = [
            {
                'stat_type': 'total_spots',
                'number': '45',
                'label_ru': 'всего мест по квотам',
                'label_kg': 'квоталар боюнча жалпы орундар',
                'label_en': 'total quota spots',
                'description_ru': 'Ежегодно выделяется',
                'description_kg': 'Жыл сайын бөлүнөт',
                'description_en': 'Allocated annually',
                'order': 1
            },
            {
                'stat_type': 'success_rate',
                'number': '98%',
                'label_ru': 'успешного зачисления',
                'label_kg': 'ийгиликтүү кабыл алуу',
                'label_en': 'successful admission',
                'description_ru': 'Проходят конкурсный отбор',
                'description_kg': 'Конкурстук тандоодон өтүшөт',
                'description_en': 'Pass competitive selection',
                'order': 2
            },
            {
                'stat_type': 'organizations',
                'number': '25+',
                'label_ru': 'спортивных организаций',
                'label_kg': 'спорттук уюмдар',
                'label_en': 'sports organizations',
                'description_ru': 'Участвуют в программе',
                'description_kg': 'Программага катышышат',
                'description_en': 'Participate in the program',
                'order': 3
            },
            {
                'stat_type': 'quota_types',
                'number': '3',
                'label_ru': 'вида квот',
                'label_kg': 'квота түрү',
                'label_en': 'types of quotas',
                'description_ru': 'Для разных категорий абитуриентов',
                'description_kg': 'Түрдүү категориядагы абитуриенттер үчүн',
                'description_en': 'For different categories of applicants',
                'order': 4
            }
        ]
        
        for stat in stats_data:
            QuotaStats.objects.create(**stat)

    def create_additional_support(self):
        """Создание дополнительной поддержки"""
        support_data = [
            {
                'support_ru': 'Персональный спортивный наставник',
                'support_kg': 'Жеке спорттук насаатчы',
                'support_en': 'Personal sports mentor',
                'order': 1
            },
            {
                'support_ru': 'Спортивная экипировка и инвентарь',
                'support_kg': 'Спорттук экипировка жана инвентарь',
                'support_en': 'Sports equipment and inventory',
                'order': 2
            },
            {
                'support_ru': 'Специализированное питание',
                'support_kg': 'Адистештирилген тамак-аш',
                'support_en': 'Specialized nutrition',
                'order': 3
            },
            {
                'support_ru': 'Медицинское сопровождение и восстановление',
                'support_kg': 'Медициналык коштоо жана калыбына келтирүү',
                'support_en': 'Medical support and recovery',
                'order': 4
            }
        ]
        
        for support in support_data:
            AdditionalSupport.objects.create(**support)

    def create_process_steps(self):
        """Создание шагов процесса"""
        steps_data = [
            {
                'step_number': 1,
                'title_ru': 'Консультация',
                'title_kg': 'Консультация',
                'title_en': 'Consultation',
                'description_ru': 'Получите консультацию в приемной комиссии и определите подходящую квоту',
                'description_kg': 'Кабыл алуу комиссиясынан консультация алып, ылайыктуу квотаны аныктаңыз',
                'description_en': 'Get consultation from admission committee and determine suitable quota',
                'color_scheme': 'from-blue-500 to-cyan-500'
            },
            {
                'step_number': 2,
                'title_ru': 'Документы',
                'title_kg': 'Документтер',
                'title_en': 'Documents',
                'description_ru': 'Подготовьте необходимый пакет документов и спортивные достижения',
                'description_kg': 'Керектүү документтердин топтомун жана спорттук жетишкендиктерди даярдаңыз',
                'description_en': 'Prepare necessary document package and sports achievements',
                'color_scheme': 'from-green-500 to-emerald-500'
            },
            {
                'step_number': 3,
                'title_ru': 'Подача',
                'title_kg': 'Тапшыруу',
                'title_en': 'Submission',
                'description_ru': 'Подайте заявление и пройдите дополнительные испытания',
                'description_kg': 'Арыз берип, кошумча сыноолордон өтүңүз',
                'description_en': 'Submit application and pass additional tests',
                'color_scheme': 'from-purple-500 to-pink-500'
            }
        ]
        
        for step in steps_data:
            ProcessStep.objects.create(**step)

    def create_master_programs(self):
        """Создание программ магистратуры"""
        programs_data = [
            {
                'program_name_ru': 'Спортивная педагогика',
                'program_name_kg': 'Спорттук педагогика',
                'program_name_en': 'Sports Pedagogy',
                'description_ru': 'Программа готовит высококвалифицированных специалистов в области спортивной педагогики и методики преподавания физической культуры.',
                'description_kg': 'Программа спорттук педагогика жана дене тарбия сабагын өткөрүү методикасы тармагында жогорку квалификациялуу адистерди даярдайт.',
                'description_en': 'The program prepares highly qualified specialists in the field of sports pedagogy and physical education teaching methodology.',
                'features_ru': [
                    'Инновационные методики обучения',
                    'Практические занятия в спортивных школах',
                    'Научно-исследовательская работа',
                    'Стажировки в ведущих спортивных центрах'
                ],
                'features_kg': [
                    'Инновациялык окутуу методикалары',
                    'Спорт мектептеринде практикалык сабактар',
                    'Илимий-изилдөө иштери',
                    'Алдыңкы спорт борборлорунда стажировкалар'
                ],
                'features_en': [
                    'Innovative teaching methods',
                    'Practical classes in sports schools',
                    'Research work',
                    'Internships in leading sports centers'
                ],
                'order': 1
            },
            {
                'program_name_ru': 'Спортивный менеджмент',
                'program_name_kg': 'Спорттук менеджмент',
                'program_name_en': 'Sports Management',
                'description_ru': 'Программа направлена на подготовку управленческих кадров для спортивной индустрии.',
                'description_kg': 'Программа спорт индустриясы үчүн башкаруу кадрларын даярдоого багытталган.',
                'description_en': 'The program is aimed at training management personnel for the sports industry.',
                'features_ru': [
                    'Управление спортивными организациями',
                    'Экономика спорта',
                    'Маркетинг в спорте',
                    'Международный спортивный бизнес'
                ],
                'features_kg': [
                    'Спорт уюмдарын башкаруу',
                    'Спорттун экономикасы',
                    'Спортто маркетинг',
                    'Эл аралык спорт бизнеси'
                ],
                'features_en': [
                    'Sports organization management',
                    'Sports economics',
                    'Sports marketing',
                    'International sports business'
                ],
                'order': 2
            },
            {
                'program_name_ru': 'Спортивная медицина',
                'program_name_kg': 'Спорттук медицина',
                'program_name_en': 'Sports Medicine',
                'description_ru': 'Подготовка специалистов по медицинскому обеспечению спортивной деятельности.',
                'description_kg': 'Спорттук ишмердүүлүктү медициналык камсыздоо боюнча адистерди даярдоо.',
                'description_en': 'Training specialists in medical support of sports activities.',
                'features_ru': [
                    'Спортивная травматология',
                    'Восстановительная медицина',
                    'Спортивная фармакология',
                    'Функциональная диагностика'
                ],
                'features_kg': [
                    'Спорттук травматология',
                    'Калыбына келтирүүчү медицина',
                    'Спорттук фармакология',
                    'Функционалдык диагностика'
                ],
                'features_en': [
                    'Sports traumatology',
                    'Rehabilitation medicine',
                    'Sports pharmacology',
                    'Functional diagnostics'
                ],
                'order': 3
            }
        ]
        
        for program in programs_data:
            MasterPrograms.objects.create(**program)

    def create_master_requirements(self):
        """Создание требований для магистратуры"""
        requirements_data = [
            {
                'title_ru': 'Образование',
                'title_kg': 'Билим берүү',
                'title_en': 'Education',
                'description_ru': 'Диплом о высшем образовании по профильной специальности или диплом о высшем образовании по любой специальности с дополнительным образованием в области физической культуры и спорта.',
                'description_kg': 'Профилдик адистик боюнча жогорку билим тууралуу диплом же кандай болбосун адистик боюнча жогорку билим тууралуу диплом дене тарбия жана спорт тармагында кошумча билим берүү менен.',
                'description_en': 'Higher education diploma in a relevant specialty or higher education diploma in any specialty with additional education in physical culture and sports.',
                'order': 1
            },
            {
                'title_ru': 'Вступительные экзамены',
                'title_kg': 'Кирүү экзамендери',
                'title_en': 'Entrance exams',
                'description_ru': 'Сдача комплексного экзамена по специальности, включающего теоретическую часть и практические задания.',
                'description_kg': 'Теориялык бөлүктү жана практикалык тапшырмаларды камтыган адистик боюнча комплекстүү экзаменди тапшыруу.',
                'description_en': 'Passing a comprehensive specialty exam that includes theoretical part and practical tasks.',
                'order': 2
            },
            {
                'title_ru': 'Документы',
                'title_kg': 'Документтер',
                'title_en': 'Documents',
                'description_ru': 'Заявление, диплом о высшем образовании, справка с места работы или учебы, медицинская справка, фотографии.',
                'description_kg': 'Арыз, жогорку билим тууралуу диплом, жумуш же окуу жеринен справка, медициналык справка, сүрөттөр.',
                'description_en': 'Application, higher education diploma, certificate from place of work or study, medical certificate, photographs.',
                'order': 3
            }
        ]
        
        for requirement in requirements_data:
            MasterRequirements.objects.create(**requirement)

    def create_master_main_dates(self):
        """Создание основных дат для магистратуры"""
        dates_data = [
            {
                'event_name_ru': 'Прием документов',
                'event_name_kg': 'Документтерди кабыл алуу',
                'event_name_en': 'Document submission',
                'date': '1 июня - 15 июля',
                'order': 1
            },
            {
                'event_name_ru': 'Вступительные экзамены',
                'event_name_kg': 'Кирүү экзамендери',
                'event_name_en': 'Entrance exams',
                'date': '20 июля - 5 августа',
                'order': 2
            },
            {
                'event_name_ru': 'Зачисление',
                'event_name_kg': 'Кабыл алуу',
                'event_name_en': 'Enrollment',
                'date': '10 августа',
                'order': 3
            },
            {
                'event_name_ru': 'Начало учебного года',
                'event_name_kg': 'Окуу жылынын башталышы',
                'event_name_en': 'Start of academic year',
                'date': '1 сентября',
                'order': 4
            }
        ]
        
        for date_item in dates_data:
            MasterMainDate.objects.create(**date_item)

    def create_master_documents(self):
        """Создание документов для магистратуры"""
        documents_data = [
            {
                'document_name_ru': 'Правила приема в магистратуру',
                'document_name_kg': 'Магистратурага кабыл алуу эрежелери',
                'document_name_en': 'Master\'s admission rules',
                'order': 1
            },
            {
                'document_name_ru': 'Программы вступительных экзаменов',
                'document_name_kg': 'Кирүү экзамендеринин программалары',
                'document_name_en': 'Entrance exam programs',
                'order': 2
            },
            {
                'document_name_ru': 'Список направлений подготовки',
                'document_name_kg': 'Даярдоо багыттарынын тизмеси',
                'document_name_en': 'List of training directions',
                'order': 3
            },
            {
                'document_name_ru': 'Образец заявления',
                'document_name_kg': 'Арыздын үлгүсү',
                'document_name_en': 'Application form',
                'order': 4
            }
        ]
        
        for doc in documents_data:
            # Создаем простой текстовый файл для примера
            content = f"Документ: {doc['document_name_ru']}\nЭто образец документа для тестирования системы."
            file_content = ContentFile(content.encode('utf-8'))
            file_name = f"master_doc_{doc['order']}.txt"
            
            master_doc = MasterDocuments.objects.create(
                document_name_ru=doc['document_name_ru'],
                document_name_kg=doc['document_name_kg'],
                document_name_en=doc['document_name_en'],
                order=doc['order']
            )
            master_doc.file.save(file_name, file_content, save=True)

    def create_aspirant_programs(self):
        """Создание программ аспирантуры"""
        programs_data = [
            {
                'program_name_ru': 'Теория и методика физического воспитания, спортивной тренировки, оздоровительной и адаптивной физической культуры',
                'program_name_kg': 'Дене тарбиясынын теориясы жана методикасы, спорттук машыгуулар, соолукту чыңдоочу жана адаптивдик дене тарбия',
                'program_name_en': 'Theory and methodology of physical education, sports training, health and adaptive physical culture',
                'description_ru': 'Подготовка научных кадров высшей квалификации в области теории и методики физического воспитания и спорта.',
                'description_kg': 'Дене тарбия жана спорттун теориясы менен методикасы тармагында жогорку квалификациялуу илимий кадрларды даярдоо.',
                'description_en': 'Training highly qualified scientific personnel in the field of theory and methodology of physical education and sports.',
                'features_ru': [
                    'Научные исследования в области спорта',
                    'Инновационные методики тренировки',
                    'Междисциплинарный подход',
                    'Публикации в международных журналах'
                ],
                'features_kg': [
                    'Спорт тармагында илимий изилдөөлөр',
                    'Инновациялык машыгуу методикалары',
                    'Дисциплиналар аралык мамиле',
                    'Эл аралык журналдарда басылмалар'
                ],
                'features_en': [
                    'Scientific research in sports',
                    'Innovative training methods',
                    'Interdisciplinary approach',
                    'Publications in international journals'
                ],
                'order': 1
            },
            {
                'program_name_ru': 'Педагогические науки',
                'program_name_kg': 'Педагогикалык илимдер',
                'program_name_en': 'Pedagogical Sciences',
                'description_ru': 'Исследования в области педагогики физической культуры и спортивного образования.',
                'description_kg': 'Дене тарбиясынын педагогикасы жана спорттук билим берүү тармагында изилдөөлөр.',
                'description_en': 'Research in the field of physical education pedagogy and sports education.',
                'features_ru': [
                    'Педагогические технологии в спорте',
                    'Образовательные инновации',
                    'Методология педагогических исследований',
                    'Практическая педагогика'
                ],
                'features_kg': [
                    'Спортто педагогикалык технологиялар',
                    'Билим берүү инновациялары',
                    'Педагогикалык изилдөөлөрдүн методологиясы',
                    'Практикалык педагогика'
                ],
                'features_en': [
                    'Pedagogical technologies in sports',
                    'Educational innovations',
                    'Methodology of pedagogical research',
                    'Practical pedagogy'
                ],
                'order': 2
            }
        ]
        
        for program in programs_data:
            AspirantPrograms.objects.create(**program)

    def create_aspirant_requirements(self):
        """Создание требований для аспирантуры"""
        requirements_data = [
            {
                'title_ru': 'Образование',
                'title_kg': 'Билим берүү',
                'title_en': 'Education',
                'description_ru': 'Диплом магистра или специалиста по профильной специальности. Средний балл не ниже 4.0.',
                'description_kg': 'Профилдик адистик боюнча магистр же адис дипломы. Орточо баа 4.0дөн төмөн эмес.',
                'description_en': 'Master\'s or specialist diploma in a relevant specialty. Average grade not less than 4.0.',
                'order': 1
            },
            {
                'title_ru': 'Научная деятельность',
                'title_kg': 'Илимий ишмердүүлүк',
                'title_en': 'Scientific activity',
                'description_ru': 'Наличие публикаций, участие в научных конференциях, исследовательских проектах.',
                'description_kg': 'Басылмалардын болушу, илимий конференцияларга катышуу, изилдөө долбоорлору.',
                'description_en': 'Availability of publications, participation in scientific conferences, research projects.',
                'order': 2
            },
            {
                'title_ru': 'Языковые требования',
                'title_kg': 'Тилдик талаптар',
                'title_en': 'Language requirements',
                'description_ru': 'Знание иностранного языка на уровне B2, подтвержденное сертификатом или тестированием.',
                'description_kg': 'Чет тилин B2 деңгээлинде билүү, сертификат же тестирлөө менен ырасталган.',
                'description_en': 'Knowledge of a foreign language at B2 level, confirmed by certificate or testing.',
                'order': 3
            }
        ]
        
        for requirement in requirements_data:
            AspirantRequirements.objects.create(**requirement)

    def create_aspirant_main_dates(self):
        """Создание основных дат для аспирантуры"""
        dates_data = [
            {
                'event_name_ru': 'Прием документов',
                'event_name_kg': 'Документтерди кабыл алуу',
                'event_name_en': 'Document submission',
                'date': '1 мая - 30 июня',
                'order': 1
            },
            {
                'event_name_ru': 'Вступительные экзамены',
                'event_name_kg': 'Кирүү экзамендери',
                'event_name_en': 'Entrance exams',
                'date': '5 июля - 20 июля',
                'order': 2
            },
            {
                'event_name_ru': 'Собеседование',
                'event_name_kg': 'Маек',
                'event_name_en': 'Interview',
                'date': '25 июля - 30 июля',
                'order': 3
            },
            {
                'event_name_ru': 'Зачисление',
                'event_name_kg': 'Кабыл алуу',
                'event_name_en': 'Enrollment',
                'date': '5 августа',
                'order': 4
            },
            {
                'event_name_ru': 'Начало обучения',
                'event_name_kg': 'Окууну баштоо',
                'event_name_en': 'Start of studies',
                'date': '1 сентября',
                'order': 5
            }
        ]
        
        for date_item in dates_data:
            AspirantMainDate.objects.create(**date_item)

    def create_aspirant_documents(self):
        """Создание документов для аспирантуры"""
        documents_data = [
            {
                'document_name_ru': 'Правила приема в аспирантуру',
                'document_name_kg': 'Аспирантурага кабыл алуу эрежелери',
                'document_name_en': 'PhD admission rules',
                'order': 1
            },
            {
                'document_name_ru': 'Программы кандидатских экзаменов',
                'document_name_kg': 'Кандидаттык экзамендердин программалары',
                'document_name_en': 'Candidate exam programs',
                'order': 2
            },
            {
                'document_name_ru': 'Требования к диссертации',
                'document_name_kg': 'Диссертацияга талаптар',
                'document_name_en': 'Dissertation requirements',
                'order': 3
            },
            {
                'document_name_ru': 'Список научных руководителей',
                'document_name_kg': 'Илимий жетекчилердин тизмеси',
                'document_name_en': 'List of scientific supervisors',
                'order': 4
            },
            {
                'document_name_ru': 'Форма заявления в аспирантуру',
                'document_name_kg': 'Аспирантурага арыз формасы',
                'document_name_en': 'PhD application form',
                'order': 5
            }
        ]
        
        for doc in documents_data:
            # Создаем простой текстовый файл для примера
            content = f"Документ: {doc['document_name_ru']}\nЭто образец документа для аспирантуры."
            file_content = ContentFile(content.encode('utf-8'))
            file_name = f"aspirant_doc_{doc['order']}.txt"
            
            aspirant_doc = AspirantDocuments.objects.create(
                document_name_ru=doc['document_name_ru'],
                document_name_kg=doc['document_name_kg'],
                document_name_en=doc['document_name_en'],
                order=doc['order']
            )
            aspirant_doc.file.save(file_name, file_content, save=True)
