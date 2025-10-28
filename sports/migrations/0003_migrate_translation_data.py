# Generated migration for data transfer from Translation tables to direct fields
# This migration is now a no-op since the translation tables no longer exist

from django.db import migrations


def migrate_translation_data(apps, schema_editor):
    """
    Перенос данных из таблиц переводов в прямые поля моделей
    SKIP: Translation tables have been removed, no data to migrate
    """
    pass


def reverse_migration(apps, schema_editor):
    """
    Обратная миграция - очистка полей (если нужно откатить)
    """
    pass


class Migration(migrations.Migration):

    dependencies = [
        (
            "sports",
            "0002_alter_infrastructurecategorytranslation_unique_together_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(migrate_translation_data, reverse_migration),
    ]
