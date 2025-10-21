import os
import json
import django

# Ensure project root is on sys.path so Django settings module can be imported
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# set settings module relative to project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ac_back.settings")
django.setup()

from student_clubs.models_disabilities import (
    DisabilitySupportService,
    DisabilityContactPerson,
    DisabilityResource,
    DisabilityEmergencyContact,
)
from student_clubs.serializers_disabilities import (
    DisabilitySupportServiceSerializer,
    DisabilityContactPersonSerializer,
    DisabilityResourceSerializer,
    DisabilityEmergencyContactSerializer,
    DisabilitiesPageDataSerializer,
)

# Create mock instances (not saved to DB)
service = DisabilitySupportService(
    icon="🔧",
    order=1,
    title_ru="Поддержка 1",
    title_en="Support 1",
    title_kg="Колдоо 1",
    description_ru="Описание RU",
    description_en="Description EN",
    description_kg="Description KG",
    features_ru="Фича1\nФича2",
    features_en="Feat1\nFeat2",
    features_kg="Функция1\nФункция2",
)
contact = DisabilityContactPerson(
    icon="👤",
    name_ru="Иван",
    name_en="Ivan",
    name_kg="Ivan KG",
    position_ru="Координатор",
    position_en="Coordinator",
    position_kg="Coordinator KG",
    phone="+123",
    email="a@example.com",
    hours_ru="9-18",
    hours_en="9-18",
    hours_kg="9-18",
    location_ru="Офис",
    location_en="Office",
    location_kg="Office KG",
)
resource = DisabilityResource(
    icon="📚",
    name_ru="Ресурс",
    name_en="Resource",
    name_kg="Resource KG",
    description_ru="Описание",
    description_en="Description",
    description_kg="Description KG",
    url="https://example.com",
    type_ru="guide",
    type_en="guide",
    type_kg="guide",
    format_ru="pdf",
    format_en="pdf",
    format_kg="pdf",
)
emergency = DisabilityEmergencyContact(
    order=0,
    title_ru="Экстренная служба",
    title_en="Emergency Service",
    title_kg="Тез жардам",
    description_ru="Звоните",
    description_en="Call us",
    description_kg="Call KG",
    phone="+1999",
    phone_link="tel:+1999",
)

# Serialize with different languages
for lang in ("ru", "en", "kg"):
    print("\n--- LANGUAGE:", lang, "---")
    s_ser = DisabilitySupportServiceSerializer(
        [service], many=True, context={"language": lang}
    )
    print("SupportService:", json.dumps(s_ser.data, ensure_ascii=False, indent=2))

    c_ser = DisabilityContactPersonSerializer(
        [contact], many=True, context={"language": lang}
    )
    print("Contact:", json.dumps(c_ser.data, ensure_ascii=False, indent=2))

    r_ser = DisabilityResourceSerializer(
        [resource], many=True, context={"language": lang}
    )
    print("Resource:", json.dumps(r_ser.data, ensure_ascii=False, indent=2))

    e_ser = DisabilityEmergencyContactSerializer(emergency, context={"language": lang})
    print("Emergency:", json.dumps(e_ser.data, ensure_ascii=False, indent=2))

# Test combined page serializer
page_data = {
    "support_services": [service],
    "contacts": [contact],
    "resources": [resource],
    "emergency": emergency,
}
page_ser = DisabilitiesPageDataSerializer(page_data, context={"language": "ru"})
print("\n--- PAGE DATA (ru) ---")
print(json.dumps(page_ser.data, ensure_ascii=False, indent=2))

print("\nCheck script finished successfully")
