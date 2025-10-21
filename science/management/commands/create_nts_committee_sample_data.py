from django.core.management.base import BaseCommand
from django.db import transaction
from science.models import NTSCommitteeMember, NTSCommitteeRole, NTSResearchDirection


class Command(BaseCommand):
    help = "Creates sample data for NTS Committee models"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating NTS Committee sample data...")

        with transaction.atomic():
            # Create committee roles
            self.create_roles()

            # Create research directions
            self.create_research_directions()

            # Create committee members
            self.create_committee_members()

        self.stdout.write(
            self.style.SUCCESS("NTS Committee sample data created successfully!")
        )

    def create_roles(self):
        roles = [
            {
                "name_ru": "Председатель",
                "name_en": "Chairman",
                "description_ru": "Руководит работой научно-технического совета, председательствует на заседаниях",
                "description_en": "Leads the work of the scientific and technical council, chairs meetings",
            },
            {
                "name_ru": "Заместитель председателя",
                "name_en": "Vice Chairman",
                "description_ru": "Помогает председателю в руководстве советом, замещает председателя в его отсутствие",
                "description_en": "Assists the chairman in leading the council, substitutes for the chairman in their absence",
            },
            {
                "name_ru": "Ученый секретарь",
                "name_en": "Scientific Secretary",
                "description_ru": "Ведет документацию совета, организует заседания, информирует членов совета",
                "description_en": "Maintains council documentation, organizes meetings, informs council members",
            },
            {
                "name_ru": "Член совета",
                "name_en": "Council Member",
                "description_ru": "Участвует в работе совета, вносит предложения, участвует в голосованиях",
                "description_en": "Participates in the work of the council, makes proposals, participates in voting",
            },
            {
                "name_ru": "Приглашенный эксперт",
                "name_en": "Invited Expert",
                "description_ru": "Привлекается для консультаций по специальным вопросам, не является постоянным членом",
                "description_en": "Engaged for consultation on special issues, not a permanent member",
            },
        ]

        for role in roles:
            NTSCommitteeRole.objects.create(**role)

        self.stdout.write(f"Created {len(roles)} NTS Committee roles")

    def create_research_directions(self):
        directions = [
            {
                "name_ru": "Спортивная физиология",
                "name_en": "Sports Physiology",
                "description_ru": "Исследование физиологических процессов в организме спортсмена во время тренировок и соревнований",
                "description_en": "Study of physiological processes in an athlete's body during training and competitions",
            },
            {
                "name_ru": "Биомеханика спорта",
                "name_en": "Sports Biomechanics",
                "description_ru": "Изучение механических аспектов движений человека в спорте для оптимизации техники",
                "description_en": "Study of the mechanical aspects of human movement in sports to optimize technique",
            },
            {
                "name_ru": "Спортивная психология",
                "name_en": "Sports Psychology",
                "description_ru": "Исследование психологических факторов, влияющих на спортивные результаты и мотивацию",
                "description_en": "Research on psychological factors affecting sports performance and motivation",
            },
            {
                "name_ru": "Спортивная медицина",
                "name_en": "Sports Medicine",
                "description_ru": "Разработка методов профилактики, диагностики и лечения спортивных травм и заболеваний",
                "description_en": "Development of methods for prevention, diagnosis and treatment of sports injuries and diseases",
            },
            {
                "name_ru": "Теория и методика спортивной подготовки",
                "name_en": "Theory and Methodology of Sports Training",
                "description_ru": "Разработка и совершенствование методик тренировки спортсменов разных видов спорта",
                "description_en": "Development and improvement of training methods for athletes in different sports",
            },
            {
                "name_ru": "Спортивное питание и фармакология",
                "name_en": "Sports Nutrition and Pharmacology",
                "description_ru": "Изучение влияния питания и фармакологических средств на спортивные результаты",
                "description_en": "Study of the effects of nutrition and pharmacological agents on sports performance",
            },
        ]

        for direction in directions:
            NTSResearchDirection.objects.create(**direction)

        self.stdout.write(
            f"Created {len(directions)} NTS Committee research directions"
        )

    def create_committee_members(self):
        # Get roles and research directions
        chairman_role = NTSCommitteeRole.objects.filter(name_ru="Председатель").first()
        vice_role = NTSCommitteeRole.objects.filter(
            name_ru="Заместитель председателя"
        ).first()
        secretary_role = NTSCommitteeRole.objects.filter(
            name_ru="Ученый секретарь"
        ).first()
        member_role = NTSCommitteeRole.objects.filter(name_ru="Член совета").first()

        # Get research directions
        directions = list(NTSResearchDirection.objects.all())

        members = [
            {
                "full_name_ru": "Иванов Сергей Петрович",
                "full_name_en": "Ivanov Sergey Petrovich",
                "role": chairman_role,
                "research_direction": directions[0],
                "position_ru": "Доктор наук, профессор",
                "position_en": "Doctor of Sciences, Professor",
                "bio_ru": "Известный ученый в области спортивной физиологии с 25-летним опытом исследований",
                "bio_en": "Well-known scientist in sports physiology with 25 years of research experience",
                "email": "ivanov@example.com",
                "phone": "+7 (999) 123-4567",
                "is_active": True,
                "order": 1,
            },
            {
                "full_name_ru": "Петрова Анна Ивановна",
                "full_name_en": "Petrova Anna Ivanovna",
                "role": vice_role,
                "research_direction": directions[1],
                "position_ru": "Кандидат наук, доцент",
                "position_en": "PhD, Associate Professor",
                "bio_ru": "Специалист по биомеханике спорта, автор более 50 научных работ",
                "bio_en": "Specialist in sports biomechanics, author of more than 50 scientific papers",
                "email": "petrova@example.com",
                "phone": "+7 (999) 234-5678",
                "is_active": True,
                "order": 2,
            },
            {
                "full_name_ru": "Сидоров Михаил Александрович",
                "full_name_en": "Sidorov Mikhail Alexandrovich",
                "role": secretary_role,
                "research_direction": directions[2],
                "position_ru": "Кандидат наук, старший научный сотрудник",
                "position_en": "PhD, Senior Researcher",
                "bio_ru": "Исследователь в области спортивной психологии, координатор научных проектов",
                "bio_en": "Researcher in sports psychology, scientific project coordinator",
                "email": "sidorov@example.com",
                "phone": "+7 (999) 345-6789",
                "is_active": True,
                "order": 3,
            },
            {
                "full_name_ru": "Козлов Андрей Викторович",
                "full_name_en": "Kozlov Andrey Viktorovich",
                "role": member_role,
                "research_direction": directions[3],
                "position_ru": "Доктор медицинских наук, профессор",
                "position_en": "Doctor of Medical Sciences, Professor",
                "bio_ru": "Ведущий специалист по спортивной медицине, главврач клиники спортивной медицины",
                "bio_en": "Leading specialist in sports medicine, chief physician of sports medicine clinic",
                "email": "kozlov@example.com",
                "phone": "+7 (999) 456-7890",
                "is_active": True,
                "order": 4,
            },
            {
                "full_name_ru": "Смирнова Елена Владимировна",
                "full_name_en": "Smirnova Elena Vladimirovna",
                "role": member_role,
                "research_direction": directions[4],
                "position_ru": "Кандидат педагогических наук, доцент",
                "position_en": "PhD in Pedagogy, Associate Professor",
                "bio_ru": "Эксперт по теории и методике спортивной подготовки, тренер национальной сборной",
                "bio_en": "Expert in theory and methodology of sports training, national team coach",
                "email": "smirnova@example.com",
                "phone": "+7 (999) 567-8901",
                "is_active": True,
                "order": 5,
            },
            {
                "full_name_ru": "Соколов Алексей Николаевич",
                "full_name_en": "Sokolov Alexey Nikolaevich",
                "role": member_role,
                "research_direction": directions[5],
                "position_ru": "Кандидат биологических наук, доцент",
                "position_en": "PhD in Biology, Associate Professor",
                "bio_ru": "Специалист по спортивному питанию и фармакологии, консультант олимпийской сборной",
                "bio_en": "Specialist in sports nutrition and pharmacology, consultant to the Olympic team",
                "email": "sokolov@example.com",
                "phone": "+7 (999) 678-9012",
                "is_active": True,
                "order": 6,
            },
            {
                "full_name_ru": "Новиков Игорь Дмитриевич",
                "full_name_en": "Novikov Igor Dmitrievich",
                "role": member_role,
                "research_direction": directions[0],
                "position_ru": "Доктор биологических наук, профессор",
                "position_en": "Doctor of Biological Sciences, Professor",
                "bio_ru": "Исследователь адаптационных механизмов организма к физическим нагрузкам",
                "bio_en": "Researcher of adaptive mechanisms of the body to physical exertion",
                "email": "novikov@example.com",
                "phone": "+7 (999) 789-0123",
                "is_active": True,
                "order": 7,
            },
            {
                "full_name_ru": "Морозова Светлана Андреевна",
                "full_name_en": "Morozova Svetlana Andreevna",
                "role": member_role,
                "research_direction": directions[1],
                "position_ru": "Кандидат наук, старший научный сотрудник",
                "position_en": "PhD, Senior Researcher",
                "bio_ru": "Специалист по компьютерному анализу движений в спорте",
                "bio_en": "Specialist in computer analysis of movements in sports",
                "email": "morozova@example.com",
                "phone": "+7 (999) 890-1234",
                "is_active": True,
                "order": 8,
            },
        ]

        for member in members:
            NTSCommitteeMember.objects.create(**member)

        self.stdout.write(f"Created {len(members)} NTS Committee members")
