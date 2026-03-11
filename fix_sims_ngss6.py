import os
import re
import glob

files = glob.glob("Simulations/PhysicalSciences/*.html")
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    # Check if there's an H1 but no HS-PS string at all
    h1_match = re.search(r'(<h1[^>]*>.*?</h1>)', content, re.IGNORECASE | re.DOTALL)
    if h1_match and "HS-PS" not in content and "NGSS" not in content:
        print(f"File {f} is missing NGSS string!")
        # Let's add a generic NGSS aligned label if we don't know the exact one.
        tag = h1_match.group(1)
        content = content.replace(tag, tag + f'\n        <p class="text-sm text-gray-600 italic mb-4">Aligned with NGSS High School Physical Sciences</p>')
        with open(f, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Added generic NGSS tag to {os.path.basename(f)}")
