from django.db import migrations


def copy_existing_to_ru(apps, schema_editor):
    """Copy data from existing generic fields into *_ru fields when those are empty.

    This migration is defensive: it only writes to *_ru fields when they are
    empty/blank to avoid overwriting intentionally provided translations.
    """

    SportSection = apps.get_model("sports", "SportSection")
    TrainingSchedule = apps.get_model("sports", "TrainingSchedule")
    Infrastructure = apps.get_model("sports", "Infrastructure")

    # SportSection: copy schedule -> schedule_ru, coach_rank -> coach_rank_ru
    for s in SportSection.objects.all():
        updated = False
        try:
            if (not getattr(s, "schedule_ru", None)) and getattr(s, "schedule", None):
                s.schedule_ru = s.schedule
                updated = True

            if (not getattr(s, "coach_rank_ru", None)) and getattr(
                s, "coach_rank", None
            ):
                s.coach_rank_ru = s.coach_rank
                updated = True

            if updated:
                s.save()
        except Exception:
            # Be robust: skip any problematic row rather than failing the whole migration
            continue

    # TrainingSchedule: copy location -> location_ru
    for t in TrainingSchedule.objects.all():
        try:
            if (not getattr(t, "location_ru", None)) and getattr(t, "location", None):
                t.location_ru = t.location
                t.save()
        except Exception:
            continue

    # Infrastructure: copy badge -> badge_ru
    for inf in Infrastructure.objects.all():
        try:
            if (not getattr(inf, "badge_ru", None)) and getattr(inf, "badge", None):
                inf.badge_ru = inf.badge
                inf.save()
        except Exception:
            continue


def noop_reverse(apps, schema_editor):
    # No-op reverse: we don't attempt to move data back to generic fields
    return


class Migration(migrations.Migration):

    dependencies = [
        ("sports", "0003_migrate_translation_data"),
    ]

    operations = [
        migrations.RunPython(copy_existing_to_ru, reverse_code=noop_reverse),
    ]
