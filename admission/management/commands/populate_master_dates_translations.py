from django.core.management.base import BaseCommand
from admission.models import MasterMainDate


class Command(BaseCommand):
    help = "Add translations for Master Main Dates"

    def handle(self, *args, **kwargs):
        self.stdout.write("Updating Master Main Dates with translations...")

        # Словарь с переводами дат
        date_translations = {
            "1 июня - 15 июля": {"en": "June 1 - July 15", "kg": "1-июнь - 15-июль"},
            "20 июля - 5 августа": {
                "en": "July 20 - August 5",
                "kg": "20-июль - 5-август",
            },
            "10 августа": {"en": "August 10", "kg": "10-август"},
            "15 августа": {"en": "August 15", "kg": "15-август"},
            "1 сентября": {"en": "September 1", "kg": "1-сентябрь"},
        }

        dates = MasterMainDate.objects.all()
        updated_count = 0

        for date in dates:
            if date.date in date_translations:
                date.date_en = date_translations[date.date]["en"]
                date.date_kg = date_translations[date.date]["kg"]
                date.save()
                updated_count += 1
                self.stdout.write(f"  ✅ Updated: {date.event_name_ru}")
                self.stdout.write(f"     RU: {date.date}")
                self.stdout.write(f"     EN: {date.date_en}")
                self.stdout.write(f"     KG: {date.date_kg}")
            else:
                self.stdout.write(
                    self.style.WARNING(f"  ⚠️  No translation found for: {date.date}")
                )

        self.stdout.write(
            self.style.SUCCESS(f"\n✅ Successfully updated {updated_count} dates!")
        )
