import os
import subprocess

readmes = [
    "README.md",
    "Simulations/README.md",
    "Simulations/EarthSpaceSciences/README.md",
    "Simulations/EngineeringTechnologyScience/README.md",
    "Simulations/LifeSciences/README.md",
    "Simulations/PhysicalSciences/README.md",
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Nicklaus Cairns - NGSS High School Science Simulations">
    <meta name="keywords" content="NGSS, Science, Simulations, High School, Physics, Chemistry, Biology, Earth Science">
    <meta name="author" content="Nicklaus Cairns">
    <title>Nicklaus Cairns - Simulations</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ font-family: 'Inter', sans-serif; background-color: #f3f4f6; color: #1f2937; }}
        .markdown-body {{ max-width: 800px; margin: 0 auto; padding: 2rem; background-color: #ffffff; border-radius: 0.5rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); }}
        .markdown-body h1 {{ font-size: 2.25rem; font-weight: 700; margin-bottom: 1.5rem; border-bottom: 2px solid #e5e7eb; padding-bottom: 0.5rem; }}
        .markdown-body h2 {{ font-size: 1.875rem; font-weight: 600; margin-top: 2rem; margin-bottom: 1rem; }}
        .markdown-body h3 {{ font-size: 1.5rem; font-weight: 500; margin-top: 1.5rem; margin-bottom: 0.75rem; }}
        .markdown-body p {{ margin-bottom: 1rem; line-height: 1.6; }}
        .markdown-body ul {{ list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1rem; }}
        .markdown-body li {{ margin-bottom: 0.5rem; }}
        .markdown-body a {{ color: #2563eb; text-decoration: none; }}
        .markdown-body a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body class="antialiased min-h-screen p-4 md:p-8">
    <div class="markdown-body">
        {content}
    </div>
</body>
</html>"""

for md_file in readmes:
    if not os.path.exists(md_file):
        print(f"Skipping {md_file}, not found.")
        continue

    html_file = md_file.replace("README.md", "index.html")

    # Run marked to convert markdown to HTML
    result = subprocess.run(['marked', md_file], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error converting {md_file}:\n{result.stderr}")
        continue

    html_content = result.stdout

    # Replace internal links ending with README.md to index.html
    html_content = html_content.replace('README.md"', 'index.html"')

    # Create final HTML file
    final_html = html_template.format(content=html_content)

    with open(html_file, 'w') as f:
        f.write(final_html)
    print(f"Created {html_file}")

print("Done.")
