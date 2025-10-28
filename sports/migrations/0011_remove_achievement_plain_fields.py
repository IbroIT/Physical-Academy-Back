# Generated migration to remove plain sport/competition/result fields now that per-language fields exist
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sports", "0010_achievement_competition_en_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="achievement",
            name="sport",
        ),
        migrations.RemoveField(
            model_name="achievement",
            name="competition",
        ),
        migrations.RemoveField(
            model_name="achievement",
            name="result",
        ),
    ]
