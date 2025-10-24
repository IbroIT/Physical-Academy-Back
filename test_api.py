#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для тестирования API эндпоинтов
"""
import os
import django
import sys

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ac_back.settings")
django.setup()

from admission.models import QuotaType, QuotaStats, AdditionalSupport, ProcessStep
from admission.serializers import BachelorQuotasDataSerializer


def test_bachelor_quotas_api():
    """Тест API для bachelor quotas"""
    print("🔍 Проверка данных в базе...")

    # Проверяем данные
    quotas = QuotaType.objects.filter(is_active=True)
    stats = QuotaStats.objects.filter(is_active=True)
    support = AdditionalSupport.objects.filter(is_active=True)
    steps = ProcessStep.objects.filter(is_active=True)

    print(f"✅ Квоты: {quotas.count()}")
    print(f"✅ Статистика: {stats.count()}")
    print(f"✅ Поддержка: {support.count()}")
    print(f"✅ Шаги: {steps.count()}")

    if quotas.count() == 0:
        print("⚠️  Нет данных о квотах в базе!")
        return False

    print("\n📋 Проверка перевода на языки...")

    # Проверяем первую квоту
    quota = quotas.first()
    print(f"\nКвота: {quota.type}")
    print(f"  RU: {quota.title_ru[:50]}...")
    print(f"  KG: {quota.title_kg[:50] if quota.title_kg else '(пусто)'}...")
    print(f"  EN: {quota.title_en[:50] if quota.title_en else '(пусто)'}...")

    # Тестируем методы get_*
    print("\n🔧 Тест методов get_title:")
    print(f"  get_title('ru'): {quota.get_title('ru')[:50]}...")
    print(f"  get_title('kg'): {quota.get_title('kg')[:50]}...")
    print(f"  get_title('en'): {quota.get_title('en')[:50]}...")

    # Тестируем сериализатор
    print("\n📦 Тест сериализатора с language=kg:")
    serializer = BachelorQuotasDataSerializer({}, context={"language": "kg"})
    data = serializer.data

    print(f"  Квоты в ответе: {len(data.get('quotas', []))}")
    print(f"  Статистика в ответе: {len(data.get('quota_stats', []))}")

    if data["quotas"]:
        first_quota = data["quotas"][0]
        print(f"\n  Первая квота:")
        print(f"    title: {first_quota.get('title', '')[:50]}...")
        print(f"    description: {first_quota.get('description', '')[:50]}...")

        if first_quota.get("requirements"):
            print(f"    Требования: {len(first_quota['requirements'])}")
            if first_quota["requirements"]:
                print(
                    f"      Первое: {first_quota['requirements'][0].get('requirement', '')[:50]}..."
                )

    print("\n✅ Все проверки пройдены!")
    return True


if __name__ == "__main__":
    try:
        test_bachelor_quotas_api()
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
