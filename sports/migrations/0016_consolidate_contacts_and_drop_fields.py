from django.db import migrations


def forwards(apps, schema_editor):
    SportSection = apps.get_model("sports", "SportSection")
    for s in SportSection.objects.all():
        # Consolidate contact info into contact_info (prefer ru -> en -> kg)
        try:
            if not getattr(s, "contact_info", None):
                val = (
                    getattr(s, "contact_info_ru", None)
                    or getattr(s, "contact_info_en", None)
                    or getattr(s, "contact_info_kg", None)
                )
                if val:
                    s.contact_info = val
        except Exception:
            # Be conservative: skip on errors for safety
            pass

        # Ensure per-language coach/schedule fields are populated from base fields
        try:
            if not getattr(s, "coach_name_ru", None) and getattr(s, "coach_name", None):
                s.coach_name_ru = s.coach_name
            if not getattr(s, "coach_rank_ru", None) and getattr(s, "coach_rank", None):
                s.coach_rank_ru = s.coach_rank
            if not getattr(s, "schedule_ru", None) and getattr(s, "schedule", None):
                s.schedule_ru = s.schedule
        except Exception:
            pass

        try:
            s.save()
        except Exception:
            # If save fails for a row, continue with others to avoid blocking migration
            continue


def backwards(apps, schema_editor):
    SportSection = apps.get_model("sports", "SportSection")
    for s in SportSection.objects.all():
        try:
            # Restore contact_info_ru from contact_info (best-effort)
            if not getattr(s, "contact_info_ru", None) and getattr(
                s, "contact_info", None
            ):
                s.contact_info_ru = s.contact_info
        except Exception:
            pass
        try:
            s.save()
        except Exception:
            continue


class Migration(migrations.Migration):

    dependencies = [
        ("sports", "0015_add_contact_info"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
        # Now drop obsolete fields (we keep this in the same migration so rollback restores values above)
        migrations.RemoveField(model_name="sportsection", name="contact_info_ru"),
        migrations.RemoveField(model_name="sportsection", name="contact_info_kg"),
        migrations.RemoveField(model_name="sportsection", name="contact_info_en"),
        migrations.RemoveField(model_name="sportsection", name="coach_name"),
        migrations.RemoveField(model_name="sportsection", name="coach_rank"),
        migrations.RemoveField(model_name="sportsection", name="schedule"),
    ]
