from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sports", "0014_achievementcategory_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sportsection",
            name="contact_info",
            field=models.CharField(
                default="",
                max_length=500,
                blank=True,
                verbose_name="Контактная информация",
            ),
        ),
    ]
