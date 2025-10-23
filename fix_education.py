#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Замена _ky → _kg в education/models.py"""


def main():
    file_path = "education/models.py"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Замены _ky → _kg
    content = content.replace("_ky =", "_kg =")
    content = content.replace("_ky)", "_kg)")
    content = content.replace("_ky,", "_kg,")
    content = content.replace('_ky"', '_kg"')
    content = content.replace("_ky'", "_kg'")

    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    print(f"✓ {file_path} - замена _ky → _kg выполнена")


if __name__ == "__main__":
    main()
