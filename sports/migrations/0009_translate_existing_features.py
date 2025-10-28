from django.db import migrations


def translate_features(apps, schema_editor):
    InfrastructureObject = apps.get_model("sports", "InfrastructureObject")

    # Simple mapping for known Russian phrases used in seed data -> English
    en_map = {
        "Вместимость: 1500": "Capacity: 1500",
        "Освещение: да": "Lighting: yes",
    }

    for obj in InfrastructureObject._default_manager.all():
        raw = obj.features or []
        # If features are already dicts (new format), skip
        if raw and isinstance(raw[0], dict):
            continue

        new_features = []
        changed = False
        for item in raw:
            if isinstance(item, str):
                ru = item
                en = en_map.get(item, item)
                kg = item
                new_features.append({"ru": ru, "en": en, "kg": kg})
                changed = True
            else:
                # unknown format, keep as-is
                new_features.append(item)

        if changed:
            obj.features = new_features
            obj.save(update_fields=["features"])


def noop_reverse(apps, schema_editor):
    return


class Migration(migrations.Migration):

    dependencies = [("sports", "0008_seed_infrastructure_demo")]

    operations = [migrations.RunPython(translate_features, reverse_code=noop_reverse)]
