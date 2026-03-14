import re

readme_path = 'Simulations/EarthSpaceSciences/README.md'

with open(readme_path, 'r') as f:
    text = f.read()

new_sim = """
- [Puerto Rican Karst Topography: Water & Bedrock Interactions](PuertoRicanKarstTopography.html) - An interactive simulation investigating how water chemically weathers limestone over thousands of years to create the unique karst landforms of Puerto Rico (sinkholes, mogotes, and aquifers).

  <details>
    <summary><b>Evaluation: Investigative Phenomenon | 4.5/5 Stars | 2026-03-12 18:00:00</b></summary>
    <ul>
      <li>
        <b>Overview:</b> Excellent investigative phenomenon exploring how water's properties affect Earth's surface materials, specifically focusing on the unique Puerto Rican karst belt. Strongly meets Criterion 4 (Investigable) by allowing students to adjust rainfall, acidity, and fractures to observe the formation of sinkholes and aquifers.
      </li>
      <li>
        <b>Dimensional Evaluation & Evidence Statements:</b> Strongly supports the DCI (ESS2.C) on the roles of water in Earth's surface processes and the CCC (Structure and Function). For HS-ESS2-5, it allows planning and conducting investigations (1.a, 2.a) to produce data on chemical weathering.
      </li>
      <li>
        <b>AI Action Items for Improvement:</b>
        <ul>
          <li><i>Minor Feature addition:</i> Add a layer of permeable topsoil to demonstrate how organic decay contributes to water acidity before it reaches the bedrock.</li>
          <li><i>UX Adjustment:</i> Enhance the visual distinction between dry caves and active groundwater aquifers.</li>
        </ul>
      </li>
      <li>
        <b>Implementation Checklist:</b>
        <ul>
          <li>[x] HTML5 Canvas for real-time cellular automata bedrock dissolution.</li>
          <li>[x] Sliders for environmental variables (Rainfall, pH, Fractures).</li>
          <li>[x] Chart.js data tracking of dissolved limestone and aquifer volume.</li>
        </ul>
      </li>
    </ul>
  </details>
"""

# Insert under HS-ESS2-5
match = re.search(r'### HS-ESS2-5.*?\n.*?\n(.*?)(\n###|$)', text, re.DOTALL)
if match:
    existing_content = match.group(1)

    # We want to append to the end of the existing content under HS-ESS2-5
    # ensuring it's after any existing details blocks
    replacement = match.group(0).replace(existing_content, existing_content + "\n" + new_sim + "\n")
    text = text.replace(match.group(0), replacement)

    with open(readme_path, 'w') as f:
        f.write(text)
    print("Updated README successfully.")
else:
    print("Failed to find HS-ESS2-5 section.")
