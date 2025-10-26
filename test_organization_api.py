#!/usr/bin/env python
"""Test organization structure API translations"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ac_back.settings")
django.setup()

from rest_framework.test import APIRequestFactory
from leadership_structure.views import OrganizationStructureViewSet
from leadership_structure.models import OrganizationStructure

# Create factory
factory = APIRequestFactory()

# Test data
structure_count = OrganizationStructure.objects.count()
print(f"📊 Total structures in DB: {structure_count}")

if structure_count == 0:
    print(
        "❌ No structures found! Run: python manage.py populate_organization_structure"
    )
    exit(1)

# Get a structure with different type
structures = OrganizationStructure.objects.all()[:3]

print("\n" + "=" * 70)
print("Testing API translations for organization structures")
print("=" * 70)

for structure in structures:
    print(f"\n🏢 Structure: {structure.name} (type: {structure.structure_type})")
    print("-" * 70)

    # Test Russian
    request_ru = factory.get(
        "/api/leadership-structure/organization-structure/", {"lang": "ru"}
    )
    view = OrganizationStructureViewSet.as_view({"get": "list"})
    response_ru = view(request_ru)

    # Find current structure in response
    item_ru = next(
        (s for s in response_ru.data["results"] if s["id"] == structure.id), None
    )

    if item_ru:
        print(f"  🇷🇺 Russian:")
        print(f"     name: {item_ru['name']}")
        print(f"     structure_type: {item_ru['structure_type']}")
        print(
            f"     structure_type_display: {item_ru.get('structure_type_display', '❌ MISSING')}"
        )

    # Test English
    request_en = factory.get(
        "/api/leadership-structure/organization-structure/", {"lang": "en"}
    )
    response_en = view(request_en)
    item_en = next(
        (s for s in response_en.data["results"] if s["id"] == structure.id), None
    )

    if item_en:
        print(f"  🇬🇧 English:")
        print(f"     name: {item_en['name']}")
        print(f"     structure_type: {item_en['structure_type']}")
        print(
            f"     structure_type_display: {item_en.get('structure_type_display', '❌ MISSING')}"
        )

    # Test Kyrgyz
    request_kg = factory.get(
        "/api/leadership-structure/organization-structure/", {"lang": "kg"}
    )
    response_kg = view(request_kg)
    item_kg = next(
        (s for s in response_kg.data["results"] if s["id"] == structure.id), None
    )

    if item_kg:
        print(f"  🇰🇬 Kyrgyz:")
        print(f"     name: {item_kg['name']}")
        print(f"     structure_type: {item_kg['structure_type']}")
        print(
            f"     structure_type_display: {item_kg.get('structure_type_display', '❌ MISSING')}"
        )

    # Check if translations are different
    if item_ru and item_en and item_kg:
        ru_display = item_ru.get("structure_type_display", "")
        en_display = item_en.get("structure_type_display", "")
        kg_display = item_kg.get("structure_type_display", "")

        if ru_display and en_display and kg_display:
            if ru_display != en_display and ru_display != kg_display:
                print(f"  ✅ Translations working!")
            else:
                print(f"  ❌ All languages return same value: {ru_display}")
        else:
            print(f"  ❌ structure_type_display field is missing!")

print("\n" + "=" * 70)
print("✅ API test completed!")
print("=" * 70)
