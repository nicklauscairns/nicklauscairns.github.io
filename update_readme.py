import re

readme_path = "Simulations/EarthSpaceSciences/README.md"
with open(readme_path, "r") as f:
    text = f.read()

# Fix readme timestamp
# Current: - [Energy & Mineral Resources Cost-Benefit Analysis](EnergyResourcesCostBenefit.html) - Evaluate competing design solutions for developing, managing, and utilizing energy and mineral resources based on cost-benefit ratios. [2026-03-13 21:18:58]
# Required: - [Energy & Mineral Resources Cost-Benefit Analysis](EnergyResourcesCostBenefit.html) - Evaluate competing design solutions for developing, managing, and utilizing energy and mineral resources based on cost-benefit ratios. [YYYY-MM-DD HH:MM:SS]  <- wait, the memory says "ensure the current date and time are appended at the end of the new description." Let me re-read the agent memory vs the code review comment.
