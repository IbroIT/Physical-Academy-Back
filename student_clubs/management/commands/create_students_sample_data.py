import random
from django.core.management.base import BaseCommand
from django.db import transaction
from student_clubs.models import Club, StudentProfile, ClubMembership


class Command(BaseCommand):
    help = "Creates sample data for student profiles and memberships"

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                self.create_sample_data()
                self.stdout.write(
                    self.style.SUCCESS("Successfully created sample student data")
                )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating sample data: {str(e)}"))

    def create_sample_data(self):
        """Create sample students and club memberships"""

        # Создаем список факультетов для примера
        faculties = [
            {
                "ru": "Факультет информационных технологий",
                "en": "Faculty of Information Technology",
                "kg": "Маалымат технологиялары факультети",
            },
            {
                "ru": "Экономический факультет",
                "en": "Faculty of Economics",
                "kg": "Экономика факультети",
            },
            {
                "ru": "Факультет медицины",
                "en": "Faculty of Medicine",
                "kg": "Медицина факультети",
            },
            {
                "ru": "Юридический факультет",
                "en": "Faculty of Law",
                "kg": "Юридика факультети",
            },
            {
                "ru": "Гуманитарный факультет",
                "en": "Faculty of Humanities",
                "kg": "Гуманитардык факультет",
            },
        ]

        # Список специальностей
        majors = [
            {
                "ru": "Программная инженерия",
                "en": "Software Engineering",
                "kg": "Программалык инженерия",
            },
            {
                "ru": "Финансы и кредит",
                "en": "Finance and Credit",
                "kg": "Финансы жана насыя",
            },
            {"ru": "Лечебное дело", "en": "General Medicine", "kg": "Дарылоо иши"},
            {"ru": "Юриспруденция", "en": "Jurisprudence", "kg": "Юриспруденция"},
            {"ru": "Иностранные языки", "en": "Foreign Languages", "kg": "Чет тилдери"},
        ]

        # Список интересов
        interests_options = [
            "programming",
            "design",
            "music",
            "sports",
            "dance",
            "art",
            "science",
            "reading",
            "travel",
            "gaming",
            "photography",
            "cooking",
        ]

        # Создаем 20 студентов
        students_data = []
        for i in range(1, 21):
            faculty_index = random.randint(0, len(faculties) - 1)
            major_index = random.randint(0, len(majors) - 1)
            year = random.randint(1, 4)

            # Случайный набор интересов
            interests = random.sample(interests_options, random.randint(2, 5))

            students_data.append(
                {
                    "full_name_ru": f"Студент {i} Тестовый",
                    "full_name_en": f"Student {i} Test",
                    "full_name_kg": f"Студент {i} Тесттик",
                    "email": f"student{i}@example.com",
                    "phone": f"+996 555 123{i:03d}",
                    "faculty_ru": faculties[faculty_index]["ru"],
                    "faculty_en": faculties[faculty_index]["en"],
                    "faculty_kg": faculties[faculty_index]["kg"],
                    "major_ru": majors[major_index]["ru"],
                    "major_en": majors[major_index]["en"],
                    "major_kg": majors[major_index]["kg"],
                    "year_of_study": year,
                    "interests": interests,
                    "bio_ru": f"Био на русском языке студента {i}",
                    "bio_en": f"English bio of student {i}",
                    "bio_kg": f"Студент {i} кыргызча био",
                }
            )

        # Сохраняем студентов
        self.stdout.write("Creating student profiles...")
        students = []
        for data in students_data:
            student = StudentProfile.objects.create(**data)
            students.append(student)
            self.stdout.write(f"  Created student: {student.full_name_ru}")

        # Получаем все существующие клубы
        clubs = list(Club.objects.filter(is_active=True))
        if not clubs:
            self.stdout.write(
                self.style.WARNING(
                    "No active clubs found. Please run create_clubs_sample_data first."
                )
            )
            return

        # Создаем членства в клубах
        self.stdout.write("Creating club memberships...")
        memberships_count = 0

        # Статусы для распределения
        statuses = ["pending", "approved", "approved", "approved", "leader", "rejected"]

        # Для каждого студента создаем 1-3 членства
        for student in students:
            # Выбираем случайные клубы для текущего студента
            num_memberships = random.randint(1, 3)
            student_clubs = random.sample(clubs, min(num_memberships, len(clubs)))

            for club in student_clubs:
                status = random.choice(statuses)

                # Текст мотивации
                if status == "pending":
                    motivation = f"Я хочу вступить в клуб {club.name_ru}, потому что меня интересует эта тема"
                else:
                    motivation = None

                # Роль (только для утвержденных и лидеров)
                role_ru = None
                role_en = None
                role_kg = None

                if status in ["approved", "leader"]:
                    if status == "leader":
                        role_ru = "Заместитель руководителя"
                        role_en = "Deputy Leader"
                        role_kg = "Жетекчинин орун басары"
                    else:
                        role_ru = "Активный участник"
                        role_en = "Active Member"
                        role_kg = "Активдүү катышуучу"

                # Создаем членство
                membership = ClubMembership.objects.create(
                    student=student,
                    club=club,
                    status=status,
                    motivation_text=motivation,
                    role_ru=role_ru,
                    role_en=role_en,
                    role_kg=role_kg,
                )

                memberships_count += 1
                self.stdout.write(
                    f"  Created membership: {student.full_name_ru} -> {club.name_ru} ({status})"
                )

        # Обновляем счетчики участников для каждого клуба
        for club in clubs:
            club.members_count = ClubMembership.objects.filter(
                club=club, status__in=["approved", "leader"]
            ).count()
            club.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {len(students)} students and {memberships_count} club memberships"
            )
        )
