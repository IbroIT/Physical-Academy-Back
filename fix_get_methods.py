#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для исправления методов get_* в admission/models.py
Добавляет проверку на пустую строку для fallback на русский язык
"""
import re


def fix_get_methods(filepath):
    """Исправить все методы get_* для правильного fallback"""

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Паттерн для поиска методов вида:
    # return getattr(self, f"field_{language}", self.field_ru)
    pattern = r'return getattr\(self, f"(\w+)_\{language\}", self\.(\w+)\)'

    def replacement(match):
        field_name = match.group(1)
        fallback_field = match.group(2)
        return f'value = getattr(self, f"{field_name}_{{language}}", None)\n        return value if value else self.{fallback_field}'

    # Заменяем паттерн
    new_content = re.sub(pattern, replacement, content)

    # Сохраняем файл
    with open(filepath, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)

    print(f"✅ Файл {filepath} успешно исправлен")

    # Подсчитываем количество замен
    old_count = len(re.findall(pattern, content))
    print(f"📊 Исправлено методов: {old_count}")


if __name__ == "__main__":
    fix_get_methods("admission/models.py")
