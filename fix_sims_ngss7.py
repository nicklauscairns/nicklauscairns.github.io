import re
import os
import glob

# Ensure EVERY simulation has some kind of data logging or export if applicable, or at least a way to engage
# Some are just visual simulations without tables. We could add a simple data table to them, or ensure they are properly styled.

# Let's review the files that didn't get modified.
files = glob.glob("Simulations/PhysicalSciences/*.html")
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    has_table = "<table" in content
    has_export = "exportTableToCSV" in content

    print(f"{os.path.basename(f)}: Table={has_table}, Export={has_export}")
