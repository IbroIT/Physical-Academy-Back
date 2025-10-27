from django.core.management.base import BaseCommand
from admission.models import (
    QuotaType, QuotaRequirement, QuotaBenefit, 
    QuotaStats, AdditionalSupport, ProcessStep
)


class Command(BaseCommand):
    help = 'Загружает начальные данные для приложения admission на основе данных из React компонента'

    def handle(self, *args, **options):
        self.stdout.write('Начинаем загрузку данных для admission...')
        
        # Очищаем существующие данные
        QuotaType.objects.all().delete()
        QuotaStats.objects.all().delete()
        AdditionalSupport.objects.all().delete()
        ProcessStep.objects.all().delete()
        
        # Создаем типы квот
        self.create_quota_types()
        
        # Создаем статистику
        self.create_quota_stats()
        
        # Создаем дополнительную поддержку
        self.create_additional_support()
        
        # Создаем шаги процесса
        self.create_process_steps()
        
        self.stdout.write(
            self.style.SUCCESS('Данные успешно загружены!')
        )

    def create_quota_types(self):
        """Создание типов квот с требованиями и преимуществами"""
        
        # Спортивная квота
        sports_quota = QuotaType.objects.create(
            type='sports',
            title_ru='Спортивная квота',
            title_ky='Спорттук квота',
            title_en='Sports Quota',
            description_ru='Для спортсменов с выдающимися достижениями',
            description_ky='Мыкты жетишкендиктери бар спортчулар үчүн',
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
            title_ky='Ден соолук абалы боюнча квота',
            title_en='Health Status Quota',
            description_ru='Для лиц с ограниченными возможностями здоровья',
            description_ky='Ден соолук мүмкүнчүлүктөрү чектелген адамдар үчүн',
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
            title_ky='Максаттуу квота',
            title_en='Target Quota',
            description_ru='Для будущих сотрудников спортивных организаций',
            description_ky='Спорттук уюмдардын келечектеги кызматкерлери үчүн',
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
                'label_ky': 'квоталар боюнча жалпы орундар',
                'label_en': 'total quota spots',
                'description_ru': 'Ежегодно выделяется',
                'description_ky': 'Жыл сайын бөлүнөт',
                'description_en': 'Allocated annually',
                'order': 1
            },
            {
                'stat_type': 'success_rate',
                'number': '98%',
                'label_ru': 'успешного зачисления',
                'label_ky': 'ийгиликтүү кабыл алуу',
                'label_en': 'successful admission',
                'description_ru': 'Проходят конкурсный отбор',
                'description_ky': 'Конкурстук тандоодон өтүшөт',
                'description_en': 'Pass competitive selection',
                'order': 2
            },
            {
                'stat_type': 'organizations',
                'number': '25+',
                'label_ru': 'спортивных организаций',
                'label_ky': 'спорттук уюмдар',
                'label_en': 'sports organizations',
                'description_ru': 'Участвуют в программе',
                'description_ky': 'Программага катышышат',
                'description_en': 'Participate in the program',
                'order': 3
            },
            {
                'stat_type': 'quota_types',
                'number': '3',
                'label_ru': 'вида квот',
                'label_ky': 'квота түрү',
                'label_en': 'types of quotas',
                'description_ru': 'Для разных категорий абитуриентов',
                'description_ky': 'Түрдүү категориядагы абитуриенттер үчүн',
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
                'support_ky': 'Жеке спорттук насаатчы',
                'support_en': 'Personal sports mentor',
                'order': 1
            },
            {
                'support_ru': 'Спортивная экипировка и инвентарь',
                'support_ky': 'Спорттук экипировка жана инвентарь',
                'support_en': 'Sports equipment and inventory',
                'order': 2
            },
            {
                'support_ru': 'Специализированное питание',
                'support_ky': 'Адистештирилген тамак-аш',
                'support_en': 'Specialized nutrition',
                'order': 3
            },
            {
                'support_ru': 'Медицинское сопровождение и восстановление',
                'support_ky': 'Медициналык коштоо жана калыбына келтирүү',
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
                'title_ky': 'Консультация',
                'title_en': 'Consultation',
                'description_ru': 'Получите консультацию в приемной комиссии и определите подходящую квоту',
                'description_ky': 'Кабыл алуу комиссиясынан консультация алып, ылайыктуу квотаны аныктаңыз',
                'description_en': 'Get consultation from admission committee and determine suitable quota',
                'color_scheme': 'from-blue-500 to-cyan-500'
            },
            {
                'step_number': 2,
                'title_ru': 'Документы',
                'title_ky': 'Документтер',
                'title_en': 'Documents',
                'description_ru': 'Подготовьте необходимый пакет документов и спортивные достижения',
                'description_ky': 'Керектүү документтердин топтомун жана спорттук жетишкендиктерди даярдаңыз',
                'description_en': 'Prepare necessary document package and sports achievements',
                'color_scheme': 'from-green-500 to-emerald-500'
            },
            {
                'step_number': 3,
                'title_ru': 'Подача',
                'title_ky': 'Тапшыруу',
                'title_en': 'Submission',
                'description_ru': 'Подайте заявление и пройдите дополнительные испытания',
                'description_ky': 'Арыз берип, кошумча сыноолордон өтүңүз',
                'description_en': 'Submit application and pass additional tests',
                'color_scheme': 'from-purple-500 to-pink-500'
            }
        ]
        
        for step in steps_data:
            ProcessStep.objects.create(**step)
