from django.db import migrations


def copy_names_to_ru(apps, schema_editor):
    SportSection = apps.get_model("sports", "SportSection")
    Achievement = apps.get_model("sports", "Achievement")

    # Copy coach_name -> coach_name_ru and coach_rank -> coach_rank_ru when empty
    for sec in SportSection.objects.all():
        changed = False
        if not sec.coach_name_ru and sec.coach_name:
            sec.coach_name_ru = sec.coach_name
            changed = True
        if not getattr(sec, "coach_rank_ru", None) and getattr(sec, "coach_rank", None):
            sec.coach_rank_ru = sec.coach_rank
            changed = True
        if changed:
            sec.save(
                update_fields=[
                    f for f in ["coach_name_ru", "coach_rank_ru"] if getattr(sec, f)
                ]
            )

    # Copy athlete_name -> athlete_name_ru when empty
    for ach in Achievement.objects.all():
        if not ach.athlete_name_ru and ach.athlete_name:
            ach.athlete_name_ru = ach.athlete_name
            ach.save(update_fields=["athlete_name_ru"])


def noop_reverse(apps, schema_editor):
    # We don't attempt to reverse copy
    return


class Migration(migrations.Migration):

    dependencies = [
        ("sports", "0006_achievement_athlete_name_en_and_more"),
    ]

    operations = [
        migrations.RunPython(copy_names_to_ru, reverse_code=noop_reverse),
    ]
