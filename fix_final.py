#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Окончательное исправление admission/models.py:
1. Удаление BOM
2. Замена _ky → _kg
3. Добавление параметров к JSON полям
"""


def main():
    file_path = "admission/models.py"

    # Читаем файл в бинарном режиме
    with open(file_path, "rb") as f:
        content_bytes = f.read()

    # Удаляем BOM если есть
    if content_bytes.startswith(b"\xef\xbb\xbf"):
        content_bytes = content_bytes[3:]
        print("✓ Удалён BOM")

    # Декодируем
    content = content_bytes.decode("utf-8")

    # Замены _ky → _kg
    content = content.replace("_ky =", "_kg =")
    content = content.replace("_ky)", "_kg)")
    content = content.replace("_ky,", "_kg,")
    content = content.replace('_ky"', '_kg"')
    content = content.replace("_ky'", "_kg'")
    print("✓ Заменено _ky → _kg")

    # Добавляем параметры к JSON полям BachelorProgram
    import re

    # Паттерн для поиска JSON полей без default/null/blank
    json_field_pattern = r"((?:mainDiscipline|CareerPerspectives|features)_(?:ru|en|kg) = models\.JSONField\(\s*(?:max_length=\d+,\s*)?verbose_name=[^)]+\))"

    def add_params(match):
        field_def = match.group(1)
        # Если уже есть default - не трогаем
        if "default=" in field_def or "null=" in field_def:
            return field_def
        # Добавляем параметры
        field_def = field_def.replace(")", ", default=list, null=True, blank=True)")
        return field_def

    content = re.sub(json_field_pattern, add_params, content)
    print("✓ Добавлены параметры к JSON полям")

    # Записываем без BOM
    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    print(f"\n✓ Файл {file_path} успешно обновлён!")
    print("  - Удалён BOM")
    print("  - Заменено _ky → _kg")
    print("  - Добавлены default=list, null=True, blank=True к JSON полям")


if __name__ == "__main__":
    main()
