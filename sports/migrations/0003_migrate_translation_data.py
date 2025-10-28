# Generated migration for data transfer from Translation tables to direct fields

from django.db import migrations


def migrate_translation_data(apps, schema_editor):
    """
    Перенос данных из таблиц переводов в прямые поля моделей
    """
    # Получаем модели
    SportSection = apps.get_model("sports", "SportSection")
    SportSectionTranslation = apps.get_model("sports", "SportSectionTranslation")
    Achievement = apps.get_model("sports", "Achievement")
    AchievementTranslation = apps.get_model("sports", "AchievementTranslation")
    Infrastructure = apps.get_model("sports", "Infrastructure")
    InfrastructureTranslation = apps.get_model("sports", "InfrastructureTranslation")
    InfrastructureCategory = apps.get_model("sports", "InfrastructureCategory")
    InfrastructureCategoryTranslation = apps.get_model(
        "sports", "InfrastructureCategoryTranslation"
    )
    InfrastructureObject = apps.get_model("sports", "InfrastructureObject")
    InfrastructureObjectTranslation = apps.get_model(
        "sports", "InfrastructureObjectTranslation"
    )

    # Миграция SportSection
    for section in SportSection.objects.all():
        translations = SportSectionTranslation.objects.filter(section=section)
        for trans in translations:
            if trans.language == "ru":
                section.name_ru = trans.name
                section.description_ru = trans.description
                section.contact_info_ru = trans.contact_info
            elif trans.language == "kg":
                section.name_kg = trans.name
                section.description_kg = trans.description
                section.contact_info_kg = trans.contact_info
            elif trans.language == "en":
                section.name_en = trans.name
                section.description_en = trans.description
                section.contact_info_en = trans.contact_info
        section.save()

    # Миграция Achievement
    for achievement in Achievement.objects.all():
        translations = AchievementTranslation.objects.filter(achievement=achievement)
        for trans in translations:
            if trans.language == "ru":
                achievement.description_ru = trans.description
            elif trans.language == "kg":
                achievement.description_kg = trans.description
            elif trans.language == "en":
                achievement.description_en = trans.description
        achievement.save()

    # Миграция Infrastructure
    for infrastructure in Infrastructure.objects.all():
        translations = InfrastructureTranslation.objects.filter(
            infrastructure=infrastructure
        )
        for trans in translations:
            if trans.language == "ru":
                infrastructure.name_ru = trans.name
                infrastructure.description_ru = trans.description
                infrastructure.stat_1_label_ru = trans.stat_1_label
                infrastructure.stat_2_label_ru = trans.stat_2_label
                infrastructure.stat_3_label_ru = trans.stat_3_label
                infrastructure.stat_4_label_ru = trans.stat_4_label
            elif trans.language == "kg":
                infrastructure.name_kg = trans.name
                infrastructure.description_kg = trans.description
                infrastructure.stat_1_label_kg = trans.stat_1_label
                infrastructure.stat_2_label_kg = trans.stat_2_label
                infrastructure.stat_3_label_kg = trans.stat_3_label
                infrastructure.stat_4_label_kg = trans.stat_4_label
            elif trans.language == "en":
                infrastructure.name_en = trans.name
                infrastructure.description_en = trans.description
                infrastructure.stat_1_label_en = trans.stat_1_label
                infrastructure.stat_2_label_en = trans.stat_2_label
                infrastructure.stat_3_label_en = trans.stat_3_label
                infrastructure.stat_4_label_en = trans.stat_4_label
        infrastructure.save()

    # Миграция InfrastructureCategory
    for category in InfrastructureCategory.objects.all():
        translations = InfrastructureCategoryTranslation.objects.filter(
            category=category
        )
        for trans in translations:
            if trans.language == "ru":
                category.name_ru = trans.name
            elif trans.language == "kg":
                category.name_kg = trans.name
            elif trans.language == "en":
                category.name_en = trans.name
        category.save()

    # Миграция InfrastructureObject
    for obj in InfrastructureObject.objects.all():
        translations = InfrastructureObjectTranslation.objects.filter(
            infrastructure_object=obj
        )
        for trans in translations:
            if trans.language == "ru":
                obj.name_ru = trans.name
                obj.description_ru = trans.description
            elif trans.language == "kg":
                obj.name_kg = trans.name
                obj.description_kg = trans.description
            elif trans.language == "en":
                obj.name_en = trans.name
                obj.description_en = trans.description
        obj.save()


def reverse_migration(apps, schema_editor):
    """
    Обратная миграция - очистка полей (если нужно откатить)
    """
    SportSection = apps.get_model("sports", "SportSection")
    Achievement = apps.get_model("sports", "Achievement")
    Infrastructure = apps.get_model("sports", "Infrastructure")
    InfrastructureCategory = apps.get_model("sports", "InfrastructureCategory")
    InfrastructureObject = apps.get_model("sports", "InfrastructureObject")

    # Очищаем новые поля
    SportSection.objects.all().update(
        name_ru="",
        name_kg="",
        name_en="",
        description_ru="",
        description_kg="",
        description_en="",
        contact_info_ru="",
        contact_info_kg="",
        contact_info_en="",
    )
    Achievement.objects.all().update(
        description_ru="", description_kg="", description_en=""
    )
    Infrastructure.objects.all().update(
        name_ru="",
        name_kg="",
        name_en="",
        description_ru="",
        description_kg="",
        description_en="",
        stat_1_label_ru="",
        stat_1_label_kg="",
        stat_1_label_en="",
        stat_2_label_ru="",
        stat_2_label_kg="",
        stat_2_label_en="",
        stat_3_label_ru="",
        stat_3_label_kg="",
        stat_3_label_en="",
        stat_4_label_ru="",
        stat_4_label_kg="",
        stat_4_label_en="",
    )
    InfrastructureCategory.objects.all().update(name_ru="", name_kg="", name_en="")
    InfrastructureObject.objects.all().update(
        name_ru="",
        name_kg="",
        name_en="",
        description_ru="",
        description_kg="",
        description_en="",
    )


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
