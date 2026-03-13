import re

readme_path = "Simulations/EarthSpaceSciences/README.md"
with open(readme_path, "r") as f:
    text = f.read()

# The qodo bot says: Entries must be exactly `- [Simulation Title](SimulationFile.html) - Brief description.` with no extra trailing metadata.
# So I need to remove the timestamp from the README.md for this specific simulation, or all of them if the others have it?
# The error was specifically: "Simulations/EarthSpaceSciences/README.md[456-456]" (which is probably my new line).
# I will fix just my new line to remove the timestamp.

text = re.sub(r'(- \[Energy & Mineral Resources Cost-Benefit Analysis\]\(EnergyResourcesCostBenefit\.html\) - Evaluate competing design solutions for developing, managing, and utilizing energy and mineral resources based on cost-benefit ratios\.) \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]', r'\1', text)

with open(readme_path, "w") as f:
    f.write(text)
