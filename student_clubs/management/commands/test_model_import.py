from django.core.management.base import BaseCommand
from student_clubs.models import Club


class Command(BaseCommand):
    help = "Tests the Club model import after restructuring"

    def handle(self, *args, **options):
        clubs = Club.objects.all().count()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully imported Club model. There are {clubs} clubs in the database."
            )
        )
