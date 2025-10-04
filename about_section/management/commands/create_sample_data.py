from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from about_section.models import Leadership, Accreditation, OrganizationStructure, DownloadableDocument


class Command(BaseCommand):
    help = 'Create sample data for testing the Academy Management System API'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating sample data...'))

        # Create sample leadership
        self.create_leadership()
        
        # Create sample accreditations
        self.create_accreditations()
        
        # Create sample organization structure
        self.create_organization_structure()

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))

    def create_leadership(self):
        """Create sample leadership members"""
        leadership_data = [
            {
                'name': 'Асанов Азамат Бекмуратович',
                'name_kg': 'Асанов Азамат Бекмурат уулу',
                'name_en': 'Asanov Azamat Bekmuratovich',
                'position': 'Директор Высшей школы менеджмента',
                'position_kg': 'Жогорку менеджмент мектебинин директору',
                'position_en': 'Director of Higher School of Management',
                'degree': 'Доктор экономических наук',
                'degree_kg': 'Экономикалык илимдердин доктору',
                'degree_en': 'Doctor of Economic Sciences',
                'experience': '20 лет',
                'experience_kg': '20 жыл',
                'experience_en': '20 years',
                'bio': 'Опытный руководитель с большим стажем в сфере образования и менеджмента.',
                'bio_kg': 'Билим берүү жана менеджмент тармагында чоң тажрыйбасы бар тажрыйбалуу жетекчи.',
                'bio_en': 'Experienced leader with extensive experience in education and management.',
                'achievements': ['Заслуженный работник образования КР', 'Лучший менеджер года 2022'],
                'achievements_kg': ['КРдын билим берүүнүн кадырлуу кызматкери', '2022-жылдын эң мыкты менеджери'],
                'achievements_en': ['Honored Education Worker of KR', 'Best Manager of 2022'],
                'department': 'Администрация',
                'department_kg': 'Администрация',
                'department_en': 'Administration',
                'email': 'director@academy.edu.kg',
                'phone': '+996 312 123456',
                'leadership_type': 'director',
                'is_director': True,
                'order': 1
            },
            {
                'name': 'Жумабекова Айгуль Сапаровна',
                'name_kg': 'Жумабекова Айгүл Сапар кызы',
                'name_en': 'Zhumabekova Aigul Saparovna',
                'position': 'Заместитель директора по учебной работе',
                'position_kg': 'Окуу иши боюнча директордун орун басары',
                'position_en': 'Deputy Director for Academic Affairs',
                'degree': 'Кандидат педагогических наук',
                'degree_kg': 'Педагогикалык илимдердин кандидаты',
                'degree_en': 'Candidate of Pedagogical Sciences',
                'experience': '15 лет',
                'experience_kg': '15 жыл',
                'experience_en': '15 years',
                'department': 'Учебная часть',
                'department_kg': 'Окуу бөлүмү',
                'department_en': 'Academic Department',
                'email': 'deputy.academic@academy.edu.kg',
                'phone': '+996 312 123457',
                'leadership_type': 'deputy_director',
                'is_director': False,
                'order': 2
            },
            {
                'name': 'Токтосунов Марат Абдылдаевич',
                'name_kg': 'Токтосунов Марат Абдылдай уулу',
                'name_en': 'Taktosunov Marat Abdyldaevich',
                'position': 'Заведующий кафедрой менеджмента',
                'position_kg': 'Менеджмент кафедрасынын башчысы',
                'position_en': 'Head of Management Department',
                'degree': 'Кандидат экономических наук',
                'degree_kg': 'Экономикалык илимдердин кандидаты',
                'degree_en': 'Candidate of Economic Sciences',
                'experience': '12 лет',
                'experience_kg': '12 жыл',
                'experience_en': '12 years',
                'department': 'Кафедра менеджмента',
                'department_kg': 'Менеджмент кафедрасы',
                'department_en': 'Management Department',
                'specialization': 'Стратегический менеджмент, управление проектами',
                'specialization_kg': 'Стратегиялык менеджмент, долбоорлорду башкаруу',
                'specialization_en': 'Strategic management, project management',
                'email': 'management@academy.edu.kg',
                'phone': '+996 312 123458',
                'leadership_type': 'department_head',
                'is_director': False,
                'order': 3
            }
        ]

        for data in leadership_data:
            Leadership.objects.get_or_create(
                email=data['email'],
                defaults=data
            )

    def create_accreditations(self):
        """Create sample accreditations"""
        accreditation_data = [
            {
                'name': 'Институциональная аккредитация',
                'name_kg': 'Институционалдык аккредитация',
                'name_en': 'Institutional Accreditation',
                'organization': 'Агентство по аккредитации образовательных программ и организаций',
                'organization_kg': 'Билим берүү программаларын жана уюмдарын аккредиттөө агентстви',
                'organization_en': 'Agency for Accreditation of Educational Programs and Organizations',
                'accreditation_type': 'institutional',
                'description': 'Подтверждение соответствия деятельности образовательной организации установленным требованиям.',
                'description_kg': 'Билим берүү уюмунун ишинин белгиленген талаптарга шайкештигин ырастоо.',
                'description_en': 'Confirmation of compliance of educational organization activities with established requirements.',
                'issue_date': date(2022, 9, 15),
                'expiry_date': date(2027, 9, 15),
                'certificate_number': 'AAEPO-2022-001',
                'order': 1
            },
            {
                'name': 'ISO 9001:2015',
                'name_kg': 'ISO 9001:2015',
                'name_en': 'ISO 9001:2015',
                'organization': 'Международная организация по стандартизации',
                'organization_kg': 'Эл аралык стандарттоо уюму',
                'organization_en': 'International Organization for Standardization',
                'accreditation_type': 'international',
                'description': 'Система менеджмента качества соответствует международным стандартам.',
                'description_kg': 'Сапат менеджменти системасы эл аралык стандарттарга шайкеш келет.',
                'description_en': 'Quality management system meets international standards.',
                'issue_date': date(2023, 3, 10),
                'expiry_date': date(2026, 3, 10),
                'certificate_number': 'ISO-9001-2023-KG-001',
                'order': 2
            }
        ]

        for data in accreditation_data:
            Accreditation.objects.get_or_create(
                certificate_number=data['certificate_number'],
                defaults=data
            )

    def create_organization_structure(self):
        """Create sample organization structure"""
        
        # Top-level structures
        administration = OrganizationStructure.objects.get_or_create(
            name_ru='Администрация',
            defaults={
                'name_en': 'Administration',
                'name_ky': 'Администрация',
                'head_name_ru': 'Асанов Азамат Бекмуратович',
                'head_name_en': 'Asanov Azamat Bekmuratovich',
                'head_name_ky': 'Асанов Азамат Бекмурат уулу',
                'structure_type': 'leadership',
                'phone': '+996 312 123456',
                'email': 'administration@academy.edu.kg',
                'icon': '🏛️',
                'order': 1
            }
        )[0]

        # Academic departments
        academic_dept = OrganizationStructure.objects.get_or_create(
            name_ru='Учебная часть',
            defaults={
                'name_en': 'Academic Department',
                'name_ky': 'Окуу бөлүмү',
                'head_name_ru': 'Жумабекова Айгуль Сапаровна',
                'head_name_en': 'Zhumabekova Aigul Saparovna',
                'head_name_ky': 'Жумабекова Айгүл Сапар кызы',
                'structure_type': 'administrative',
                'phone': '+996 312 123457',
                'email': 'academic@academy.edu.kg',
                'icon': '📚',
                'order': 2
            }
        )[0]

        # Faculties
        management_faculty = OrganizationStructure.objects.get_or_create(
            name_ru='Факультет менеджмента',
            defaults={
                'name_en': 'Faculty of Management',
                'name_ky': 'Менеджмент факультети',
                'head_name_ru': 'Токтосунов Марат Абдылдаевич',
                'head_name_en': 'Taktosunov Marat Abdyldaevich',
                'head_name_ky': 'Токтосунов Марат Абдылдай уулу',
                'structure_type': 'faculties',
                'phone': '+996 312 123458',
                'email': 'management@academy.edu.kg',
                'icon': '💼',
                'parent': academic_dept,
                'order': 1
            }
        )[0]

        # Departments under faculties
        OrganizationStructure.objects.get_or_create(
            name_ru='Кафедра стратегического менеджмента',
            defaults={
                'name_en': 'Department of Strategic Management',
                'name_ky': 'Стратегиялык менеджмент кафедрасы',
                'head_name_ru': 'Токтосунов Марат Абдылдаевич',
                'head_name_en': 'Taktosunov Marat Abdyldaevich',
                'head_name_ky': 'Токтосунов Марат Абдылдай уулу',
                'structure_type': 'faculties',
                'phone': '+996 312 123459',
                'email': 'strategic@academy.edu.kg',
                'icon': '🎯',
                'parent': management_faculty,
                'order': 1
            }
        )

        # Support departments
        OrganizationStructure.objects.get_or_create(
            name_ru='Библиотека',
            defaults={
                'name_en': 'Library',
                'name_ky': 'Китепкана',
                'head_name_ru': 'Абдикадырова Нурсулу Маматовна',
                'head_name_en': 'Abdikadyrova Nursulu Mamatovna',
                'head_name_ky': 'Абдикадырова Нурсулу Мамат кызы',
                'structure_type': 'support',
                'phone': '+996 312 123460',
                'email': 'library@academy.edu.kg',
                'icon': '📖',
                'order': 1
            }
        )

        OrganizationStructure.objects.get_or_create(
            name_ru='IT-отдел',
            defaults={
                'name_en': 'IT Department',
                'name_ky': 'IT бөлүмү',
                'head_name_ru': 'Исмаилов Бекзат Нурланович',
                'head_name_en': 'Ismailov Bekzat Nurlanovich',
                'head_name_ky': 'Исмаилов Бекзат Нурлан уулу',
                'structure_type': 'support',
                'phone': '+996 312 123461',
                'email': 'it@academy.edu.kg',
                'icon': '💻',
                'order': 2
            }
        )