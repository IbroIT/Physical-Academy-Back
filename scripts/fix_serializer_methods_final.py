import re


def fix_serializer_methods(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Исправляем все проблемы одним регулярным выражением:
    # 1. Удаляем дублированные декораторы
    # 2. Удаляем пустые строки между декоратором и методом
    # 3. Исправляем некорректный синтаксис определения метода
    content = re.sub(
        r"(@extend_schema_field\(OpenApiTypes\.STR\)\s*\n)"  # Первый декоратор
        r"(?:\s*@extend_schema_field\(OpenApiTypes\.STR\)\s*\n)*"  # Повторы декоратора (если есть)
        r"(?:\s*\n)*"  # Пустые строки (если есть)
        r"(\s*def\s+(\w+)\(self,\s+obj\))(?::\s*->(?:\s*str)+|:)",  # Определение метода
        r"\1\2 -> str:",
        content,
    )

    # Записываем обновленное содержимое обратно в файл
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    return "Successfully fixed serializer methods in " + file_path


# Запускаем для файла лидерства
result = fix_serializer_methods(
    "c:/Users/Lenovo/Desktop/su projects/Physical-Academy-Back/leadership_structure/serializers.py"
)
print(result)
