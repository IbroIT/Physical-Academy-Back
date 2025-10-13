import re


def fix_serializer_methods(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Паттерн для поиска дублирующихся @extend_schema_field и неправильного определения метода
    pattern = r"(@extend_schema_field\(OpenApiTypes\.STR\)[\s\n]+)(?:@extend_schema_field\(OpenApiTypes\.STR\)[\s\n]+)*def\s+(\w+)\(self,\s+obj\)(?::\s*->\s*str\s*->\s*str|:)"
    replacement = r"\1def \2(self, obj) -> str:"

    # Замена
    content = re.sub(pattern, replacement, content)

    # Записываем обновленное содержимое обратно в файл
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    return "Successfully fixed serializer methods in " + file_path


# Запускаем для файла лидерства
result = fix_serializer_methods(
    "c:/Users/Lenovo/Desktop/su projects/Physical-Academy-Back/leadership_structure/serializers.py"
)
print(result)
