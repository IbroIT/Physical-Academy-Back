#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to extract CollegePrograms and PhdPrograms from education_models_new.txt,
fix their encoding, and add them to education/models.py
"""


def fix_encoding(text):
    """Fix the corrupted Cyrillic encoding"""
    try:
        # The text was incorrectly decoded, so encode it back as latin-1 and decode as cp1251
        return text.encode("latin-1").decode("cp1251")
    except:
        return text


def extract_class(lines, class_name):
    """Extract a class definition from lines"""
    class_lines = []
    in_class = False
    indent_level = 0

    for i, line in enumerate(lines):
        if f"class {class_name}(models.Model):" in line:
            in_class = True
            indent_level = len(line) - len(line.lstrip())
            class_lines.append(line)
            continue

        if in_class:
            # Check if we've reached the next class or end of file
            if (
                line.strip()
                and not line.startswith(" " * (indent_level + 1))
                and not line.startswith("\t")
            ):
                # Check if it's a new class definition
                if "class " in line and "(models.Model):" in line:
                    break
            class_lines.append(line)

    return class_lines


# Read the source file - first try with different encodings to handle corruption
try:
    with open("education_models_new.txt", "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    # File has encoding issues, read as bytes and handle carefully
    with open("education_models_new.txt", "rb") as f:
        content = f.read().decode("utf-8", errors="ignore")

lines = content.split("\n")

# Extract both classes
phd_lines = extract_class(lines, "PhdPrograms")
college_lines = extract_class(lines, "CollegePrograms")

# Fix encoding in extracted classes
phd_fixed = "\n".join([fix_encoding(line) for line in phd_lines])
college_fixed = "\n".join([fix_encoding(line) for line in college_lines])

# Read current education/models.py
with open("education/models.py", "r", encoding="utf-8") as f:
    current_content = f.read()

# Find the position to insert (before MasterPrograms class)
insert_position = current_content.find("class MasterPrograms(models.Model):")

if insert_position == -1:
    print("Error: Could not find MasterPrograms class")
    exit(1)

# Create new content with inserted classes
new_content = (
    current_content[:insert_position]
    + phd_fixed
    + "\n\n"
    + college_fixed
    + "\n\n"
    + current_content[insert_position:]
)

# Write the updated file
with open("education/models.py", "w", encoding="utf-8", newline="\n") as f:
    f.write(new_content)

print("Successfully added PhdPrograms and CollegePrograms to education/models.py")
print(f"PhdPrograms: {len(phd_lines)} lines")
print(f"CollegePrograms: {len(college_lines)} lines")
