import re


def fix_serializer_methods(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Удаляем дублированные декораторы и пустые строки
    content = re.sub(
        r"(@extend_schema_field\(OpenApiTypes\.STR\)\s*\n)\s*@extend_schema_field\(OpenApiTypes\.STR\)(\s*\n\s*)",
        r"\1",
        content,
    )

    # Удаляем пустые строки между декоратором и методом
    content = re.sub(
        r"(@extend_schema_field\(OpenApiTypes\.STR\)\s*\n)(\s*\n)+(\s*def)",
        r"\1\3",
        content,
    )

    # Исправляем некорректный синтаксис определения метода
    content = re.sub(
        r"def\s+(\w+)\(self,\s+obj\):\s*->\s*str\s*->\s*str",
        r"def \1(self, obj) -> str:",
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
