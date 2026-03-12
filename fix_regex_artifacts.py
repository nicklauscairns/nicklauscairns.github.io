import re
import os

files = [
    'NGSS/HighSchoolEarthSpaceSciencesEvidenceStatements.md',
    'NGSS/HighSchoolEngineeringTechnologyScienceEvidenceStatements.md',
    'NGSS/HighSchoolLifeSciencesEvidenceStatements.md'
]

def clean_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # We need to find mistaken list items.
    # The mistaken ones are usually a single character from the start of a wrapped line.
    # For example:
    # "   * a. species to survive and reproduce." -> "a species to survive and reproduce."
    # Wait, the original text might have been " a species to survive and reproduce."

    # Let's fix specific known ones found by the reviewer:
    content = content.replace("   * a. species to survive and reproduce.", " a species to survive and reproduce.")
    content = content.replace("   * a. selected technology", " a selected technology")

    # Are there more? We can do a quick check on lines like `   * a. ` where the previous line doesn't end in a period or colon.
    # Actually, the easiest is to just fix the known ones, and then do a quick manual regex replacement for any other obvious ones.

    with open(filepath, 'w') as f:
        f.write(content)

for file in files:
    clean_file(file)
