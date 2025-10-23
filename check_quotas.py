#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Простая проверка данных QuotaType
"""

# Подключаем Django через manage.py shell_plus
check_code = """
from admission.models import QuotaType, QuotaStats, AdditionalSupport, ProcessStep

print('🔍 Проверка данных в базе...')
quotas = QuotaType.objects.filter(is_active=True)
print(f'Квоты: {quotas.count()}')

if quotas.exists():
    quota = quotas.first()
    print(f'\\nПервая квота: {quota.type}')
    print(f'  title_ru: {quota.title_ru}')
    print(f'  title_kg: {quota.title_kg if quota.title_kg else "(пусто)"}')
    print(f'\\n  get_title("ru"): {quota.get_title("ru")}')
    print(f'  get_title("kg"): {quota.get_title("kg")}')
    
    # Проверка fallback
    if not quota.title_kg:
        print('\\n⚠️  Поле title_kg пустое - должен работать fallback на русский')
    
    if quota.get_title('kg') == quota.title_ru:
        print('✅ Fallback на русский работает!')
    elif quota.get_title('kg') == quota.title_kg:
        print('✅ Поле title_kg заполнено и используется!')
else:
    print('⚠️  Нет данных о квотах!')
"""

print("Запустите эту команду:")
print("=" * 60)
print(f'cd "c:\\Users\\Lenovo\\Desktop\\su projects\\Physical-Academy-Back"')
print(f'python manage.py shell -c "{check_code.replace(chr(10), "; ")}"')
print("=" * 60)
