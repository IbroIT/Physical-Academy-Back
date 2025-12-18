#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ac_back.settings')
django.setup()

from pedagogical_faculty.models import TabCategory, Management

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
        'name_ru': 'Иванов Иван Иванович',
        'name_kg': 'Иванов Иван Иванович',
        'name_en': 'Ivanov Ivan Ivanovich',
        'role_ru': 'Декан факультета',
        'role_kg': 'Факультет деканы',
        'role_en': 'Dean of Faculty',
        'phone': '+996 (312) 12-34-56',
        'email': 'ivanov@academy.kg',
        'photo': 'https://res.cloudinary.com/dyg5p8i69/image/upload/v1765861417/syc2ndjoxika129iqr5m.pdf',  # placeholder
        'resume': 'https://res.cloudinary.com/dyg5p8i69/raw/upload/v1765861418/owqmzghtytt97w3innkw.jpg',  # placeholder
        'order': 1
    },
    {
        'name_ru': 'Петрова Мария Сергеевна',
        'name_kg': 'Петрова Мария Сергеевна',
        'name_en': 'Petrova Maria Sergeevna',
        'role_ru': 'Заместитель декана',
        'role_kg': 'Декандын орун басары',
        'role_en': 'Deputy Dean',
        'phone': '+996 (312) 12-34-57',
        'email': 'petrova@academy.kg',
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

print("Тестовые данные для management добавлены.")