import re
import os
import ast


def fix_model_objects_none(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Find occurrences of "Model.objects.none()"
    pattern = r"return\s+Model\.objects\.none\(\)"
    matches = re.finditer(pattern, content)

    # Track positions to replace
    replacements = []

    for match in matches:
        # Get the position of the match
        start_pos = match.start()
        end_pos = match.end()

        # Find the class this method belongs to
        class_pattern = r"class\s+(\w+)\(.*?\):"
        class_matches = list(re.finditer(class_pattern, content[:start_pos]))

        if class_matches:
            # Get the last class definition before this match
            class_match = class_matches[-1]
            class_name = class_match.group(1)

            # Look for queryset = Model.objects... within the class
            class_content = content[class_match.start() : start_pos]
            queryset_pattern = r"queryset\s*=\s*(\w+)\.objects"
            queryset_match = re.search(queryset_pattern, class_content)

            if queryset_match:
                model_name = queryset_match.group(1)
                # Add to replacements list
                replacements.append((start_pos, end_pos, model_name))
            else:
                # Try to get model from serializer_class
                serializer_pattern = r"serializer_class\s*=\s*(\w+)Serializer"
                serializer_match = re.search(serializer_pattern, class_content)
                if serializer_match:
                    model_name = serializer_match.group(1)
                    replacements.append((start_pos, end_pos, model_name))
                else:
                    print(
                        f"WARNING: Could not determine model for class {class_name} in {file_path}"
                    )

    # Apply replacements in reverse order to avoid offset issues
    if replacements:
        result = list(content)
        for start_pos, end_pos, model_name in sorted(replacements, reverse=True):
            replacement = f"return {model_name}.objects.none()"
            result[start_pos:end_pos] = replacement

        # Save the modified content
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("".join(result))

        return (
            f"Fixed {len(replacements)} Model.objects.none() instances in {file_path}"
        )
    else:
        return f"No Model.objects.none() instances found in {file_path}"


# Apply to views.py files
base_dir = "c:/Users/Lenovo/Desktop/su projects/Physical-Academy-Back"
view_files = [
    os.path.join(base_dir, "admission/views.py"),
    os.path.join(base_dir, "leadership_structure/views.py"),
    os.path.join(base_dir, "student_clubs/views.py"),
]

for file_path in view_files:
    result = fix_model_objects_none(file_path)
    print(result)
