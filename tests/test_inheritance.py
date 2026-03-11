from playwright.sync_api import sync_playwright
import os

def test_inheritance():
    possible_paths = [
        "Simulations/LifeSciences/InheritanceModel.html",
        "../Simulations/LifeSciences/InheritanceModel.html",
        "/app/Simulations/LifeSciences/InheritanceModel.html"
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = os.path.abspath(path)
            break

    if not file_path:
        raise FileNotFoundError("Could not find InheritanceModel.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{file_path}", wait_until="networkidle")

        # 1. Verify Initial State
        assert page.locator("#mom-genotype").text_content() == "Bb Ee"
        assert page.locator("#dad-genotype").text_content() == "bb ee"

        # Offspring panel should be hidden initially
        assert page.locator("#offspring-panel").is_hidden() == True

        # 2. Manipulate Parent Genes
        # Change Dad to BB ee by clicking top gene bands
        page.evaluate("document.querySelectorAll('.gene-band[data-parent=\"dad\"][data-locus=\"fur\"]')[0].click()")
        page.wait_for_timeout(100)
        page.evaluate("document.querySelectorAll('.gene-band[data-parent=\"dad\"][data-locus=\"fur\"]')[1].click()")
        page.wait_for_timeout(100)

        assert page.locator("#dad-genotype").text_content() == "BB ee"

        # 3. Produce Offspring
        # Mom is Bb Ee, Dad is BB ee
        # Offspring Fur will be BB or Bb (always Purple, dominant)
        # Offspring Eye will be Ee or ee (50/50 Blue or Red)
        page.locator("#btn-breed").click()
        page.wait_for_timeout(500)

        # Offspring panel should now be visible
        assert page.locator("#offspring-panel").is_visible() == True

        # Verify phenotype
        phenotype_text = page.locator("#offspring-phenotype").text_content()
        assert "Purple Fur" in phenotype_text
        assert "Eyes" in phenotype_text # Eye color is random based on mom, but text should render

        # Take screenshot for verification
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/inheritance_screenshot.png', full_page=True)

        browser.close()
        print("DNA and Inheritance simulation test passed.")

if __name__ == "__main__":
    test_inheritance()