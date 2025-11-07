from django.core.management.base import BaseCommand
from ipchain_app.models import (
    IPChainInfo,
    IPChainInfoTranslation,
    IPChainStatistic,
    IPChainStatisticTranslation,
    Patent,
    PatentTranslation,
    BlockchainFeature,
    BlockchainFeatureTranslation,
    IPChainBenefit,
    IPChainBenefitTranslation,
    BlockchainData,
    BlockchainDataTranslation,
)
from datetime import date


class Command(BaseCommand):
    help = "Добавляет тестовые данные для IPChain"

    def handle(self, *args, **options):
        self.stdout.write("Добавление тестовых данных для IPChain...")

        # 1. IPChain Info
        info, created = IPChainInfo.objects.get_or_create(
            order=0,
            defaults={
                "title": "IPChain",
                "subtitle": "Blockchain-система для защиты интеллектуальной собственности",
                "is_active": True,
            },
        )

        if created:
            IPChainInfoTranslation.objects.create(
                info=info,
                language="ru",
                title="IPChain - Защита интеллектуальной собственности",
                subtitle="Инновационная blockchain-система для регистрации и защиты патентов и авторских прав в академической среде",
            )
            IPChainInfoTranslation.objects.create(
                info=info,
                language="en",
                title="IPChain - Intellectual Property Protection",
                subtitle="Innovative blockchain system for registration and protection of patents and copyrights in academic environment",
            )
            IPChainInfoTranslation.objects.create(
                info=info,
                language="kg",
                title="IPChain - Интеллектуалдык менчикти коргоо",
                subtitle="Академиялык чөйрөдө патенттерди жана автордук укуктарды каттоо жана коргоо үчүн инновациялык блокчейн системасы",
            )

        # 2. Statistics
        stats_data = [
            {
                "value": "1000+",
                "labels": {
                    "ru": "Защищено патентов",
                    "en": "Patents Protected",
                    "kg": "Корголгон патенттер",
                },
            },
            {
                "value": "500+",
                "labels": {
                    "ru": "Активных пользователей",
                    "en": "Active Users",
                    "kg": "Активдүү колдонуучулар",
                },
            },
            {
                "value": "99.9%",
                "labels": {
                    "ru": "Надежность системы",
                    "en": "System Reliability",
                    "kg": "Системанын ишенимдүүлүгү",
                },
            },
            {
                "value": "24/7",
                "labels": {
                    "ru": "Круглосуточная поддержка",
                    "en": "24/7 Support",
                    "kg": "Тегерек саат колдоо",
                },
            },
        ]

        for idx, stat_data in enumerate(stats_data):
            stat, created = IPChainStatistic.objects.get_or_create(
                value=stat_data["value"], defaults={"is_active": True, "order": idx}
            )
            if created:
                for lang, label in stat_data["labels"].items():
                    IPChainStatisticTranslation.objects.create(
                        statistic=stat, language=lang, label=label
                    )

        # 3. Patents
        patents_data = [
            {
                "number": "PAT2024001",
                "status": "Granted",
                "year": "2024",
                "date": date(2024, 1, 15),
                "icon": "📄",
                "translations": {
                    "ru": {
                        "title": "Система мониторинга спортивных показателей",
                        "description": "Инновационная технология для отслеживания результатов спортсменов",
                        "full_description": "Разработана комплексная система мониторинга физических показателей спортсменов с использованием IoT датчиков и машинного обучения для прогнозирования результатов и предотвращения травм.",
                        "technologies": ["IoT", "Machine Learning", "Blockchain"],
                        "applications": [
                            "Спортивная медицина",
                            "Тренировочный процесс",
                            "Реабилитация",
                        ],
                    },
                    "en": {
                        "title": "Sports Performance Monitoring System",
                        "description": "Innovative technology for tracking athlete performance",
                        "full_description": "A comprehensive system has been developed for monitoring athletes physical indicators using IoT sensors and machine learning to predict results and prevent injuries.",
                        "technologies": ["IoT", "Machine Learning", "Blockchain"],
                        "applications": [
                            "Sports Medicine",
                            "Training Process",
                            "Rehabilitation",
                        ],
                    },
                    "kg": {
                        "title": "Спорттук көрсөткүчтөрдү мониторинг системасы",
                        "description": "Спортчулардын натыйжаларын көзөмөлдөө үчүн инновациялык технология",
                        "full_description": "Натыйжаларды болжолдоо жана жаракаттардын алдын алуу үчүн IoT датчиктерин жана машина окутуусун колдонуу менен спортчулардын физикалык көрсөткүчтөрүн көзөмөлдөө үчүн комплекстүү система иштелип чыккан.",
                        "technologies": ["IoT", "Машина окутуу", "Блокчейн"],
                        "applications": [
                            "Спорттук медицина",
                            "Машыгуу процесси",
                            "Реабилитация",
                        ],
                    },
                },
            },
            {
                "number": "PAT2024002",
                "status": "Active",
                "year": "2024",
                "date": date(2024, 3, 20),
                "icon": "🔬",
                "translations": {
                    "ru": {
                        "title": "Методика анализа биомеханики движений",
                        "description": "Программное обеспечение для 3D-анализа техники выполнения упражнений",
                        "full_description": "Создано ПО для детального анализа биомеханики спортивных движений с использованием компьютерного зрения и нейросетей для оптимизации техники и повышения эффективности тренировок.",
                        "technologies": [
                            "Computer Vision",
                            "Neural Networks",
                            "3D Analysis",
                        ],
                        "applications": [
                            "Техническая подготовка",
                            "Анализ движений",
                            "Оптимизация техники",
                        ],
                    },
                    "en": {
                        "title": "Biomechanics Movement Analysis Method",
                        "description": "Software for 3D analysis of exercise technique",
                        "full_description": "Software has been created for detailed analysis of sports movement biomechanics using computer vision and neural networks to optimize technique and increase training efficiency.",
                        "technologies": [
                            "Computer Vision",
                            "Neural Networks",
                            "3D Analysis",
                        ],
                        "applications": [
                            "Technical Training",
                            "Movement Analysis",
                            "Technique Optimization",
                        ],
                    },
                    "kg": {
                        "title": "Кыймылдардын биомеханикасын талдоо методикасы",
                        "description": "Көнүгүүлөрдү аткаруу техникасын 3D талдоо үчүн программалык камсыздоо",
                        "full_description": "Техниканы оптималдаштыруу жана машыгуулардын натыйжалуулугун жогорулатуу үчүн компьютердик көрүү жана нейротармактарды колдонуу менен спорттук кыймылдардын биомеханикасын деталдуу талдоо үчүн ПК түзүлгөн.",
                        "technologies": [
                            "Компьютердик көрүү",
                            "Нейротармактар",
                            "3D талдоо",
                        ],
                        "applications": [
                            "Техникалык даярдык",
                            "Кыймылдарды талдоо",
                            "Техниканы оптималдаштыруу",
                        ],
                    },
                },
            },
            {
                "number": "PAT2023015",
                "status": "Granted",
                "year": "2023",
                "date": date(2023, 11, 10),
                "icon": "💊",
                "translations": {
                    "ru": {
                        "title": "Система персонализированного питания спортсменов",
                        "description": "Алгоритм расчета индивидуального рациона на основе ДНК-анализа",
                        "full_description": "Разработана система персонализированного питания на основе генетического анализа, учитывающая индивидуальные особенности метаболизма спортсмена для максимизации результатов.",
                        "technologies": ["Genomics", "AI", "Nutrition Science"],
                        "applications": [
                            "Спортивное питание",
                            "Метаболизм",
                            "Восстановление",
                        ],
                    },
                    "en": {
                        "title": "Personalized Athlete Nutrition System",
                        "description": "Algorithm for calculating individual diet based on DNA analysis",
                        "full_description": "A personalized nutrition system has been developed based on genetic analysis, taking into account individual characteristics of athlete metabolism to maximize results.",
                        "technologies": ["Genomics", "AI", "Nutrition Science"],
                        "applications": ["Sports Nutrition", "Metabolism", "Recovery"],
                    },
                    "kg": {
                        "title": "Спортчулардын жекелештирилген тамактануу системасы",
                        "description": "ДНК талдоосуна негизделген жеке рационду эсептөө алгоритми",
                        "full_description": "Натыйжаларды максималдуу кылуу үчүн спортчунун метаболизминин жеке өзгөчөлүктөрүн эске алуу менен генетикалык талдоого негизделген жекелештирилген тамактануу системасы иштелип чыккан.",
                        "technologies": ["Геномика", "AI", "Тамактануу илими"],
                        "applications": [
                            "Спорттук тамактануу",
                            "Метаболизм",
                            "Калыбына келүү",
                        ],
                    },
                },
            },
        ]

        for idx, patent_data in enumerate(patents_data):
            patent, created = Patent.objects.get_or_create(
                number=patent_data["number"],
                defaults={
                    "status": patent_data["status"],
                    "year": patent_data["year"],
                    "date": patent_data["date"],
                    "icon": patent_data["icon"],
                    "is_active": True,
                    "order": idx,
                },
            )
            if created:
                for lang, trans_data in patent_data["translations"].items():
                    PatentTranslation.objects.create(
                        patent=patent, language=lang, **trans_data
                    )

        # 4. Blockchain Features
        features_data = [
            {
                "icon": "🔒",
                "translations": {
                    "ru": {
                        "title": "Неизменяемость записей",
                        "description": "Невозможность изменения или удаления зарегистрированных данных",
                    },
                    "en": {
                        "title": "Immutable Records",
                        "description": "Impossibility to change or delete registered data",
                    },
                    "kg": {
                        "title": "Өзгөртүлбөс жазуулар",
                        "description": "Каттоодон өткөн маалыматтарды өзгөртүү же өчүрүү мүмкүн эмес",
                    },
                },
            },
            {
                "icon": "🌐",
                "translations": {
                    "ru": {
                        "title": "Децентрализация",
                        "description": "Распределенное хранение данных без единой точки отказа",
                    },
                    "en": {
                        "title": "Decentralization",
                        "description": "Distributed data storage without single point of failure",
                    },
                    "kg": {
                        "title": "Децентрализация",
                        "description": "Бир баштык катасыз маалыматтарды бөлүштүрүлгөн сактоо",
                    },
                },
            },
            {
                "icon": "⏱️",
                "translations": {
                    "ru": {
                        "title": "Временные метки",
                        "description": "Точная фиксация времени регистрации каждого патента",
                    },
                    "en": {
                        "title": "Timestamps",
                        "description": "Accurate recording of registration time for each patent",
                    },
                    "kg": {
                        "title": "Убакыт белгилери",
                        "description": "Ар бир патенттин катталуу убактысын так белгилөө",
                    },
                },
            },
            {
                "icon": "🔍",
                "translations": {
                    "ru": {
                        "title": "Прозрачность",
                        "description": "Возможность проверки подлинности и истории любого документа",
                    },
                    "en": {
                        "title": "Transparency",
                        "description": "Ability to verify authenticity and history of any document",
                    },
                    "kg": {
                        "title": "Ачыктык",
                        "description": "Каалаган документтин чыныгылыгын жана тарыхын текшерүү мүмкүнчүлүгү",
                    },
                },
            },
            {
                "icon": "🛡️",
                "translations": {
                    "ru": {
                        "title": "Криптографическая защита",
                        "description": "Использование современных алгоритмов шифрования для безопасности",
                    },
                    "en": {
                        "title": "Cryptographic Protection",
                        "description": "Use of modern encryption algorithms for security",
                    },
                    "kg": {
                        "title": "Криптографиялык коргоо",
                        "description": "Коопсуздук үчүн заманбап шифрлөө алгоритмдерин колдонуу",
                    },
                },
            },
        ]

        for idx, feature_data in enumerate(features_data):
            feature, created = BlockchainFeature.objects.get_or_create(
                icon=feature_data["icon"], defaults={"is_active": True, "order": idx}
            )
            if created:
                for lang, trans_data in feature_data["translations"].items():
                    BlockchainFeatureTranslation.objects.create(
                        feature=feature, language=lang, **trans_data
                    )

        # 5. Benefits
        benefits_data = [
            {
                "icon": "⚡",
                "translations": {
                    "ru": {
                        "title": "Быстрая регистрация",
                        "description": "Моментальная регистрация патентов и авторских прав в системе",
                    },
                    "en": {
                        "title": "Fast Registration",
                        "description": "Instant registration of patents and copyrights in the system",
                    },
                    "kg": {
                        "title": "Тез каттоо",
                        "description": "Системада патенттерди жана автордук укуктарды дароо каттоо",
                    },
                },
            },
            {
                "icon": "💰",
                "translations": {
                    "ru": {
                        "title": "Экономия средств",
                        "description": "Снижение затрат на регистрацию и защиту интеллектуальной собственности",
                    },
                    "en": {
                        "title": "Cost Savings",
                        "description": "Reduced costs for registration and protection of intellectual property",
                    },
                    "kg": {
                        "title": "Каражаттарды үнөмдөө",
                        "description": "Интеллектуалдык менчикти каттоо жана коргоого чыгымдарды кыскартуу",
                    },
                },
            },
            {
                "icon": "🌍",
                "translations": {
                    "ru": {
                        "title": "Международное признание",
                        "description": "Глобальная система признания прав на интеллектуальную собственность",
                    },
                    "en": {
                        "title": "International Recognition",
                        "description": "Global system for recognition of intellectual property rights",
                    },
                    "kg": {
                        "title": "Эл аралык таануу",
                        "description": "Интеллектуалдык менчик укуктарын тануунун глобалдык системасы",
                    },
                },
            },
            {
                "icon": "📊",
                "translations": {
                    "ru": {
                        "title": "Аналитика и отчетность",
                        "description": "Детальная статистика и отчеты по использованию патентов",
                    },
                    "en": {
                        "title": "Analytics and Reporting",
                        "description": "Detailed statistics and reports on patent usage",
                    },
                    "kg": {
                        "title": "Аналитика жана отчеттуулук",
                        "description": "Патенттерди колдонуу боюнча деталдуу статистика жана отчеттор",
                    },
                },
            },
            {
                "icon": "🤝",
                "translations": {
                    "ru": {
                        "title": "Упрощенное сотрудничество",
                        "description": "Легкий обмен правами и лицензирование через платформу",
                    },
                    "en": {
                        "title": "Simplified Collaboration",
                        "description": "Easy exchange of rights and licensing through the platform",
                    },
                    "kg": {
                        "title": "Жөнөкөйлөштүрүлгөн кызматташтык",
                        "description": "Платформа аркылуу укуктарды жана лицензиялоону оңой алмашуу",
                    },
                },
            },
        ]

        for idx, benefit_data in enumerate(benefits_data):
            benefit, created = IPChainBenefit.objects.get_or_create(
                icon=benefit_data["icon"], defaults={"is_active": True, "order": idx}
            )
            if created:
                for lang, trans_data in benefit_data["translations"].items():
                    IPChainBenefitTranslation.objects.create(
                        benefit=benefit, language=lang, **trans_data
                    )

        # 6. Blockchain Data
        blockchain_data, created = BlockchainData.objects.get_or_create(
            order=0,
            defaults={
                "current_block": "15,842,367",
                "ip_registrations": "2,847",
                "smart_contracts": "1,563",
                "network_hash": "0x8f3a...c42b",
                "is_active": True,
            },
        )

        if created:
            BlockchainDataTranslation.objects.create(
                blockchain_data=blockchain_data,
                language="ru",
                current_block_label="Текущий блок",
                ip_registrations_label="Регистраций IP",
                smart_contracts_label="Смарт-контрактов",
                network_hash_label="Хэш сети",
            )
            BlockchainDataTranslation.objects.create(
                blockchain_data=blockchain_data,
                language="en",
                current_block_label="Current Block",
                ip_registrations_label="IP Registrations",
                smart_contracts_label="Smart Contracts",
                network_hash_label="Network Hash",
            )
            BlockchainDataTranslation.objects.create(
                blockchain_data=blockchain_data,
                language="kg",
                current_block_label="Учурдагы блок",
                ip_registrations_label="IP каттоолору",
                smart_contracts_label="Смарт-контракттар",
                network_hash_label="Тармак хэши",
            )

        self.stdout.write(
            self.style.SUCCESS("✅ Тестовые данные для IPChain успешно добавлены!")
        )
        self.stdout.write(f"📊 Статистика: {IPChainStatistic.objects.count()}")
        self.stdout.write(f"📄 Патентов: {Patent.objects.count()}")
        self.stdout.write(f"⚙️ Функций блокчейна: {BlockchainFeature.objects.count()}")
        self.stdout.write(f"✅ Преимуществ: {IPChainBenefit.objects.count()}")
        self.stdout.write(f"🔗 Данных блокчейна: {BlockchainData.objects.count()}")
