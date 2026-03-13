import re
with open('Simulations/EarthSpaceSciences/README.md', 'r') as f:
    content = f.read()

# 4. Remove timestamp from planetary defense entry
# Current: - [Planetary Defense: Asteroid Deflection](PlanetaryDefense.html) - Use orbital mechanics and kinetic impactors to alter an asteroid's trajectory and save Earth from a catastrophic collision. [2026-03-13 22:17:29]
content = re.sub(r'(- \[Planetary Defense: Asteroid Deflection\]\(PlanetaryDefense\.html\) - .*?)\s*\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]', r'\1', content)

with open('Simulations/EarthSpaceSciences/README.md', 'w') as f:
    f.write(content)
