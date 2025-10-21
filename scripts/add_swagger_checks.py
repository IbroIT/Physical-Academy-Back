import re
import os


def add_swagger_check_to_get_queryset(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Pattern to match get_queryset methods within classes
    pattern = r"(class\s+([A-Za-z0-9_]+)[\(\s\w\,\_\:]+?)\n.*?queryset\s*=\s*([A-Za-z0-9_]+)\.objects.*?\n.*?(def get_queryset\(self\):.*?\n)(\s+)(return)"

    # Add swagger_fake_view check
    def add_swagger_check(match):
        class_def = match.group(1)
        class_name = match.group(2)
        model_name = match.group(3)  # Extract model from queryset attribute
        method_def = match.group(4)
        indent = match.group(5)
        return_stmt = match.group(6)

        # If no model found from queryset attribute, try to extract from method body
        if not model_name or model_name == "Model":
            # Extract model from return statement using regex
            model_pattern = r"return\s+([A-Za-z]+)\.objects"
            model_match = re.search(
                model_pattern, content[match.start() : match.start() + 500]
            )
            model_name = model_match.group(1) if model_match else "Model"

        # Add swagger_fake_view check
        return (
            f"{class_def}\n"  # Keep original class definition
            f".*?{method_def}"  # Keep everything up to get_queryset method
            f"{indent}# Check for swagger schema generation\n"
            f'{indent}if getattr(self, "swagger_fake_view", False):\n'
            f"{indent}    return {model_name}.objects.none()\n"
            f"{indent}{return_stmt}"
        )

    # Apply replacements
    modified_content = re.sub(pattern, add_swagger_check, content, flags=re.DOTALL)

    # Write the modified content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)

    return f"Successfully added swagger_fake_view checks to get_queryset methods in {file_path}."


# Apply to views.py files
base_dir = "c:/Users/Lenovo/Desktop/su projects/Physical-Academy-Back"
view_files = [
    os.path.join(base_dir, "admission/views.py"),
    os.path.join(base_dir, "leadership_structure/views.py"),
    os.path.join(base_dir, "student_clubs/views.py"),
]

for file_path in view_files:
    result = add_swagger_check_to_get_queryset(file_path)
    print(result)
