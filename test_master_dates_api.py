#!/usr/bin/env python
"""Test Master Main Dates API translations"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ac_back.settings")
django.setup()

from rest_framework.test import APIRequestFactory
from admission.views import MasterMainDateViewSet
from admission.models import MasterMainDate

# Create factory
factory = APIRequestFactory()

# Test data
date_count = MasterMainDate.objects.count()
print(f"📊 Total Master Main Dates in DB: {date_count}")

if date_count == 0:
    print("❌ No dates found!")
    exit(1)

print("\n" + "=" * 70)
print("Testing Master Main Dates Translations")
print("=" * 70)

dates = MasterMainDate.objects.all()

for date_obj in dates:
    print(f"\n📅 {date_obj.event_name_ru}")
    print("-" * 70)

    # Test Russian
    request_ru = factory.get("/api/admission/master/main-dates/", {"lang": "ru"})
    view = MasterMainDateViewSet.as_view({"get": "list"})
    response_ru = view(request_ru)
    # ViewSet returns a list directly, not {'results': [...]}
    data_ru = (
        response_ru.data
        if isinstance(response_ru.data, list)
        else response_ru.data.get("results", [])
    )
    item_ru = next((d for d in data_ru if d["id"] == date_obj.id), None)

    if item_ru:
        print(f"  🇷🇺 Russian:")
        print(f"     event_name: {item_ru.get('event_name')}")
        print(f"     date: {item_ru.get('date')}")

    # Test English
    request_en = factory.get("/api/admission/master/main-dates/", {"lang": "en"})
    response_en = view(request_en)
    data_en = (
        response_en.data
        if isinstance(response_en.data, list)
        else response_en.data.get("results", [])
    )
    item_en = next((d for d in data_en if d["id"] == date_obj.id), None)

    if item_en:
        print(f"  🇬🇧 English:")
        print(f"     event_name: {item_en.get('event_name')}")
        print(f"     date: {item_en.get('date')}")

    # Test Kyrgyz
    request_kg = factory.get("/api/admission/master/main-dates/", {"lang": "kg"})
    response_kg = view(request_kg)
    data_kg = (
        response_kg.data
        if isinstance(response_kg.data, list)
        else response_kg.data.get("results", [])
    )
    item_kg = next((d for d in data_kg if d["id"] == date_obj.id), None)

    if item_kg:
        print(f"  🇰🇬 Kyrgyz:")
        print(f"     event_name: {item_kg.get('event_name')}")
        print(f"     date: {item_kg.get('date')}")

    # Check if translations are different
    if item_ru and item_en and item_kg:
        ru_date = item_ru.get("date", "")
        en_date = item_en.get("date", "")
        kg_date = item_kg.get("date", "")

        if ru_date and en_date and kg_date:
            if ru_date != en_date and ru_date != kg_date:
                print(f"  ✅ Translations working!")
            else:
                print(f"  ❌ All languages return same value: {ru_date}")

print("\n" + "=" * 70)
print("✅ API test completed!")
print("=" * 70)
