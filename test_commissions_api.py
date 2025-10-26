#!/usr/bin/env python
"""Test commissions API translations for category tags"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ac_back.settings")
django.setup()

from rest_framework.test import APIRequestFactory
from leadership_structure.views import CommissionViewSet
from leadership_structure.models import Commission

# Create factory
factory = APIRequestFactory()

# Test data
commission_count = Commission.objects.count()
print(f"📊 Total commissions in DB: {commission_count}")

if commission_count == 0:
    print("❌ No commissions found!")
    print("Creating test commission...")
    Commission.objects.create(
        name="Академический совет",
        name_en="Academic Council",
        name_kg="Академиялык кеңеш",
        chairman="Председатель",
        chairman_en="Chairman",
        chairman_kg="Төрага",
        description="Описание",
        description_en="Description",
        description_kg="Сүрөттөмө",
        category="academic",
        is_active=True,
    )
    commission_count = Commission.objects.count()
    print(f"✅ Created test commission. Total: {commission_count}")

print("\n" + "=" * 70)
print("Testing Commission Category Translations")
print("=" * 70)

# Test all categories
categories = ["all", "methodical", "academic", "quality", "student"]

for category in categories:
    print(f"\n📌 Category: {category}")
    print("-" * 70)

    # Test Russian
    request_ru = factory.get("/api/leadership-structure/commissions/", {"lang": "ru"})
    view = CommissionViewSet.as_view({"get": "list"})
    response_ru = view(request_ru)

    # Find commission with this category
    item_ru = next(
        (c for c in response_ru.data["results"] if c.get("category") == category), None
    )

    if item_ru:
        print(f"  🇷🇺 Russian: {item_ru.get('category_display', '❌ MISSING')}")

    # Test English
    request_en = factory.get("/api/leadership-structure/commissions/", {"lang": "en"})
    response_en = view(request_en)
    item_en = next(
        (c for c in response_en.data["results"] if c.get("category") == category), None
    )

    if item_en:
        print(f"  🇬🇧 English: {item_en.get('category_display', '❌ MISSING')}")

    # Test Kyrgyz
    request_kg = factory.get("/api/leadership-structure/commissions/", {"lang": "kg"})
    response_kg = view(request_kg)
    item_kg = next(
        (c for c in response_kg.data["results"] if c.get("category") == category), None
    )

    if item_kg:
        print(f"  🇰🇬 Kyrgyz: {item_kg.get('category_display', '❌ MISSING')}")

    # Check if translations are different
    if item_ru and item_en and item_kg:
        ru_display = item_ru.get("category_display", "")
        en_display = item_en.get("category_display", "")
        kg_display = item_kg.get("category_display", "")

        if ru_display and en_display and kg_display:
            if ru_display != en_display and ru_display != kg_display:
                print(f"  ✅ Translations working!")
            else:
                print(f"  ❌ All languages return same value: {ru_display}")
        else:
            print(f"  ❌ category_display field is missing!")
    elif not item_ru and not item_en and not item_kg:
        print(f"  ⚠️  No commission with category '{category}' found in DB")

print("\n" + "=" * 70)
print("Expected Frontend Display:")
print("=" * 70)
print(
    "🇷🇺 Russian: Все комиссии | Методические | Академические | Качество образования | Студенческие"
)
print("🇬🇧 English: All | Methodical | Academic | Quality of Education | Student")
print(
    "🇰🇬 Kyrgyz: Баары | Методикалык | Академиялык | Билим берүүнүн сапаты | Студенттик"
)
print("=" * 70)
