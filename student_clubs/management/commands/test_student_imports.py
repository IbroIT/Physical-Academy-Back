from django.core.management.base import BaseCommand
from student_clubs.models import StudentProfile, ClubMembership


class Command(BaseCommand):
    help = (
        "Tests the StudentProfile and ClubMembership model imports after restructuring"
    )

    def handle(self, *args, **options):
        students = StudentProfile.objects.all().count()
        memberships = ClubMembership.objects.all().count()

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully imported StudentProfile model. There are {students} student profiles in the database."
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully imported ClubMembership model. There are {memberships} club memberships in the database."
            )
        )
