# Generated migration to remove the plain athlete_name column
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sports", "0011_remove_achievement_plain_fields"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="achievement",
            name="athlete_name",
        ),
    ]
