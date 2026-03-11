import os
import glob
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

def generate_sitemap():
    # Root of the repository
    repo_root = '.'

    # Base URL
    base_url = 'https://nicklauscairns.com/'

    # Find all HTML files in Simulations directory
    html_files = glob.glob('./Simulations/**/*.html', recursive=True)

    # Sort for consistency
    html_files.sort()

    # Create the root element
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')

    # Add root URL
    root_url = ET.SubElement(urlset, 'url')
    root_loc = ET.SubElement(root_url, 'loc')
    root_loc.text = base_url

    # Add each HTML file
    for filepath in html_files:
        # Normalize path
        normalized_path = filepath.replace('./', '').replace('\\', '/')

        # Create full URL
        full_url = f"{base_url}{normalized_path}"

        # Create XML elements
        url_elem = ET.SubElement(urlset, 'url')
        loc_elem = ET.SubElement(url_elem, 'loc')
        loc_elem.text = full_url

    # Convert to string and pretty print
    xml_str = ET.tostring(urlset, encoding='utf-8')
    parsed_xml = minidom.parseString(xml_str)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")

    # Remove empty lines from pretty_xml
    pretty_xml = '\n'.join([line for line in pretty_xml.split('\n') if line.strip()])

    # Write to file
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        # minidom adds a generic <?xml version="1.0" ?> declaration
        # We replace it with the specific one we want
        if pretty_xml.startswith('<?xml'):
            # Find the end of the XML declaration
            end_idx = pretty_xml.find('?>') + 2
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(pretty_xml[end_idx:].lstrip())
        else:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(pretty_xml)

    print(f"Sitemap generated successfully with {len(html_files) + 1} URLs.")

if __name__ == "__main__":
    generate_sitemap()
