#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Скрипт для исправления кодировки в admission/models.py
Преобразует испорченный текст обратно в правильную кириллицу
"""


def fix_encoding(file_path):
    # Читаем файл как есть (с кракозябрами)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Пытаемся исправить кодировку
    # Кракозябры появились из-за двойного кодирования UTF-8 → cp1251 → UTF-8
    try:
        # Пробуем декодировать как latin-1 и закодировать как cp1251, потом раскодировать как utf-8
        fixed_content = content.encode("latin1").decode("utf-8")
    except:
        try:
            # Альтернативный метод
            fixed_content = content.encode("cp1252").decode("utf-8")
        except:
            print("❌ Не удалось автоматически исправить кодировку")
            return False

    # Записываем исправленный файл
    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(fixed_content)

    print(f"✓ Файл {file_path} успешно исправлен")
    return True


if __name__ == "__main__":
    success = fix_encoding("admission/models.py")
    if success:
        print("\nТеперь можно продолжить работу с файлом")
    else:
        print("\nПопробуйте восстановить файл из старого коммита")
