import re


def add_schema_annotations(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Regular expression pattern to find get_* methods in serializer classes
    pattern = r"(\s+)(def get_\w+\(self, obj\):.*?)(\n\s+.*?return)"

    # Add @extend_schema_field decorator and return type annotation
    def replace_method(match):
        indent = match.group(1)
        method_def = match.group(2)
        return_line = match.group(3)

        # Add decorator and return type
        annotated_method = f"{indent}@extend_schema_field(OpenApiTypes.STR)\n{indent}{method_def} -> str{return_line}"
        return annotated_method

    # Apply replacements
    modified_content = re.sub(pattern, replace_method, content, flags=re.DOTALL)

    # Write the modified content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)

    return "Successfully added schema annotations to all get_* methods in serializers."


# Apply to serializers.py
result = add_schema_annotations(
    "c:/Users/Lenovo/Desktop/su projects/Physical-Academy-Back/admission/serializers.py"
)
print(result)

# Apply to leadership_structure serializers
result = add_schema_annotations(
    "c:/Users/Lenovo/Desktop/su projects/Physical-Academy-Back/leadership_structure/serializers.py"
)
print(result)

# Apply to student_clubs serializers
result = add_schema_annotations(
    "c:/Users/Lenovo/Desktop/su projects/Physical-Academy-Back/student_clubs/serializers.py"
)
print(result)
