from playwright.sync_api import sync_playwright
import os

def test_chemical_reactions():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        file_path = f"file://{os.path.abspath('Simulations/PhysicalSciences/ChemicalReactionsOutcomes.html')}"
        page.goto(file_path, wait_until="networkidle")

        # Verify initial state
        assert "Chemical Reaction Outcomes Predictor" in page.title()
        assert page.locator("#reactBtn").is_disabled()

        # Test Na + Cl -> NaCl
        page.click("button[data-element='Na']")
        page.click("button[data-element='Cl']")

        assert page.locator(".atom-container").count() == 2
        assert not page.locator("#reactBtn").is_disabled()

        page.click("#reactBtn")

        # Verify result
        assert page.locator("#productsArea").is_visible()
        result_text = page.locator("#productsArea").inner_text()
        assert "Na+ Cl-\nSodium Chloride" in result_text

        # Clear
        page.click("#clearBtn")
        assert page.locator(".atom-container").count() == 0
        assert page.locator("#reactBtn").is_disabled()
        assert not page.locator("#productsArea").is_visible()

        # Test invalid combination
        page.click("button[data-element='Na']")
        page.click("button[data-element='Na']")
        page.click("button[data-element='Na']")
        page.click("#reactBtn")

        result_text = page.locator("#productsArea").inner_text()
        assert "No Reaction / Unstable Combination" in result_text

        print("Playwright test passed: ChemicalReactionsOutcomes logic functions correctly.")

        browser.close()

if __name__ == "__main__":
    test_chemical_reactions()