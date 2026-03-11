import os
import glob
from bs4 import BeautifulSoup
import json

def add_meta_if_missing(soup, attrs, existing_metas):
    name_or_prop = attrs.get('name') or attrs.get('property')
    if name_or_prop not in existing_metas:
        new_meta = soup.new_tag('meta')
        for key, value in attrs.items():
            new_meta[key] = value

        # Find the best place to insert (after title or at the end of head)
        title_tag = soup.find('title')
        if title_tag:
            title_tag.insert_after(new_meta)
            title_tag.insert_after("\n    ")
        else:
            soup.head.append(new_meta)
            soup.head.append("\n    ")

        existing_metas.add(name_or_prop)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    if not soup.head:
        print(f"No <head> found in {filepath}. Skipping.")
        return

    # Extract title
    title_tag = soup.find('title')
    title = title_tag.text.strip() if title_tag else os.path.basename(filepath).replace('.html', '')

    # Create a description based on the title if none exists
    description = f"Interactive science simulation for {title}. Explore and learn with this engaging, NGSS-aligned high school educational tool."

    # Check existing meta tags to avoid duplication
    existing_metas = set()
    for meta in soup.find_all('meta'):
        name = meta.get('name')
        prop = meta.get('property')
        if name:
            existing_metas.add(name)
        if prop:
            existing_metas.add(prop)

    # Standard Meta Tags
    add_meta_if_missing(soup, {'name': 'description', 'content': description}, existing_metas)
    add_meta_if_missing(soup, {'name': 'keywords', 'content': f"science, simulation, NGSS, {title}, education, interactive"}, existing_metas)
    add_meta_if_missing(soup, {'name': 'author', 'content': 'Nicklaus Cairns'}, existing_metas)
    add_meta_if_missing(soup, {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}, existing_metas)

    # Open Graph Tags
    url_path = filepath.replace('./', '').replace('\\', '/')
    full_url = f"https://nicklauscairns.com/{url_path}"

    add_meta_if_missing(soup, {'property': 'og:title', 'content': title}, existing_metas)
    add_meta_if_missing(soup, {'property': 'og:description', 'content': description}, existing_metas)
    add_meta_if_missing(soup, {'property': 'og:type', 'content': 'website'}, existing_metas)
    add_meta_if_missing(soup, {'property': 'og:url', 'content': full_url}, existing_metas)

    # Schema.org Structured Data (JSON-LD)
    existing_scripts = soup.find_all('script', type='application/ld+json')
    has_schema = any(s.string and ('LearningResource' in s.string or 'SoftwareApplication' in s.string) for s in existing_scripts)

    if not has_schema:
        schema_data = {
            "@context": "https://schema.org",
            "@type": "LearningResource",
            "name": title,
            "description": description,
            "url": full_url,
            "author": {
                "@type": "Person",
                "name": "Nicklaus Cairns"
            },
            "educationalAlignment": {
                "@type": "AlignmentObject",
                "alignmentType": "educational framework",
                "educationalFramework": "Next Generation Science Standards (NGSS)"
            },
            "learningResourceType": "Interactive Simulation"
        }

        json_ld_script = soup.new_tag('script', type='application/ld+json')
        json_ld_script.string = "\n" + json.dumps(schema_data, indent=4) + "\n    "
        soup.head.append("\n    ")
        soup.head.append(json_ld_script)
        soup.head.append("\n")

    # Write back to file
    # We serialize without forcing formatting that breaks scripts, bs4 is good enough
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"Processed: {filepath}")

# Process all HTML files in Simulations directory
for filepath in glob.glob('./Simulations/**/*.html', recursive=True):
    process_file(filepath)

print("SEO update complete.")
