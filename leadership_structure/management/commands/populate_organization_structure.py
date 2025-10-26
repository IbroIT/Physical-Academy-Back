from django.core.management.base import BaseCommand
from leadership_structure.models import OrganizationStructure


class Command(BaseCommand):
    help = "Populate organization structure with sample data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Clearing existing organization structure...")
        OrganizationStructure.objects.all().delete()

        self.stdout.write("Creating organization structure...")

        # 1. Ректорат (верхний уровень - без родителя)
        rectorat = OrganizationStructure.objects.create(
            name="Ректорат",
            name_kg="Ректорат",
            name_en="Rectorate",
            structure_type="unit",
            description="Центральный орган управления академией",
            description_kg="Академиянын борбордук башкаруу органы",
            description_en="Central governing body of the academy",
            head="Ректор академии",
            head_kg="Академиянын ректору",
            head_en="Rector of the academy",
            email="rector@ksapcs.kg",
            phone="+996 312 XXX XXX",
            location="Главный корпус, 3 этаж",
            location_kg="Башкы имарат, 3-кабат",
            location_en="Main building, 3rd floor",
            staff_count=15,
            icon="🏛️",
            is_active=True,
            order=1,
        )

        # 2. Физический факультет
        physics_faculty = OrganizationStructure.objects.create(
            name="Физический факультет",
            name_kg="Физика факультети",
            name_en="Faculty of Physics",
            structure_type="faculty",
            description="Факультет физики и математики",
            description_kg="Физика жана математика факультети",
            description_en="Faculty of Physics and Mathematics",
            parent=rectorat,
            head="Декан физического факультета",
            head_kg="Физика факультетинин деканы",
            head_en="Dean of Physics Faculty",
            email="physics@ksapcs.kg",
            phone="+996 312 XXX XXX",
            location="Корпус А, 2 этаж",
            location_kg="А имарат, 2-кабат",
            location_en="Building A, 2nd floor",
            staff_count=45,
            icon="🔬",
            is_active=True,
            order=2,
        )

        # 3. Кафедра общей физики
        OrganizationStructure.objects.create(
            name="Кафедра общей физики",
            name_kg="Жалпы физика кафедрасы",
            name_en="Department of General Physics",
            structure_type="department",
            description="Преподавание общей физики",
            description_kg="Жалпы физиканы окутуу",
            description_en="Teaching of general physics",
            parent=physics_faculty,
            head="Заведующий кафедрой",
            head_kg="Кафедра башчысы",
            head_en="Head of Department",
            email="gen.physics@ksapcs.kg",
            location="Корпус А, 3 этаж",
            location_kg="А имарат, 3-кабат",
            location_en="Building A, 3rd floor",
            staff_count=12,
            icon="⚛️",
            is_active=True,
            order=3,
        )

        # 4. Кафедра теоретической физики
        OrganizationStructure.objects.create(
            name="Кафедра теоретической физики",
            name_kg="Теориялык физика кафедрасы",
            name_en="Department of Theoretical Physics",
            structure_type="department",
            description="Исследования в области теоретической физики",
            description_kg="Теориялык физика тармагында изилдөөлөр",
            description_en="Research in theoretical physics",
            parent=physics_faculty,
            head="Заведующий кафедрой",
            head_kg="Кафедра башчысы",
            head_en="Head of Department",
            email="theor.physics@ksapcs.kg",
            location="Корпус А, 4 этаж",
            location_kg="А имарат, 4-кабат",
            location_en="Building A, 4th floor",
            staff_count=10,
            icon="📐",
            is_active=True,
            order=4,
        )

        # 5. Математический факультет
        math_faculty = OrganizationStructure.objects.create(
            name="Математический факультет",
            name_kg="Математика факультети",
            name_en="Faculty of Mathematics",
            structure_type="faculty",
            description="Факультет математики и информатики",
            description_kg="Математика жана информатика факультети",
            description_en="Faculty of Mathematics and Informatics",
            parent=rectorat,
            head="Декан математического факультета",
            head_kg="Математика факультетинин деканы",
            head_en="Dean of Mathematics Faculty",
            email="math@ksapcs.kg",
            phone="+996 312 XXX XXX",
            location="Корпус Б, 2 этаж",
            location_kg="Б имарат, 2-кабат",
            location_en="Building B, 2nd floor",
            staff_count=38,
            icon="📊",
            is_active=True,
            order=5,
        )

        # 6. Кафедра высшей математики
        OrganizationStructure.objects.create(
            name="Кафедра высшей математики",
            name_kg="Жогорку математика кафедрасы",
            name_en="Department of Higher Mathematics",
            structure_type="department",
            description="Преподавание высшей математики",
            description_kg="Жогорку математиканы окутуу",
            description_en="Teaching of higher mathematics",
            parent=math_faculty,
            head="Заведующий кафедрой",
            head_kg="Кафедра башчысы",
            head_en="Head of Department",
            email="higher.math@ksapcs.kg",
            location="Корпус Б, 3 этаж",
            location_kg="Б имарат, 3-кабат",
            location_en="Building B, 3rd floor",
            staff_count=15,
            icon="∑",
            is_active=True,
            order=6,
        )

        # 7. Учебная служба
        OrganizationStructure.objects.create(
            name="Учебная служба",
            name_kg="Окуу кызматы",
            name_en="Academic Service",
            structure_type="service",
            description="Управление учебным процессом",
            description_kg="Окуу процессин башкаруу",
            description_en="Academic process management",
            parent=rectorat,
            head="Начальник учебной службы",
            head_kg="Окуу кызматынын начальниги",
            head_en="Head of Academic Service",
            email="academic@ksapcs.kg",
            phone="+996 312 XXX XXX",
            location="Главный корпус, 2 этаж",
            location_kg="Башкы имарат, 2-кабат",
            location_en="Main building, 2nd floor",
            staff_count=8,
            icon="📚",
            is_active=True,
            order=7,
        )

        # 8. Научный центр
        OrganizationStructure.objects.create(
            name="Научный центр",
            name_kg="Илимий борбор",
            name_en="Research Center",
            structure_type="center",
            description="Координация научной деятельности",
            description_kg="Илимий ишти координациялоо",
            description_en="Research activities coordination",
            parent=rectorat,
            head="Директор научного центра",
            head_kg="Илимий борборунун директору",
            head_en="Director of Research Center",
            email="science@ksapcs.kg",
            phone="+996 312 XXX XXX",
            location="Корпус В, 1 этаж",
            location_kg="В имарат, 1-кабат",
            location_en="Building C, 1st floor",
            staff_count=12,
            icon="🔬",
            is_active=True,
            order=8,
        )

        # 9. Центр информационных технологий
        OrganizationStructure.objects.create(
            name="Центр информационных технологий",
            name_kg="Маалыматтык технологиялар борбору",
            name_en="IT Center",
            structure_type="center",
            description="Техническая поддержка и IT-инфраструктура",
            description_kg="Техникалык колдоо жана IT инфраструктура",
            description_en="Technical support and IT infrastructure",
            parent=rectorat,
            head="Директор IT-центра",
            head_kg="IT борборунун директору",
            head_en="Director of IT Center",
            email="it@ksapcs.kg",
            phone="+996 312 XXX XXX",
            location="Главный корпус, 1 этаж",
            location_kg="Башкы имарат, 1-кабат",
            location_en="Main building, 1st floor",
            staff_count=6,
            icon="💻",
            is_active=True,
            order=9,
        )

        # 10. Библиотека
        OrganizationStructure.objects.create(
            name="Библиотека",
            name_kg="Китепкана",
            name_en="Library",
            structure_type="service",
            description="Библиотечное обслуживание",
            description_kg="Китепкана тейлөө",
            description_en="Library services",
            parent=rectorat,
            head="Директор библиотеки",
            head_kg="Китепкананын директору",
            head_en="Library Director",
            email="library@ksapcs.kg",
            phone="+996 312 XXX XXX",
            location="Главный корпус, цокольный этаж",
            location_kg="Башкы имарат, төмөнкү кабат",
            location_en="Main building, basement",
            staff_count=5,
            icon="📖",
            is_active=True,
            order=10,
        )

        total = OrganizationStructure.objects.count()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {total} organization structures!")
        )

        # Показываем структуру
        self.stdout.write("\nCreated structure:")
        root_structures = OrganizationStructure.objects.filter(parent__isnull=True)
        for root in root_structures:
            self.stdout.write(f"  📁 {root.name} ({root.structure_type})")
            children = OrganizationStructure.objects.filter(parent=root)
            for child in children:
                self.stdout.write(f"    └─ {child.name} ({child.structure_type})")
                grandchildren = OrganizationStructure.objects.filter(parent=child)
                for grandchild in grandchildren:
                    self.stdout.write(
                        f"       └─ {grandchild.name} ({grandchild.structure_type})"
                    )
