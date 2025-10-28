from django.db import migrations


def seed_infrastructure_demo(apps, schema_editor):
    Infrastructure = apps.get_model("sports", "Infrastructure")
    InfrastructureStatistic = apps.get_model("sports", "InfrastructureStatistic")
    InfrastructureCategory = apps.get_model("sports", "InfrastructureCategory")
    InfrastructureObject = apps.get_model("sports", "InfrastructureObject")

    infra = Infrastructure.objects.first()
    if not infra:
        return

    # Seed statistics only if none exist for this infrastructure
    if not InfrastructureStatistic._default_manager.filter(
        infrastructure_id=infra.id
    ).exists():
        stats = [
            {
                "label_ru": "Площадки",
                "label_kg": "Аянттар",
                "label_en": "Venues",
                "value": "12",
                "icon": "🏟️",
                "order": 0,
                "is_active": True,
            },
            {
                "label_ru": "Тренеры",
                "label_kg": "Мугалимдер",
                "label_en": "Coaches",
                "value": "8",
                "icon": "👥",
                "order": 1,
                "is_active": True,
            },
            {
                "label_ru": "Мест",
                "label_kg": "Орындар",
                "label_en": "Seats",
                "value": "5000+",
                "icon": "💺",
                "order": 2,
                "is_active": True,
            },
        ]
        for s in stats:
            InfrastructureStatistic._default_manager.create(
                infrastructure_id=infra.id, **s
            )

    # For each category, add a sample active object if none exist
    categories = InfrastructureCategory._default_manager.filter(
        infrastructure_id=infra.id
    )
    for cat in categories:
        if not InfrastructureObject._default_manager.filter(
            category_id=cat.id
        ).exists():
            InfrastructureObject._default_manager.create(
                category_id=cat.id,
                name_ru=f"{cat.name_ru} — Главный объект",
                name_kg=f"{cat.name_kg} — Негизги объект",
                name_en=f"{cat.name_en} — Main object",
                description_ru=f"Описание для {cat.name_ru}",
                description_kg=f"{cat.name_kg} үчүн сүрөттөө",
                description_en=f"Description for {cat.name_en}",
                features=["Вместимость: 1500", "Освещение: да"],
                is_active=True,
                order=0,
            )


def noop_reverse(apps, schema_editor):
    # We don't attempt to reverse seed data
    return


class Migration(migrations.Migration):

    dependencies = [
        ("sports", "0007_copy_names_to_ru"),
    ]

    operations = [
        migrations.RunPython(seed_infrastructure_demo, reverse_code=noop_reverse),
    ]
