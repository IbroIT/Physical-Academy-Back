import os
import sys
import django
from datetime import date

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ac_back.settings")
django.setup()

from student_clubs.models_scholarship_visa import (
    ScholarshipProgram,
    ScholarshipRequiredDocument,
)
from student_clubs.serializers_scholarship_visa import ScholarshipPageDataSerializer
from rest_framework.test import APIRequestFactory


def create_sample_data():
    # Create a sample scholarship program
    scholarship = ScholarshipProgram.objects.create(
        name_ru="Стипендия для отличников",
        name_en="Excellence Scholarship",
        name_kg="Мыкты окуучулар үчүн стипендия",
        description_ru="Стипендия для студентов с высокой успеваемостью",
        description_en="Scholarship for high-achieving students",
        description_kg="Жогорку жетишкендиктери бар студенттер үчүн стипендия",
        eligibility_criteria_ru="GPA 4.0 и выше\nАктивное участие",
        eligibility_criteria_en="GPA 4.0 or higher\nActive participation",
        eligibility_criteria_kg="GPA 4.0 жана жогору\nАктивдүү катышуу",
        amount=5000,
        currency="KGS",
        application_deadline=date(2025, 12, 31),
        application_link="https://example.com/apply",
        contact_email="scholarship@example.com",
        contact_phone="+996123456789",
        is_active=True,
    )

    # Create required documents
    ScholarshipRequiredDocument.objects.create(
        scholarship=scholarship,
        name_ru="Транскрипт",
        name_en="Transcript",
        name_kg="Транскрипт",
        description_ru="Официальный транскрипт с оценками",
        description_en="Official transcript with grades",
        description_kg="Баалары менен расмий транскрипт",
        is_required=True,
        order=1,
    )


def test_serialization():
    # Create a request
    factory = APIRequestFactory()

    print("\nTesting scholarship page data serialization:")

    # Test for each language
    for lang in ["ru", "en", "kg"]:
        print(f"\n=== Testing {lang.upper()} language ===")

        request = factory.get(f"/api/scholarship-page/?lang={lang}")
        serializer = ScholarshipPageDataSerializer(
            context={"language": lang, "request": request}
        )
        data = serializer.to_representation(None)

        print(f"Total scholarships: {data['total_scholarships']}")
        print(f"Active scholarships: {data['active_scholarships']}")

        if data["scholarships"]:
            scholarship = data["scholarships"][0]
            print("\nSample scholarship data:")
            print(f"Name: {scholarship['name']}")
            print(f"Description: {scholarship['description']}")
            print(f"Amount: {scholarship['amount']} {scholarship['currency']}")
            print(f"Deadline: {scholarship['application_deadline']}")
            print(
                f"Contact: {scholarship['contact_email']}, {scholarship['contact_phone']}"
            )
            print(f"Application Link: {scholarship['application_link']}")
            print(f"Is Active: {scholarship['is_active']}")
            if scholarship["required_documents"]:
                print("\nRequired documents:")
                for doc in scholarship["required_documents"]:
                    print(
                        f"- {doc['name']}: {'Required' if doc['is_required'] else 'Optional'}"
                    )


if __name__ == "__main__":
    # Clear existing data
    ScholarshipRequiredDocument.objects.all().delete()
    ScholarshipProgram.objects.all().delete()

    print("Creating sample data...")
    create_sample_data()

    print("Running serialization tests...")
    test_serialization()

    print("\nCheck script finished successfully")
