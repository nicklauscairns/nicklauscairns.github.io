import re
with open('Simulations/EarthSpaceSciences/README.md', 'r') as f:
    content = f.read()

# Fix Tambora
content = re.sub(r'(- \[Tambora 1816: Year Without a Summer\]\(Tambora1816\.html\) - .*?)\s*\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]', r'\1', content)

with open('Simulations/EarthSpaceSciences/README.md', 'w') as f:
    f.write(content)
