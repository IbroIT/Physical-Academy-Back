#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ac_back.settings')
django.setup()

from coaching_faculy.models import TabCategory, Management

# Создаем таб management, если не существует
tab, created = TabCategory.objects.get_or_create(
    key='management',
    defaults={
        'title_ru': 'Руководство',
        'title_kg': 'Жетекчилик',
        'title_en': 'Management',
        'order': 3,
        'is_active': True
    }
)

# Создаем тестовые данные для management
management_data = [
    {
        'name_ru': 'Иванов Олег Сергеевич',
        'name_kg': 'Иванов Олег Сергеевич',
        'name_en': 'Ivanov Oleg Sergeevich',
        'role_ru': 'Декан тренерского факультета',
        'role_kg': 'Тренердик факультеттин деканы',
        'role_en': 'Dean of Coaching Faculty',
        'phone': '+996 (312) 12-34-56',
        'email': 'ivanov.coaching@academy.kg',
        'photo': 'https://res.cloudinary.com/dyg5p8i69/image/upload/v1765861417/syc2ndjoxika129iqr5m.pdf',  # placeholder
        'resume': 'https://res.cloudinary.com/dyg5p8i69/raw/upload/v1765861418/owqmzghtytt97w3innkw.jpg',  # placeholder
        'order': 1
    },
    {
        'name_ru': 'Петрова Ольга Андреевна',
        'name_kg': 'Петрова Ольга Андреевна',
        'name_en': 'Petrova Olga Andreevna',
        'role_ru': 'Заместитель декана по спортивной работе',
        'role_kg': 'Спорт иштери боюнча декандын орун басары',
        'role_en': 'Deputy Dean for Sports Work',
        'phone': '+996 (312) 12-34-57',
        'email': 'petrova.coaching@academy.kg',
        'photo': 'https://res.cloudinary.com/dyg5p8i69/image/upload/v1765861417/syc2ndjoxika129iqr5m.pdf',  # placeholder
        'resume': 'https://res.cloudinary.com/dyg5p8i69/raw/upload/v1765861418/owqmzghtytt97w3innkw.jpg',  # placeholder
        'order': 2
    }
]

for data in management_data:
    Management.objects.get_or_create(
        tab=tab,
        name_ru=data['name_ru'],
        defaults=data
    )

print("Тестовые данные для coaching management добавлены.")