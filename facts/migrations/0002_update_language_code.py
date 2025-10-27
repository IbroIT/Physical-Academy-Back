# Generated migration to update language code from 'ky' to 'kg'

from django.db import migrations


def update_language_codes(apps, schema_editor):
    """Update existing 'ky' language codes to 'kg'"""
    FactTranslation = apps.get_model('facts', 'FactTranslation')
    FactTranslation.objects.filter(language='ky').update(language='kg')


def reverse_update_language_codes(apps, schema_editor):
    """Reverse migration: update 'kg' back to 'ky'"""
    FactTranslation = apps.get_model('facts', 'FactTranslation')
    FactTranslation.objects.filter(language='kg').update(language='ky')


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_language_codes, reverse_update_language_codes),
    ]
